namespace Debrid_Skeleton
{
    partial class Forget_Login
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
            Forgot_Password_Label = new Label();
            email_Textbox = new TextBox();
            Email_label = new Label();
            submitEmail_Button = new Button();
            button_Exit = new Button();
            SuspendLayout();
            // 
            // Forgot_Password_Label
            // 
            Forgot_Password_Label.AutoSize = true;
            Forgot_Password_Label.Location = new Point(202, 92);
            Forgot_Password_Label.Name = "Forgot_Password_Label";
            Forgot_Password_Label.Size = new Size(418, 15);
            Forgot_Password_Label.TabIndex = 0;
            Forgot_Password_Label.Text = "Please enter your info here, and we will send you a link to access your account";
            // 
            // email_Textbox
            // 
            email_Textbox.Location = new Point(270, 187);
            email_Textbox.Name = "email_Textbox";
            email_Textbox.Size = new Size(232, 23);
            email_Textbox.TabIndex = 1;
            // 
            // Email_label
            // 
            Email_label.AutoSize = true;
            Email_label.Location = new Point(157, 195);
            Email_label.Name = "Email_label";
            Email_label.Size = new Size(95, 15);
            Email_label.TabIndex = 2;
            Email_label.Text = "Enter email here:";
            // 
            // submitEmail_Button
            // 
            submitEmail_Button.Location = new Point(270, 240);
            submitEmail_Button.Name = "submitEmail_Button";
            submitEmail_Button.Size = new Size(126, 23);
            submitEmail_Button.TabIndex = 3;
            submitEmail_Button.Text = "Submit Email";
            submitEmail_Button.UseVisualStyleBackColor = true;
            submitEmail_Button.Click += submitEmail_Button_Click;
            // 
            // button_Exit
            // 
            button_Exit.Location = new Point(427, 240);
            button_Exit.Name = "button_Exit";
            button_Exit.Size = new Size(75, 23);
            button_Exit.TabIndex = 4;
            button_Exit.Text = "Return";
            button_Exit.UseVisualStyleBackColor = true;
            button_Exit.Click += button_Exit_Click;
            // 
            // Forget_Login
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(button_Exit);
            Controls.Add(submitEmail_Button);
            Controls.Add(Email_label);
            Controls.Add(email_Textbox);
            Controls.Add(Forgot_Password_Label);
            Name = "Forget_Login";
            Text = "Forget_Login";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label Forgot_Password_Label;
        private TextBox email_Textbox;
        private Label Email_label;
        private Button submitEmail_Button;
        private Button button_Exit;
    }
}