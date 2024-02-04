Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#cv2.adaptiveThreshold fonksiyonu, görüntüde adaptif eşikleme (adaptive thresholding) işlemi yapmak için kullanılır. Bu yöntem, görüntüdeki her pikselin eşik değerinin otomatik olarak belirlendiği bir süreçtir. Özellikle ışık koşullarının değiştiği veya kontrastın düşük olduğu durumlarda kullanışlıdır.
#"threshold" veya "thresh" terimleri, genellikle görüntü işleme ve bilgisayarlı görü analiz uygulamalarında kullanılan bir kavramdır. Bu terim, bir görüntüde belirli bir eşik değeri üzerinde veya altında kalan pikselleri belirlemek için kullanılır. Bu işlem genellikle bir görüntüyü ikili hale getirmek (siyah-beyaz) veya belirli özellikleri vurgulamak için yapılır.
import cv2 as cv



 img = cv.imread('Photos/cats.jpg')



cv.imshow('Cats', img)



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)



cv.imshow('GRay', gray)





threshold, thresh = cv.threshold gray, 100, 255, cv.THRESH_BINARY



cv.imshow('Simple Thresholded', thresh)


cv.waitKey(0)



... 
... 
... import cv2 as cv
... 
... 
... 
...  img = cv.imread('Photos/cats.jpg')
... 
... 
... 
... cv.imshow('Cats', img)
... 
... 
... 
... gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
... 
... 
... 
... cv.imshow('GRay', gray)
... 
... 
... 
... threshold, thresh = cv. threshold (gray, 150, 255, cv. THRESH_BINARY )
... 
...  cv.imshow('Simple Thresholded', thresh)
... 
... threshold, thresh_inv cv.threshold(gray, 150, 255, cv. THRESH_BINARY_INV)
... 
... cv.imshow('Simple Thresholded Inverse', thresh_inv)
... 
... 
... 
... 
... adaptive_thresh = cv.adaptive Threshold (gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv. THRESH BINARY INV, 11, 35)
... 
... cv.imshow('Adaptive Thresholding', adaptive_thresh)
... 
... 
