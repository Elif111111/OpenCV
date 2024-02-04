Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#plt.figure() fonksiyonu, yeni bir matplotlib figürü (figure) oluşturarak grafiği ayrı bir pencerede veya alanında göstermenizi sağlar.
#plt.xlabel fonksiyonu, matplotlib kütüphanesinde x-ekseni etiketini (label) belirlemek için kullanılır.
#plt.ylabel fonksiyonu, matplotlib kütüphanesinde y-ekseni etiketini (label) belirlemek için kullanılır.
#plt.plot fonksiyonu, matplotlib kütüphanesinde çeşitli grafik türlerini çizmek için kullanılır.
#plt.xlim fonksiyonu, matplotlib kütüphanesinde x-ekseninin görüntülenecek aralığını belirlemek için kullanılır.

import cv2 as cv



import matplotlib.pyplot as plt



img = cv.imread('Photos/cats.jpg')


... 
... cv.imshow('Cats', img)
... 
... 
... 
... 
... 
... gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
... 
... cv.imshow('Gray', gray)
... 
... #GRayscale histogram
... 
... gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
... 
... plt.figure()
... 
... plt.title('Grayscale Histogram')
... 
... 
... 
... plt.xlabel('Bins')
... 
... 
... 
... plt.ylabel('# of pixels')
... 
... 
... plt.plot(gray_hist)
... 
... 
... plt.xlim([0,256])
... 
... 
... plt.show()
... 
... 
... 
... 
