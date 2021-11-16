import os
from numpy import genfromtxt, savetxt
from seamcarver import SeamCarver
from matplotlib.pyplot import imsave
import Huffman

path_enfermos = input("Path de enfermo_csv: ")
path_sanos = input("Path de sano_csv: ")

path = "Imagenes_Comprimidas"      

try:    
    os.mkdir(path)
    os.mkdir(path + "/sanos")
    os.mkdir(path + "/enfermos")
except OSError:
    print("Las carpetas han sido comprimidas")
      
for archivos in os.listdir(path_enfermos):

    file_data = genfromtxt(path_enfermos + "/" + archivos, delimiter=',')
    
    

    # Aqui usariamos el algoritmo de compresion usando file_data
    
    sm = SeamCarver(file_data)
    print("comprimiendo")
    sm.crop(0.75)
    
    
    filename = archivos[:-4]
    folder = "Imagenes_Comprimidas/enfermos/"+filename+".csv"
    
    savetxt(folder,sm.image, delimiter = ",")
        
    file = open(folder,'r')

    file = file.read()

    encoding, tree = Huffman.Huffman_Encoding(file)

    a = Huffman.Huffman_Decoding(encoding,tree)

    with open(folder,'w') as f:
	    f.write(a)

    
    
    
for archivos in os.listdir(path_sanos):
        
    file_data = genfromtxt(path_sanos + "/" + archivos, delimiter=',')

    # Aqui usariamos el algoritmo de compresion usando file_data
    
    sm = SeamCarver(file_data)
    print("comprimiendo")
    sm.crop(0.75)
    

    
    
    filename = archivos[:-4]
    folder = "Imagenes_Comprimidas/sanos/"+filename+".csv"
    
    file = open(folder,'r')

    file = file.read()

    encoding, tree = Huffman.Huffman_Encoding(file)

    a = Huffman.Huffman_Decoding(encoding,tree)

    with open(folder,'w') as f:
	    f.write(a)
     
     
            
    




