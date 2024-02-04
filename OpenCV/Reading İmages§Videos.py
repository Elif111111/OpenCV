Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #height: Görüntünün yüksekliğini temsil eder.
... #width: Görüntünün genişliğini temsil eder.
... #channels: Görüntünün renk kanallarının sayısını temsil eder (örneğin, bir renkli görüntüde genellikle 3 kanal vardır: kırmızı, yeşil ve mavi)
>>> #frame.shape, OpenCV kütüphanesinde bir görüntünün boyutlarını temsil eden bir özelliktir.
>>> #frame_resized adlı değişken, orijinal görüntünün image boyutlarını new_width ve new_height değerlerine göre yeniden boyutlandırmak için kullanılır.
>>> #"Dimensions"  genellikle bir nesnenin uzunluğu, genişliği ve yüksekliği gibi ölçüleri ifade eder.
>>> import cv2 as cv
... 
... def rescaleFrame(frame, scale=0.75):
... 
... width = int(frame.shape[1]*
... 
...  height = int(frame.shape[0]* scale) scale)
... 
... 
... dimensions (width, height)
... 
... 
... return cv.resize(frame, dimensions, interpolation-cv.INTER_AREA)
... 
... #Reading videos
... capture=cv.VideoCapture(‘Videos/dog.mp4’)
... 
... while TRUE:
... isTrue,frame=capture.read()
... 
... frame_resized=rescaleFrame(frame,scale=2.)
... cv.imshow(‘Video’,frame)
