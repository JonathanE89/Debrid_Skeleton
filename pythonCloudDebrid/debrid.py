import targetPath
import re, requests, os
from bs4 import BeautifulSoup

class Debrid:
    def __init__(self):
        
        #Initialize a Target Path Object
        #NOTE: CURRENTLY NOT INTEGRATED WITH ANYTHING 
        self.activePath = targetPath.TargetPath()
        
        # Finds a Method for the site based on the URL
        self.site_methods = {
            "drive.google.com": self.get_google_drive_direct_download_link,
            "archive.org": self.get_archive_org_download_links,
            "github.com": self.find_github_downloads
        }

    #Sets the Path for the Debrid:
    def set_download_path(self, url):
        self.activePath.set_path(url)

    # Figures out Which Site to Download From
    def get_site(self, url):
        domain_pattern = r'^(?:https?://)?(?:www\.)?([^/:]+)'
        match = re.search(domain_pattern, url)

        if match:
            return match.group(1)
        else:
            raise ValueError("Invalid URL")

    # Method to Download from Google Drive
    def get_google_drive_direct_download_link(self, url):
        file_id_pattern = r'(?:/file/d/|id=)([\w-]+)'
        match = re.search(file_id_pattern, url)

        if match:
            file_id = match.group(1)
            direct_download_link = f'https://drive.google.com/uc?export=download&id={file_id}'
            return [direct_download_link]  # Wrap the direct_download_link in a list
        else:
            raise ValueError("Invalid Google Drive URL")

    # Method to Download from Archive.org
    def get_archive_org_download_links(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')

        download_links = []
        base_url = "https://archive.org"
        for link in links:
            href = link.get('href')
            if href and (href.endswith('.pdf') or href.endswith('.docx') or href.endswith('.zip') or href.endswith('.mp4') or href.endswith('.torrent')):
                full_url = base_url + href
                download_links.append(full_url)

        return download_links

    # Method to Download from GitHub
    def find_github_downloads(self, url):
        url += "/releases"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        releases_section = soup.find('div', {'id': 'releases'})
        if not releases_section:
            return []

        download_links = []
        for button in releases_section.find_all('a', {'href': True}):
            href = button['href']
            if href.endswith('.zip') or href.endswith('.tar.gz'):
                download_links.append(href)

        return download_links

    # The Core Method to Find Downloads from a Given URL
    def find_all_downloads(self, text):
        urls = find_urls(text)
        all_download_links = set()
        for url in urls:
            site = self.get_site(url)
            if site in self.site_methods:
                download_links = self.site_methods[site](url)
                for link in download_links:
                    all_download_links.add(link)
            else:
                print(f"No method available for site: {site}")

        return list(all_download_links)

    #Allows the Debrid to downlad Files to a Target Path
    def download_single_file(self, url):
        if not self.activePath.get_path():
            raise ValueError("No active path set. Please set the target path before downloading.")

        local_filename = url.split('/')[-1]
        target_path = os.path.join(self.activePath.get_path(), local_filename)

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(target_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        return local_filename

    # Downloads all Debrid Text to a Given Target Path
    def download_to_target(self, text):
        print(f"Downloading to Target Path: {self.activePath.get_path()}")
        
        # Check if the active path is set
        if not self.activePath.get_path():
            raise ValueError("No active path set. Please set the target path before downloading.")

        # Collect download links
        download_links = self.find_all_downloads(text)

        # Download each file to the specified path
        for url in download_links:
            local_filename = url.split('/')[-1]
            target_path = os.path.join(self.activePath.get_path(), local_filename)

            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(target_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            print(f"Downloaded {local_filename} to {target_path}")
    

# Method that uses regular expressions to find all the URLs in a text and return them as an array
def find_urls(text):
    urls = []
    pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    for url in re.findall(pattern, text):
        urls.append(url)
    return urls


'''# Example usage
text = "hey guys I found this cool website https://archive.org/details/quake-3-arena you should check it out"
finder = Debrid()
downloads = finder.find_all_downloads(text)
print(downloads)'''

