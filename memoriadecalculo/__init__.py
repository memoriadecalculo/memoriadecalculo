#!/usr/bin/env python3
# -*- coding: cp1252 -*-

# Base
# ====
# 
# Este m�dulo define vari�veis, cria objetos e mostra como importar
# as bibliotecas comuns, para todos os demais m�dulos.
# 
# O c�digo abaixo desliga a divis�o padr�o para n�meros inteiros. Desta
# forma, ao dividir n�meros inteiros, o resultado poder� ser real tamb�m.
# Divis�o de n�meros inteiros � um erro comum.
# 
# .. code:: python

from __future__ import division

# O c�digo abaixo inicializa o diret�rio base e serve de c�digo para os
# demais arquivos importarem esta biblioteca.
# 
# .. code-block:: python
#  
#   import os
#   import sys
#   BASE_DIR = os.path.dirname(os.path.abspath(os.getcwd()))
#   if not BASE_DIR in sys.path:
#       sys.path.insert(0, BASE_DIR)
# 
# Bibliotecas
# -----------
# 
# math
# ~~~~
# 
# Biblioteca com as fun��es matem�ticas comumente utilizadas na engenharia
# como, por exemplo, seno, cosseno, tangente, etc.
# 
# .. code-block:: python
# 
#   from math import *
# 
# NumPy
# ~~~~~
# 
# Biblioteca para manipula��o de arrays multidimensionais e matrizes.
# Ideal para �lgebra linear.
# 
# .. code:: python

## import numpy as np

# SymPy
# ~~~~~
# 
# Biblioteca para manipula��o de equa��es simb�licas.
# 
# Altere a configura��o "mp.pretty" para que a impress�o n�o saia com o
# tipo "mpf(...)".
# 
# .. code:: python

import sympy as syp
syp.mpmath.mp.pretty = True

# Unidades
# --------
# 
# A biblioteca Unum � �tima para trabalhar com dimens�es em Python.
# 
# Acesse: http://home.scarlet.be/be052320/Unum.html, ou
# http://home.scarlet.be/be052320/docs.html para visualizar a
# documenta��o.
# 
# Para importar as unidades e trabalhar com elas no script, execute o
# c�digo abaixo:
# 
# .. code:: python

from unum import Unum
from unum.units import m, s, N, Pa, kg

# A fim de facilitar o desenvolvimento de c�lculos nesta se��o, seguem
# abaixo algumas defini��es:
# 
# .. code:: python

Unum.VALUE_FORMAT = "%.2f"

grav  = Unum.unit('grav',10*m/s**2,'gravity')
# gravV = grav * np.array([0,0,-1])
kN    = Unum.unit('kN',1000*N,'kilo Newton')
MPa   = Unum.unit('MPa',10**6*Pa,'mega Pascal')

# 
# Objetos e Fun��es
# -----------------
# 
# Segue abaixo um objeto base para facilitar atividades comuns como, por
# exemplo, impress�o de resultados, controle de altera��o, etc:
# 
# .. code:: python

class base(object):
    def __init__(self):
        self.log = ""
        self._alterado = True

    def set_alterado(self, value):
        if value is bool:
            self._alterado = value

    def get_alterado(self):
        return self._alterado

    alterado = property(fget=get_alterado, fset=set_alterado, doc="controle de altera��o do objeto")

    def calcular(self):
        # Nas subclasses, chamar este m�todo a implementa��o do mesmo nela.
        self.alterado = False

# Fun��o para exibir o conte�do de um arquivo tipo CSV:
# 
# .. code:: python

def arquivo2dict(nomeArquivo, sep = ";"):
    from collections import OrderedDict

    arquivo = open(nomeArquivo, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    # L� o cabe�alho e cria os dicion�rios para cada coluna
    cabecalho = linhas[0].split(sep)
    result = OrderedDict()
    for nome in cabecalho:
        result[nome] = []

    # Carrega os dados em cada coluna
    for linha in linhas[1:]:
        valores = linha.split(sep)
        if len(valores) == 0:
            continue
        i = 0
        for nome in cabecalho:
            result[nome].append(valores[i])
            i += 1

    return result

# Detona��es
# ----------------
# Durante as explos�es s�o utilizados sensores de acelera��o de part�culas com posterior compara��o com valores especificados em NBR (n�o lembro qual).
# Quando a campanha de detona��es for demorar muito tempo, utiliza-se tamb�m pinos de recalque fixados nas edifica��es pr�ximas com medi��o de tempos em tempos.
# 
# TODO: Verificar um local melhor para estas fun��es e se��o.
# 
# .. code:: python

def area34(b_maior,b_menor,altura):
    result = (b_maior + b_menor) * altura / 2

    return result

def area4(base,altura):
    result = area34(base,base,altura)

    return result

def area3(base,altura):
    result = area34(base,0,altura)

    return result

# 
# TODO: Colocar figura para esta fun��o.
# 
# .. code:: python

def subvetor(vetorP1,vetorP2,coord,eixo):
    vetor21 = vetorP2 - vetorP1
    proporcao = (coord - vetorP1[eixo]) / (vetorP2[eixo] - vetorP1[eixo])
    result = vetor21 * proporcao + vetorP1

    return result

def areavetor3(P1,P2,P3):
    vetor21 = P2 - P1
    vetor31 = P3 - P1
    # matriz = np.vstack([vetor21,vetor31])
    # result = np.linalg.det(matriz) / 2
    # result = (np.cross(vetor21, vetor31) / 2 + np.cross(vetor41, vetor31) / 2)
    # return result

def areavetor4(P1,P2,P3,P4):
    result = areavetor3(P1,P2,P4) + areavetor3(P1,P4,P3)
    return result

def centroide3(P1,P2,P3):
    result = (P1 + P2 + P3) / 3
    return result

def centroide4(P1,P2,P3,P4):
    area1 = areavetor3(P1,P2,P4)
    area2 = areavetor3(P1,P4,P3)
    result = (centroide3(P1,P2,P4) * area1 + centroide3(P1,P4,P3) * area2) / (area1 + area2)
    return result

def x_m(b_0,b):
    result = (b_0**2 + b*b_0 + b**2) / (3 * (b + b_0))

    return result

# .. include:: <isoamsr.txt>
# 
# .. include:: </PRJ/mc/wsgi/variaveis.txt>
# 