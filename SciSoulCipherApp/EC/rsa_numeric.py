import tkinter as tk
from tkinter import scrolledtext, messagebox
from pathlib import Path
import json

class RSANumericApp:
    def __init__(self, selector_root):
        self.selector_root = selector_root
        self.root = tk.Toplevel()
        self.root.title("RSA Numeric Cryptosystem")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.message_value = ""
        self.ciphertext_value = ""   

        self.log_panel = scrolledtext.ScrolledText(self.root, width=70, height=20, wrap=tk.WORD)
        self.log_panel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.create_widgets()
        self.key_data = {}


    def on_close(self):
        self.root.destroy()
        if self.selector_root:
            self.selector_root.deiconify()

    def log_message(self, message, color="black"):
        self.log_panel.insert(tk.END, message + "\n", color)
        self.log_panel.tag_configure(color, foreground=color)
        self.log_panel.see(tk.END)

    def create_widgets(self):
        tk.Label(self.root, text="Enter p:").grid(row=1, column=0)
        self.p_entry = tk.Entry(self.root, width=10)
        self.p_entry.insert(0, "61")
        self.p_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Enter q:").grid(row=2, column=0)
        self.q_entry = tk.Entry(self.root, width=10)
        self.q_entry.insert(0, "53")
        self.q_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Enter e:").grid(row=3, column=0)
        self.e_entry = tk.Entry(self.root, width=10)
        self.e_entry.insert(0, "17")
        self.e_entry.grid(row=3, column=1)

        tk.Button(self.root, text="Generate Keys", command=self.generate_keys, bg="lightblue").grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        tk.Label(self.root, text="Enter Number to Encrypt:").grid(row=5, column=0)
        self.encrypt_entry = tk.Entry(self.root, width=50)
        self.encrypt_entry.grid(row=5, column=1)

        tk.Button(self.root, text="Encrypt", command=self.encrypt_number, bg="lightgreen").grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        tk.Label(self.root, text="Enter Ciphertext to Decrypt:").grid(row=7, column=0)
        self.decrypt_entry = tk.Entry(self.root, width=50)
        self.decrypt_entry.grid(row=7, column=1)

        tk.Button(self.root, text="Decrypt", command=self.decrypt_number, bg="orange").grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_rsa_data, bg="lightgreen")
        self.save_button.place(relx=0.85, rely=0.99, anchor="se")

        self.load_button = tk.Button(self.root, text="Load", command=self.load_rsa_data, bg="orange")
        self.load_button.place(relx=0.95, rely=0.99, anchor="se")

    def save_rsa_data(self):
        file_path = Path(__file__).parent / "rsa_data_numeric.json"
        data = {
            "p": self.p_entry.get(),
            "q": self.q_entry.get(),
            "e": self.e_entry.get(),
            "message": str(self.message_value),
            "ciphertext": str(self.ciphertext_value)
        }
        with file_path.open("w") as file:
            json.dump(data, file)
            self.log_message("Data saved successfully.", "green")

    def load_rsa_data(self):
        try:
            file_path = Path(__file__).parent / "rsa_data_numeric.json"
            with file_path.open("r") as file:
                data = json.load(file)

            self.p_entry.delete(0, "end")
            self.p_entry.insert(0, data["p"])

            self.q_entry.delete(0, "end")
            self.q_entry.insert(0, data["q"])

            self.e_entry.delete(0, "end")
            self.e_entry.insert(0, data["e"])

            self.message_value = data["message"]
            self.ciphertext_value = data["ciphertext"]

            self.encrypt_entry.delete(0, tk.END)
            self.encrypt_entry.insert(0, self.message_value)

            self.decrypt_entry.delete(0, tk.END)
            self.decrypt_entry.insert(0, self.ciphertext_value)

            self.log_message("Data loaded successfully.", "green")
        except FileNotFoundError:
            print("No saved data found.")

    def isprime(self, n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_keys(self):
        try:
            p = int(self.p_entry.get())
            q = int(self.q_entry.get())
            e = int(self.e_entry.get())

            if p <= 1 or q <= 1 or e <= 1:
                raise ValueError("Numbers must be greater than 1.")
            if p == q:
                raise ValueError("p and q must be distinct primes.")
            if not self.isprime(p) or not self.isprime(q):
                raise ValueError("p and q must be prime numbers.")

            n = p * q
            phi = (p - 1) * (q - 1)

            if e >= phi or pow(e, -1, phi) is None:
                raise ValueError("e must be coprime with φ(n) and less than φ(n).")

            d = pow(e, -1, phi)

            self.key_data["n"], self.key_data["e"], self.key_data["d"] = n, e, d
            self.log_panel.delete(1.0, tk.END)
            self.log_message(f"Keys Generated!\nPublic: (e={e}, n={n})\nPrivate: (phi={phi}, d={d}, n={n})", "blue")

        except ValueError as ex:
            messagebox.showerror("Input Error", str(ex))

    def encrypt_number(self):
        try:
            n, e = self.key_data["n"], self.key_data["e"]
            number = int(self.encrypt_entry.get())

            if number >= n:
                self.log_message("Error: Number too large for encryption!", "red")
                return

            self.message_value = number
            
            ciphertext = pow(number, e, n)
            self.log_message(f"Encrypted: {number} → {ciphertext}", "green")
            self.encrypt_entry.delete(0, tk.END)
            self.decrypt_entry.delete(0, tk.END)
            self.decrypt_entry.insert(0, str(ciphertext))

        except (KeyError, ValueError):
            self.log_message("Error: Generate keys first or check number format!", "red")

    def decrypt_number(self):
        try:
            n, d = self.key_data["n"], self.key_data["d"]
            ciphertext = int(self.decrypt_entry.get())

            self.ciphertext_value = ciphertext

            decrypted_number = pow(ciphertext, d, n)
            self.log_message(f"Decrypted: {ciphertext} → {decrypted_number}", "orange")
            self.decrypt_entry.delete(0, tk.END)

        except (KeyError, ValueError):
            self.log_message("Error: Generate keys first or check ciphertext format!", "red")
