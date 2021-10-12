import os
from numpy import genfromtxt
from seamcarver import SeamCarver
from matplotlib.pyplot import imsave 

path_enfermos = input("Path de enfermo_csv: ")
path_sanos = input("Path de sano_csv: ")

path = "Imagenes_Comprimidas"      

try:    
    os.mkdir(path)
    os.mkdir(path + "/sanos")
    os.mkdir(path + "/enfermos")
except OSError:
    print("Las imagenes ya han sido comprimidas")
      
for archivos in os.listdir(path_enfermos):

    file_data = genfromtxt(path_enfermos + "/" + archivos, delimiter=',')

    # Aqui usariamos el algoritmo de compresion usando file_data
    
    sm = SeamCarver(file_data)
    print("comprimiendo")
    sm.crop(0.75)
    
    
    filename = archivos[:-4]
    folder = "Imagenes_Comprimidas/enfermos/"+filename+".jpg"
    imsave(folder,sm.image, cmap = "gray")
    print("guardao!")
    
    
for archivos in os.listdir(path_sanos):
        
    file_data = genfromtxt(path_sanos + "/" + archivos, delimiter=',')

    # Aqui usariamos el algoritmo de compresion usando file_data
    
    sm = SeamCarver(file_data)
    print("comprimiendo")
    sm.crop(0.75)
    
    
    filename = archivos[:-4]
    folder = "Imagenes_Comprimidas/sanos/"+filename+".jpg"
    imsave(folder,sm.image, cmap = "gray")
    print("guardao!")
            
    




