# -*- coding: utf-8 -*-

"New line added to check the merge and the conflict status """
Spyder Editor

This is a temporary script file.
"""
import sys

class Train:

    
    def __init__(self, number,traintype):
        
        if not number[:2].isalpha():
            raise ValueError(f"No train code in '{number}")
        
        
        if not number[:2].isupper():
            raise ValueError(f"Invalide train code '{number}")
        
        if not (number[2:].isdigit() and (int(number[2:])<=9999)):
            raise ValueError(f"invalid route number '{number}")
            
        self._number =number
        self._traintype = traintype
        rows,  seats = self._traintype.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]


    def number (self):
        return(self._number)
    
    
    def train(self):
        return self._number[:2]
    
    def traintype_model(self):
        return self._traintype.model()
    
 

# Class  to accept the seat booking as per train model we need to know the seating layout
# train model nuumber, coach model number.
 

class TrainType:
    
    def  __init__(self, registeration, model, num_rows, num_seat_per_row):
        
        if num_rows<0:
            raise ValueError(f"Invalied number of row'{num_rows}")
        
        if num_seat_per_row<0:
            raise ValueError(f"Invalied number of row'{num_seat_per_row}")
            
        self._registeration = registeration
        self._model = model
        self._num_rows = num_rows
        self._num_seat_per_row = num_seat_per_row
    
    def model(self):
        return self._model
    
    def seating_plan(self):
        return(range(1,self._num_rows),"ABCDEFGHJ"[:self._num_seat_per_row])
    




 
 
 
 
    