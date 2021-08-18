import os

def read_csv(filename):
    try:
        with open(filename, 'r') as f:
            raw_data = f.readlines()
            
        for line in range(len(raw_data)):
            raw_data[line] = list(map(int,raw_data[line].strip().split(',')))
            
        return raw_data
    except:
        print("Data wasn't processed correctly")
        

path_enfermos = input("Path de enfermo_csv: ")
path_sanos = input("Path de sano_csv: ")
      
for archivos in os.listdir(path_enfermos):

    file_data = read_csv(path_enfermos + "/" + archivos)

    # Aqui usariamos el algoritmo de compresion usando file_data
    
for archivos in os.listdir(path_sanos):
        
    file_data = read_csv(path_sanos + "/"  + archivos)
    # Aqui usariamos el algoritmo de compresion usando file_data 
            
    
