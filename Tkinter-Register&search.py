import tkinter as tk
from tkinter import messagebox


def enregistrer():
    nom = nom_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    if nom == "" or email == "" or age == "":
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
    else:

        with open("info.txt", "a") as f:
            f.write(f"{nom}, {email}, {age}\n")
        messagebox.showinfo("Message info", "Utilisateur enregistré")

def chercher():
    nom = nom_cherche_entry.get()
    with open("info.txt", "r") as f:
        noms = [ligne.strip().split(", ")[0] for ligne in f]
    
    if nom in noms:
        messagebox.showinfo("Message info", "Le nom existe.")
    else:
        messagebox.showerror("Erreur", "Le nom n'existe pas.")


root = tk.Tk()
root.geometry('450x220')

nom_cherche_label = tk.Label(root, text="Chercher ")
nom_cherche_entry = tk.Entry(root)
valider_button = tk.Button(root, text="Valider", command=enregistrer)

chercher_button = tk.Button(root, text="Chercher", command=chercher)

nom_label = tk.Label(root, text="Name ")
nom_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email ")
email_entry = tk.Entry(root)

age_label = tk.Label(root, text="Âge ")
age_entry = tk.Entry(root)

nom_cherche_label.place(x=10,y=15)
nom_cherche_entry.place(x=110,y=15,width=200)
chercher_button.place(x=335,y=10)

nom_label.place(x=20,y=40)
nom_entry.place(x=110,y=40,width=200)

email_label.place(x=30,y=65)
email_entry.place(x=110,y=65,width=200)

age_label.place(x=40,y=90)
age_entry.place(x=110,y=90,width=200)

valider_button.place(x=110,y=130,width=200)


root.mainloop()
