Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Canny kenar tespiti
>>> import cv2 as cv
... 
... img = cv.imread('Photos/cats.jpg')
... 
... cv.imshow('Cats', img)
... 
... 
... gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
... cv.imshow('Gray', gray)
... 
... canny=cv.Canny(img,125,175)
... 
... cv.waitKey(0)
... 
... 
... 
... import cv2 as cv
... 
... img = cv.imread('Photos/cats.jpg')
... 
... cv.imshow('Cats', img)
... 
... 
... gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
... cv.imshow('Gray', gray)
... 
... blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
... cv.imshow(‘Blur’,blur)
... 
... 
... canny=cv.Canny(blur,125,175)
... cv.imshow(‘Canny Edges’,canny)
... Contoursh,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
... print(f’{len(contours)}contour(s) found!’)
... 
... cv.waitKey(0)
