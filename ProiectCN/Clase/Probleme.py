# Zona de import-uri
import json
import string
import random
import numpy as np


class Problema:
    # Dictionarul principal
    dictionarPrincipal = dict()
    
    # Lista principala 
    listaPrincipala = list()

    # Constructor
    def __init__(self, val_X0, val_Y0, val_n, val_h, val_fxy, val_solutiaOdeint, val_timp):
        self.X0 = val_X0
        self.Y0 = val_Y0
        self.n = val_n
        self.h = val_h
        self.f_xy = val_fxy
        self.solutiaOdeint = val_solutiaOdeint
        self.timp_de_executie = val_timp
        # Apelarea metodei care realizeaza fisierul JSON
        self.trimitere_info_json()
        
    # Zona de Gettere
    
    @property
    def X0(self):
        return self._X0
    
    @property
    def Y0(self):
        return self._Y0
    
    @property 
    def n(self):
        return self._n
    
    @property 
    def h(self):
        return self._h
    
    @property 
    def f_xy(self):
        return self._f_xy
    
    @property 
    def solutiaOdeint(self):
        return self._solutiaOdeint

    @property
    def timp_de_executie(self):
        return self._timp_de_executie
    
    # Zona de Settere
    
    @X0.setter 
    def X0(self, val):
        try:
            assert type(val) == float
            self._X0 = val
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip float'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'X0\'!')
            
    @Y0.setter
    def Y0(self, val):
        try:
            assert type(val) == float
            self._Y0 = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip float'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'Y0\'!')
            
    @n.setter 
    def n(self, val):
        try:
            assert type(val) == int 
            self._n = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip float'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'n\'!')
            
    @h.setter 
    def h(self, val):
        try:
            assert type(val) == float 
            self._h = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip float'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'h\'!')
            
    @f_xy.setter 
    def f_xy(self, val):
        try:
            assert type(val) == str 
            self._f_xy = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip string'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'f(x,y)\'!')
            
    @solutiaOdeint.setter
    def solutiaOdeint(self, val):
        try:
            assert type(val) == list
            self._solutiaOdeint = val
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip nr.array'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'solutia exacta\'!')

    @timp_de_executie.setter
    def timp_de_executie(self, val):
        try:
            assert type(val) == str
            self._timp_de_executie = val
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip string'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'timp de executie\'!')

    # Zona de metode 
    
    # Metoda de trimiterea a informatiilor catre un fisier de tip JSON
    def trimitere_info_json(self):
        # Realizarea unui dictionar primar
        dictionarPrimar = dict()
        
        # Realizarea unui dictionar secundar
        dictionarSecundar = dict()
        
        # Adaugarea atributelor clasei in dictionarul secundar
        
        dictionarSecundar.update({'X0': self.X0})
        dictionarSecundar.update({'Y0': self.Y0})
        dictionarSecundar.update({'n': self.n})
        dictionarSecundar.update({'h': self.h})
        dictionarSecundar.update({'f(x,y)': self.f_xy})
        dictionarSecundar.update({'solutia odeint': self.solutiaOdeint})
        dictionarSecundar.update({'timp de executie': self.timp_de_executie})
        
        # Realizarea cheii unice pt. dictionarul primar
        cheie = str(random.randrange(0, 9999, 1)) + random.choice(string.ascii_letters) + random.choice(
            string.ascii_letters)
        
        # Adaugarea dictionarului secundar ca argument al cheii '' din dictionarul principal
        dictionarPrimar.update({cheie: dictionarSecundar})
        
        # Adaugarea dictionarului primar in lista principala
        self.listaPrincipala.append(dictionarPrimar)
        
        # Adaugarea listei principale ca argument al cheii 'Probleme' din dictionarul principal
        self.dictionarPrincipal.update({'Probleme': self.listaPrincipala})
        
        # Realizarea fisierului de tip JSON
        try:
            with open('..\\Fisiere\\JSON\\Date.json', 'r+') as fisier_json:
                informatii = json.load(fisier_json)
                informatii['Probleme'].append(dictionarPrimar)
                fisier_json.seek(0)
                json.dump(informatii, fisier_json, indent=2)
        except FileNotFoundError:
            with open('..\\Fisiere\\JSON\\Date.json', 'w') as fisier_json:
                json.dump(self.dictionarPrincipal, fisier_json, indent=2)


# x = Problema(0.0, 0.0, 0, 0.0, 'None', np.zeros((2, 3)).tolist(), '0.0')
