import SecureAlgorithm as sa
import customtkinter
from PIL import ImageTk,Image

# User database (in real-world application, this would be stored securely)
def add_user(username, password):
            with open("users.txt", "a") as file:
             file.write("{},{}\n".format(username,password))

def cancel():
      home.destroy()
def new_note():
      pass
def voice_note():
      pass
def delete_note():
      pass
def home():
    home = customtkinter.CTk()
    home.title("Notencrypt")
    # configure window
    img1=ImageTk.PhotoImage(Image.open("pattern.png"))
    l1=customtkinter.CTkLabel(master=home,image= img1)
    l1.place(x=0,y=0)
    home.geometry(f"{750}x{480}")
    # create sidebar frame with widgets
    sidebar_frame = customtkinter.CTkFrame(master=home,width=140, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    sidebar_frame.grid_rowconfigure(4, weight=1)
    logo_label = customtkinter.CTkLabel(sidebar_frame, text="Notencrypt", font=customtkinter.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, text="Add New Note")
    sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
    sidebar_button_2 = customtkinter.CTkButton(sidebar_frame, text="Add Voice Note")
    sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
    sidebar_button_3 = customtkinter.CTkButton(sidebar_frame, text="Delete a Note")
    sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
    appearance_mode_label = customtkinter.CTkLabel(sidebar_frame, text="Appearance Mode:", anchor="w")
    appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
    appearance_mode_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["Light", "Dark", "System"])
    appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
    scaling_label = customtkinter.CTkLabel(sidebar_frame, text="UI Scaling:", anchor="w")
    scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
    scaling_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"])
    scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))
    entry1 = customtkinter.CTkEntry(master=home, width=400,height=50, placeholder_text="Enter Plain Text",fg_color="transparent", border_width=2,corner_radius=7)
    entry1.place(x=250,y=120,bordermode="inside")
    entry2 = customtkinter.CTkEntry(master=home, width=400,height=50, placeholder_text="Enter Cipher Text",fg_color="transparent", border_width=2,corner_radius=7)
    entry2.place(x=250,y=200,bordermode="inside")
    welcome_label=customtkinter.CTkLabel(master=home,text="Enter text below to perform Encryption or Decryption",width=200,height=40,fg_color="transparent",corner_radius=8)
    welcome_label.place(x=320,y=50)
    def submit1():
          out=sa.chained_encrypt(entry1.get())
          output_label=customtkinter.CTkLabel(master=home,text=out,width=400,height=43,corner_radius=8)
          output_label.place(x=250,y=350)
          success = customtkinter.CTkLabel(home, text="Operation Successful !!",text_color="green")
          success.place(x=380, y=410)
    def submit2():
          out=sa.chained_decrypt(entry2.get())
          output_label=customtkinter.CTkLabel(master=home,text=out,width=400,height=43,corner_radius=8)
          output_label.place(x=250,y=350)
          success = customtkinter.CTkLabel(home, text="Operation Successful !!",text_color="green")
          success.place(x=370, y=530)     
    submit_button1 = customtkinter.CTkButton(master=home, width=100,height=37, text= "Encrypt",command=submit1,fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),corner_radius=7)
    submit_button1.place(x=310,y=280)
    submit_button2 = customtkinter.CTkButton(master=home, width=100,height=37, text= "Decrypt",command=submit2,fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),corner_radius=7)
    submit_button2.place(x=470,y=280)
    
    home.mainloop()
home()