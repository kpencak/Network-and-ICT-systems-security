# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 21:08:13 2020

@author: katar
"""
import numpy

def decode(pair):
    if pair == 'TT':
        return 'TT'
    else:
        for i in klucz:
            for j in klucz[i]:
                if pair[0] == klucz[i][j]:
                    a_row = i
                    a_col = j
                if pair[1] == klucz[i][j]:
                    b_row = i
                    b_col = j
        if a_row == b_row:
            litera1 = klucz[a_row][a_col-1]
            litera2 = klucz[b_row][b_col-1]
        elif a_col == b_col:
            litera1 = klucz[a_row-1][a_col]
            litera2 = klucz[b_row-1][b_col]
        else:
            if a_row > b_row and a_col < b_col:
                litera1

klucz = numpy.char.array([['R', 'O', 'Y', 'A', 'L'],
         ['N', 'E', 'W', 'Z', 'D'],
         ['V', 'B', 'C', 'F', 'G'],
         ['H', 'I', 'K', 'M', 'P'],
         ['Q', 'S', 'T', 'U', 'X']])

szyfrogram = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBWT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
szyfrogram.replace(" ", "")
szyfrogram.replace("J", "I")

tekst = []
for i in range(0, len(szyfrogram)-1, 2):
    tekst.append(decode(szyfrogram[i:i+1]))
   