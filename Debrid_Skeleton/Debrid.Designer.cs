namespace Debrid_Skeleton
{
    partial class Debrid
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            getLink_button = new Button();
            account_button = new Button();
            exit_button = new Button();
            label1 = new Label();
            link_listBox = new ListBox();
            Link_Textbox = new RichTextBox();
            label2 = new Label();
            label3 = new Label();
            SuspendLayout();
            // 
            // getLink_button
            // 
            getLink_button.Location = new Point(196, 225);
            getLink_button.Name = "getLink_button";
            getLink_button.Size = new Size(75, 23);
            getLink_button.TabIndex = 0;
            getLink_button.Text = "Get Link";
            getLink_button.UseVisualStyleBackColor = true;
            getLink_button.Click += getLink_button_Click;
            // 
            // account_button
            // 
            account_button.Location = new Point(196, 272);
            account_button.Name = "account_button";
            account_button.Size = new Size(75, 23);
            account_button.TabIndex = 1;
            account_button.Text = "Account";
            account_button.UseVisualStyleBackColor = true;
            account_button.Click += account_button_Click;
            // 
            // exit_button
            // 
            exit_button.Location = new Point(196, 320);
            exit_button.Name = "exit_button";
            exit_button.Size = new Size(75, 23);
            exit_button.TabIndex = 2;
            exit_button.Text = "Exit";
            exit_button.UseVisualStyleBackColor = true;
            exit_button.Click += exit_button_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(196, 47);
            label1.Name = "label1";
            label1.Size = new Size(381, 15);
            label1.TabIndex = 4;
            label1.Text = "Hello, welcome to the Debrid! Please enter a URL and click on a button.";
            // 
            // link_listBox
            // 
            link_listBox.FormattingEnabled = true;
            link_listBox.ItemHeight = 15;
            link_listBox.Location = new Point(350, 225);
            link_listBox.Name = "link_listBox";
            link_listBox.Size = new Size(227, 139);
            link_listBox.TabIndex = 5;
            link_listBox.SelectedIndexChanged += link_listBox_SelectedIndexChanged;
            // 
            // Link_Textbox
            // 
            Link_Textbox.Location = new Point(196, 127);
            Link_Textbox.Name = "Link_Textbox";
            Link_Textbox.Size = new Size(381, 54);
            Link_Textbox.TabIndex = 6;
            Link_Textbox.Text = "";
            Link_Textbox.TextChanged += Link_Textbox_TextChanged;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(350, 207);
            label2.Name = "label2";
            label2.Size = new Size(109, 15);
            label2.TabIndex = 7;
            label2.Text = "Download Options:";
            label2.Click += label2_Click;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(196, 109);
            label3.Name = "label3";
            label3.Size = new Size(105, 15);
            label3.TabIndex = 8;
            label3.Text = "Insert Link(s) Here:";
            // 
            // Debrid
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(Link_Textbox);
            Controls.Add(link_listBox);
            Controls.Add(label1);
            Controls.Add(exit_button);
            Controls.Add(account_button);
            Controls.Add(getLink_button);
            Name = "Debrid";
            Text = "Debrid";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button getLink_button;
        private Button account_button;
        private Button exit_button;
        private Label label1;
        private ListBox link_listBox;
        private RichTextBox Link_Textbox;
        private Label label2;
        private Label label3;
    }
}