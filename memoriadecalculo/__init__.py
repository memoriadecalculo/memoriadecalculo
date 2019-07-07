#!/usr/bin/env python3
# -*- coding: cp1252 -*-

# Base
# ====
# 
# Este módulo define variáveis, cria objetos e mostra como importar
# as bibliotecas comuns, para todos os demais módulos.
# 
# O código abaixo desliga a divisão padrão para números inteiros. Desta
# forma, ao dividir números inteiros, o resultado poderá ser real também.
# Divisão de números inteiros é um erro comum.
# 
# .. code:: python

from __future__ import division

# O código abaixo inicializa o diretório base e serve de código para os
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
# Biblioteca com as funções matemáticas comumente utilizadas na engenharia
# como, por exemplo, seno, cosseno, tangente, etc.
# 
# .. code-block:: python
# 
#   from math import *
# 
# NumPy
# ~~~~~
# 
# Biblioteca para manipulação de arrays multidimensionais e matrizes.
# Ideal para álgebra linear.
# 
# .. code:: python

## import numpy as np

# SymPy
# ~~~~~
# 
# Biblioteca para manipulação de equações simbólicas.
# 
# Altere a configuração "mp.pretty" para que a impressão não saia com o
# tipo "mpf(...)".
# 
# .. code:: python

import sympy as syp
syp.mpmath.mp.pretty = True

# Unidades
# --------
# 
# A biblioteca Unum é ótima para trabalhar com dimensões em Python.
# 
# Acesse: http://home.scarlet.be/be052320/Unum.html, ou
# http://home.scarlet.be/be052320/docs.html para visualizar a
# documentação.
# 
# Para importar as unidades e trabalhar com elas no script, execute o
# código abaixo:
# 
# .. code:: python

from unum import Unum
from unum.units import m, s, N, Pa, kg

# A fim de facilitar o desenvolvimento de cálculos nesta seção, seguem
# abaixo algumas definições:
# 
# .. code:: python

Unum.VALUE_FORMAT = "%.2f"

grav  = Unum.unit('grav',10*m/s**2,'gravity')
# gravV = grav * np.array([0,0,-1])
kN    = Unum.unit('kN',1000*N,'kilo Newton')
MPa   = Unum.unit('MPa',10**6*Pa,'mega Pascal')

# 
# Objetos e Funções
# -----------------
# 
# Segue abaixo um objeto base para facilitar atividades comuns como, por
# exemplo, impressão de resultados, controle de alteração, etc:
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

    alterado = property(fget=get_alterado, fset=set_alterado, doc="controle de alteração do objeto")

    def calcular(self):
        # Nas subclasses, chamar este método a implementação do mesmo nela.
        self.alterado = False

# Função para exibir o conteúdo de um arquivo tipo CSV:
# 
# .. code:: python

def arquivo2dict(nomeArquivo, sep = ";"):
    from collections import OrderedDict

    arquivo = open(nomeArquivo, 'r')
    linhas = arquivo.readlines()
    arquivo.close()

    # Lê o cabeçalho e cria os dicionários para cada coluna
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

# Detonações
# ----------------
# Durante as explosões são utilizados sensores de aceleração de partículas com posterior comparação com valores especificados em NBR (não lembro qual).
# Quando a campanha de detonações for demorar muito tempo, utiliza-se também pinos de recalque fixados nas edificações próximas com medição de tempos em tempos.
# 
# TODO: Verificar um local melhor para estas funções e seção.
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
# TODO: Colocar figura para esta função.
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