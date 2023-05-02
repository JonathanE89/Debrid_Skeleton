namespace Debrid_Skeleton
{
    partial class Account
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            textBox3 = new TextBox();
            createAccount_button = new Button();
            returnHome_button = new Button();
            exisitingAccount_button = new Button();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(355, 93);
            label1.Name = "label1";
            label1.Size = new Size(143, 15);
            label1.TabIndex = 0;
            label1.Text = "Create your account here!";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(136, 168);
            label2.Name = "label2";
            label2.Size = new Size(140, 15);
            label2.TabIndex = 1;
            label2.Text = "Please enter a username: ";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(136, 209);
            label3.Name = "label3";
            label3.Size = new Size(138, 15);
            label3.TabIndex = 2;
            label3.Text = "Please enter a password: ";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(136, 251);
            label4.Name = "label4";
            label4.Size = new Size(186, 15);
            label4.TabIndex = 3;
            label4.Text = "Please enter a confirmation email:";
            // 
            // textBox1
            // 
            textBox1.Location = new Point(372, 164);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(168, 23);
            textBox1.TabIndex = 4;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(372, 208);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(168, 23);
            textBox2.TabIndex = 5;
            // 
            // textBox3
            // 
            textBox3.Location = new Point(370, 254);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(170, 23);
            textBox3.TabIndex = 6;
            // 
            // createAccount_button
            // 
            createAccount_button.Location = new Point(272, 323);
            createAccount_button.Name = "createAccount_button";
            createAccount_button.Size = new Size(112, 23);
            createAccount_button.TabIndex = 7;
            createAccount_button.Text = "Create Account";
            createAccount_button.UseVisualStyleBackColor = true;
            createAccount_button.Click += createAccount_button_Click;
            // 
            // returnHome_button
            // 
            returnHome_button.Location = new Point(562, 323);
            returnHome_button.Name = "returnHome_button";
            returnHome_button.Size = new Size(75, 23);
            returnHome_button.TabIndex = 8;
            returnHome_button.Text = "Home";
            returnHome_button.UseVisualStyleBackColor = true;
            returnHome_button.Click += returnHome_button_Click;
            // 
            // exisitingAccount_button
            // 
            exisitingAccount_button.Location = new Point(412, 305);
            exisitingAccount_button.Name = "exisitingAccount_button";
            exisitingAccount_button.Size = new Size(117, 59);
            exisitingAccount_button.TabIndex = 9;
            exisitingAccount_button.Text = "Already have an account? Click here.";
            exisitingAccount_button.UseVisualStyleBackColor = true;
            exisitingAccount_button.Click += exisitingAccount_button_Click;
            // 
            // Form2
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(exisitingAccount_button);
            Controls.Add(returnHome_button);
            Controls.Add(createAccount_button);
            Controls.Add(textBox3);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Name = "Form2";
            Text = "Account";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private TextBox textBox1;
        private TextBox textBox2;
        private TextBox textBox3;
        private Button createAccount_button;
        private Button returnHome_button;
        private Button exisitingAccount_button;
    }
}