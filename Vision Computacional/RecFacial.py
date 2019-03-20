#pip install numpy
import numpy as np
#pip install matplotlib
import matplotlib.pyplot as plt
#pip install scikit-image
#pip install scipy
from skimage import io
#pip install opencv-python
#pip install opencv-contrib-python
import cv2
#pip install imutils
import imutils# utilidades con imagenes para instalar en anaconda  conda install -c pjamesjoyce imutils 
from imutils.object_detection import non_max_suppression



font = cv2.FONT_HERSHEY_SIMPLEX
def initialize_caffe_models():
	age_net = cv2.dnn.readNetFromCaffe(
		'Librerias/deploy_age.prototxt', 
		'Librerias/age_net.caffemodel')
	gender_net = cv2.dnn.readNetFromCaffe(
		'Librerias/deploy_gender.prototxt', 
		'Librerias/gender_net.caffemodel')
	return(age_net, gender_net)

age_net, gender_net = initialize_caffe_models()

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
age_list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)', '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
gender_list = ['Male', 'Female']

##########################
##Leer Imagen##
im_file='Data/conjanny.jpg'
im = io.imread(im_file)#leer la imagen
fig, ax = plt.subplots(1, 1, figsize=(8, 6))#tamaño de imagen y generacion de plot
ax.imshow(im)#muestra imagen
ax.axis('on')#muestra datos de grafico
ax.set_title('Carlos Gonzalez', fontsize=20)#pone titulo a la imagen
im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)#de esta manera se arregla
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.imshow(im_rgb)

#########################################
##Buscar Caras##
face_cascade = cv2.CascadeClassifier('Librerias/haarcascade_frontalface_default.xml')#carga libreria para reconocer rostros
eye_cascade = cv2.CascadeClassifier('Librerias/haarcascade_eye.xml')#carga libreria para reconocer ojos
im_bgr = im.copy()#crea una copia de la imagen para manipular
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# detect faces in the image
faces = face_cascade.detectMultiScale(im_gray, scaleFactor=1.3, minNeighbors=5)#detecta caras
for (x,y,w,h) in faces:#por cada rostro encontrado
    cv2.rectangle(im_bgr,(x,y),(x+w,y+h),(255,0,0),2)#dibuja un rectangulo
    roi_gray = im_gray[y:y+h, x:x+w]
    roi_color = im_bgr[y:y+h, x:x+w]
    blob = cv2.dnn.blobFromImage(im_bgr, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
    #Predict Gender
    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender = gender_list[gender_preds[0].argmax()]
    print("Gender : " + gender)
    #Predict Age
    age_net.setInput(blob)
    age_preds = age_net.forward()
    age = age_list[age_preds[0].argmax()]
    print("Age Range: " + age)
    overlay_text = "%s %s" % (gender, age)
    cv2.putText(im_bgr, overlay_text, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3, minSize=(10,10), maxSize=(120,120))
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)#dibuja un cuadro por cada ojo

im_rgb = cv2.cvtColor(im_bgr, cv2.COLOR_BGR2RGB)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.imshow(im_rgb)
##################################################


    

################################
cv2.imshow('image',im_rgb)
cv2.waitKey(0)#para cerrar la ventana al apretar una tecla
cv2.destroyAllWindows()
##########################

#detectar genero y edad









