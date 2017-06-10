#!/usr/bin/python
# -*- coding: utf-8 -*-

 
#pruebas con BeautifulSoup y requests
 #no te preocupes no es un spyware
# las librerias
from bs4 import BeautifulSoup
import requests
import time
import os
 
# Bucle infinito
while True:
 
 # Capturamos la url 
 url = "http://www.timeanddate.com/weather/chile/santiago"
 

 r  = requests.get(url)
 data = r.text
 
 # objeto soup y le pasamos lo capturado con request
 soup = BeautifulSoup(data, 'lxml')
 
 # Buscamos el div para sacar los grados
 temp = soup.find_all('div', class_="h2")
 
 # Buscamos el div para sacar la sensacion termica
 sTerm = soup.find_all('div', class_="clear")


         
        # Con [0] saco el primer elemento y con [1] el segundo
 print "La temperatura en santiago: " + temp[0].text
 print "La sesacion termica: " + sTerm[1].text

  
 # Tiempo en segundos para ejecutarse nuevamente
 time.sleep(15)
  

 os.system("clear")