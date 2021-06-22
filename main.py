import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import time 
import recipes

class App:
    root: tk.Tk
    db: recipes.RecipesDatabase

    def __init__(self, root):
        self.root = root
        #setting title
        self.root.title("Python Laborprojekt | Rezept Auswahl")
        #setting window size
        width=600
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)


        #Label for the DHBW Logo
        label_banner=tk.Label(self.root)
        label_banner["bg"] = "#e2001a"
        label_banner["disabledforeground"] = "#e2001a"
        ft = tkFont.Font(family='Times',size=10)
        label_banner["font"] = ft
        label_banner["fg"] = "#333333"
        label_banner["justify"] = "center"
        label_banner["text"] = ""
        label_banner.place(x=0,y=0,width=599,height=30)   


        #Label with the Author within the Label for the DHBW Logo
        label_author=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        label_author["bg"] = "#e2001a"
        label_author["font"] = ft
        label_author["fg"] = "#ffffff"
        label_author["justify"] = "center"
        label_author["text"] = "Erstellt von: Jennifer L. Krüger"
        label_author.place(x=400,y=0,width=200,height=30)


        #Label for the main header
        label_mainheader=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=22)
        label_mainheader["font"] = ft
        label_mainheader["fg"] = "#333333"
        label_mainheader["justify"] = "center"
        label_mainheader["text"] = "Python Laborprojekt"
        label_mainheader.place(x=180,y=30,width=256,height=53)


        #Label for the second header
        label_subheader=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=16)
        label_subheader["font"] = ft
        label_subheader["fg"] = "#333333"
        label_subheader["justify"] = "center"
        label_subheader["text"] = "Rezept Auswahl"
        label_subheader.place(x=240,y=70,width=142,height=30)


        #Entry-Widget for the Foodkeys
        entry_enterfoodkey=tk.Entry(self.root)
        entry_enterfoodkey["bg"] = "#cfcccc"
        entry_enterfoodkey["borderwidth"] = "1px"
        entry_enterfoodkey["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=12)
        entry_enterfoodkey["font"] = ft
        entry_enterfoodkey["fg"] = "#000000"
        entry_enterfoodkey["justify"] = "center"
        entry_enterfoodkey["text"] = "Eingabe "
        entry_enterfoodkey.place(x=430,y=110,width=157,height=30)


        #Button to reset all the Foodkey within the Entry-Widget
        button_reset=tk.Button(self.root)
        button_reset["bg"] = "#cfcccc"
        ft = tkFont.Font(family='Times',size=12)
        button_reset["font"] = ft
        button_reset["fg"] = "#000000"
        button_reset["justify"] = "center"
        button_reset["text"] = "Eingabe Rücksetzen"
        button_reset.place(x=430,y=150,width=157,height=30)
        button_reset["command"] = self.button_reset_command


        #Button to close the Application
        button_close=tk.Button(self.root)
        button_close["bg"] = "#cfcccc"
        ft = tkFont.Font(family='Times',size=12)
        button_close["font"] = ft
        button_close["fg"] = "#000000"
        button_close["justify"] = "center"
        button_close["text"] = "Schließen"
        button_close.place(x=20,y=450,width=157,height=30)
        print(self.button_close_command)
        button_close["command"] = self.button_close_command


        #Button to show a Message for Using-Informations
        button_help=tk.Button(self.root)
        button_help["bg"] = "#cfcccc"
        ft = tkFont.Font(family='Times',size=12)
        button_help["font"] = ft
        button_help["fg"] = "#000000"
        button_help["justify"] = "center"
        button_help["text"] = "Hilfe"
        button_help.place(x=220,y=450,width=157,height=30)
        button_help["command"] = self.button_help_command


        #Button to show all the Recipes within the database
        button_allrecipes=tk.Button(self.root)
        button_allrecipes["bg"] = "#cfcccc"
        ft = tkFont.Font(family='Times',size=12)
        button_allrecipes["font"] = ft
        button_allrecipes["fg"] = "#000000"
        button_allrecipes["justify"] = "center"
        button_allrecipes["text"] = "Alle Rezepte anzeigen"
        button_allrecipes.place(x=420,y=450,width=157,height=30)
        button_allrecipes["command"] = self.button_allrecipes_command


        #Label for the Listbox
        label_listbox=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=16)
        label_listbox["font"] = ft
        label_listbox["fg"] = "#000000"
        label_listbox["justify"] = "center"
        label_listbox["text"] = "Auflistung der Rezepte"
        label_listbox.place(x=20,y=190,width=200,height=30)


        #Listbox which show all the Recipes within the database
        listbox = tk.Listbox(self.root)
        listbox.place(x=20,y=220,width=300,height=200)
        ft = tkFont.Font(family='Times',size=12)
        listbox["font"] = ft
        listbox.insert(1, "Gemüsepaste")
        listbox.insert(2, "Sommer-Kartoffelsalat")
        listbox.insert(3, "Kartoffelsuppe")
        listbox.insert(4, "Regenbogen Nudeln")
        listbox.insert(5, "Gefüllte Cannelloni")
        listbox.insert(6, "Gemüseschmarrn")
        listbox.insert(7, "Spargel in Parmesancrêps")
        listbox.insert(8, "Warmer-Tortellini-Salat")
        listbox.insert(9, "Couscous-Salat")
        listbox.insert(10, "Möhren-Ingwer-Kokos-Schaumsüppchen")
        listbox.insert(11, "China-Nudel-Pfanne")
        listbox.insert(12, "Gemüse-Curry")
        listbox.insert(13, "Fischbouletten")
        listbox.insert(14, "Bandnudeln mit frischen Lachs")
        listbox.insert(15, "Gefüllte Paprikaschoten")
        listbox.insert(16, "Fleischkäse mit Honig und Röstzwiebeln")
        listbox.insert(17, "Paprika Rahmenschnitzel")
        listbox.insert(18, "Schweinefilet")
        listbox.insert(19, "Gemüse-Reis-Pfanne")
        listbox.insert(20, "Schupfnudel-Pfanne")


    def button_allrecipes_command(self):
        """ The method outputs a message within the command line 
            indicating that it was executed successfully"""
        print('Es wurden alle Rezepte erfolgreich angezeigt.')


    def button_close_command(self):
        """ The method outputs a message within the command line 
            indicating that it was executed successfully"""
        question_box = messagebox.askquestion('Schließen der Anwendung', 'Möchten Sie die Anwendung wirklich schließen?', icon='error')
        if question_box == 'yes':
            self.root.destroy()
            print('Die Anwendung wurde geschlossen.')
        else:
            tk.messagebox.showinfo('Willkommen zurück', 'Willkommen zurück in der Anwendung.')
            print('Die Anwendung wurde wiederhergestellt.')
        
        
    def button_help_command(self):
        """ The method outputs a message within the command line 
            indicating that it was executed successfully"""
        print('Die Hilfeseite wurde aufgerufen.')
        messagebox.showinfo('Hilfe', 'Geben Sie ein beliebiges Lebensmittel in das Suchfeld ein und es werden Ihnen entsprechende Rezepte mit dem Lebensmittel ausgegeben.\n\nViel Spaß.')
        print('Die Hilfeseite wurde geschlossen.')


    def button_reset_command(self):
        """ The method outputs a message within the command line 
            indicating that it was executed successfully"""
        print('Die Lebensmitteleingabe wurde erfolgreich zurückgesetzt.')
#End Class App

if __name__ == "__main__":
    db = recipes.RecipesDatabase()
    db.read_json()
    tmp = db.search_recipes_by_ingredients("Nudeln")
for recipe in tmp:
    print(f"Id {recipe.id}: {recipe.name}")
    #print(f"Id {recipe.id}: {recipe.name} -> Schwierigkeit: {recipe.difficulty}")
    #print(f"Id {recipe.id}: {recipe.name}\n Zubereitung: {recipe.preparation}")
    #print(f"Id {recipe.id}: {recipe.name}\n Zutaten: {recipe.ingredients}")
#print(db.show_recipes_by_id(6))
root = tk.Tk()
app = App(root)
root.mainloop()