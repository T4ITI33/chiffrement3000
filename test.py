import tkinter as tk
from tkinter import messagebox

# Exemple de fonction de chiffrement (remplace avec ton vrai code AES)
def aes_encrypt(plaintext):
    # Remplace ceci avec ton chiffrement AES réel
    return plaintext.encode('utf-8').hex()

def aes_decrypt(hexstring):
    try:
        return bytes.fromhex(hexstring).decode('utf-8')
    except Exception as e:
        return f"Erreur : {e}"

# Fonction appelée lors du clic sur "Chiffrer"
def chiffrer():
    texte = input_entry.get()
    if texte:
        resultat = aes_encrypt(texte)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, resultat)
    else:
        messagebox.showwarning("Entrée manquante", "Veuillez entrer un texte à chiffrer.")

# Fonction appelée lors du clic sur "Déchiffrer"
def dechiffrer():
    hex_input = input_entry.get()
    if hex_input:
        resultat = aes_decrypt(hex_input)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, resultat)
    else:
        messagebox.showwarning("Entrée manquante", "Veuillez entrer un texte hexadécimal à déchiffrer.")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Démo Chiffrement AES")
window.geometry("500x300")

# Titre
tk.Label(window, text="Entrée (texte ou hex)", font=("Arial", 12)).pack(pady=5)

# Zone d'entrée
input_entry = tk.Entry(window, width=60)
input_entry.pack(pady=5)

# Boutons
frame = tk.Frame(window)
frame.pack(pady=5)
tk.Button(frame, text="🔐 Chiffrer", command=chiffrer).pack(side=tk.LEFT, padx=10)
tk.Button(frame, text="🔓 Déchiffrer", command=dechiffrer).pack(side=tk.LEFT, padx=10)

# Zone de sortie
tk.Label(window, text="Résultat :", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(window, height=6, width=60)
output_text.pack()

# Lancement de l'interface
window.mainloop()
