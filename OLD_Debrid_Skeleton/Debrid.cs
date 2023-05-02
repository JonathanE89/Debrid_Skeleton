using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
namespace Debrid_Skeleton
{
    public partial class Debrid : Form
    {
        public Debrid()
        {
            InitializeComponent();
        }

        private void getLink_button_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Getting Link from Text Box");
        }

        private void account_button_Click(object sender, EventArgs e)
        {
            Account form2 = new Account();
            form2.Show();
        }

        private void exit_button_Click(object sender, EventArgs e)
        {
            MessageBox.Show("This is the end of the Debrid. Goodbye!");
            this.Close();
            //process.Kill();
        }

        private void textBox_Link_TextChanged(object sender, EventArgs e)
        {

        }

        private void link_listBox_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        public System.Diagnostics.Process process = new System.Diagnostics.Process();
        private void Link_Textbox_TextChanged(object sender, System.Windows.Forms.LinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start(e.LinkText);
            process = System.Diagnostics.Process.Start("IExplore.exe", e.LinkText);
            /*
            this.Link_Textbox_TextChanged.LinkClicked += new
            System.Windows.Forms.LinkClickedEventHandler
            (this.Link_Textbox_TextChanged); 
            */
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void Link_Textbox_TextChanged(object sender, EventArgs e)
        {

        }
    }
}