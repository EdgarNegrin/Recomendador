#
# Nombre: Edgar Negrin Gonzalez
# Correo: alu0101210964@ull.edu.es
#
# Practica: Recomendador
#
# main.py: fichero principal para ejecutar el recomendador
#
#
# Ejemplo de uso: python3 main.py ./matriz/matriz1.txt -M pearson -V 2 -P media 
# Fichero: ./matriz/matriz1.txt, Metrica: pearson, Numero de vecinos: 2, Prediccion: media
#

import argparse
from recomender import recomender

parser = argparse.ArgumentParser(description='Recomendador')
parser.add_argument('file', help='Load the file')
parser.add_argument('-M', '--metrica', help='Tipo de metrica', choices=['pearson', 'coseno', 'euclidea'], required=True)
parser.add_argument('-V', '--vecinos', help='Numero de vecinos', required=True)
parser.add_argument('-P', '--prediccion', help='Tipo de prediccion', choices=['simple', 'media'], required=True)

args = parser.parse_args()

if int(args.vecinos) < 2:
  print("Es necesario un numero de vecinos superior a 1")
  exit()

rec = recomender(args.file, int(args.vecinos))

###############################

# Correlacion de Pearson
if args.metrica == 'pearson': 
  rec.pearson()

# Distancia coseno
if args.metrica == 'coseno': 
  rec.coseno()
  
# Distancia euclidea
if args.metrica == 'euclidea': 
  rec.euclidea()

###############################

# Prediccion simple
if args.prediccion == 'simple':
  rec.prediccionSimple()
  
# Prediccion simple
if args.prediccion == 'media':
  rec.prediccionMedia()

###############################

rec.showInfo()
