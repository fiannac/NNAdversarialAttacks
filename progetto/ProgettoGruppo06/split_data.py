"""
Created on Thu May 13 15:23:29 2021

@author: franc
"""
import numpy as np
import os
from glob import glob

folders = glob("C:/Users/franc/OneDrive/Desktop/AnimalFace/*")#ottengo tutte la lista dei path delle cartelle
folder_names = os.listdir('C:/Users/franc/OneDrive/Desktop/AnimalFace')#lista dei nomi delle cartelle in quella directory

os.mkdir("C:/Users/franc/OneDrive/Desktop/dataset")
os.mkdir("C:/Users/franc/OneDrive/Desktop/dataset/train")
os.mkdir("C:/Users/franc/OneDrive/Desktop/dataset/test")
os.mkdir("C:/Users/franc/OneDrive/Desktop/dataset/validation")

for i in folder_names:
    os.mkdir("C:/Users/franc/OneDrive/Desktop/dataset/test/" + i)
for i in folder_names:
    os.mkdir("C:/Users/franc/OneDrive/Desktop/dataset/train/" + i)
for i in folder_names:
    os.mkdir("C:/Users/franc/OneDrive/Desktop/dataset/validation/" + i)

sizes = list()

for i in folders:
    data = glob(i + "/*")#ottengo la lista di tutti i path delle immagini in una cartella
    sizes.append(len(data))
#sizes conterrà per ogni cartella la sua dimensione in termini di immagini

for i,j,k in zip(folders, folder_names,sizes):#prende iteratori, li aggrega in tuple e li ritorna
    data = glob(i + "/*")
    size = k
    train_size = np.int64(np.round(4/6 * size))
    name = 0
    for img in data[:train_size]:
        os.rename(img, "C:/Users/franc/OneDrive/Desktop/dataset/train/" + j + "/" + str(name) + ".jpg")#sposto l'immagine dalla sua cartella originaria
        name += 1

for i,j,k in zip(folders, folder_names,sizes):
    data = glob(i + "/*")
    size = k
    train_size = np.int64(np.round(1/6 * size))
    name = 0
    for img in data[:train_size]:
        os.rename(img, "C:/Users/franc/OneDrive/Desktop/dataset/validation/" + j + "/" + str(name) + ".jpg")
        name += 1

for i,j,k in zip(folders, folder_names, sizes):
    data = glob(i + "/*")
    size = k
    train_size = np.int64(np.round(1/6 * size))
    name = 0
    for img in data[:train_size]:
        os.rename(img, "C:/Users/franc/OneDrive/Desktop/dataset/test/" + j + "/" + str(name) + ".jpg")
        name += 1
