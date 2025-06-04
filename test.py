import tkinter as tk

def text_to_hex(text):
    return text.encode('utf-8').hex()

def hex_to_text(hex_str):
    try:
        return bytes.fromhex(hex_str).decode('utf-8')
    except Exception as e:
        return f"Erreur : {e}"

def chiffrement_aes():
    texte = texte_input.get("1.0", tk.END).strip()
    cle = cle_input.get().strip()

    if not texte or not cle:
        resultat_chiffre.delete("1.0", tk.END)
        resultat_chiffre.insert(tk.END, "Texte et clé requis.")
        return

    # 🔐 Remplacer par ton vrai chiffrement AES
    texte_chiffre = text_to_hex(texte)

    resultat_chiffre.delete("1.0", tk.END)
    resultat_chiffre.insert(tk.END, texte_chiffre)

def dechiffrement_aes():
    texte_hex = texte_chiffre_input.get("1.0", tk.END).strip()
    cle = cle_dechif_input.get().strip()

    if not texte_hex or not cle:
        resultat_dechiffre.delete("1.0", tk.END)
        resultat_dechiffre.insert(tk.END, "Texte et clé requis.")
        return

    # 🔓 Remplacer par ton vrai déchiffrement AES
    texte = hex_to_text(texte_hex)

    resultat_dechiffre.delete("1.0", tk.END)
    resultat_dechiffre.insert(tk.END, texte)

# ---- Interface ----
window = tk.Tk()
window.title("AES - Chiffrement / Déchiffrement")

# Utilise un frame principal divisé en 2 colonnes
frame_gauche = tk.Frame(window, padx=10, pady=10)
frame_gauche.pack(side="left", fill="both", expand=True)

frame_droite = tk.Frame(window, padx=10, pady=10)
frame_droite.pack(side="right", fill="both", expand=True)

# Partie chiffrement (gauche)
tk.Label(frame_gauche, text="Texte à chiffrer :").pack()
texte_input = tk.Text(frame_gauche, height=5, width=50)
texte_input.pack()

tk.Label(frame_gauche, text="Clé AES :").pack()
cle_input = tk.Entry(frame_gauche, width=50)
cle_input.pack()

tk.Button(frame_gauche, text="Chiffrer", command=chiffrement_aes).pack(pady=5)

tk.Label(frame_gauche, text="Résultat chiffré (hex) :").pack()
resultat_chiffre = tk.Text(frame_gauche, height=5, width=50)
resultat_chiffre.pack()

# Partie déchiffrement (droite)
tk.Label(frame_droite, text="Texte chiffré (hex) :").pack()
texte_chiffre_input = tk.Text(frame_droite, height=5, width=50)
texte_chiffre_input.pack()

tk.Label(frame_droite, text="Clé AES :").pack()
cle_dechif_input = tk.Entry(frame_droite, width=50)
cle_dechif_input.pack()

tk.Button(frame_droite, text="Déchiffrer", command=dechiffrement_aes).pack(pady=5)

tk.Label(frame_droite, text="Résultat déchiffré :").pack()
resultat_dechiffre = tk.Text(frame_droite, height=5, width=50)
resultat_dechiffre.pack()

window.mainloop()
