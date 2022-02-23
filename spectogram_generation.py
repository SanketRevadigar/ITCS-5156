# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 00:02:29 2022

@author: Sanket Revadigar
"""

import librosa
import matplotlib.pyplot as plt
import librosa.display
import os

class specto:
    def func(cls):
      img_names = os.listdir('genres/'+cls)
      os.makedirs('spectrogram/train/'+cls)
      os.makedirs('spectrogram/test/'+cls)
      train_names = img_names[:70]
      test_names = img_names[70:]
      cnt = 0
      for nm in train_names:
        cnt+=1
        x , sr = librosa.load('genres/'+cls+'/'+nm)
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        librosa.display.specshow(Xdb)
        plt.savefig('spectrogram/train/'+cls+'/'+str(cnt)+'.png')
        plt.close()
      
      cnt = 0
      for nm in test_names:
        cnt+=1
        x , sr = librosa.load('genres/'+cls+'/'+nm)
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        librosa.display.specshow(Xdb)
        plt.savefig('spectrogram/test/'+cls+'/'+str(cnt)+'.png')
        plt.close()
        

#specto.func('blues')
#specto.func('classical')
#specto.func('country')
specto.func('disco')
specto.func('hiphop')
specto.func('jazz')
specto.func('metal')
specto.func('pop')
specto.func('reggae')
specto.func('rock')