# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:30:08 2020

@author: binej
"""
import numpy as np
import random

switch={'A':[14, 21, 28], 'M':[25, 50, 75], 'O':[32, 34, 36], 'N':[55, 65, 75], 'L':[22, 33, 44], 
        'F':[42, 48, 54], 'B':[11, 99, 77], 'E':[87, 98, 76], 'T':[13, 26, 38], 'Y':[61, 41, 81], 
        'C':[17, 18, 19], 'Z':[99, 97, 95], 'I':[12, 23, 15], ' ':[' ',' ',' '], 'W':[44, 66, 64],
        'U':[16, 10, 20], 'S':[24, 27, 29], 'R':[30, 40, 50], 'G':[31, 35, 37], 'J':[39, 43, 45],
        'K':[46, 47, 49], 'P':[51, 52, 53], 'H':[56, 57, 58], 'D':[59, 60, 62]} 

def litera(i):   
    if(i in switch):
        zbior=switch.get(i)
        index = random.randrange(0,3)
        return zbior[index]
    
tekst = "JAK LATWO ZAUWAZYC SZYFR MONOALFABETYCZNY NIE JEST WCALE BEZPIECZNY PONIEWAZ ZDRADZA CHARAKTERYSTYKE JEZYKOWA TEKSTU ZASZYFROWANEGO"
for i in tekst:
    print(str(litera(i)),end=" ")
    
cipher = [39, 28, 46,   44, 21, 38, 44, 36,  95, 14, 10, 44, 28, 99, 61, 18,  27, 97, 81, 48, 30,   25, 32, 55, 32, 14, 33, 54, 28, 11, 87, 38, 81, 17, 97, 55, 61,   55, 23, 98,   45, 98, 27, 38,   66, 18, 28, 44, 87,   77, 87, 99, 53, 23, 98, 19, 99, 75, 61,   53, 32, 65, 12, 76, 64, 21, 95,   95, 62, 40, 21, 62, 97, 14,   17, 57, 28, 40, 28, 46, 38, 87, 50, 61, 27, 26, 81, 49, 87,   43, 87, 97, 81, 49, 34, 64, 21,   26, 76, 46, 29, 38, 20,   95, 14, 27, 99, 61, 42, 30, 34, 64, 21, 65, 98, 37, 36]
print("-----------------------------")
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
            print(list1.count(x),x)

    
unique(cipher)