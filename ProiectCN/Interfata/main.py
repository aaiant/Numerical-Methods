# Importarea clasei Problema
import sys
sys.path.insert(0, '..')
from Clase.Probleme import Problema  # noqa: E402
from Clase.Tabel import Tabel  # noqa: E402
from Clase.Probleme import Problema  # noqa: E402
import os  # noqa: E402
import threading  # noqa: E402
import time  # noqa: E402
# <><><><><><><><><><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

# Importarea modulelor pentru calcule
import numpy as np  # noqa: E402
from matplotlib.figure import Figure as Mtp  # noqa: E402
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk  # noqa: E402
import tkinter as tk  # noqa: E402
from sympy import lambdify, Symbol   # noqa: E402
import timeit  # noqa: E402
import webbrowser  # noqa: E402
from scipy.integrate import odeint  # noqa: E402
import random  # noqa: E402
import string  # noqa: E402
from matplotlib.animation import FuncAnimation  # noqa: E402


# Clasa pentru Interfata Tkinter
class GUI:
    
    # <><><><><><><><><><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

    # Tabel folosit pentru a crea zona de istoric
    tabelINITIAL = Tabel()

    # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'X0'
    lista_x0_duplicata = tabelINITIAL.tabel_probleme['X0'].tolist()
    set_x0 = set(lista_x0_duplicata)
    lista_x0 = list(set_x0)

    # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'Y0'
    lista_y0_duplicata = tabelINITIAL.tabel_probleme['Y0'].tolist()
    set_y0 = set(lista_y0_duplicata)
    lista_y0 = list(set_y0)

    # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'n'
    lista_n_duplicata = tabelINITIAL.tabel_probleme['n'].tolist()
    set_n = set(lista_n_duplicata)
    lista_n = list(set_n)

    # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'h'
    lista_h_duplicata = tabelINITIAL.tabel_probleme['h'].tolist()
    set_h = set(lista_h_duplicata)
    lista_h = list(set_h)

    # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'f(x,y)'
    lista_fxy_duplicata = tabelINITIAL.tabel_probleme['f(x,y)'].tolist()
    set_fxy = set(lista_fxy_duplicata)
    lista_fxy = list(set_fxy)
    
