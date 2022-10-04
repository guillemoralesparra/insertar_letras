#!/usr/bin/env python
# coding: utf-8

# In[2]:
#es necesario instalar numpy, cv2 y rembg
##rembg:  https://github.com/danielgatis/rembg


from PIL import Image
import cv2
import numpy as np
from rembg import remove
from typing import ContextManager


# In[15]:


######Meter letras que no solapa
def letras_sin(path, path_l):
    #1 - leer imagen
    img = cv2.imread(path)
    img_pil_original = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img_original = cv2.imread(path)

    #3 - meter letras
    letras = Image.open(path_l)
    img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img.paste(letras, (1220,240), letras.convert("RGBA"))
    return img


######Meter letras que solapa
def letras_con(path,path_l):
    #1 - leer imagen
    img = cv2.imread(path)
    img_pil_original = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img_original = cv2.imread(path)

    #2 - remove background
    car = remove(img_pil_original)

    #3 - meter letras
    letras = Image.open(path_l)
    img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img.paste(letras, (1220,240), letras.convert("RGBA"))
    img

    #meter el cotxe encima de las letras
    img_pil = img
    img_pil.paste(car, (0,0), car.convert("RGBA"))
    return img_pil


#####Control
def check(path,path_l):
    #1 - leer imagen
    img = cv2.imread(path)
    img_pil_original = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img_original = cv2.imread(path)

    #2 - remove background
    car = remove(img_pil_original)

    #3 - meter letras
    letras = Image.open(path_l)
    img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img.paste(car, (0,0), car.convert("RGBA"))
    img.paste(letras, (1220,240), letras.convert("RGBA"))
    return img

#####insertar_letras
def insertar_letras(path, path_l):
    im1 = check(path, path_l)
    im2 = letras_con(path, path_l)
    im3 = cv2.cvtColor(np.asarray(im1),cv2.COLOR_RGB2BGR) #PIL - opencv
    im4 = cv2.cvtColor(np.asarray(im2),cv2.COLOR_RGB2BGR) #PIL - opencv
    dif = cv2.subtract(im4,im3)
    if not np.any(dif):
        img = letras_sin(path,path_l)
    else:
        img = letras_con(path,path_l)
    return img


# In[49]:

##Ejemplo de como llamar la función
##Se le pasa la imagen del coche y la imagen con las letras
path = 'Documents/FLEXICAR/test/7845LFT_05.jpg'
path_l = 'Documents/FLEXICAR/font/f_esplugues.png'
insertar_letras(path,path_l)

