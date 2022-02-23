# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 23:31:45 2022

@author: Sanket Revadigar
"""

import librosa
import matplotlib.pyplot as plt
import librosa.display
import os

class wave:
    def func(cls):
      img_names = os.listdir('genres/'+cls)
      os.makedirs('wavelets/train/'+cls)
      os.makedirs('wavelets/test/'+cls)
      #print(cls)
      train_names = img_names[:70]
      test_names = img_names[70:]
      cnt = 0
      for nm in train_names:
        cnt+=1
        x , sr = librosa.load('genres/'+cls+'/'+nm)
        plt.figure(figsize=(14, 5))
        librosa.display.waveshow(x)
        plt.savefig('wavelets/train/'+cls+'/'+str(cnt)+'.png')
        plt.close()
      
      cnt = 0
      for nm in test_names:
        cnt+=1
        x , sr = librosa.load('genres/'+cls+'/'+nm)
        plt.figure(figsize=(14, 5))
        librosa.display.waveshow(x)
        plt.savefig('wavelets/test/'+cls+'/'+str(cnt)+'.png')
        plt.close()

#wave.func('blues')
wave.func('classical')
wave.func('country')
wave.func('disco')
wave.func('hiphop')
wave.func('jazz')
wave.func('metal')
wave.func('pop')
wave.func('reggae')
wave.func('rock')


