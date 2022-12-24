#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
from distutils import command
import jsonschema
from jsonschema import validators

if __name__ == "__main__":

    a = {1: "sova", 2 :"sich", 3: "mouse"}
    print(a)
    print(a[1])
    print(type(a[1]))
    
    print("Введите путь к файлу")
    
    f = input()
    gr = {}
    
    with open(f, "r", encoding = "utf-8") as test:
        
        b = [f for line in test for f in line.split()]
        test.close()
        print(b)
        print(b[0])
        print(type(b[0]))
        
        i = 0
        
        while i < len(b):
            q = b[i]
            print(b[i])
            print(type(b[i]))
            
            if a[1] == q.lower() or a[2] == q.lower() or a[3] == q.lower():
                print("Слово не имеет ошибок")
                gr[q.lower()] = i
            else:
                print("В слове ошибка или его нет в списке")
                gr["___"] = i
            i = i + 1

    with open("ewr.txt", "w") as json_file:
        json.dump(a, json_file, indent=4)  
