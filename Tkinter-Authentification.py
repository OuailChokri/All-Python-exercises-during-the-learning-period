from tkinter import *
import csv
from tkinter import messagebox


def enregistrer_utilisateur(nom, password):
    with open('utilisateurss.csv', mode='a', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, password])
    messagebox.showinfo("Message info", "Utilisateur enregistré")

def connecter():
    nom = nom_entry.get()
    password = password_entry.get()

    with open('utilisateurss.csv') as fichier:
        reader = csv.reader(fichier)
        for row in reader:
            if row[0] == nom:
                if row[1] == password:
                    messagebox.showinfo("Connexion réussie", "Bravo et bienvenue !")
                    return
                else:
                    messagebox.showerror("Erreur de connexion", "L'utilisateur n'existe pas ou le mot de passe est incorrect.")
                    return
                    messagebox.showerror("Erreur de connexion", "L'utilisateur n'existe pas ou le mot de passe est incorrect.")

def afficher_interface_enregistrement():
    enregistrement_window = Toplevel(root)
    enregistrement_window.geometry('330x180')
    enregistrement_window.title("activiter 2")

    nom_label = Label(enregistrement_window, text="Nom :")
    nom_label.place(x=10,y=15)
    nom_entry = Entry(enregistrement_window)
    nom_entry.place(x=110,y=15,width=150)

    password_label = Label(enregistrement_window, text="Mot de passe :")
    password_label.place(x=10,y=40)
    password_entry = Entry(enregistrement_window, show="*")
    password_entry.place(x=110,y=40,width=150)

    enregistrer_button = Button(enregistrement_window, text="Enregistrer", command=lambda: enregistrer_utilisateur(nom_entry.get(), password_entry.get()))
    enregistrer_button.place(x=110,y=75,width=90)


def afficher_interface_principale():
    global nom_entry, password_entry
    nom_entry = None
    password_entry = None

    root.title("activiter 1")

    nom_label = Label(root, text="Nom :")
    nom_label.place(x=10,y=15)
    nom_entry = Entry(root)
    nom_entry.place(x=110,y=15,width=150)

    password_label = Label(root, text="Mot de passe :")
    password_label.place(x=10,y=40)
    password_entry = Entry(root, show="*")
    password_entry.place(x=110,y=40,width=150)

    inscrire_button = Button(root, text="S'inscrire", command=afficher_interface_enregistrement)
    inscrire_button.place(x=10,y=75,width=90)

    connecter_button = Button(root, text="Se connecter", command=connecter)
    connecter_button.place(x=130,y=75,width=100)


root = Tk()

root.geometry('330x180')
afficher_interface_principale()
root.mainloop()
