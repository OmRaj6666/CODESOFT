import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("300x300")

        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master, width=20)
        self.length_entry.pack()

        self.complexity_label = tk.Label(master, text="Password Complexity:")
        self.complexity_label.pack()

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Alphanumeric")

        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, "Alphanumeric", "Numeric", "Alpha")
        self.complexity_menu.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.pack()

        self.password_text = tk.Text(master, width=30, height=2)
        self.password_text.pack()

    def generate_password(self):
        length = int(self.length_entry.get())
        complexity = self.complexity_var.get()

        if complexity == "Alphanumeric":
            chars = string.ascii_letters + string.digits
        elif complexity == "Numeric":
            chars = string.digits
        else:
            chars = string.ascii_letters

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(tk.END, password)

root = tk.Tk()
password_generator = PasswordGenerator(root)
root.mainloop()