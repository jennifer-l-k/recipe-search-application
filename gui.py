import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_194=tk.Entry(root)
        GLineEdit_194["bg"] = "#a4a5a6"
        GLineEdit_194["borderwidth"] = "1px"
        GLineEdit_194["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=8)
        GLineEdit_194["font"] = ft
        GLineEdit_194["fg"] = "#ffffff"
        GLineEdit_194["justify"] = "center"
        GLineEdit_194["text"] = "Eingabe von Lebensmittel"
        GLineEdit_194.place(x=410,y=110,width=169,height=30)

        GButton_365=tk.Button(root)
        GButton_365["bg"] = "#a4a5a6"
        GButton_365["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=12)
        GButton_365["font"] = ft
        GButton_365["fg"] = "#ffffff"
        GButton_365["justify"] = "center"
        GButton_365["text"] = "Alle Rezepte anzeigen"
        GButton_365.place(x=420,y=450,width=157,height=30)
        GButton_365["command"] = self.GButton_365_command

        GLabel_585=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_585["font"] = ft
        GLabel_585["fg"] = "#333333"
        GLabel_585["justify"] = "center"
        GLabel_585["text"] = "Python Laborprojekt"
        GLabel_585.place(x=180,y=30,width=256,height=53)

        GLabel_163=tk.Label(root)
        GLabel_163["bg"] = "#e2001a"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_163["font"] = ft
        GLabel_163["fg"] = "#333333"
        GLabel_163["justify"] = "center"
        GLabel_163["text"] = ""
        GLabel_163.place(x=0,y=0,width=599,height=30)

        GLabel_211=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_211["font"] = ft
        GLabel_211["fg"] = "#333333"
        GLabel_211["justify"] = "center"
        GLabel_211["text"] = "Rezept Auswahl"
        GLabel_211.place(x=240,y=70,width=142,height=30)

        GButton_221=tk.Button(root)
        GButton_221["bg"] = "#a4a5a6"
        GButton_221["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=12)
        GButton_221["font"] = ft
        GButton_221["fg"] = "#ffffff"
        GButton_221["justify"] = "center"
        GButton_221["text"] = "Schließen"
        GButton_221.place(x=20,y=450,width=157,height=30)
        GButton_221["command"] = self.GButton_221_command

        GLabel_562=tk.Label(root)
        ft = tkFont.Font(family='Times',size=8)
        GLabel_562["font"] = ft
        GLabel_562["fg"] = "#ffffff"
        GLabel_562["justify"] = "center"
        GLabel_562["text"] = "Erstellt von: Jennifer L. Krüger"
        GLabel_562.place(x=450,y=0,width=147,height=30)

        GButton_418=tk.Button(root)
        GButton_418["bg"] = "#a4a5a6"
        ft = tkFont.Font(family='Times',size=12)
        GButton_418["font"] = ft
        GButton_418["fg"] = "#ffffff"
        GButton_418["justify"] = "center"
        GButton_418["text"] = "Hilfe"
        GButton_418.place(x=220,y=450,width=157,height=30)
        GButton_418["command"] = self.GButton_418_command

    def GButton_365_command(self):
        print("command")


    def GButton_221_command(self):
        print("command")


    def GButton_418_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
