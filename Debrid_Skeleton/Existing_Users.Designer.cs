namespace Debrid_Skeleton
{
    partial class Existing_Users
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
            textBox2 = new TextBox();
            textBox1 = new TextBox();
            label3 = new Label();
            label2 = new Label();
            forgetInfo_Button = new Button();
            login_button = new Button();
            button_Close = new Button();
            SuspendLayout();
            // 
            // textBox2
            // 
            textBox2.Location = new Point(425, 227);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(168, 23);
            textBox2.TabIndex = 9;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(425, 183);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(168, 23);
            textBox1.TabIndex = 8;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(189, 228);
            label3.Name = "label3";
            label3.Size = new Size(138, 15);
            label3.TabIndex = 7;
            label3.Text = "Please enter a password: ";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(189, 187);
            label2.Name = "label2";
            label2.Size = new Size(140, 15);
            label2.TabIndex = 6;
            label2.Text = "Please enter a username: ";
            // 
            // forgetInfo_Button
            // 
            forgetInfo_Button.Location = new Point(425, 292);
            forgetInfo_Button.Name = "forgetInfo_Button";
            forgetInfo_Button.Size = new Size(227, 23);
            forgetInfo_Button.TabIndex = 10;
            forgetInfo_Button.Text = "Forget your login info? Click here.";
            forgetInfo_Button.UseVisualStyleBackColor = true;
            forgetInfo_Button.Click += forgetInfo_Button_Click;
            // 
            // login_button
            // 
            login_button.Location = new Point(246, 292);
            login_button.Name = "login_button";
            login_button.Size = new Size(125, 23);
            login_button.TabIndex = 11;
            login_button.Text = "Login";
            login_button.UseVisualStyleBackColor = true;
            login_button.Click += login_button_Click;
            // 
            // button_Close
            // 
            button_Close.Location = new Point(364, 341);
            button_Close.Name = "button_Close";
            button_Close.Size = new Size(75, 23);
            button_Close.TabIndex = 12;
            button_Close.Text = "Home";
            button_Close.UseVisualStyleBackColor = true;
            button_Close.Click += button_Close_Click;
            // 
            // Form3
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(button_Close);
            Controls.Add(login_button);
            Controls.Add(forgetInfo_Button);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Controls.Add(label3);
            Controls.Add(label2);
            Name = "Form3";
            Text = "Exisiting Users";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox textBox2;
        private TextBox textBox1;
        private Label label3;
        private Label label2;
        private Button forgetInfo_Button;
        private Button login_button;
        private Button button_Close;
    }
}