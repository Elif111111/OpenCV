Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#import os ifadesi, Python programlamada "os" (işletim sistemi) modülünü içe aktarmak için kullanılır. os modülü, işletim sistemi ile ilgili işlemleri gerçekleştirmek için çeşitli fonksiyonları içerir.
#"features" kelimesi, genel olarak bir nesnenin veya sistemin belirli özelliklerini ifade eder
# "def create_train():" ifadesini kullanıyorsanız, muhtemelen bu fonksiyon, bir eğitim veri seti oluşturma veya hazırlama işlevini yerine getiriyor olabilir.
#Python'da "path", dosya veya dizinlerin yerini belirtmek için kullanılan bir terimdir. Path, bir dosyanın veya dizinin konumunu gösteren bir dizedir
#faces_roi" terimi,  bir görüntü işleme veya nesne tanıma bağlamında kullanılan bir değişkenin adını ifade ediyor. Bu terim, "faces" (yüzler) ve "roi" (region of interest - ilgi alanı) kelimelerinin birleşiminden oluşur.
#face_recognizer" genellikle yüz tanıma (face recognition) uygulamalarında kullanılan bir terimdir ve yüz tanıma algoritmalarının veya kütüphanelerinin bir parçasını ifade eder.
#np.save terimi, NumPy kütüphanesinin bir fonksiyonunu ifade eder ve NumPy dizilerini bir dosyaya kaydetmek için kullanılır. Bu fonksiyon, diziyi bir NPY dosyası olarak kaydeder
import os



import cv2 as cv

import numpy as np


 people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

 DTR = 'C:\isers\jas\Documents\dev\older\Faces\train'



features: list

features = []



labels = []


def create_train():



for person in people:



path = os.path.join(DIR, person)



label = people.index(person)



for img in os.listdir (path):



img_path = os.path.join(path, img)



img_array = cv.imread(img_path)



gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)




faces_rect haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)



... for (x,y,w,h) in faces_rect:
... 
... 
... 
... faces_roi = gray[y:y+h, x:x+w]
... 
... 
... 
... features.append(faces_roi) labels.append(label)
... 
... 
... 
... 
... 
...  create_train()
... 
...  print('Training done --')
... 
... 
... 
... features = np.array(features, dtype='object')
... 
...  labels = np.array(labels)
... 
... 
... 
... face_recognizer = cv. face.LBPHFaceRecognizer_create()
... 
... 
... 
... 
... 
... face_recognizer.train(features, labels)
... 
... 
... 
... np.save('features.npy', features)
... 
... np.save('labels.npy', labels)
