import customtkinter as ctk

from Model.calcul import Calcul

# --- Configuration de l'apparence ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- Création de la fenêtre principale ---
app = ctk.CTk()
app.geometry("600x600")
app.title("Interface Calculatrice")

# Les Fonction

def click_btn(nombre):
    res = resultat_label.cget("text")
    resultat_label.configure(text=str(res) + str(nombre))
def click_EXE():
    try:
        nbatrad = resultat_label.cget("text")
        res = calculRealiser.verifcode(nbatrad)
        resultat_label.configure(text=res)

    except ValueError:
        resultat_label.configure(text="erreur")



# --- Interface Graphique (Grid Layout) ---
calculRealiser = Calcul()

# 1. Le titre
# On le place sur la ligne 0. Il s'étale sur 3 colonnes (columnspan=3)
titre_label = ctk.CTkLabel(app, text="CALCULATRICE", font=("Arial", 20, "bold"))
titre_label.grid(row=0, column=0, columnspan=3, pady=20)

# 2. L'écran d'affichage
# Ligne 1. On utilise une couleur de fond (fg_color) pour simuler un écran.
resultat_label = ctk.CTkLabel(app, text="0", width=350, height=70, fg_color="#2b2b2b", corner_radius=10, font=("Arial", 30))
resultat_label.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

# 3. Le pavé numérique (1 à 9)
# On crée une liste pour organiser nos chiffres
boutons_chiffres = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3'
]

simbole = [ '+', '-', 'x', '/']

index = 0
nbSymbole = 0
for r in range(3):    # On boucle sur 3 lignes (lignes indexées 0, 1, 2)
    for c in range(3): # On boucle sur 3 colonnes (colonnes indexées 0, 1, 2)
        texte_bouton = boutons_chiffres[index]
        btn = ctk.CTkButton(app, text=texte_bouton, width=80, height=80, font=("Arial", 20),command=lambda x=texte_bouton: click_btn(x))
        
        # On ajoute +2 à 'r' car les lignes 0 et 1 sont déjà prises par le titre et l'écran
        btn.grid(row=r+2, column=c, padx=10, pady=10)
        if c == 2 and nbSymbole < len(simbole):
            btn_symb = ctk.CTkButton(app, text=simbole[nbSymbole], width=80, height=80, 
                                     fg_color="orange", font=("Arial", 20),
                                     command=lambda x=simbole[nbSymbole]: click_btn(x))
            btn_symb.grid(row=r+2, column=3, padx=10, pady=10)
            nbSymbole += 1
        index += 1

# 4. La dernière ligne (Ligne 5)
btn_0 = ctk.CTkButton(app, text="0", width=80, height=80, font=("Arial", 20))
btn_0.grid(row=5, column=0, padx=10, pady=10)

btn_clear = ctk.CTkButton(app, text="C", width=80, height=80, fg_color="#d35400", font=("Arial", 20))
btn_clear.grid(row=5, column=1, padx=10, pady=10)

btn_exe = ctk.CTkButton(app, text="EXE", width=80, height=80, fg_color="#27ae60", font=("Arial", 20), command=click_EXE)
btn_exe.grid(row=5, column=2, padx=10, pady=10)

# --- Lancement ---
app.mainloop()