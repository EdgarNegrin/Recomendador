import numpy as np

class recomender:
  def __init__(self, nameFile, vecinos):
    self.matrix = None
    self.vecinos = vecinos
    self.medias = []
    self.vacios = []
    self.FlagEuclidea = False
    self.loadFile(nameFile)
    self.similitud = np.empty(shape=(len(self.matrix),len(self.matrix)))
    self.similitudSorted = []
    self.similitudVecinos = []

  def pearson(self):
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
          sumatorios[0].append((persona1[j] - self.medias[i]) * (persona2[j] - self.medias[k]))
          sumatorios[1].append((persona1[j] - self.medias[i]) ** 2)
          sumatorios[2].append((persona2[j] - self.medias[k]) ** 2)
        
        solucion.append(sum(sumatorios[0]))
        solucion.append(np.sqrt(sum(sumatorios[1])))
        solucion.append(np.sqrt(sum(sumatorios[2])))
        
        similitud = solucion[0] / (solucion[1] * solucion[2])
        self.similitud[i][k] = similitud
    self.similitudSort()


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
    self.similitudSort()


  def euclidea(self):
    self.FlagEuclidea = True
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
    self.similitudSort()
  

  def prediccionSimple(self):
    sumatorio = ([], [])
    
    for i in range(len(self.vacios)):
      vecinos = self.vecinosProximos(self.vacios[i][0], self.vacios[i][1])
      for j in range(self.vecinos):
        sumatorio[0].append(self.similitud[self.vacios[i][0]][vecinos[j]] * 
                            self.matrix[vecinos[j]][self.vacios[i][1]])
        sumatorio[1].append(abs(self.similitud[self.vacios[i][0]][vecinos[j]]))
      self.matrix[self.vacios[i][0]][self.vacios[i][1]] = (sum(sumatorio[0])) / (sum(sumatorio[1]))
  

  def prediccionMedia(self):
    sumatorio = ([], [])
    
    for i in range(len(self.vacios)):
      vecinos = self.vecinosProximos(self.vacios[i][0], self.vacios[i][1])
      for j in range(self.vecinos):
        sumatorio[0].append(self.similitud[self.vacios[i][0]][vecinos[j]] * 
                            (self.matrix[vecinos[j]][self.vacios[i][1]] - self.medias[vecinos[j]]))
        sumatorio[1].append(abs(self.similitud[self.vacios[i][0]][vecinos[j]]))
      self.matrix[self.vacios[i][0]][self.vacios[i][1]] = self.medias[self.vacios[i][0]] + ((sum(sumatorio[0])) / 
                                                                                            (sum(sumatorio[1])))
    
    
  def vecinosProximos(self, indicePersona, item): 
    similitudSorted = self.similitudSorted[indicePersona].copy()
    # Eliminamos los vecinos que no tengan el item
    for i in similitudSorted:
      eliminated = True
      for j in self.vacios:
        if (j[1] == item) and (j[0] == i[0]) and eliminated:
          similitudSorted.remove(i)
          eliminated = False

    vecinosSimilitud = []
    for i in range(self.vecinos):
      vecinosSimilitud.append(similitudSorted[i][0])

    self.similitudVecinos.append([indicePersona, vecinosSimilitud])
    return vecinosSimilitud


  def similitudSort(self):
    for i in range(len(self.similitud)):
      self.similitudSorted.append(list(enumerate(self.similitud[i])))
      if self.FlagEuclidea: # Si la metrica usada es euclidea debemos invertir el orden de preferencia
        self.similitudSorted[i].sort(key = lambda x: x[1], reverse=False)
      else:
        self.similitudSorted[i].sort(key = lambda x: x[1], reverse=True)


  def showInfo(self):
    print("Matriz Predicciones", end="\n\n")
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[i])):
        print(str(round(self.matrix[i][j], 2)), end="\t")
      print()
    print()
    
    for i in range(len(self.similitud)):
      print("--------------------------------------------", end="\n\n")
      print("Similaridades con Persona " + str(i))
      for j in range(len(self.similitud[i])):
        print("Persona" + str(j) + ": " + str(round(self.similitud[i][j], 2)))
      print()
      for k in range(len(self.similitudVecinos)):
        if self.similitudVecinos[k][0] == i: # Comprobamos si estan calculados los vecinos de la persona
          print("Similaridades de los " + str(self.vecinos) + " vecinos con Persona " + str(i))
          for j in self.similitudVecinos[k][1]: # Recorremos los vecinos
            print("Persona" + str(j) + ": " + str(round(self.similitud[i][j], 2)))
          print()
          break


  def loadFile(self, nameFile):
    textFile = open(nameFile, 'r')
    datos = ''.join(textFile.readlines())
    vector = datos.split("\n")
    for i in range(len(vector)):
      suma = 0
      numOfDigits = 0
      vector[i] = vector[i].split(" ")
      for j in range(len(vector[i])):
        if(vector[i][j].isdigit()):
          vector[i][j] = int(vector[i][j])
          suma += vector[i][j]
          numOfDigits += 1
        else:
          vector[i][j] = -1
          self.vacios.append((i,j))
      self.medias.append(suma / numOfDigits)
    self.matrix = vector
    
    textFile.close()
  