from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import numpy as np
import cv2
import csv

def makecsv(file):
    with open('disease/test.csv','w',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['image_id'])
        writer.writerow([file])
def test_image():
    test = pd.read_csv('disease/test.csv')
    train_datagen = ImageDataGenerator( horizontal_flip=True,
        vertical_flip=True,
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=.1,
        fill_mode='nearest',
        shear_range=0.1,
        rescale=1/255,
        brightness_range=[0.5, 1.5])
    model = load_model('disease/my_model.hdf5')
    test_generator=train_datagen.flow_from_dataframe(test,directory='media',
                                                          target_size=(128,128),
                                                          x_col="image_id",
                                                          y_col=None,
                                                          class_mode=None,
                                                          shuffle=False,
                                                          batch_size=16)
    probs_RESNET = model.predict(test_generator, verbose=1)
    maximum=np.amax(probs_RESNET)
    result=np.where(probs_RESNET == maximum)
    if(result[1][0]==0):
        data="healthy"
    if(result[1][0]==1):
        data="multiple disease"
    if(result[1][0]==2):
         data = "rust"
    if(result[1][0]==3):
        data = "scab"
    return data,maximum*100

