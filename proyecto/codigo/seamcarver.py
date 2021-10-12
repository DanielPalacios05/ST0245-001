import numpy as np
from math import sqrt
from skimage import transform
from numba import jit


class SeamCarver:

    def __init__(self, image):
        self.image = image
        self.H, self.W = image.shape

    def getXgradient(self, i, j):
        r_side = 0
        l_side = 0

        if(j == 0):
            # lADO DERECHO ESTA IZQUIERDO NO
            r_side = self.image[i][j+1]
            l_side = self.image[i][self.W-1]
        elif(j == self.W-1):
            # IZQUIERDO ESTA DERECHO NO
            r_side = self.image[i][0]
            l_side = self.image[i][j-1]
        else:
            r_side = self.image[i][j+1]
            l_side = self.image[i][j-1]

        return r_side - l_side

    def getYgradient(self, i, j):
        top = 0
        bottom = 0

        if(i == 0):
            # EN LA PARTE SUPERIOR
            top = self.image[self.H-1][j]
            bottom = self.image[i+1][j]
        elif(i == self.H-1):
            # PARTE INFERIOR
            top = self.image[i-1][j]
            bottom = self.image[0][j]
        else:
            top = self.image[i+1][j]
            bottom = self.image[i-1][j]

        return top - bottom

    def energy(self, i, j):
        x_grad = self.getXgradient(i, j)**2
        y_grad = self.getYgradient(i, j)**2

        resul = sqrt(x_grad + y_grad)

        return resul

    def energyMap(self):

        energyMap = np.empty((self.H, self.W))

        for i in range(self.H):
            for j in range(self.W):
                energyMap[i][j] = self.energy(i, j)

        return energyMap
    
    def minimum_seam(self):
        
        r, c,  = self.H,self.W
        energy_map = self.energyMap()

        M = energy_map.copy()
        
        backtrack = np.zeros_like(M, dtype=np.int)

        for i in range(1, r):
            for j in range(0, c):
                # Handle the left edge of the image, to ensure we don't index -1
                if j == 0:
                    idx = np.argmin(M[i - 1, j:j + 2])
                    backtrack[i, j] = idx + j
                    min_energy = M[i - 1, idx + j]
                else:
                    idx = np.argmin(M[i - 1, j - 1:j + 2])
                    backtrack[i, j] = idx + j - 1
                    min_energy = M[i - 1, idx + j - 1]

                M[i, j] += min_energy

        return M, backtrack
    
    def carve_column(self):
        r, c = self.H,self.W
        
        M, backtrack = self.minimum_seam()

        mask = np.ones((r, c), dtype=np.bool)

        j = np.argmin(M[-1])
        for i in reversed(range(r)):
            mask[i, j] = False
            j = backtrack[i, j]
            
        self.image = self.image[mask].reshape((r, c - 1))
        self.W -= 1
    
    def carve(self):
        #Crop a row and a column
        self.carve_column()
        self.image = np.rot90(self.image,1,(1,0))
        self.H, self.W = self.image.shape
        self.carve_column()
        self.image = np.rot90(self.image,3,(1,0))
        self.H, self.W = self.image.shape
        
    def crop(self,percent):
        new_c = int(percent * self.W)
        
        for _ in range(self.W-new_c):
            self.carve()

        
        
        
        
        

        