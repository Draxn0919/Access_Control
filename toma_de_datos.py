import cv2
import os

nombre = input("Introduce el nombre de la persona: ")
ruta = f"imagenes_entrenamiento/{nombre}"
if not os.path.exists(ruta):
    os.makedirs(ruta)

cap = cv2.VideoCapture(0) 
contador = 0

while contador < 20:  
    ret, frame = cap.read()
    if ret:
        contador += 1
        cv2.imwrite(f"{ruta}/{nombre}_{contador}.jpg", frame)
        cv2.imshow("Captura de imagen", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
