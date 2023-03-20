import SecureAlgorithm as sa
import tkinter
import customtkinter
from PIL import ImageTk,Image
import hashlib

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("1000x700")
app.title(' Welcome to Notencrypt')


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

# Sign up page GUI
def signup_page():
        def cancel():
            signup_window.destroy()

    
        def add_user(username, password):
            with open("users.txt", "a") as file:
                file.write("{},{}\n".format(username, hash_password(password)))

        def add_new_user():
            username=entry1.get()
            password=entry2.get()
            confirm=entry3.get()
            if (password != confirm):
                error_label = customtkinter.CTkLabel(frame2, text="Passwords doesn't match !!",text_color="red")
                error_label.place(x=230, y=190)
            else:
                add_user(username,password)
                signup_window.destroy()
                



        signup_window = customtkinter.CTkToplevel(app)
        signup_window.title("Sign Up")
        signup_window.geometry("800x650")
        signup_window.resizable(False, False)
        signup_window.attributes('-topmost', True)
        img2=ImageTk.PhotoImage(Image.open("signupbg.jpg"))
        l2=customtkinter.CTkLabel(master=signup_window,image=img2)
        l2.pack()
        welcome=customtkinter.CTkLabel(master=signup_window, text="Welcome to Notencrypt",font=('Century Gothic',30))
        welcome.place(x=240, y=75)
        #creating custom frame
        frame2=customtkinter.CTkFrame(master=l2, width=600, height=280, corner_radius=15, bg_color="transparent",)
        frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        l2=customtkinter.CTkLabel(master=frame2, text="Create your Account",font=('Century Gothic',24))
        l2.place(x=180, y=35)
        entry1=customtkinter.CTkEntry(master=frame2, width=250, placeholder_text='Username')
        entry1.place(x=180, y=80)
        entry2=customtkinter.CTkEntry(master=frame2, width=250, placeholder_text='Password', show="*")
        entry2.place(x=180, y=120)
        entry3=customtkinter.CTkEntry(master=frame2, width=250, placeholder_text='Confirm Password')
        entry3.place(x=180, y=160)
        button1 = customtkinter.CTkButton(master=frame2, width=90, text="Sign-Up",command=add_new_user, corner_radius=6)
        button1.place(x=200,y=220) 
        button2 = customtkinter.CTkButton(master=frame2, width=90, text="Cancel",command=cancel ,corner_radius=6)
        button2.place(x=320,y=220) 
        

  

img1=ImageTk.PhotoImage(Image.open("pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=420, height=360, corner_radius=16)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
l2.place(x=100, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=250, placeholder_text='Username')
entry1.place(x=83, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=250, placeholder_text='Password', show="*")
entry2.place(x=83, y=165)

def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()

# Function to check user credentials in the file
def check_credentials(username, password):
    with open("users.txt", "r") as file:
        for line in file:
            u, p = line.strip().split(",")
            if u == username and p == hash_password(password):
                return True
    return False

def button_function():
    username= entry1.get()
    password= entry2.get()
    if check_credentials(username, password):
            app.destroy()
            home()
    else:
        error_label = customtkinter.CTkLabel(frame, text="Invalid Username or Password !!",text_color="red")
        error_label.place(x=110, y=200)
        
    
#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=110, text="Login", command=button_function, corner_radius=7)
button1.place(x=90, y=230)
button2 = customtkinter.CTkButton(master=frame, width=110, text="Sign-up", command=signup_page, corner_radius=7)
button2.place(x=210, y=230)

app.mainloop()