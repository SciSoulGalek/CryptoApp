import tkinter as tk
from tkinter import scrolledtext, messagebox
from pathlib import Path
import json
import random
import math

class RSADSS:
    def __init__(self, selector_root):
        self.selector_root = selector_root
        self.root = tk.Toplevel()
        self.root.title("RSA DSS Algorithm")
        self.root.geometry("600x620")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.public_key = ""
        self.message_value = ""   
        self.signature_value = ""

        self.log_panel = scrolledtext.ScrolledText(self.root, width=70, height=20, wrap=tk.WORD)
        self.log_panel.place(x=20, y=20)

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

    #Labels, fields and buttons
    def create_widgets(self):
        tk.Label(self.root, text="Enter p:").place(x=20, y=360)
        self.p_entry = tk.Entry(self.root, width=20)
        self.p_entry.insert(0, "61")
        self.p_entry.place(x=120, y=360)

        tk.Label(self.root, text="Enter q:").place(x=20, y=390)
        self.q_entry = tk.Entry(self.root, width=20)
        self.q_entry.insert(0, "53")
        self.q_entry.place(x=120, y=390)

        tk.Label(self.root, text="Enter e:").place(x=20, y=420)
        self.e_entry = tk.Entry(self.root, width=20)
        self.e_entry.insert(0, "17")
        self.e_entry.place(x=120, y=420)

        tk.Button(self.root, text="Generate Keys", command=self.generate_keys, bg="lightblue").place(x=498, y=360)

        tk.Label(self.root, text="Enter n:").place(x=300, y=420)
        self.n_entry = tk.Entry(self.root, width=20)
        self.n_entry.insert(0, "17")
        self.n_entry.place(x=390, y=420)

        tk.Label(self.root, text="Enter Message to Sign:").place(x=20, y=460)
        self.sign_entry = tk.Entry(self.root, width=63)
        self.sign_entry.place(x=200, y=460)

        tk.Button(self.root, text="Sign", command=self.sign_number, bg="lightgreen").place(x=530, y=485)

        tk.Label(self.root, text="Enter Singatures to Verify:").place(x=20, y=525)
        self.verify_entry = tk.Entry(self.root, width=63)
        self.verify_entry.place(x=200, y=525)

        tk.Button(self.root, text="Verify", command=self.verify_number, bg="orange").place(x=530, y=555)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_rsa_dss_data, bg="lightgreen")
        self.save_button.place(x=500, y=590)

        self.load_button = tk.Button(self.root, text="Load", command=self.load_rsa_dss_data, bg="orange")
        self.load_button.place(x=545, y=590)

    #Data saver and loader
    def save_rsa_dss_data(self):
        file_path = Path(__file__).parent / "rsa_dss_data.json"
        data = {
            "p": self.p_entry.get(),
            "q": self.q_entry.get(),
            "e": self.e_entry.get(),
            "n": self.n_entry.get(),
            "message": str(self.message_value),
            "signature": str(self.signature_value),
        }
        with file_path.open("w") as file:
            json.dump(data, file)
            self.log_message("Data saved successfully.", "green")

    def load_rsa_dss_data(self):
        try:
            file_path = Path(__file__).parent / "rsa_dss_data.json"
            with file_path.open("r") as file:
                data = json.load(file)

            self.p_entry.delete(0, "end")
            self.p_entry.insert(0, data["p"])

            self.q_entry.delete(0, "end")
            self.q_entry.insert(0, data["q"])

            self.e_entry.delete(0, "end")
            self.e_entry.insert(0, data["e"])

            self.n_entry.delete(0, "end")
            self.n_entry.insert(0, data["n"])

            self.message_value = data["message"]
            self.signature_value = data["signature"]

            self.sign_entry.delete(0, tk.END)
            self.sign_entry.insert(0, self.message_value)

            self.verify_entry.delete(0, tk.END)
            self.verify_entry.insert(0, self.signature_value)

            self.log_message("Data loaded successfully.", "green")
        except FileNotFoundError:
            print("No saved data found.")

    #Math
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

            if not (self.isprime(p) and self.isprime(q)):
                raise ValueError("p and q must both be prime.")

            n = p * q
            phi_n = (p - 1) * (q - 1)

            if math.gcd(e, phi_n) != 1:
                raise ValueError("e must be coprime with φ(n).")

            d = pow(e, -1, phi_n)

            self.public_key = (e, n)
            self.key_data["p"], self.key_data["q"], self.key_data["e"], self.key_data["d"], self.key_data["n"] = p, q, e, d, n
            self.log_panel.delete(1.0, tk.END)
            self.log_message(f"Keys Generated!\nPublic: (e={e}, n={n})\nPrivate: d = {d}", "blue")
            self.n_entry.delete(0, tk.END)
            self.n_entry.insert(0, n)
        except ValueError as ex:
            messagebox.showerror("Input Error", str(ex))


    def sign_number(self):
        try:
            d, n = self.key_data["d"], self.key_data["n"]
            message = int(self.sign_entry.get())
            if message >= n:
                raise ValueError("Message must be less than n.")

            signature = pow(message, d, n)

            self.message_value = message
            self.signature_value = signature

            self.log_message(f"Signed: {message} → {signature}", "green")
            self.sign_entry.delete(0, tk.END)
            self.verify_entry.delete(0, tk.END)
            self.verify_entry.insert(0, signature)
        except (KeyError, ValueError) as ex:
            self.log_message(f"Error: {str(ex)}", "red")

    def verify_number(self):
        try:
            e, n = self.key_data["e"], self.key_data["n"]
            signature = int(self.verify_entry.get())
            message = int(self.sign_entry.get())

            decrypted = pow(signature, e, n)

            if decrypted == message:
                self.log_message("Signature Verified", "green")
                self.log_message(f"Verified: {signature} → {message}", "orange")
            else:
                self.log_message("Signature Failed to Verify", "red")

            self.verify_entry.delete(0, tk.END)
        except (KeyError, ValueError) as ex:
            self.log_message(f"Error: {str(ex)}", "red")
