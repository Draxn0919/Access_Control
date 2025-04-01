import face_recognition
import numpy as np
import os
import pickle

# Definir la ruta donde están almacenadas las imágenes de entrenamiento
ruta_entrenamiento = "imagenes_entrenamiento/"

# Listas para almacenar los encodings faciales y los nombres asociados
lista_encodings = []  # Aquí se guardarán los vectores de características de los rostros
lista_nombres = []    # Aquí se guardarán los nombres de las personas correspondientes

# Recorrer cada carpeta en la ruta de entrenamiento (cada carpeta representa a una persona)
for nombre_persona in os.listdir(ruta_entrenamiento):
    carpeta_individual = os.path.join(ruta_entrenamiento, nombre_persona)
    
    # Verificar que la ruta corresponde a un directorio (para evitar archivos sueltos)
    if os.path.isdir(carpeta_individual):
        # Recorrer todas las imágenes dentro de la carpeta de cada persona
        for nombre_archivo in os.listdir(carpeta_individual):
            # Cargar cada imagen individualmente
            ruta_imagen = os.path.join(carpeta_individual, nombre_archivo)
            imagen = face_recognition.load_image_file(ruta_imagen)

            # Calcular el encoding (vector de características) del rostro en la imagen
            encodings_rostro = face_recognition.face_encodings(imagen)

            # Si se detecta al menos un rostro en la imagen
            if len(encodings_rostro) > 0:
                # Guardar el encoding y el nombre de la persona
                lista_encodings.append(encodings_rostro[0])  # Agregar el primer encoding a la lista
                lista_nombres.append(nombre_persona)          # Asignar el nombre correspondiente

# Guardar los encodings y los nombres en un archivo .pickle para su uso posterior
with open("encodings.pickle", "wb") as archivo_pickle:
    datos_entrenamiento = {"encodings": lista_encodings, "nombres": lista_nombres}
    pickle.dump(datos_entrenamiento, archivo_pickle)

print("Entrenamiento completado y guardado en 'encodings.pickle'.")
