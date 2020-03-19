import cv2, os
import face_recognition as fr
from IPython.display import Image, display
from matplotlib import pyplot as pit

Image_path = "image_path"

image = fr.load_image_file(Image_path)
face_locations = fr.face_locations(image)

for(top,right,bottom,left) in face_locations: #face_location 함수를 통해 얼굴 기준으로 value 생성
  cv2.rectangle(image, (left,top),(right,bottom),(0,255,0), 3)
  
#이미지 버퍼 출력
pit.rcParams["figure.figsize"]=(16,16) #figure 사이즈 지정
pit.imshow(image)
pit.show()
