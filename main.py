import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import time 
import recipes

class App:
    root: tk.Tk
    listbox: tk.Listbox
    entry_enterfoodkey: tk.Entry
    selected_recipe: tk.Label
    db: recipes.RecipesDatabase


    def __init__(self, root):
        self.root = root
        self.root.configure(background='white')
        #setting title
        self.root.title("Programmiersprachen - Einführung in Python")
        #setting window size
        width=915
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.db = recipes.RecipesDatabase()
        self.db.read_json()
        

        #Label for the DHBW Logo
        label_banner = tk.Label(self.root)
        label_banner["bg"] = "#e2001a"
        label_banner["disabledforeground"] = "#e2001a"
        ft = tkFont.Font(family='Times',size=10)
        label_banner["font"] = ft
        label_banner["fg"] = "#333333"
        label_banner["justify"] = "center"
        label_banner["text"] = ""
        label_banner.place(x=0,y=0,width=915,height=30)   


        #Label for the main header
        label_mainheader = tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        label_mainheader["bg"] = "#e2001a"
        label_mainheader["font"] = ft
        label_mainheader["fg"] = "#ffffff"
        label_mainheader["justify"] = "center"
        label_mainheader["text"] = "Python Laborprojekt | Rezeptauswahl"
        label_mainheader.place(x=0,y=0,width=250,height=30)


        #Label with the Author within the Label for the DHBW Logo
        label_author = tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=10)
        label_author["bg"] = "#e2001a"
        label_author["font"] = ft
        label_author["fg"] = "#ffffff"
        label_author["justify"] = "center"
        label_author["text"] = "Erstellt von: Jennifer L. Krüger"
        label_author.place(x=710,y=0,width=200,height=30)


        #Entry-Widget for the Foodkeys
        self.entry_enterfoodkey = tk.Entry(self.root)
        self.entry_enterfoodkey["bg"] = "#D3D3D3"
        self.entry_enterfoodkey["borderwidth"] = "1px"
        self.entry_enterfoodkey["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=12)
        self.entry_enterfoodkey["font"] = ft
        self.entry_enterfoodkey["fg"] = "#000000"
        self.entry_enterfoodkey["justify"] = "center"
        #self.entry_enterfoodkey.insert(0, "Suchen nach...")
        self.entry_enterfoodkey.place(x=28,y=60,width=157,height=30)


        #Button to search after recipes within the Foodkey
        button_search=tk.Button(self.root)
        button_search["bg"] = "#D3D3D3"
        ft = tkFont.Font(family='Times',size=12)
        button_search["font"] = ft
        button_search["fg"] = "#000000"
        button_search["justify"] = "center"
        button_search["text"] = "Suchen"
        button_search.place(x=195,y=60,width=157,height=30)
        print(self.button_search_command)
        button_search["command"] = self.button_search_command


        #Listbox with a scrollbar which show all the Recipes within the database
        self.listbox = tk.Listbox(self.root, selectmode = "browse")
        self.listbox["bg"] = "#D3D3D3"
        self.listbox.place(x=23,y=100,width=333,height=290)
        ft = tkFont.Font(family='Times',size=12)
        self.listbox["font"] = ft
        
        scrollbar_listbox = tk.Scrollbar(self.root)
        scrollbar_listbox.place(x=345,y=101,height=289)
        scrollbar_listbox.config(command = self.listbox.yview)

        self.listbox.config(yscrollcommand = scrollbar_listbox.set)

        self.listbox.bind("<<ListboxSelect>>", self.show_selected_recipe)
        
        self.show_all_recipes()


        #Button to reset all the Foodkey within the Entry-Widget
        button_reset = tk.Button(self.root)
        button_reset["bg"] = "#D3D3D3"
        ft = tkFont.Font(family='Times',size=12)
        button_reset["font"] = ft
        button_reset["fg"] = "#000000"
        button_reset["justify"] = "center"
        button_reset["text"] = "Eingabe Rücksetzen"
        button_reset.place(x=28,y=400,width=157,height=30)
        button_reset["command"] = self.button_reset_command


        #Button to show all the Recipes within the database
        button_allrecipes = tk.Button(self.root)
        button_allrecipes["bg"] = "#D3D3D3"
        ft = tkFont.Font(family='Times',size=12)
        button_allrecipes["font"] = ft
        button_allrecipes["fg"] = "#000000"
        button_allrecipes["justify"] = "center"
        button_allrecipes["text"] = "Alle Rezepte anzeigen"
        button_allrecipes.place(x=195,y=400,width=157,height=30)
        button_allrecipes["command"] = self.button_allrecipes_command


        #Button to show a Message for Using-Informations
        button_help = tk.Button(self.root)
        button_help["bg"] = "#D3D3D3"
        ft = tkFont.Font(family='Times',size=12)
        button_help["font"] = ft
        button_help["fg"] = "#000000"
        button_help["justify"] = "center"
        button_help["text"] = "Hilfe"
        button_help.place(x=28,y=440,width=157,height=30)
        button_help["command"] = self.button_help_command


        #Button to close the Application
        button_close = tk.Button(self.root)
        button_close["bg"] = "#D3D3D3"
        ft = tkFont.Font(family='Times',size=12)
        button_close["font"] = ft
        button_close["fg"] = "#000000"
        button_close["justify"] = "center"
        button_close["text"] = "Schließen"
        button_close.place(x=195,y=440,width=157,height=30)
        print(self.button_close_command)
        button_close["command"] = self.button_close_command


        #Text widget with a write proteced version to show the selected recipe
        self.selected_recipe = tk.Text(self.root, wrap="word")
        ft = tkFont.Font(family='Times',size=12)
        self.selected_recipe["bg"] = "#D3D3D3"
        self.selected_recipe["font"] = ft
        self.selected_recipe["fg"] = "#000000"
        self.selected_recipe.place(x=362,y=60,width=522,height=410)
        self.selected_recipe.configure(state = "disabled")

        scrollbar_selected_recipe = tk.Scrollbar(self.root)
        scrollbar_selected_recipe.place(x=882,y=61,height=409)
        scrollbar_selected_recipe.config(command = self.listbox.yview)

        self.selected_recipe.config(yscrollcommand = scrollbar_selected_recipe.set)


    def button_search_command(self):
        """..."""
        self.listbox.delete(0,'end')
        try:
            searched_recipes = self.db.search_recipes_by_ingredients(self.entry_enterfoodkey.get())
            for recipe in searched_recipes:
                self.listbox.insert(tk.END, recipe)
            print('Es wurden Rezepte für den Suchbegriff gefunden.')
        except:
            self.listbox.insert(0,'Keine Rezepte für die Suchabfrage verfügbar.')
            print('Suchanfrage fehlgeschlagen')


    def button_allrecipes_command(self):
        """..."""
        self.listbox.delete(0,'end')
        self.entry_enterfoodkey.delete(0,'end')

        self.selected_recipe.configure(state = "normal")
        self.selected_recipe.delete(1.0,tk.END)

        self.show_all_recipes()
        print('Es wurden alle Rezepte erfolgreich angezeigt.')


    def show_selected_recipe(self, event):
        """..."""
        select = event.widget.curselection()
        recipe = None
        if select:
         index = select[0]
         recipe = self.db.name_dict.get(event.widget.get(index), None)
        
        if recipe is None:
            return        

        self.selected_recipe.configure(state = "normal")
        self.selected_recipe.delete(1.0,tk.END)
        self.selected_recipe.insert(tk.END, recipe.format_recipe())
        self.selected_recipe.configure(state = "disabled")


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
        self.entry_enterfoodkey.delete(0,'end')
        self.listbox.delete(0,'end')

        self.selected_recipe.configure(state = "normal")
        self.selected_recipe.delete(1.0,tk.END)
        print('Die Lebensmitteleingabe wurde erfolgreich zurückgesetzt.')

    
    def show_all_recipes(self):
        """..."""
        for recipe_key in self.db.all_recipes_dict:
            recipe_value = self.db.all_recipes_dict[recipe_key]
            self.listbox.insert(tk.END, recipe_value)
#End Class App


root = tk.Tk()
app = App(root)
root.mainloop()