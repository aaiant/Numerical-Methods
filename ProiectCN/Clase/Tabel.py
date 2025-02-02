# Zona de import

import pandas as pd
import json
import numpy as np
import os
from Clase.Probleme import Problema


class Tabel:
    
    # Constructor
    def __init__(self):
        self.lista_index_problema = list()
        self.lista_coloane_problema = list()
        self.lista_obiecte_problema = list()
        # Apelarea automata a metodei prelucrare_tabel_pandas_probleme si stocarea ei
        self.tabel_probleme, self.forma_tabel_pandas, self.nr_linii_tabel_pandas, \
            self.nr_coloane_tabel_pandas, self.nr_elemente_tabel_pandas = self.prelucrare_tabel_pandas_probleme()
    
    # Zona de Gettere
    
    @property
    def lista_index_problema(self):
        return self._lista_index_problema
    
    @property 
    def lista_coloane_problema(self):
        return self._lista_coloane_problema
    
    @property 
    def lista_obiecte_problema(self):
        return self._lista_obiecte_problema
    
    @property
    def tabel_probleme(self):
        return self._tabel_probleme
    
    @property
    def nr_linii_tabel_pandas(self):
        return self._nr_linii_tabel_pandas
    
    @property
    def nr_coloane_tabel_pandas(self):
        return self._nr_coloane_tabel_pandas
    
    @property
    def forma_tabel_pandas(self):
        return self._forma_tabel_pandas
    
    @property
    def nr_elemente_tabel_pandas(self):
        return self._nr_elemente_tabel_pandas
    
    # Zona de Settere
    
    @lista_index_problema.setter 
    def lista_index_problema(self, val):
        try:
            assert type(val) == list
            self._lista_index_problema = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip lista!'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'lista_index_problema\'!')

    @lista_coloane_problema.setter 
    def lista_coloane_problema(self, val):
        try:
            assert type(val) == list
            self._lista_coloane_problema = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip lista!'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'lista_coloane_problema\'!')

    @lista_obiecte_problema.setter 
    def lista_obiecte_problema(self, val):
        try:
            assert type(val) == list
            self._lista_obiecte_problema = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip lista!'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'lista_obiecte_problema\'!')

    @tabel_probleme.setter 
    def tabel_probleme(self, val):
        try:
            assert type(val) == pd.DataFrame
            self._tabel_probleme = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip DataFrame!'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'tabel_probleme\'!')
            
    @nr_linii_tabel_pandas.setter 
    def nr_linii_tabel_pandas(self, val):
        try:
            assert type(val) == int
            self._nr_linii_tabel_pandas = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip int!'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'nr_linii_tabel_pandas\'!')
            
    @nr_coloane_tabel_pandas.setter 
    def nr_coloane_tabel_pandas(self, val):
        try:
            assert type(val) == int
            self._nr_coloane_tabel_pandas = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip int!'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'nr_coloane_tabel_pandas\'!')
            
    @forma_tabel_pandas.setter 
    def forma_tabel_pandas(self, val):
        try:
            assert type(val) == tuple
            self._forma_tabel_pandas = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip tuplu!'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'forma_tabel_pandas\'!')
            
    @nr_elemente_tabel_pandas.setter 
    def nr_elemente_tabel_pandas(self, val):
        try:
            assert type(val) == int
            self._nr_elemente_tabel_pandas = val 
        except AssertionError:
            print('Valoarea \'{0}\' nu este de tip int!'.format(val))
        except AttributeError:
            print('Ati omis argumentul in cadrul setter-ului pt. \'nr_elemente_tabel_pandas\'!')
    # Zona de metode
    
    def prelucrare_tabel_pandas_probleme(self):
        
        # Deschiderea fisierului de tip JSON
        with open('..\\Fisiere\\JSON\\Date.json') as fisier_json:
            informatii = json.load(fisier_json)
            
            # Accesarea elementelor din fisierul JSON
            for lista in informatii.values():
                for dictionar in lista:
                    for index in dictionar.keys():
                        # Determinarea fiecarui index al obiectelor
                        self.lista_index_problema.append(index)
                    for obiect in dictionar.values():
                        # Determinarea dictionariilor / obiectelor
                        self.lista_obiecte_problema.append(obiect)
                    for coloana in obiect.keys():
                        # Determinarea coloanelor
                        self.lista_coloane_problema.append(coloana)

            # Inchiderea fisierului de tip JSON
            fisier_json.close()
            
        # Realizarea tabelului de tip DataFrame
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        tabel_pandas = pd.DataFrame(self.lista_obiecte_problema, self.lista_index_problema)
        
        # Determinarea formei tabelului de tip DataFrame
        forma_tabel_pandas = tabel_pandas.shape
        
        # Determinarea nr. liniilor tabelului de tip DataFrame
        nr_linii_tabel_pandas = tabel_pandas.shape[0]
        
        # Determinarea nr. coloanelor tabelului de tip DataFrame
        nr_coloane_tabel_pandas = tabel_pandas.shape[1]
        
        # Determinarea nr. de elemente ale tabelului de tip DataFrame
        nr_elemente_tabel_pandas = int(tabel_pandas.size)
        
        # Zona de return
        return tabel_pandas, forma_tabel_pandas, nr_linii_tabel_pandas, \
            nr_coloane_tabel_pandas, nr_elemente_tabel_pandas

    @staticmethod
    def curatare_tabel_pandas_probleme_json():
        # Redeschiderea fisierului de tip JSON
        adresa = '..\\Fisiere\\JSON\\Date.json'
        os.remove(adresa)
        prima_problema = Problema(0.0, 0.0, 0, 0.0, 'None', np.zeros((2, 3)).tolist(), '0.0')

