import tkinter as tk
import hashlib
import SecureAlgorithm as secure

# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Main page GUI
def main_page(login_window):
    login_window.destroy()
    main_window = tk.Tk()
    main_window.title("Main Page")
    
    # Function to reverse the string
    def reverse_string():
        input_string = input_box.get()
        eversed_string = secure.chained_encrypt(input_string)
        reversed_string = secure.chained_decrypt(eversed_string)
        output_box.delete(0, tk.END)
        output_box.insert(0, reversed_string)

    # Input label and entry
    input_label = tk.Label(main_window, text="Enter a string:")
    input_label.grid(row=0, column=0)
    input_box = tk.Entry(main_window)
    input_box.grid(row=0, column=1)
    
    # Output label and entry
    output_label = tk.Label(main_window, text="Reversed string:")
    output_label.grid(row=1, column=0)
    output_box = tk.Entry(main_window,width=100)
    output_box.grid(row=1, column=1)
    
    # Reverse button
    reverse_button = tk.Button(main_window, text="Reverse", command=reverse_string)
    reverse_button.grid(row=2, column=1)
    
    main_window.mainloop()

# Function to check user credentials in the file
def check_credentials(username, password):
    with open("users.txt", "r") as file:
        for line in file:
            u, p = line.strip().split(",")
            if u == username and p == hash_password(password):
                return True
    return False

# Function to add a new user to the file
def add_user(username, password):
    with open("users.txt", "a") as file:
        file.write("{},{}\n".format(username, hash_password(password)))

def authenticate_user(username, password, login_window):
    if check_credentials(username,password):
        main_page(login_window)
    else:
        error_label = tk.Label(login_window, text="Invalid username or password")
        error_label.grid(row=3, column=1)

# Login page GUI
def login_page():
    login_window = tk.Tk()
    login_window.title("Login Page")
    
    # Username label and entry
    username_label = tk.Label(login_window, text="Username:")
    username_label.grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)
    
    # Password label and entry
    password_label = tk.Label(login_window, text="Password:")
    password_label.grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1)
    
    # Login button
    login_button = tk.Button(login_window, text="Login", command=lambda: authenticate_user(username_entry.get(), password_entry.get(), login_window))
    login_button.grid(row=2, column=1)
    
    # Sign up button
    signup_button = tk.Button(login_window, text="Sign up", command=lambda: signup_page(login_window))
    signup_button.grid(row=3, column=1)
    
    login_window.mainloop()

# Sign up page GUI
def signup_page(login_window):
    signup_window = tk.Toplevel(login_window)
    signup_window.title("Sign Up")
    
    # Username label and entry
    username_label = tk.Label(signup_window, text="Username:")
    username_label.grid(row=0, column=0)
    username_entry = tk.Entry(signup_window)
    username_entry.grid(row=0, column=1)
    
    # Password label and entry
    password_label = tk.Label(signup_window, text="Password:")
    password_label.grid(row=1, column=0)
    password_entry = tk.Entry(signup_window, show="*")
    password_entry.grid(row=1, column=1)
    
    # Confirm password label and entry
    confirm_label = tk.Label(signup_window, text="Confirm Password:")
    confirm_label.grid(row=2, column=0)
    confirm_entry = tk.Entry(signup_window)
    confirm_entry.grid(row=2, column=1)
    
    # Sign up button
    signup_button = tk.Button(signup_window, text="Sign up", command=lambda: add_new_user(username_entry.get(), password_entry.get(), confirm_entry.get(), signup_window))
    signup_button.grid(row=3, column=1)
    
    signup_window.mainloop()

# Function to add a new user to the file
def add_new_user(username, password, confirm, signup_window):
    if password == confirm:
        add_user(username,password)
        signup_window.destroy()
   
login_page()