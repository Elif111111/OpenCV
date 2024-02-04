Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#cv.imread fonksiyonu, OpenCV kütüphanesinde bir görüntüyü diskten okumak için kullanılan bir fonksiyondur. Bu fonksiyon, belirtilen dosya yolundaki bir görüntü dosyasını okur ve bir NumPy dizisi olarak döndürür.
#gray "gri tonlama" anlamına gelir ve OpenCV'de görüntü işleme ile ilgili olarak sıkça kullanılır. Görüntülerin gri tonlamaya dönüştürülmesi, renk bilgisini yitirerek sadece parlaklık bilgisini korur.
#Blur" kelimesi, görüntü işleme alanında bir görüntü üzerinde yumuşatma veya bulanıklık efekti uygulama işlemine işaret eder. Bu efekt, görüntüdeki gürültüyü azaltmak, kenarları yumuşatmak veya bazı detayları gizlemek gibi çeşitli amaçlar için kullanılır.
>>> #
... #Canny kenar tespiti (Canny edge detection), görüntü işleme alanında oldukça yaygın olarak kullanılan bir kenar tespiti algoritmasıdır.
>>> #Dilatasyon (Dilation), morfolojik görüntü işleme operasyonlarından biridir. Dilatasyon, bir görüntüdeki nesnelerin sınırlarını genişletmek veya belirginleştirmek için kullanılır. Bu işlem, görüntüdeki beyaz bölgeyi genişletirken siyah bölgeyi küçültür.
>>> #Erozyon (Erosion), morfolojik görüntü işleme operasyonlarından biridir ve dilatasyonun tersidir. Erozyon işlemi, bir görüntüdeki beyaz bölgeyi küçültmek veya inceltmek amacıyla kullanılır. Bu işlem, görüntüdeki beyaz bölgeyi daraltırken siyah bölgeyi genişletir.
>>> import cv2 as cv
... 
... 
... img = cv.imread(‘Photos/boston.jpg')
...  cv.imshow('Boston', img)
... 
... 
... #Converting to grayscole
... 
... gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
...  cv.imshow('Gray', gray)
... #Blur
... blur=cv.GaussingianBlur(ing,(7,7),cv.BORDER_DEFAULT)
... cv.imshow(‘Blur’,blur)
... 
... #Edge Cascade
... canny=cv.Canny(blur,125,175)
... cv.imshow(‘Canny Edges’,canny)
... 
... #Dilating the image 
... dilated=cv.dilate(canny,(7,7),iterations=3)
... cv.imshow(‘Dilated’,dilated)
... 
... #Eroding
... eroded=cv.erode(dilated,(3,3),iterateions=1)
... cv.waitKey(0)
