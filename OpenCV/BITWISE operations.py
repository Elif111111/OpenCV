Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#cv2.rectangle fonksiyonu, bir görüntü üzerinde dikdörtgen çizmek için kullanılır. Bu fonksiyon, başlangıç ve bitiş noktaları belirlenmiş bir dikdörtgeni belirtilen renk ve kalınlıkla çizer.
#
#cv2.circle fonksiyonu, bir görüntü üzerinde daire çizmek için kullanılır. Bu fonksiyon, merkez koordinatları ve yarıçapı belirtilen bir daireyi belirtilen renk ve kalınlıkla çizer.
# rectangle adlı bir değişkenin önceden tanımlanmış ve doğru bir şekilde bir dikdörtgen içermesi gerekiyor.
#cv2.bitwise_and fonksiyonu, iki görüntü arasında bitwise AND işlemi gerçekleştirir. Bu işlem, her iki pikselin de değeri 1 (beyaz) ise çıktı görüntüsündeki piksel de 1 olacaktır; aksi takdirde, çıktı pikseli 0 (siyah) olacaktır. Bu işlem, iki görüntü arasında belirli bir bölgenin ortaklığını kontrol etmek veya maskelerle çalışmak için yaygın olarak kullanılır.

... import cv2 as cv
... 
... 
... import numpy as np
... 
... 
... blank = np.zeros((400,400), dtype='uint8')
... 
... 
... 
... rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
... 
... 
... circle = cv.circle(blank.copy(), (200,200), 200, 255 , -1)
... 
... 
... 
... cv.imshow('Rectangle', rectangle)
... 
... 
... cv.imshow('Circle', circle)
... 
... 
... #bitwise AND
... bitwise_and = cv.bitwise_and(rectangle, circle)
... 
... cv.imshow('Bitwise AND', bitwise_and)
... 
... bitwise_or = cv.bitwise_or(rectangle, circle)
... 
... 
... cv.imshow('Bitwise OR', bitwise_or)
... 
... bitwise_xor=cv.bitwise_xor(rectangle,circle)
... Cv.imshow(‘Bitwise XOR’,bitwise xor)
... 
... cv.waitKey(0)
... 
... 
