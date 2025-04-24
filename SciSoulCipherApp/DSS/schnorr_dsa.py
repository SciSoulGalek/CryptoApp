import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from pathlib import Path
import json, math, random, hashlib

class SchnorrDSA:
    def __init__(self, selector_root):
        self.selector_root = selector_root
        self.root = tk.Toplevel()
        self.root.title("SchnorrDSA Algorithm")
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

        self.save_button = tk.Button(self.root, text="Save", command=self.save_dsa_data, bg="lightgreen")
        self.save_button.place(x=500, y=590)

        self.load_button = tk.Button(self.root, text="Load", command=self.load_dsa_data, bg="orange")
        self.load_button.place(x=545, y=590)

        self.hash_label = tk.Label(self.root, text="Hash Algorithm:")
        self.hash_label.place(x=230, y=360)
        
        self.hash_var = tk.StringVar()
        self.hash_var.set("256")  # Default to SHA-256
        
        self.hash_dropdown = ttk.Combobox(self.root, textvariable=self.hash_var, values=["256", "384", "512"], state="readonly")
        self.hash_dropdown.place(x=340, y=360)


    #Data saver and loader
    def save_dsa_data(self):
        file_path = Path(__file__).parent / "schnorr_dsa_data.json"
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

    def load_dsa_data(self):
        try:
            file_path = Path(__file__).parent / "schnorr_dsa_data.json"
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

    #Encryption Process
    def sha256_hash(self, m):
        concat = f"{m}".encode()
        h = hashlib.sha256(concat).hexdigest()
        return int(h, 16)
    
    def find_large_prime_factor(self, n):
        for i in range(n // 2, 1, -1):
            if n % i == 0 and self.isprime(i):
                return i
        return None

    def generate_keys(self):
        try:
            p = int(self.p_entry.get())
            g = int(self.g_entry.get())
            x = int(self.x_entry.get())

            if not self.isprime(p):
                raise ValueError("p must be a prime number.")
            if not (2 <= g <= p - 2):
                raise ValueError("g must be between 2 and p - 2.")
          
            q = self.find_large_prime_factor(p - 1)
            if not q:
                raise ValueError("Failed to find suitable q where q | (p - 1)")

            if not (1 <= x < q):
                raise ValueError("x must be in range [1, q-1]")

            y = pow(g, x, p)
            self.public_key = y
            self.q = q  # Store q for later
            self.key_data["p"], self.key_data["g"], self.key_data["x"], self.key_data["y"], self.key_data["q"] = p, g, x, y, q

            self.log_panel.delete(1.0, tk.END)
            self.log_message(f"Keys Generated!\nPublic: y = {y}\nPrivate: x = {x}\nq = {q}", "blue")
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
            p, g, x, y, q = self.key_data["p"], self.key_data["g"], self.key_data["x"], self.key_data["y"], self.key_data["q"]
            message = self.sign_entry.get().strip()

            k = random.randint(1, q - 1)
            
            hash_int = self.sha256_hash(message)
            s_1 = pow(g, k, p) % q
            s_2 = ((hash_int + x * s_1) * pow(k, -1, q)) % q

            self.message_value = message
            self.signature_1_value = s_1
            self.signature_2_value = s_2

            self.log_message(f"Signed: {message} → (e: {s_1}, s: {s_2})", "green")
            self.verify_1_entry.delete(0, tk.END)
            self.verify_2_entry.delete(0, tk.END)
            self.verify_1_entry.insert(0, int(s_1))
            self.verify_2_entry.insert(0, int(s_2))

        except (KeyError, ValueError):
            self.log_message("Error: Generate keys first or check number format!", "red")

    def verify_number(self):
        try:
            p, g, x, y, q = self.key_data["p"], self.key_data["g"], self.key_data["x"], self.key_data["y"], self.key_data["q"]
            s_1 = int(self.verify_1_entry.get())
            s_2 = int(self.verify_2_entry.get())
            message = self.sign_entry.get().strip()

            hash_int = self.sha2_hash(message) % q

            s_2_inv = pow(s_2, -1, q)
            z1 = (hash_int * s_2_inv) % q
            z2 = (s_1 * s_2_inv) % q

            v = (pow(g, z1, p) * pow(y, z2, p)) % p % q

            if s_1 == v:
                self.log_message("Signature Verified", "green")
                self.log_message(f"Verified: (S_1: {s_1}, S_2: {s_2}) → {message}", "orange")
            else:
                self.log_message("Signature Failed to Verify", "red")

        except (KeyError, ValueError):
            self.log_message("Error: Generate keys first or check signature format!", "red")
