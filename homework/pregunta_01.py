"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", "r") as f:
      lineas = f.readlines()

    cleaned_column = []
    for linea in lineas:
      if len(linea.strip()) > 0:
        cleaned_column.append(linea.strip())

    cleaned_column[0]= cleaned_column[0] + " " + cleaned_column[1]
    cleaned_column.pop(1)
    column= ["Cluster", "Cantidad de palabras clave", "Porcentaje de palabras clave", "Principales palabras clave"]
  	
    for i in range(len(column)):
      column[i] = column[i].lower().replace(" ", "_")
 
    data=[]
    for linea in cleaned_column[2:]:
      parte=linea.split()
      
      if parte[0].isdigit():
        cluster= int(parte[0])
        cantidad_palabras_clave = int(parte[1])
        porcentaje_palabras_clave= float(parte[2].replace(",", "."))
        # porcentaje_palabras_clave = f"{porcentaje_palabras_clave:} %"
        principales_palabras_clave = " ".join(parte[4:]).rstrip('.')
        data.append({ "cluster": cluster, "cantidad_de_palabras_clave": cantidad_palabras_clave, "porcentaje_de_palabras_clave": porcentaje_palabras_clave, "principales_palabras_clave": principales_palabras_clave})
      
      else:
        data[-1]["principales_palabras_clave"] += " " + " ".join(parte).rstrip('.')

    df = pd.DataFrame(data, columns=column)

    return df