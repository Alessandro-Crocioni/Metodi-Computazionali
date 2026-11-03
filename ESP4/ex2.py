import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class muone1():
    """
    classe per rappresentare il muone incidente sul piano1 (più alto)

    Parametri
    ------------------------------------
    ang_pol1 = angolo polare (del primo impatto)
    ang_az1  = angolo azimutale (del primo impatto)
    x1       = coordinata x di impatto (del primo impatto)
    y1       = coordinata y di impatto (del primo impatto)
    
    """
    def __init__(self, ang_pol1, ang_az1, x1, y1):
        self.ang_pol1 = ang_pol1
        self.ang_az1 = ang_az1
        self.x1 = x1
        self.y1 = y1


class muone2():   
    """
    classe per rappresentare un muone incidente sul piano2 (più basso)
    
    Parametri
    ------------------------------------
    ang_pol2 = angolo polare (del secondo impatto)
    ang_az2  = angolo azimutale (del secondo impatto)
    x2       = coordinata x di impatto (del secondo impatto)
    y2       = coordinata y di impatto (del secondo impatto)
        
    """
    def __init__(self, ang_pol2, ang_az2, x2, y2):
        self.ang_pol1 = ang_pol2
        self.ang_az1 = ang_az2
        self.x1 = x2
        self.y1 = y2


class Rilevatore():
    """
    Classe che definisce il rilevatore di muoni

    Parametri
    --------------------------------------
    pitch = Largezza di ogni striscia rilevatrice
    h     = distanza tra i due piani (circa 500mm)
    l     = larghezza lato del rilevatore (circa 400mm)
    num   = numero striscie in entrambe le direzioni 
    error = errore associato alle misure di x e y

    """

    def __init__(self, pitch, h, l):
        self.pitch = pitch
        self.h = h
        self.l = l
        num = l/pitch
        error = pitch / np.sqrt(12)

        