# <><><><><><><><><><><><><><><<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    
    def actualizare_entrybox1(self):
        self.entrybox1.delete(0, tk.END)
        self.entrybox1.insert(0, self.variabila_0.get())
        
    def actualizare_entrybox2(self):
        self.entrybox2.delete(0, tk.END)
        self.entrybox2.insert(0, self.variabila_1.get())
        
    def actualizare_entrybox3(self):
        self.entrybox3.delete(0, tk.END)
        self.entrybox3.insert(0, self.variabila_2.get())
        
    def actualizare_entrybox4(self):
        self.entrybox4.delete(0, tk.END)
        self.entrybox4.insert(0, self.variabila_3.get())
        
    def actualizare_entrybox5(self):
        self.entrybox5.delete(0, tk.END)
        self.entrybox5.insert(0, self.variabila_4.get())

    @staticmethod
    def actualizare_meniuri_istoric(tabelul_curent):
        # Lista generala
        lista_generala = list()
        # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'X0'
        lista_x0_duplicata = tabelul_curent.tabel_probleme['X0'].tolist()
        set_x0 = set(lista_x0_duplicata)
        lista_x0 = list(set_x0)

        # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'Y0'
        lista_y0_duplicata = tabelul_curent.tabel_probleme['Y0'].tolist()
        set_t0 = set(lista_y0_duplicata)
        lista_y0 = list(set_t0)

        # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'h'
        lista_h_duplicata = tabelul_curent.tabel_probleme['h'].tolist()
        set_h = set(lista_h_duplicata)
        lista_h = list(set_h)

        # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'n'
        lista_n_duplicata = tabelul_curent.tabel_probleme['n'].tolist()
        set_n = set(lista_n_duplicata)
        lista_n = list(set_n)

        # Pasii pentru a obtine o lista cu el. unice din tabelul pandas, coloana 'f(x,y)'
        lista_fxy_duplicata = tabelul_curent.tabel_probleme['f(x,y)'].tolist()
        set_fxy = set(lista_fxy_duplicata)
        lista_fxy = list(set_fxy)

        # Adaugarea rezultatelor in lista generala
        lista_generala.append(lista_x0)
        lista_generala.append(lista_y0)
        lista_generala.append(lista_n)
        lista_generala.append(lista_h)
        lista_generala.append(lista_fxy)
        return lista_generala

    @staticmethod
    def export_html():
        tabel = Tabel()
        tabel_html = tabel.tabel_probleme.to_html()
        os.remove('..\\Fisiere\\HTML\\BazaDeDate.html')
        with open('..\\Fisiere\\HTML\\BazaDeDate.html', 'w') as fisier_html:
            fisier_html.write(tabel_html)
            fisier_html.close()
        webbrowser.open('..\\Fisiere\\HTML\\BazaDeDate.html')

    def curatare_json(self):
        self.tabelINITIAL.curatare_tabel_pandas_probleme_json()

    def schimbare_culori(self):
        while True:
            time.sleep(1)
            # Zona de Butoane
            self.button.config(fg='#FF775E')
            self.clear_button.config(fg='#FF775E')
            self.curatare_lista_json_buton.config(fg='#FF775E')
            self.export_lista_json_html_buton.config(fg='#FF775E')

            # Zona de Frame
            self.toolbar_frame.config(bg='#FF775E')

            # Zona de Meniuri

            self.Meniu_0.configure(fg='#FF775E')
            self.Meniu_1.configure(fg='#FF775E')
            self.Meniu_2.configure(fg='#FF775E')
            self.Meniu_3.configure(fg='#FF775E')
            self.Meniu_3.configure(fg='#FF775E')
            self.Meniu_4.configure(fg='#FF775E')

            # Zona de entrybox-uri

            self.entrybox1.configure(highlightbackground="#FF775E", highlightcolor="#FF775E")
            self.entrybox2.configure(highlightbackground="#FF775E", highlightcolor="#FF775E")
            self.entrybox3.configure(highlightbackground="#FF775E", highlightcolor="#FF775E")
            self.entrybox4.configure(highlightbackground="#FF775E", highlightcolor="#FF775E")
            self.entrybox5.configure(highlightbackground="#FF775E", highlightcolor="#FF775E")

            time.sleep(1)

            # Zona de Butoane
            self.button.config(fg='#DD11FF')
            self.clear_button.config(fg='#DD11FF')
            self.curatare_lista_json_buton.config(fg='#DD11FF')
            self.export_lista_json_html_buton.config(fg='#DD11FF')

            # Zona de Frame
            self.toolbar_frame.config(bg='#DD11FF')

            # Zona de Meniuri

            self.Meniu_0.configure(fg='#DD11FF')
            self.Meniu_1.configure(fg='#DD11FF')
            self.Meniu_2.configure(fg='#DD11FF')
            self.Meniu_3.configure(fg='#DD11FF')
            self.Meniu_4.configure(fg='#DD11FF')

            # Zona de entrybox-uri

            self.entrybox1.configure(highlightbackground="#DD11FF", highlightcolor="#DD11FF")
            self.entrybox2.configure(highlightbackground="#DD11FF", highlightcolor="#DD11FF")
            self.entrybox3.configure(highlightbackground="#DD11FF", highlightcolor="#DD11FF")
            self.entrybox4.configure(highlightbackground="#DD11FF", highlightcolor="#DD11FF")
            self.entrybox5.configure(highlightbackground="#DD11FF", highlightcolor="#DD11FF")

            time.sleep(1)

            # Zona de Butoane
            self.button.config(fg='#FE02A2')
            self.clear_button.config(fg='#FE02A2')
            self.curatare_lista_json_buton.config(fg='#FE02A2')
            self.export_lista_json_html_buton.config(fg='#FE02A2')

            # Zona de Frame
            self.toolbar_frame.config(bg='#FE02A2')

            # Zona de Meniuri

            self.Meniu_0.configure(fg='#FE02A2')
            self.Meniu_1.configure(fg='#FE02A2')
            self.Meniu_2.configure(fg='#FE02A2')
            self.Meniu_3.configure(fg='#FE02A2')
            self.Meniu_4.configure(fg='#FE02A2')

            # Zona de entrybox-uri

            self.entrybox1.configure(highlightbackground="#FE02A2", highlightcolor="#FE02A2")
            self.entrybox2.configure(highlightbackground="#FE02A2", highlightcolor="#FE02A2")
            self.entrybox3.configure(highlightbackground="#FE02A2", highlightcolor="#FE02A2")
            self.entrybox4.configure(highlightbackground="#FE02A2", highlightcolor="#FE02A2")
            self.entrybox5.configure(highlightbackground="#FE02A2", highlightcolor="#FE02A2")

            time.sleep(1)

            # Zona de Butoane
            self.button.config(fg='#FF1476')
            self.clear_button.config(fg='#FF1476')
            self.curatare_lista_json_buton.config(fg='#FF1476')
            self.export_lista_json_html_buton.config(fg='#FF1476')

            # Zona de Frame
            self.toolbar_frame.config(bg='#FF1476')

            # Zona de Meniuri

            self.Meniu_0.configure(fg='#FF1476')
            self.Meniu_1.configure(fg='#FF1476')
            self.Meniu_2.configure(fg='#FF1476')
            self.Meniu_3.configure(fg='#FF1476')
            self.Meniu_4.configure(fg='#FF1476')

            # Zona de entrybox-uri

            self.entrybox1.configure(highlightbackground="#FF1476", highlightcolor="#FF1476")
            self.entrybox2.configure(highlightbackground="#FF1476", highlightcolor="#FF1476")
            self.entrybox3.configure(highlightbackground="#FF1476", highlightcolor="#FF1476")
            self.entrybox4.configure(highlightbackground="#FF1476", highlightcolor="#FF1476")
            self.entrybox5.configure(highlightbackground="#FF1476", highlightcolor="#FF1476")

            time.sleep(1)

            # Zona de Butoane
            self.button.config(fg='#FE2C54')
            self.clear_button.config(fg='#FE2C54')
            self.curatare_lista_json_buton.config(fg='#FE2C54')
            self.export_lista_json_html_buton.config(fg='#FE2C54')

            # Zona de Frame
            self.toolbar_frame.config(bg='#FE2C54')

            # Zona de Meniuri

            self.Meniu_0.configure(fg='#FE2C54')
            self.Meniu_1.configure(fg='#FE2C54')
            self.Meniu_2.configure(fg='#FE2C54')
            self.Meniu_3.configure(fg='#FE2C54')
            self.Meniu_4.configure(fg='#FE2C54')

            # Zona de entrybox-uri

            self.entrybox1.configure(highlightbackground="#FE2C54", highlightcolor="#FE2C54")
            self.entrybox2.configure(highlightbackground="#FE2C54", highlightcolor="#FE2C54")
            self.entrybox3.configure(highlightbackground="#FE2C54", highlightcolor="#FE2C54")
            self.entrybox4.configure(highlightbackground="#FE2C54", highlightcolor="#FE2C54")
            self.entrybox5.configure(highlightbackground="#FE2C54", highlightcolor="#FE2C54")

            time.sleep(1)

            # Zona de Butoane
            self.button.config(fg='#FF007F')
            self.clear_button.config(fg='#FF007F')
            self.curatare_lista_json_buton.config(fg='#FF007F')
            self.export_lista_json_html_buton.config(fg='#FF007F')

            # Zona de Frame
            self.toolbar_frame.config(bg='#FF007F')

            # Zona de Meniuri

            self.Meniu_0.configure(fg='#FF007F')
            self.Meniu_1.configure(fg='#FF007F')
            self.Meniu_2.configure(fg='#FF007F')
            self.Meniu_3.configure(fg='#FF007F')
            self.Meniu_4.configure(fg='#FF007F')

            # Zona de entrybox-uri

            self.entrybox1.configure(highlightbackground="#FF007F", highlightcolor="#FF007F")
            self.entrybox2.configure(highlightbackground="#FF007F", highlightcolor="#FF007F")
            self.entrybox3.configure(highlightbackground="#FF007F", highlightcolor="#FF007F")
            self.entrybox4.configure(highlightbackground="#FF007F", highlightcolor="#FF007F")
            self.entrybox5.configure(highlightbackground="#FF007F", highlightcolor="#FF007F")

            time.sleep(1)

            # Zona de Butoane
            self.button.config(fg='magenta')
            self.clear_button.config(fg='magenta')
            self.curatare_lista_json_buton.config(fg='magenta')
            self.export_lista_json_html_buton.config(fg='magenta')

            # Zona de Frame
            self.toolbar_frame.config(bg='magenta')

            # Zona de Meniuri

            self.Meniu_0.configure(fg='magenta')
            self.Meniu_1.configure(fg='magenta')
            self.Meniu_2.configure(fg='magenta')
            self.Meniu_3.configure(fg='magenta')
            self.Meniu_4.configure(fg='magenta')

            # Zona de entrybox-uri

            self.entrybox1.configure(highlightbackground="magenta", highlightcolor="magenta")
            self.entrybox2.configure(highlightbackground="magenta", highlightcolor="magenta")
            self.entrybox3.configure(highlightbackground="magenta", highlightcolor="magenta")
            self.entrybox4.configure(highlightbackground="magenta", highlightcolor="magenta")
            self.entrybox5.configure(highlightbackground="magenta", highlightcolor="magenta")

    @staticmethod
    def informatii():
        tk.messagebox.showinfo('Membrii echipei', 'Membrii echipei sunt: Tatu Denis (rol: calculul functiilor)' +
                               ', Antohi Andi-Ionel (rol: partea de Back-end; divizarea proiectului in ' +
                               'mai multe foldere [Ierarhie] + realizarea JSON-ului & a fisierului de tip HTML ' +
                               ' + crearea claselor din folder-ul intitulat \'Clase\' + implementarea ' +
                               'thread-urilor & relizarea interfetei in Tkinter, fara partea de calcul de la plotare).')
        tk.messagebox.showinfo('Informatii generale', 'Chiar daca datele acceptate de interfata, in functie de ordine, ' +
                               'sunt: float, float, int, float & string;' +
                               ' puteti introduce: int, int, int, int & string, ' +
                               'intrucat programul va face conversia automat!')
        tk.messagebox.showinfo('Informatii generale', 'Pentru a putea curata JSON-ul, butonul \'Curatare JSON\' ' +
                               ' trebuie sa fie apasat prima data in interfata! Pentru a putea vizualiza JSON-ul' +
                               ', va rugam sa apasati pe butonul \'Export JSON\'!')

    def __init__(self):
        
        try:

            self.root = tk.Tk()
        
            self.root.geometry("1800x900")
            self.root.title("Aproximarea solutiilor ecuatiilor diferentiale ordinare de ordinul I")
            self.eveniment0 = threading.Thread(target=self.schimbare_culori)
            self.eveniment0.setDaemon(True)
            self.eveniment0.start()
            self.eveniment1 = threading.Thread(target=self.informatii)
            self.eveniment1.setDaemon(True)
            self.eveniment1.start()
            
            # Crearea tk.Label
        
            self.label0 = tk.Label(self.root, text="  Date de intrare:", font=("Calibri", 16),
                                   fg='#F88379', bg='#020B10')
            self.label1 = tk.Label(self.root, text="X0 : ", fg='#F88379', bg='#020B10')
            self.label2 = tk.Label(self.root, text="Y0 : ", fg='#F88379', bg='#020B10')
            self.label3 = tk.Label(self.root, text="n : ", fg='#F88379', bg='#020B10')
            self.label4 = tk.Label(self.root, text="h : ", fg='#F88379', bg='#020B10')
            self.label5 = tk.Label(self.root, text="f'(x,y) : ", fg='#F88379', bg='#020B10')
            self.labelrb = tk.Label(self.root, text="Metode: ", font=('Calibri', 16), fg='#F88379', bg='#020B10')
            self.time_label = tk.Label(self.root, text="Timp executie", font=('Calibri', 12),
                                       fg='#F88379', bg='#020B10')
            
            # Asezarea Widget-urilor de tip Label

            self.label0.grid(row=0, column=0, padx=10, pady=10)
            self.label1.grid(row=1, column=0, padx=15, pady=15)
            self.label2.grid(row=2, column=0, padx=15, pady=15)
            self.label3.grid(row=3, column=0, padx=15, pady=15)
            self.label4.grid(row=4, column=0, padx=15, pady=15)
            self.label5.grid(row=5, column=0, padx=15, pady=15)
            self.labelrb.grid(row=0, column=3, padx=15, pady=10)
            self.time_label.grid(row=0, column=4)
            
            # Crearea tk.Entry

            self.entrybox1 = tk.Entry(self.root, width=15, font=('Calibri', 10),
                                      textvariable=tk.DoubleVar(), fg='white', bg='#915F6D',
                                      highlightthickness=1)
            self.entrybox2 = tk.Entry(self.root, width=15, font=('Calibri', 10),
                                      textvariable=tk.DoubleVar(), fg='white', bg='#915F6D',
                                      highlightthickness=1)
            self.entrybox3 = tk.Entry(self.root, width=15, font=('Calibri', 10),
                                      textvariable=tk.DoubleVar(), fg='white', bg='#915F6D',
                                      highlightthickness=1)
            self.entrybox4 = tk.Entry(self.root, width=15, font=('Calibri', 10),
                                      textvariable=tk.DoubleVar(), fg='white', bg='#915F6D',
                                      highlightthickness=1)
            self.entrybox5 = tk.Entry(self.root, width=15, font=('Calibri', 10), fg='white', bg='#915F6D',
                                      highlightthickness=1)
            
            #   Stergerea datelor initiale din Entry-uri

            self.entrybox1.delete(0, tk.END)
            self.entrybox2.delete(0, tk.END)
            self.entrybox3.delete(0, tk.END)
            self.entrybox4.delete(0, tk.END)
            self.entrybox5.delete(0, tk.END)

            # Asezarea Widget-urilor de tip Entry
            
            self.entrybox1.grid(row=1, column=1, padx=15, pady=15)
            self.entrybox2.grid(row=2, column=1, padx=15, pady=15)
            self.entrybox3.grid(row=3, column=1, padx=15, pady=15)
            self.entrybox4.grid(row=4, column=1, padx=15, pady=15)
            self.entrybox5.grid(row=5, column=1, padx=15, pady=15)
            
            # Crearea tk.StringVar() pentru istoric
            
            self.variabila_0 = tk.StringVar(self.root)
            self.variabila_1 = tk.StringVar(self.root)
            self.variabila_2 = tk.StringVar(self.root)
            self.variabila_3 = tk.StringVar(self.root)
            self.variabila_4 = tk.StringVar(self.root)
            self.v = tk.StringVar(self.root, "1")
            self.time_text = tk.StringVar()
            
            # Setarea valorii initiale pt. tk.StringVar() 
            
            self.variabila_0.set('Istoric')
            self.variabila_1.set("Istoric")
            self.variabila_2.set("Istoric")
            self.variabila_3.set("Istoric")
            self.variabila_4.set("Istoric")
            
            # Creare tk.OptionMenu

            self.Meniu_0 = tk.OptionMenu(self.root, self.variabila_0,
                                         *self.lista_x0, command=lambda _: self.actualizare_entrybox1())
            self.Meniu_1 = tk.OptionMenu(self.root, self.variabila_1,
                                         *self.lista_y0, command=lambda _: self.actualizare_entrybox2())
            self.Meniu_2 = tk.OptionMenu(self.root, self.variabila_2,
                                         *self.lista_n, command=lambda _: self.actualizare_entrybox3())
            self.Meniu_3 = tk.OptionMenu(self.root, self.variabila_3,
                                         *self.lista_h, command=lambda _: self.actualizare_entrybox4())
            self.Meniu_4 = tk.OptionMenu(self.root, self.variabila_4,
                                         *self.lista_fxy, command=lambda _: self.actualizare_entrybox5())
            
            # Asezarea Widget-urilor de tip OptionMenu
            
            self.Meniu_0.grid(row=1, column=2)
            self.Meniu_1.grid(row=2, column=2)
            self.Meniu_2.grid(row=3, column=2)
            self.Meniu_3.grid(row=4, column=2)
            self.Meniu_4.grid(row=5, column=2)
            
            # Stiluri pt. Widget-urile de OptionMenu
            
            self.Meniu_0.configure(bg='#182631', fg='white', activeforeground='#182631', activebackground='#FFC1CC')
            self.Meniu_1.configure(bg='#182631', fg='white', activeforeground='#182631', activebackground='#FFC1CC')
            self.Meniu_2.configure(bg='#182631', fg='white', activeforeground='#182631', activebackground='#FFC1CC')
            self.Meniu_3.configure(bg='#182631', fg='white', activeforeground='#182631', activebackground='#FFC1CC')
            self.Meniu_4.configure(bg='#182631', fg='white', activeforeground='#182631', activebackground='#FFC1CC')
            
            # Crearea tk.Button
        
            self.button = tk.Button(self.root, text="Compute", width=20, font=("Calibri", 14),
                                    command=self.compute, bg='#182631', fg='white',
                                    activeforeground='#182631', activebackground='#FFC1CC')

            self.clear_button = tk.Button(self.root, text="Clear", width=20, font=("Calibri", 14),
                                          command=self.clear, bg='#182631', fg='white',
                                          activeforeground='#182631', activebackground='#FFC1CC')

            self.curatare_lista_json_buton = tk.Button(self.root, text='Curatare JSON',
                                                       width=20, font=('Calibri', 14), bg='#182631',
                                                       fg='white', activeforeground='#182631',
                                                       activebackground='#FFC1CC',
                                                       command=self.curatare_json)

            self.export_lista_json_html_buton = tk.Button(self.root, text='Export JSON',
                                                          width=20, font=('Calibri', 14), bg='#182631',
                                                          fg='white', activeforeground='#182631',
                                                          activebackground='#FFC1CC',
                                                          command=self.export_html)
            # Asezarea Widet-urilor de tip tk.Button
            
            self.button.grid(row=8, column=0, padx=20, pady=100)
            self.clear_button.grid(row=8, column=1, pady=100)
            self.curatare_lista_json_buton.grid(row=8, column=2, padx=20, pady=100)
            self.export_lista_json_html_buton.grid(row=8, column=3, padx=20, pady=100)

            # Optiuni
            
            self.options = {"Euler": "1", "Runge-Kutta ordin 2": "2", "Runge-Kutta ordin 4": "3"}
            for (txt, val) in self.options.items():
                self.rb = tk.Radiobutton(self.root, text=txt, variable=self.v, value=val,
                                         relief='groove', fg='#FF007F', bg='#020B10')
                self.rb.grid(row=val, column=3, padx=30, pady=10)
        
            # Crearea tk.Menu
        
            self.menubar = tk.Menu(self.root)
        
            self.filemenu = tk.Menu(self.menubar, tearoff=0)
            self.filemenu.add_command(label="Compute", command=self.compute)
            self.filemenu.add_command(label="Clear", command=self.clear)
            self.filemenu.add_command(label="Exit", command=self.root.destroy)
        
            self.menubar.add_cascade(menu=self.filemenu, label="File")
            self.root.config(menu=self.menubar, bg='#020B10')
            
            # Crearea Matplotlib
        
            self.fig = Mtp(figsize=(7, 5), dpi=100, facecolor='#5b4965')
            self.ax = self.fig.add_subplot(1, 1, 1)
            self.ax.tick_params(colors='#F2B8C6', which='both')
            self.ax.spines['top'].set_color('#FE7D6A')
            self.ax.spines['right'].set_color('#FE7D6A')
            self.ax.spines['bottom'].set_color('#FE7D6A')
            self.ax.spines['left'].set_color('#FE7D6A')
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('y')
            self.ax.set_facecolor('#2e293a')
            self.ax.grid(True)
            self.plot_canvas = FigureCanvasTkAgg(self.fig, master=self.root)
            self.toolbar_frame = tk.Frame(master=self.root, bd=2)
            self.toolbar_frame.grid(row=7, column=4)
            self.toolbar = NavigationToolbar2Tk(self.plot_canvas, self.toolbar_frame)
            self.plot_canvas.draw()
            self.plot_canvas.get_tk_widget().grid(row=2, column=4, rowspan=5, padx=20, pady=50)

            # Zona de final
        
            self.time_entry = tk.Entry(self.root, width=22, font=('Calibri', 12),
                                       state='readonly', textvariable=self.time_text,
                                       fg='white', readonlybackground='#915F6D')
            self.time_entry.grid(row=1, column=4)
        
            self.root.mainloop()
            
        except KeyboardInterrupt:
            self.root.destroy()
            
    '''

    def plot(self, x, y, sol, title):
        
        self.ax.clear()
        self.ax.plot(x, y, ls='solid', marker='o', mfc='red', mec='cyan', label='Solutia metodei')
        self.ax.plot(x, sol, ls='solid', marker='o', mfc='#FA8070', mec='#FF00FF', label='Solutia Exacta', color='cyan')
        self.ax.set_title(title)
        self.ax.set_facecolor('#2e293a')
        self.ax.legend()
        self.ax.grid(True)
        self.plot_canvas.draw()
        
    '''
        
    def animate(self, x, y, sol, title):
        xu = []
        yu = []
        solu = []
        
        self.ax.plot(xu, yu, ls='solid', marker='o', mfc='red',
                     mec='cyan', label='Solutia metodei')
        self.ax.plot(xu, solu, ls='solid', marker='o', mfc='#FA8070',
                     mec='#FF00FF', label='Solutia Exacta', color='cyan')

        def update(i):
            try:
                xu.append(x[i])
                yu.append(y[i])
                solu.append(sol[i])
                self.ax.clear()
                self.ax.plot(xu, yu, ls='solid', marker='o', mfc='red',
                             mec='cyan', label='Solutia metodei')
                self.ax.plot(xu, solu, ls='solid', marker='o', mfc='#FA8070',
                             mec='#FF00FF', label='Solutia Exacta', color='cyan')
                self.ax.tick_params(colors='#F2B8C6', which='both')
                self.ax.spines['top'].set_color('#FE7D6A')
                self.ax.spines['right'].set_color('#FE7D6A')
                self.ax.spines['bottom'].set_color('#FE7D6A')
                self.ax.spines['left'].set_color('#FE7D6A')
                self.ax.set_xlabel('x')
                self.ax.set_ylabel('y')
                self.ax.set_title(title)
                self.ax.set_facecolor('#2e293a')
                self.ax.legend()
                self.ax.grid(True)
            except Exception:
                return
        ani = FuncAnimation(fig=self.fig, func=update, interval=1000)
        print(ani)
        self.plot_canvas.draw()

    def compute(self):
        start = timeit.timeit()
        try:
            x0 = float(self.entrybox1.get())
            y0 = float(self.entrybox2.get())
            n = int(self.entrybox3.get())
            if n == 0:
                tk.messagebox.showerror('Eroare', "Camp completat invalid")
            h = float(self.entrybox4.get())
            if h == 0:
                tk.messagebox.showerror('Eroare', "Camp completat invalid")
            expr = self.entrybox5.get()
            if expr == "":
                tk.messagebox.showerror('Eroare', "Camp completat invalid")
            x = Symbol('x')
            y = Symbol('y')
            f = lambdify((x, y), expr)

            def returns_dydt(elem1, elem2):
                return f(elem1, elem2)

            method = self.v.get()
            sol_ode = list()

            x = np.linspace(x0, x0 + (n - 1) * h, n)
            y = np.zeros(n)
            y[0] = y0

            if method == "1":
                title = "Euler:"
                for i in range(0, n - 1):
                    x[i + 1] = x[i] + h
                    y[i + 1] = y[i] + h * f((x[i]), (y[i]))

                sol_ode = odeint(returns_dydt, y0, x)
                self.animate(x, y, sol_ode, title)
            # self.plot(x, y, sol_ode, title)
            elif method == "2":
                title = "Runge-Kutta ordin 2"
                for i in range(0, n - 1):
                    x[i + 1] = x[i] + h
                    k1 = h * f(x[i], y[i])
                    k2 = h * f(x[i + 1], y[i] + k1)
                    y[i + 1] = y[i] + 1 / 2 * (k1 + k2)

                sol_ode = odeint(returns_dydt, y0, x)
                self.animate(x, y, sol_ode, title)
            # self.plot(x, y, sol_ode, title)

            elif method == "3":
                title = "Runge-Kutta ordin 4"
                for i in range(0, n - 1):
                    x[i + 1] = x[i] + h
                    k1 = h * f(x[i], y[i])
                    k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
                    k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
                    k4 = h * f(x[i] + h, y[i] + k3)
                    y[i + 1] = y[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

                sol_ode = odeint(returns_dydt, y0, x)
                self.animate(x, y, sol_ode, title)
            # self.plot(x, y, sol_ode, title)

            end = timeit.timeit()
            timp = start - end
            self.time_text.set(str(timp))

            # ZONA PT. BACK-END

            # Realizarea unui obiect de tip Problema
            info30 = Problema(x0, y0, n, h, expr, sol_ode.tolist(), str(timp))
            print('Problema noua care va fi introdusa: ' + str(info30))
            # Realizarea unui obiect de tip Tabel
            GUI.tabelINITIAL = Tabel()
            # Actualizarea meniului de tip istoric
            # Pentru istoricul lui X0
            meniu0 = self.Meniu_0['menu']
            meniu0.delete(0, 'end')
            for element in self.actualizare_meniuri_istoric(GUI.tabelINITIAL)[0]:
                meniu0.add_command(label=element, command=lambda value=element: self.variabila_0.set(value))

                # Pentru istoricul lui Y0
            meniu1 = self.Meniu_1['menu']
            meniu1.delete(0, 'end')
            for element in self.actualizare_meniuri_istoric(GUI.tabelINITIAL)[1]:
                meniu1.add_command(label=element, command=lambda value=element: self.variabila_1.set(value))

                # Pentru istoricul lui n
            meniu2 = self.Meniu_2['menu']
            meniu2.delete(0, 'end')
            for element in self.actualizare_meniuri_istoric(GUI.tabelINITIAL)[2]:
                meniu2.add_command(label=element, command=lambda value=element: self.variabila_2.set(value))

                #  Pentru istoricul lui h
            meniu3 = self.Meniu_3['menu']
            meniu3.delete(0, 'end')
            for element in self.actualizare_meniuri_istoric(GUI.tabelINITIAL)[3]:
                meniu3.add_command(label=element, command=lambda value=element: self.variabila_3.set(value))

                # Pentru istoricul lui fxy
            meniu4 = self.Meniu_4['menu']
            meniu4.delete(0, 'end')
            for element in self.actualizare_meniuri_istoric(GUI.tabelINITIAL)[4]:
                meniu4.add_command(label=element, command=lambda value=element: self.variabila_4.set(value))

            # Afisarea tabelului in consola
            print(GUI.tabelINITIAL.tabel_probleme)
            print('\n')
            # Terminarea zonei

        except Exception:
            tk.messagebox.showerror('Eroare',
                                    "Unul sau mai multe campuri introduse sunt invalide! (Tipurile acceptate, " +
                                    "in functie de ordine, sunt: float, float, int, float & string).")

    def clear(self):
        self.entrybox1.delete(0, tk.END)
        self.entrybox2.delete(0, tk.END)
        self.entrybox3.delete(0, tk.END)
        self.entrybox4.delete(0, tk.END)
        self.entrybox5.delete(0, tk.END)

    
GUI()
