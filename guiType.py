import tkinter as tk
from tkinter import messagebox
import gtts
import playsound
import time
import random

# Create the welcome sound file
text = 'Welcome! You have successfully logged in this page'
sound = gtts.gTTS(text, lang='en')
sound.save('welcome.mp3')

# Typing Master functionality
dic = {}

def calculate_wpm(words_typed, time_taken):
    words_per_minute = (words_typed / 5) / (time_taken / 60)
    return round(words_per_minute, 2)

def start_typing(name):
    text = [
        "In the heart of a tranquil town, an ancient library cradled forgotten tales. Emma, a curious girl, unearthed a dusty book one day. As its pages unfurled, she danced through enchanted realms. Emma's daily returns breathed life into the neglected haven, transforming it into a sanctuary of imagination. Word of her discoveries spread, and soon, the library echoed with laughter. Inspired by Emma's tales, the townsfolk rekindled their love for reading. The once-silent library emerged as a testament to the profound impact a single, dusty book, and an inquisitive spirit, could have on an entire community, unveiling the magic within forgotten stories.",
        # Add more texts here
    ]

    random_text = random.choice(text)
    
    def calculate_result():
        end_time = time.time()
        user_input = typing_area.get("1.0", tk.END).strip()
        words_typed = len(user_input.split())
        time_taken = end_time - start_time
        
        wpm = calculate_wpm(words_typed, time_taken)
        errors = sum(1 for i, j in zip(random_text.split(), user_input.split()) if i != j)

        result_msg = f"Words per minute: {wpm}\nErrors: {errors}"
        messagebox.showinfo("Typing Test Result", result_msg)
        
        update_leaderboard(name, wpm, errors)
        
        typing_screen.destroy()
        show_welcome(name)
    
    typing_screen = tk.Tk()
    typing_screen.title("Typing Speed Checker")
    typing_screen.configure(bg='#e9ecef')
    typing_screen.geometry('800x600')

    tk.Label(typing_screen, text="Type the following text:", font=('Helvetica', 14), bg='#e9ecef').pack(pady=10)
    tk.Label(typing_screen, text=random_text, wraplength=700, font=('Helvetica', 12), bg='#e9ecef', fg='#495057').pack(pady=10)
    tk.Label(typing_screen, text="Start typing below:", font=('Helvetica', 14), bg='#e9ecef').pack(pady=10)

    typing_area = tk.Text(typing_screen, height=10, width=60, font=('Helvetica', 12))
    typing_area.pack(pady=10)
    tk.Button(typing_screen, text="Submit", font=('Helvetica', 14), command=calculate_result, bg='#007bff', fg='#ffffff').pack(pady=20)
    
    start_time = time.time()
    typing_screen.mainloop()

def show_leaderboard():
    leaderboard_screen = tk.Tk()
    leaderboard_screen.title("Leaderboard")
    leaderboard_screen.configure(bg='#e9ecef')
    leaderboard_screen.geometry('800x600')

    tk.Label(leaderboard_screen, text="Leaderboard", font=('Helvetica', 24), bg='#e9ecef').pack(pady=20)

    try:
        with open("leaderboard.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                tk.Label(leaderboard_screen, text="Leaderboard is empty.", font=('Helvetica', 14), bg='#e9ecef').pack(pady=20)
            else:
                leaderboard_msg = ""
                data_list = []
                for line in lines:
                    data = line.strip().split(",")
                    if len(data) >= 3:
                        data_list.append((data[0], float(data[1]), int(data[2])))

                sorted_data = sorted(data_list, key=lambda x: (-x[1], x[2]))

                for i, entry in enumerate(sorted_data, start=1):
                    name, wpm, errors = entry
                    leaderboard_msg += f"{i}. {name}: WPM - {wpm}, Errors - {errors}\n"
                
                tk.Label(leaderboard_screen, text=leaderboard_msg, font=('Helvetica', 12), bg='#e9ecef').pack(pady=10)

    except FileNotFoundError:
        tk.Label(leaderboard_screen, text="Leaderboard not found. No scores yet.", font=('Helvetica', 14), bg='#e9ecef').pack(pady=20)

    tk.Button(leaderboard_screen, text="Back to Welcome", font=('Helvetica', 14), command=lambda: [leaderboard_screen.destroy(), show_welcome()]).pack(pady=20)
    leaderboard_screen.mainloop()

def update_leaderboard(name, wpm, errors):
    try:
        filename = "leaderboard.txt"
        with open(filename, "r") as file:
            lines = file.readlines()

        found = False
        for i in range(len(lines)):
            data = lines[i].strip().split(",")
            if len(data) >= 3 and data[0] == name:
                lines[i] = f"{name},{wpm},{errors}\n"
                found = True
                break

        if not found:
            lines.append(f"{name},{wpm},{errors}\n")

        with open(filename, "w") as file:
            file.writelines(lines)

    except FileNotFoundError:
        with open(filename, "w") as file:
            file.write(f"{name},{wpm},{errors}\n")

def show_welcome(name=None):
    top = tk.Tk()
    top.configure(bg='skyblue')
    top.title('Welcome Page')
    top.geometry('600x400')

    tk.Label(top, text='Welcome!', font=('Arial', 30), fg='white', bg='skyblue').pack(pady=20)
    
    if name:
        tk.Label(top, text=f'Hello, {name}!', font=('Arial', 20), fg='white', bg='skyblue').pack(pady=10)
    
    tk.Button(top, text='Start Typing Master', font=('Arial', 15), bg='#007bff', fg='#ffffff', command=lambda: [top.destroy(), start_typing(name)]).pack(pady=10)
    tk.Button(top, text='Show Leaderboard', font=('Arial', 15), bg='#28a745', fg='#ffffff', command=show_leaderboard).pack(pady=10)
    tk.Button(top, text='Exit', font=('Arial', 15), bg='#dc3545', fg='#ffffff', command=top.destroy).pack(pady=10)

    top.mainloop()

def validate_login():
    username = entry1.get()
    password = entry2.get()

    if username == '' or password == '':
        messagebox.showerror('Login', 'Fill in all the required information')
    else:
        if not username.replace(" ", "").isalpha():
            messagebox.showerror('Login', 'Username should contain only alphabets.')
        else:
            min_length = 8
            has_letter = False
            has_digit = False
            has_symbol = False
            for char in password:
                if char.isalpha():
                    has_letter = True
                elif char.isdigit():
                    has_digit = True
                elif not char.isalnum():
                    has_symbol = True
            if len(password) <= min_length or not (has_letter and has_digit and has_symbol):
                messagebox.showerror('Login', 'Password should contain alphabets, symbols, and digits.')
            else:
                messagebox.showinfo('Login', 'Login successful!')
                playsound.playsound('welcome.mp3')
                root.destroy()
                show_welcome(username)

# Create and show the login screen
root = tk.Tk()
root.config(bg='#333333')

global entry1
global entry2
root.title('Login Page')

tk.Label(root, text='Login Page', bg='cyan4', fg='cyan', font=('Arial', 24)).place(x=500, y=20)
tk.Label(root, text='UserName:', font=('Arial', 20), bg='cyan4', fg='white').place(x=310, y=190)
tk.Label(root, text='Password:', font=('Arial', 20), bg='cyan4', fg='white').place(x=310, y=340)

entry1 = tk.Entry(root, font=('Arial', 15))
entry1.place(x=600, y=200)
entry2 = tk.Entry(root, font=('Arial', 15), show='*')
entry2.place(x=600, y=350)

tk.Button(root, text='Login', bg='cyan3', font=('Arial', 15), bd=5, command=validate_login).place(x=600, y=500)

root.mainloop()
