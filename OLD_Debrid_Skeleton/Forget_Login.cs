using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Debrid_Skeleton
{
    public partial class Forget_Login : Form
    {
        public Forget_Login()
        {
            InitializeComponent();
        }

        private void submitEmail_Button_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Thanks, an email has been sent! Please follow the directions!");
        }

        private void button_Exit_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
