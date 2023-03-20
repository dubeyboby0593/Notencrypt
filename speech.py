import speech_recognition as sr

# User database (in real-world application, this would be stored securely)
def add_user(username, password):
            with open("users.txt", "a") as file:
             file.write("{},{}\n".format(username,password))
# Function to register a new user
def signup():
    print("Welcome to the signup page.")
    
    # Prompt the user to speak their username
    print("Please say your username.")
    with sr.Microphone() as source:
        audio = r.listen(source)
    username = r.recognize_google(audio)
    
    # Prompt the user to speak their password
    print("Please say your password.")
    with sr.Microphone() as source:
        audio = r.listen(source)
    password = r.recognize_google(audio)
    
    add_user(username,password)
    print("Signup successful. Please log in to continue.")

# Function to authenticate a user
def check_credentials(username, password):
        with open("users.txt", "r") as file:
            for line in file:
                u, p = line.strip().split(",")
                if u == username and p == (password):
                    return True
        return False

# Initialize the speech recognizer
r = sr.Recognizer()

# Prompt the user to choose between login and signup
print("Welcome to the authentication system.")
print("Would you like to login or signup?")
with sr.Microphone() as source:
    audio = r.listen(source)
response = r.recognize_google(audio)

# Process the user's response
if response == "login":
    # Prompt the user to speak their username
    print("Please say your username.")
    with sr.Microphone() as source:
        audio = r.listen(source)
    username = r.recognize_google(audio)

    # Prompt the user to speak their password
    print("Please say your password.")
    with sr.Microphone() as source:
        audio = r.listen(source)
    password = r.recognize_google(audio)

    # Authenticate the user
    if check_credentials(username, password):
        print("Authentication successful!")
    else:
        print("Authentication failed.")
elif response == "sign up":
    # Call the signup function to register a new user
    signup()
else:
    print("Invalid response.")