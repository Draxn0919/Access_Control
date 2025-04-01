import cv2
import face_recognition
import pickle

# Cargar el modelo entrenado
with open("encodings.pickle", "rb") as archivo:
    datos = pickle.load(archivo)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Convertir el frame a 8 bits y RGB si es necesario
    if frame.dtype != 'uint8':
        frame = frame.astype('uint8')  # Convertir a 8 bits por canal si no lo está
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB

    # Redimensionar el frame para un procesamiento más rápido
    frame_resized = cv2.resize(frame_rgb, (0, 0), fx=0.25, fy=0.25)

    # Detectar rostros en el frame redimensionado
    face_locations = face_recognition.face_locations(frame_resized)
    face_encodings = face_recognition.face_encodings(frame_resized, face_locations)

    mensaje = "Rostro no encontrado"
    color_mensaje = (0, 255, 255)  # Amarillo

    if len(face_locations) > 0:
        for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
            # Comparar con los rostros conocidos
            coincidencias = face_recognition.compare_faces(datos["encodings"], encoding)
            nombre = "Desconocido"

            if True in coincidencias:
                index = coincidencias.index(True)
                nombre = datos["nombres"][index]
                mensaje = "Usuario autorizado"
                color_mensaje = (0, 255, 0)  # Verde
            else:
                mensaje = "Usuario no autorizado"
                color_mensaje = (0, 0, 255)  # Rojo

            # Escalar las coordenadas a tamaño original
            top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
            
            # Dibujar cuadro de detección y nombre de usuario
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, nombre, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Mostrar el mensaje de estado en la parte superior de la pantalla
    cv2.putText(frame, mensaje, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color_mensaje, 2)
    cv2.imshow("Reconocimiento Facial", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
