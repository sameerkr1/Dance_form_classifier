# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E-yEE59BrmdA8BFN-DFNUt69AqK5yNw_
"""

from google.colab import drive
drive.mount('/content/drive/')

!pip install -U -q PyDrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

downloaded = drive.CreateFile({'id':'10iCLojNi0tgsGuYU5iG7VSuNAZ1MzASl'})
downloaded.GetContentFile('train.csv')

downloaded = drive.CreateFile({'id':'1GvqWEEXwet3XU7pXngc2yCkatW41F8v3'})
downloaded.GetContentFile('test.csv')

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from tqdm import tqdm

train=pd.read_csv('train.csv')

dic={'manipuri':0,'bharatanatyam':1,'odissi':2,'kathakali':3,'kathak':4,'sattriya':5,'kuchipudi':6,'mohiniyattam':7}

from keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
datagen = ImageDataGenerator(rescale = 1./255,shear_range = 0.2,zoom_range = 0.2,horizontal_flip = True,rotation_range=40,width_shift_range=0.2,height_shift_range=0.2)

for i in tqdm(range(train.shape[0])):
    img = image.load_img('/content/drive/My Drive/2/train/'+train['Image'][i])
    img=img_to_array(img)
    img=img.reshape((1,)+img.shape)
    j=0
    string=train['target'][i]
    string=str(dic[string])
    for batch in datagen.flow(img ,batch_size = 1,save_to_dir='/content/drive/My Drive/ima_gen/'+string,save_format='jpg',save_prefix='img'):
        j+=1
        if j>21:
            break



import os
output = pd.DataFrame()
data1=[]
data2=[]
for i in range(8):
      local_download_path='/content/drive/My Drive/ima_gen/'+str(i)
      for filename in os.listdir(local_download_path):
          if filename.endswith("jpg"):
              data1.append(filename)
              data2.append(i)
output['image']=data1
output['target']=data2

output.to_csv('check.csv', header=True, index=False)

output

print(output)

