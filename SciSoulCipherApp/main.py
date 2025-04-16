import tkinter as tk
from EC.rsa_module import RSAApp
from EC.rsa_numeric import RSANumericApp
from EC.elgamal import ElGamalApp

from DSS.elgamal_dss import ElGamalDSS
from DSS.schnorr_dsa import SchnorrDSA

class CryptoSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptosystem Selector")
        self.root.geometry("620x400")
        self.root.resizable(False, False)

        left_frame = tk.Frame(root)
        left_frame.pack(side="left", padx=40, pady=20)

        right_frame = tk.Frame(root)
        right_frame.pack(side="right", padx=40, pady=20)

        tk.Label(left_frame, text="Encryption Cryptosystems", font=("Arial", 14)).pack(pady=10)

        self.options = {
            "RSA (Text)": self.launch_rsa,
            "RSA (Numbers)": self.launch_rsa_numeric,
            "ElGamal": self.launch_elgamal_app,
        }

        for name, func in self.options.items():
            tk.Button(left_frame, text=name, command=func, width=30, height=3).pack(pady=5)

        tk.Label(right_frame, text="Digital Singature Schemes", font=("Arial", 14)).pack(pady=10)
        
        self.options_2 = {
            "RSA": None,
            "ElGamal": self.launch_elgamal_DSS,
            "SchnorrDSA": self.launch_schnorr_DSA
        }

        for name, func in self.options_2.items():
            tk.Button(right_frame, text=name, command=func, width=30, height=3).pack(pady=5)

    def launch_rsa(self):
        self.root.withdraw()
        RSAApp(self.root)

    def launch_rsa_numeric(self):
        self.root.withdraw()
        RSANumericApp(self.root)

    def launch_elgamal_app(self):
        self.root.withdraw()
        ElGamalApp(self.root)

    def launch_elgamal_DSS(self):
        self.root.withdraw()
        ElGamalDSS(self.root)
    
    def launch_schnorr_DSA(self):
        self.root.withdraw()
        SchnorrDSA(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptoSelector(root)
    root.mainloop()
