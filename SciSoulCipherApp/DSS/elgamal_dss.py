import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from pathlib import Path
import json, math, random, hashlib

class ElGamalDSS:
    def __init__(self, selector_root):
        self.selector_root = selector_root
        self.root = tk.Toplevel()
        self.root.title("ElGamal Algorithm")
        self.root.geometry("600x620")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.public_key = ""
        self.message_value = ""   
        self.signature_1_value = ""
        self.signature_2_value = ""

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
        self.p_entry.place(x=80, y=360)

        tk.Label(self.root, text="Enter g:").place(x=20, y=390)
        self.g_entry = tk.Entry(self.root, width=20)
        self.g_entry.insert(0, "53")
        self.g_entry.place(x=80, y=390)

        tk.Label(self.root, text="Enter x:").place(x=20, y=420)
        self.x_entry = tk.Entry(self.root, width=20)
        self.x_entry.insert(0, "17")
        self.x_entry.place(x=80, y=420)

        tk.Button(self.root, text="Generate Keys", command=self.generate_keys, bg="lightblue").place(x=498, y=420)

        tk.Label(self.root, text="Public Key:").place(x=260, y=420)
        self.y_entry = tk.Entry(self.root, width=20)
        self.y_entry.place(x=340, y=420)

        tk.Label(self.root, text="Enter Message to Sign:").place(x=20, y=460)
        self.sign_entry = tk.Entry(self.root, width=63)
        self.sign_entry.place(x=200, y=460)

        tk.Button(self.root, text="Sign", command=self.sign_number, bg="lightgreen").place(x=530, y=485)

        tk.Label(self.root, text="Enter Singatures to Verify:").place(x=20, y=525)
        self.verify_1_entry = tk.Entry(self.root, width=30)
        self.verify_1_entry.place(x=200, y=525)
        self.verify_2_entry = tk.Entry(self.root, width=30)
        self.verify_2_entry.place(x=400, y=525)

        tk.Button(self.root, text="Verify", command=self.verify_number, bg="orange").place(x=530, y=555)

        self.save_button = tk.Button(self.root, text="Save", command=self.save_elgamal_data, bg="lightgreen")
        self.save_button.place(x=500, y=590)

        self.load_button = tk.Button(self.root, text="Load", command=self.load_elgamal_data, bg="orange")
        self.load_button.place(x=545, y=590)

        self.hash_label = tk.Label(self.root, text="Hash Algorithm:")
        self.hash_label.place(x=230, y=360)
        
        self.hash_var = tk.StringVar()
        self.hash_var.set("256")  # Default to SHA-256
        
        self.hash_dropdown = ttk.Combobox(self.root, textvariable=self.hash_var, values=["256", "384", "512"], state="readonly")
        self.hash_dropdown.place(x=340, y=360)

    #Data saver and loader
    def save_elgamal_data(self):
        file_path = Path(__file__).parent / "elgamal_dss_data.json"
        data = {
            "p": self.p_entry.get(),
            "g": self.g_entry.get(),
            "x": self.x_entry.get(),
            "y": self.public_key,
            "message": str(self.message_value),
            "signature_1": str(self.signature_1_value),
            "signature_2": str(self.signature_2_value)
        }
        with file_path.open("w") as file:
            json.dump(data, file)
            self.log_message("Data saved successfully.", "green")

    def load_elgamal_data(self):
        try:
            file_path = Path(__file__).parent / "elgamal_dss_data.json"
            with file_path.open("r") as file:
                data = json.load(file)

            self.p_entry.delete(0, "end")
            self.p_entry.insert(0, data["p"])

            self.g_entry.delete(0, "end")
            self.g_entry.insert(0, data["g"])

            self.x_entry.delete(0, "end")
            self.x_entry.insert(0, data["x"])

            self.y_entry.delete(0, "end")
            self.y_entry.insert(0, data["y"])

            self.message_value = data["message"]
            self.signature_1_value = data["signature_1"]
            self.signature_2_value = data["signature_2"]

            self.sign_entry.delete(0, tk.END)
            self.sign_entry.insert(0, self.message_value)

            self.verify_1_entry.delete(0, tk.END)
            self.verify_1_entry.insert(0, self.signature_1_value)

            self.verify_2_entry.delete(0, tk.END)
            self.verify_2_entry.insert(0, self.signature_2_value)

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

    def generate_k(self):
        p = int(self.p_entry.get())
        while True:
            k = random.randint(2, p - 2)
            if math.gcd(k, p - 1) == 1:
                return k

    def is_primitive_root(self, g, p):
        if not self.isprime(p):
            return False

        phi = p - 1
        factors = self.get_prime_factors(phi)

        for factor in factors:
            if pow(g, phi // factor, p) == 1:
                return False
        return True

    def get_prime_factors(self, n):
        i = 2
        factors = set()
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors


    def generate_keys(self):
        try:
            p = int(self.p_entry.get())
            g = int(self.g_entry.get())
            x = int(self.x_entry.get())

            if not self.isprime(p):
                raise ValueError("p must be a prime number.")

            if not (2 <= g <= p - 2):
                raise ValueError("g must be between 2 and p - 2.")
            
            if not self.is_primitive_root(g, p):
                raise ValueError(f"g = {g} is not a primitive root modulo {p}.")

            if not (1 <= x <= p - 2):
                raise ValueError("Private key x must be between 1 and p - 2.")

            y = pow(g, x, p)
            if y == 1:
                raise ValueError("Invalid public key: g^x mod p must not be 1.")

            self.public_key = y

            self.key_data["p"], self.key_data["g"], self.key_data["x"], self.key_data["y"] = p, g, x, y 
            self.log_panel.delete(1.0, tk.END)
            self.log_message(f"Keys Generated!\nPublic: y = {y}\nPrivate: x = {x}", "blue")
            self.y_entry.delete(0, tk.END)
            self.y_entry.insert(0, y)

        except ValueError as ex:
            messagebox.showerror("Input Error", str(ex))

    def sha2_hash(self, message: str) -> int:
        hash_choice = self.hash_var.get()
        message_bytes = message.encode()

        if hash_choice == "256":
            digest = hashlib.sha256(message_bytes).digest()
        elif hash_choice == "384":
            digest = hashlib.sha384(message_bytes).digest()
        elif hash_choice == "512":
            digest = hashlib.sha512(message_bytes).digest()
        else:
            raise ValueError("Unsupported SHA version")

        return int.from_bytes(digest, byteorder='big')

    def sign_number(self):
        try:
            p, g, x, y = self.key_data["p"], self.key_data["g"], self.key_data["x"], self.key_data["y"]
            message = int(self.sign_entry.get())
            k = self.generate_k()

            self.message_value = message
            
            signature_1 = pow(g, k, p)
            step_1 = (message - x * signature_1) % (p - 1)
            k_inv = pow(k, -1, (p - 1))
            signature_2 = (step_1 * k_inv) % (p - 1)

            self.signature_1_value = signature_1
            self.signature_2_value = signature_2
            
            self.log_message(f"Signed: {message} → {signature_1}, {signature_2}", "green")
            self.verify_1_entry.delete(0, tk.END)
            self.verify_2_entry.delete(0, tk.END)
            self.verify_1_entry.insert(0, int(signature_1))
            self.verify_2_entry.insert(0, int(signature_2))

        except (KeyError, ValueError):
            self.log_message("Error: Generate keys first or check number format!", "red")

    def verify_number(self):
        try:
            p, g, x, y = self.key_data["p"], self.key_data["g"], self.key_data["x"], self.key_data["y"]
            signature_1 = int(self.verify_1_entry.get())
            signature_2 = int(self.verify_2_entry.get())

            message = int(self.sign_entry.get())

            v_1 = pow(g, message, p)
            v_2 = (pow(y, signature_1, p) * pow(signature_1, signature_2, p)) % p
            
            if v_1 == v_2:
                self.log_message("Signature Verified", "green")
                self.log_message(f"Verified: {signature_1}, {signature_2} → {message}", "orange")
            else:
                self.log_message("Signature Failed to Verify", "red")

        except (KeyError, ValueError):
            self.log_message("Error: Generate keys first or check ciphertext format!", "red")
