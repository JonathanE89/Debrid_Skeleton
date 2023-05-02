using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Debrid_Skeleton
{
    public partial class Existing_Users : Form
    {
        public Existing_Users()
        {
            InitializeComponent();
        }



        private void login_button_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Meow Meow Meow!");
        }

        private void button_Close_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void forgetInfo_Button_Click(object sender, EventArgs e)
        {
            Forget_Login form4= new Forget_Login();
            form4.Show();
        }
    }
}
