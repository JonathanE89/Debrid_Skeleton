import requests
import requests
from bs4 import BeautifulSoup

# URL of the website to extract files from
url = 'https://example.com/files/'

# Send a request to the website and get the HTML response
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Loop through each link and extract the href attribute
for link in links:
    href = link.get('href')
    # Check if the link is a file (ends with .pdf, .docx, etc.)
    if href.endswith('.pdf') or href.endswith('.docx'):
        # Download the file
        file_response = requests.get(href)
        # Save the file to disk
        with open(href.split('/')[-1], 'wb') as f:
            f.write(file_response.content)
        print(f'Successfully downloaded {href.split("/")[-1]}')
# Find all video tags on the page
videos = soup.find_all('video')

# Loop through each video tag and extract the source attribute
for video in videos:
    source = video.find('source')
    src = source.get('src')
    # Check if the video is an MP4 file
    if src.endswith('.mp4'):
        # Download the video
        video_response = requests.get(src)
        # Save the video to disk
        with open(src.split('/')[-1], 'wb') as f:
            f.write(video_response.content)
        print(f'Successfully downloaded {src.split("/")[-1]}')
        
for link in links:
    href = link.get('href')
    # Check if the link is a zip file
    if href.endswith('.zip'):
        # Download the zip file
        zip_response = requests.get(href)
        # Save the zip file to disk
        with open(href.split('/')[-1], 'wb') as f:
            f.write(zip_response.content)
        print(f'Successfully downloaded {href.split("/")[-1]}')
