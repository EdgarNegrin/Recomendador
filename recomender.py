import numpy as np
from numpy.lib.function_base import append

class recomender:
  def __init__(self, nameFile):
    self.matrix = None
    self.vecinos = 0
    self.medias = []
    self.loadFile(nameFile)
    self.similitud = np.zeros(shape=(len(self.matrix),len(self.matrix)))


  def pearson(self):
    # Calculo de items a comparar
    similitud = 0
    
    for i in range(len(self.matrix)):
      for k in range(len(self.matrix)):
        persona1 = self.matrix[i]
        persona2 = self.matrix[k]
        media1 = 0
        media2 = 0
        indices = []
        sumatorios = [[], [], []]
        solucion = []
        
        for j in range(len(persona1)):
          if (persona1[j] != -1) and (persona2[j] != -1):
            indices.append(j)
      
        # Calculo de las medias
        for j in indices:
          media1 += persona1[j]
          media2 += persona2[j]
        
        media1 = media1 / len(indices)
        media2 = media2 / len(indices)
        
        # Calculo
        for j in indices:
          sumatorios[0].append((persona1[j] - media1) * (persona2[j] - media2))
          sumatorios[1].append((persona1[j] - media1) ** 2)
          sumatorios[2].append((persona2[j] - media2) ** 2)
        
        solucion.append(sum(sumatorios[0]))
        solucion.append(np.sqrt(sum(sumatorios[1])))
        solucion.append(np.sqrt(sum(sumatorios[2])))
        
        similitud = solucion[0] / (solucion[1] * solucion[2])
        self.similitud[i][k] = similitud
        print(similitud)


  def coseno(self):
    # Calculo de items a comparar
    similitud = 0
    for i in range(len(self.matrix)):
      for k in range(len(self.matrix)):
        persona1 = self.matrix[i]
        persona2 = self.matrix[k]
        indices = []
        sumatorios = [[], [], []]
        solucion = []
        
        for j in range(len(persona1)):
          if (persona1[j] != -1) and (persona2[j] != -1):
            indices.append(j)
        
        # Calculo
        for j in indices:
          sumatorios[0].append(persona1[j] * persona2[j])
          sumatorios[1].append(persona1[j] ** 2)
          sumatorios[2].append(persona2[j] ** 2)
        
        solucion.append(sum(sumatorios[0]))
        solucion.append(np.sqrt(sum(sumatorios[1])))
        solucion.append(np.sqrt(sum(sumatorios[2])))
        
        similitud = solucion[0] / (solucion[1] * solucion[2])
        self.similitud[i][k] = similitud


  def euclidea(self):
    # Calculo de items a comparar
    similitud = 0
    for i in range(len(self.matrix)):
      for k in range(len(self.matrix)):
        persona1 = self.matrix[i]
        persona2 = self.matrix[k]
        indices = []
        sumatorio = []
        
        for j in range(len(persona1)):
          if (persona1[j] != -1) and (persona2[j] != -1):
            indices.append(j)
        
        # Calculo
        for j in indices:
          sumatorio.append((persona1[j] - persona2[j]) ** 2)
        
        similitud = (np.sqrt(sum(sumatorio)))
        
        self.similitud[i][k] = similitud
        print(i, k, similitud)
  

  def loadFile(self, nameFile):
    textFile = open(nameFile, 'r')
    datos = ''.join(textFile.readlines())
    vector = datos.split("\n")
    for i in range(0, len(vector)):
       vector[i] = vector[i].split(" ")
       for j in range(0, len(vector[i])):
         if(vector[i][j].isdigit()):
           vector[i][j] = int(vector[i][j])
         else:
           vector[i][j] = -1
    self.matrix = vector
    
    textFile.close()

  