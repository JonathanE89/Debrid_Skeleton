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
    public partial class Account : Form
    {
        public Account()
        {
            InitializeComponent();
        }

        private void createAccount_button_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Thanks! A confirmation email was sent to you.");
        }

        private void returnHome_button_Click(object sender, EventArgs e)
        {
            this.Close();

        }

        private void exisitingAccount_button_Click(object sender, EventArgs e)
        {
            Existing_Users form3 = new Existing_Users();
            form3.Show();
        }
    }
}
