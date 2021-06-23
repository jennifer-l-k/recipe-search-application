import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import time 
import recipes

class App:
    root: tk.Tk
    listbox: tk.Listbox
    entry_enterfoodkey: tk.Entry
    db: recipes.RecipesDatabase


    def __init__(self, root):
        self.root = root
        #setting title
        self.root.title("Programmiersprachen - Einführung in Python")
        #setting window size
        width=700
        height=450
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.db = recipes.RecipesDatabase()
        self.db.read_json()
        

        #Label for the DHBW Logo
        label_banner=tk.Label(self.root)
        label_banner["bg"] = "#e2001a"
        label_banner["disabledforeground"] = "#e2001a"
        ft = tkFont.Font(family='Times',size=10)
        label_banner["font"] = ft
        label_banner["fg"] = "#333333"
        label_banner["justify"] = "center"
        label_banner["text"] = ""
        label_banner.place(x=0,y=0,width=700,height=30)   


        #Label with the Author within the Label for the DHBW Logo
        label_author=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        label_author["bg"] = "#e2001a"
        label_author["font"] = ft
        label_author["fg"] = "#ffffff"
        label_author["justify"] = "center"
        label_author["text"] = "Erstellt von: Jennifer L. Krüger"
        label_author.place(x=500,y=0,width=200,height=30)


        #Label for the main header
        label_mainheader=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        label_mainheader["bg"] = "#e2001a"
        label_mainheader["font"] = ft
        label_mainheader["fg"] = "#ffffff"
        label_mainheader["justify"] = "center"
        label_mainheader["text"] = "Python Laborprojekt | Rezeptauswahl"
        label_mainheader.place(x=0,y=0,width=250,height=30)


        #Entry-Widget for the Foodkeys
        self.entry_enterfoodkey=tk.Entry(self.root)
        self.entry_enterfoodkey["bg"] = "#cfcccc"
        self.entry_enterfoodkey["borderwidth"] = "1px"
        self.entry_enterfoodkey["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=12)
        self.entry_enterfoodkey["font"] = ft
        self.entry_enterfoodkey["fg"] = "#000000"
        self.entry_enterfoodkey["justify"] = "center"
        #self.entry_enterfoodkey.insert(0, "Suchen nach...")
        self.entry_enterfoodkey.place(x=361,y=50,width=157,height=30)


        #Button to search after recipes within the Foodkey
        button_search=tk.Button(self.root)
        button_search["bg"] = "#cfcccc"
        ft = tkFont.Font(family='Times',size=12)
        button_search["font"] = ft
        button_search["fg"] = "#000000"
        button_search["justify"] = "center"
        button_search["text"] = "Suchen"
        button_search.place(x=528,y=50,width=157,height=30)
        print(self.button_search_command)
        button_search["command"] = self.button_search_command


        #Button to reset all the Foodkey within the Entry-Widget
        button_reset=tk.Button(self.root)
        button_reset["bg"] = "#cfcccc"
        ft = tkFont.Font(family='Times',size=12)
        button_reset["font"] = ft
        button_reset["fg"] = "#000000"
        button_reset["justify"] = "center"
        button_reset["text"] = "Eingabe Rücksetzen"
        button_reset.place(x=28,y=360,width=157,height=30)
        button_reset["command"] = self.button_reset_command


        #Button to close the Application
        button_close=tk.Button(self.root)
        button_close["bg"] = "#cfcccc"
        ft = tkFont.Font(family='Times',size=12)
        button_close["font"] = ft
        button_close["fg"] = "#000000"
        button_close["justify"] = "center"
        button_close["text"] = "Schließen"
        button_close.place(x=195,y=400,width=157,height=30)
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
        button_help.place(x=28,y=400,width=157,height=30)
        button_help["command"] = self.button_help_command


        #Button to show all the Recipes within the database
        button_allrecipes=tk.Button(self.root)
        button_allrecipes["bg"] = "#cfcccc"
        ft = tkFont.Font(family='Times',size=12)
        button_allrecipes["font"] = ft
        button_allrecipes["fg"] = "#000000"
        button_allrecipes["justify"] = "center"
        button_allrecipes["text"] = "Alle Rezepte anzeigen"
        button_allrecipes.place(x=195,y=360,width=157,height=30)
        button_allrecipes["command"] = self.button_allrecipes_command


        #Listbox with a scrollbar which show all the Recipes within the database
        self.listbox = tk.Listbox(self.root)
        self.listbox.place(x=23,y=100,width=333,height=250)
        ft = tkFont.Font(family='Times',size=12)
        self.listbox["font"] = ft
        
        scrollbar_y = tk.Scrollbar(self.root)
        scrollbar_y.place(x=345,y=100,height=250)
        scrollbar_y.config(command = self.listbox.yview)

        self.listbox.config(yscrollcommand = scrollbar_y.set)

        self.show_all_recipes()


    def button_search_command(self):
        """..."""
        self.listbox.delete(0,'end')
        try:
            searched_recipes = self.db.search_recipes_by_ingredients(self.entry_enterfoodkey.get())
            for recipe in searched_recipes:
                self.listbox.insert(recipe.id, recipe.name)
            print('Es wurden Rezepte für den Suchbegriff gefunden.')
        except:
            self.listbox.insert(0,'Keine Rezepte verfügbar.')
            print('Suchanfrage fehlgeschlagen')
        #Layout überarbeiten: Links Listbox, Rechts Rezeptausgabe, Fenster vergrößern, Scrollbar für die Rezeptausgabe, Unten Buttons


    def button_allrecipes_command(self):
        """..."""
        self.listbox.delete(0,'end')
        self.show_all_recipes()
        print('Es wurden alle Rezepte erfolgreich angezeigt.')


    def button_close_command(self):
        """..."""
        question_box = messagebox.askquestion('Schließen der Anwendung', 'Möchten Sie die Anwendung wirklich schließen?', icon='error')
        if question_box == 'yes':
            self.root.destroy()
            print('Die Anwendung wurde geschlossen.')
        else:
            tk.messagebox.showinfo('Willkommen zurück', 'Willkommen zurück in der Anwendung.')
            print('Die Anwendung wurde wiederhergestellt.')
        
        
    def button_help_command(self):
        """..."""
        print('Die Hilfeseite wurde aufgerufen.')
        messagebox.showinfo('Hilfe', 'Geben Sie ein beliebiges Lebensmittel in das Suchfeld ein und es werden Ihnen entsprechende Rezepte mit dem Lebensmittel ausgegeben.\n\nViel Spaß.')
        print('Die Hilfeseite wurde geschlossen.')


    def button_reset_command(self):
        """..."""
        self.listbox.delete(0,'end')
        print('Die Lebensmitteleingabe wurde erfolgreich zurückgesetzt.')

    
    def show_all_recipes(self):
        """..."""
        for recipe_key in self.db.all_recipes_dict:
            recipe_value = self.db.all_recipes_dict[recipe_key]
            self.listbox.insert(recipe_key, recipe_value.name)
#End Class App


root = tk.Tk()
app = App(root)
root.mainloop()