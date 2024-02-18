from tkinter import *
import string
import secrets
import pyperclip
import pyttsx3
from pathlib import Path

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def generate_password():
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    all_characters = upper + lower + digits + punctuation
    password_len = int(length_box.get())

    part1 = round(password_len * (30 / 100))  # letters % 60
    part2 = round(password_len * (20 / 100))  # digits + punc % 40
    password = ""
    for _ in range(part1):
        password += secrets.choice(upper)
        password += secrets.choice(digits)

    for _ in range(part2):
        password += secrets.choice(punctuation)
        password += secrets.choice(lower)

    password_field.delete(0, END)
    password_field.insert(0, password)

    # Speak the generated password
    global pass_temp
    pass_temp = password
    root.after(90, lambda: speak("Generated password: " + password))

def copy_to_clipboard():
    random_password = password_field.get()
    pyperclip.copy(random_password)

    # Specify the path to the desktop where you want to save the text file
    desktop_path = Path.home() / "Desktop"
    if not desktop_path.exists():
        desktop_path.mkdir(parents=True)

    # Specify the path for the text file on the desktop
    file_path = desktop_path / "generated_password.txt"

    try:
        # Save the password to the text file
        with open(file_path, 'w') as file:
            file.write(random_password)

        # Speak the message
        speak("Password copied to clipboard ")
    except Exception as e:
        print(f"Error saving password to file: {e}")
        speak("Error saving password to file. Please check the folder path.")

def txt_file():
    try:
        f = open("Passwords.txt", 'w')
        f.write(f"{password_field.get()}\n")
    except FileNotFoundError:
        f = open("Passwords.txt", 'w')
        f.write(f"{password_field.get()}\n")
    finally:
        f.close()


# Build Window
root = Tk()
root.title(" Password Generator")

my_color = '#001c33'  # Dark blue background
font_color = '#00bcd4'  # Cyan font color
highlight_color = '#005c83'  # Darker blue for highlighting
root.config(bg=my_color)
font = ('Arial', 13, 'bold')
spin_color='black'

# Set the window size and position it in the center of the screen
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create labels and entry widgets
password_label = Label(root, text=' Password Generator', font=('Arial', 18, 'bold'), bg=my_color, fg=font_color)
password_label.grid(row=0, column=0, pady=10, columnspan=2)

length_label = Label(root, text="Password Length", font=('Arial', 13, 'bold'), bg=my_color, fg=font_color)
length_label.grid(row=1, column=0)

length_box = Spinbox(root, from_=8, to_=34, bg="black",background="grey", fg=spin_color, font=font, width=5, wrap=True)
length_box.grid(row=1, column=1, pady=10)

generate_button = Button(root, text='Generate', font=(font, 10, 'bold'), bg="#00bcd4", fg=my_color,
                         activebackground=highlight_color, command=generate_password)
generate_button.grid(row=2, column=0, pady=5, columnspan=2)

password_field = Entry(root, width=20, bd=2, font=font)
password_field.grid(row=3, column=0, columnspan=2, pady=5)

copy_button = Button(root, text='Copy to Clipboard', font=(font, 10, 'bold'), bg="#00bcd4", fg=my_color,
                     activebackground=highlight_color, command=copy_to_clipboard)
copy_button.grid(row=4, column=0, pady=5, columnspan=2)

txt_button = Button(root, text="Add to Text File", font=(font, 10, 'bold'), bg="#00bcd4", fg=my_color,
                    activebackground=highlight_color, command=txt_file)
txt_button.grid(row=5, column=0, pady=5, columnspan=2)

# Load your image
imgg = PhotoImage(file="C:\\Users\\Siddhesh\\OneDrive\\Documents\\python project\\fd905511133a4cd27d1ce30d666b89e4.png")

# Create a canvas
canvas = Canvas(root, width=300, height=300, bg=my_color, borderwidth=0, highlightthickness=0)
canvas.grid(row=0, column=2, rowspan=6, padx=10)

# Calculate the center of the canvas
canvas_center_x = canvas.winfo_reqwidth() / 2
canvas_center_y = canvas.winfo_reqheight() / 2

# Create the image on the canvas with anchor set to the center
logo = canvas.create_image(canvas_center_x, canvas_center_y, image=imgg)

# Grid the canvas
canvas.grid()
root.mainloop()
