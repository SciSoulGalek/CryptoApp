import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from pathlib import Path
import json, math, random, hashlib
from sympy import isprime

class RSADSS:
    def __init__(self, selector_root):
        self.selector_root = selector_root
        self.root = tk.Toplevel()
        self.root.title("RSA DSS Algorithm")
        self.root.geometry("800x640")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.public_key = ""
        self.message_value = ""   
        self.signature_value = ""

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
    #Log
        self.log_panel = scrolledtext.ScrolledText(self.root)
        self.log_panel.place(relx=0.013, rely=0.023, relheight=0.314, relwidth=0.978)

    #Entries
        #public key
        self.e_entry = tk.Entry(self.root)
        self.e_entry.insert(0, "e")
        self.e_entry.place(relx=0.2, rely=0.391, height=30, relwidth=0.293)

        self.n_entry = tk.Entry(self.root)
        self.n_entry.insert(0, "n")
        self.n_entry.place(relx=0.688, rely=0.391, height=30, relwidth=0.293)
        
        self.hash_var = tk.StringVar()
        self.hash_var.set("256")

        self.hash_dropdown = ttk.Combobox(self.root, textvariable=self.hash_var, values=["256", "384", "512"], state="readonly")
        self.hash_dropdown.place(relx=0.85, rely=0.342, relheight=0.045, relwidth=0.12)

        #private key
        self.p_entry = tk.Entry(self.root)
        self.p_entry.insert(0, "p")
        self.p_entry.place(relx=0.2, rely=0.5, height=30, relwidth=0.293)

        self.q_entry = tk.Entry(self.root)
        self.q_entry.insert(0, "q")
        self.q_entry.place(relx=0.2, rely=0.563, height=30, relwidth=0.293)

        self.d_entry = tk.Entry(self.root)
        self.d_entry.insert(0, "d")
        self.d_entry.place(relx=0.688, rely=0.563, height=30, relwidth=0.293)
        
        #sign
        self.sign_message_entry = tk.Entry(self.root)
        self.sign_message_entry.place(relx=0.198, rely=0.669, height=50, relwidth=0.293)

        self.new_sign_entry = tk.Entry(self.root, state="readonly")
        self.new_sign_entry.place(relx=0.198, rely=0.834, height=50, relwidth=0.293)

        #verify
        self.verify_message_entry = tk.Entry(self.root)
        self.verify_message_entry.place(relx=0.69, rely=0.669, height=50, relwidth=0.293)

        self.verify_sign_entry = tk.Entry(self.root)
        self.verify_sign_entry.place(relx=0.69, rely=0.77, height=50, relwidth=0.293)

    #Buttons
        #key generation
        tk.Button(self.root, text="Load Private Keys", command=self.load_rsa_dss_data).place(relx=0.7, rely=0.516, height=26, width=97)

        tk.Button(self.root, text="Generate Keys", command=self.generate_keys).place(relx=0.85, rely=0.516, height=26, width=97)

        #sign
        tk.Button(self.root, text="Sign", command=self.sign_number).place(relx=0.358, rely=0.772, height=26, width=97)

        tk.Button(self.root, text="Save Keys", command=self.save_keys).place(relx=0.025, rely=0.947, height=26, width=177)

        tk.Button(self.root, text="Save Message and Signature", command= self.save_message_and_signature).place(relx=0.259, rely=0.947, height=26, width=177)
        
        #verify
        tk.Button(self.root, text="Verify", command=self.verify_number).place(relx=0.85, rely=0.87, height=26, width=97)

        tk.Button(self.root, text="Load Public Keys", command=self.load_public_keys).place(relx=0.513, rely=0.947, height=26, width=177)

        tk.Button(self.root, text="Load Message and Signature", command=self.load_message_and_signature).place(relx=0.75, rely=0.947, height=26, width=177)

    #Labels    
        #public key
        tk.Label(self.root, text="Public Key").place(relx=0.038, rely=0.344, height=21, width=75)
        
        tk.Label(self.root, text="Enter e:").place(relx=0.038, rely=0.406, height=20, width=50)

        tk.Label(self.root, text="Enter n:").place(relx=0.525, rely=0.406, height=20, width=50)

        tk.Label(self.root, text="Choose SHA:").place(relx=0.700, rely=0.350, height=21, width=75)

        #key generation
        tk.Label(self.root, text="Private Key").place(relx=0.038, rely=0.453, height=21, width=75)

        tk.Label(self.root, text="Enter p:").place(relx=0.038, rely=0.516, height=20, width=50)

        tk.Label(self.root, text="Enter q:").place(relx=0.038, rely=0.563, height=20, width=50)

        tk.Label(self.root, text="Enter d:").place(relx=0.525, rely=0.563, height=21, width=50)

        #sign
        tk.Label(self.root, text="Sign").place(relx=0.038, rely=0.641, height=21, width=35)

        tk.Label(self.root, text="Enter your message:").place(relx=0.038, rely=0.703, height=21, width=110)

        tk.Label(self.root, text="Signature:").place(relx=0.038, rely=0.872, height=21, width=65)

        #verify
        tk.Label(self.root, text="Verify").place(relx=0.525, rely=0.641, height=21, width=34)

        tk.Label(self.root, text="Enter your message:").place(relx=0.525, rely=0.703, height=21, width=110)

        tk.Label(self.root, text="Enter signature:").place(relx=0.525, rely=0.797, height=21, width=80)

    #Separators
        ttk.Separator(self.root, orient="vertical").place(relx=0.5, rely=0.611,  relheight=0.395)

        ttk.Separator(self.root).place(relx=0.0, rely=0.441,  relwidth=0.999)

        ttk.Separator(self.root).place(relx=0.0, rely=0.614,  relwidth=0.998)

        ttk.Separator(self.root).place(relx=0.0, rely=0.93,  relwidth=0.996)


    def save_keys(self):
        try:
            file_path = Path(__file__).parent / "rsa_keys.json"
            data = {
                "p": self.p_entry.get(),
                "q": self.q_entry.get(),
                "e": self.e_entry.get(),
                "n": self.n_entry.get()
            }
            with file_path.open("w") as file:
                json.dump(data, file)
            self.log_message("Keys saved successfully.", "green")
        except Exception as e:
            self.log_message(f"Error saving keys: {e}", "red")

    def save_message_and_signature(self):
        try:
            file_path = Path(__file__).parent / "rsa_signature.json"
            data = {
                "message": str(self.sign_message_entry.get()),
                "signature": str(self.new_sign_entry.get())
            }
            with file_path.open("w") as file:
                json.dump(data, file)
            self.log_message("Message and signature saved successfully.", "green")
        except Exception as e:
            self.log_message(f"Error saving message and signature: {e}", "red")

    def load_public_keys(self):
        try:
            file_path = Path(__file__).parent / "rsa_keys.json"
            with file_path.open("r") as file:
                data = json.load(file)
            self.e_entry.delete(0, tk.END)
            self.e_entry.insert(0, data.get("e", ""))
            self.n_entry.delete(0, tk.END)
            self.n_entry.insert(0, data.get("n", ""))
            self.log_message("Public keys loaded successfully.", "green")
        except Exception as e:
            self.log_message(f"Error loading public keys: {e}", "red")

    def load_message_and_signature(self):
        try:
            file_path = Path(__file__).parent / "rsa_signature.json"
            with file_path.open("r") as file:
                data = json.load(file)
            self.verify_message_entry.delete(0, tk.END)
            self.verify_message_entry.insert(0, data.get("message", ""))
            self.verify_sign_entry.delete(0, tk.END)
            self.verify_sign_entry.insert(0, data.get("signature", ""))
            self.log_message("Message and signature loaded successfully.", "green")
        except Exception as e:
            self.log_message(f"Error loading message and signature: {e}", "red")

    #Data saver and loader
    def save_rsa_dss_data(self):
        file_path = Path(__file__).parent / "rsa_dss_data.json"
        data = {
            "p": self.p_entry.get(),
            "q": self.q_entry.get(),
            "e": self.e_entry.get(),
            "n": self.n_entry.get()
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

            self.log_message("Data loaded successfully.", "green")
        except FileNotFoundError:
            print("No saved data found.")

    def generate_keys(self):
        try:
            p = int(self.p_entry.get())
            q = int(self.q_entry.get())
            e = int(self.e_entry.get())

            if not (isprime(p) and isprime(q)):
                raise ValueError("p and q must both be prime.")

            n = p * q
            phi_n = (p - 1) * (q - 1)

            if math.gcd(e, phi_n) != 1:
                raise ValueError("e must be coprime with φ(n).")

            d = pow(e, -1, phi_n)

            self.public_key = (e, n)
            self.key_data["p"], self.key_data["q"], self.key_data["e"], self.key_data["d"] = p, q, e, d
            self.log_panel.delete(1.0, tk.END)
            self.log_message(f"Keys Generated!\nPublic: (e={e}, n={n})\nPrivate: d = {d}", "blue")
            self.n_entry.delete(0, tk.END)
            self.n_entry.insert(0, n)
            self.d_entry.delete(0, tk.END)
            self.d_entry.insert(0, d)
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
            d, n = self.key_data["d"], int(self.n_entry.get())
            raw_message = self.sign_message_entry.get()

            hash_int = self.sha2_hash(raw_message) % n
            if hash_int >= n:
                raise ValueError("Hash is too large for modulus n. Use larger primes.")

            signature = pow(hash_int, d, n)

            self.message_value = hash_int
            self.signature_value = signature

            self.log_message(f"Signed: {raw_message} → \n{signature}", "green")
            self.new_sign_entry.configure(state="normal")
            self.new_sign_entry.delete(0, tk.END)
            self.new_sign_entry.insert(0, signature)
            self.new_sign_entry.configure(state="readonly")
        except (KeyError, ValueError) as ex:
            self.log_message(f"Error: {str(ex)}", "red")

    def verify_number(self):
        try:
            e, n = int(self.e_entry.get()), int(self.n_entry.get())
            signature = int(self.verify_sign_entry.get())
            raw_message = self.verify_message_entry.get()

            hash_int = self.sha2_hash(raw_message) % n
            decrypted_hash = pow(signature, e, n)

            if decrypted_hash == hash_int:
                self.log_message("Signature Verified", "green")
            else:
                self.log_message("Signature Failed to Verify", "red")

        except (KeyError, ValueError) as ex:
            self.log_message(f"Error: {str(ex)}", "red")
