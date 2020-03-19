pit.rcParams["figure.figsize"] = (1,1)
import cv2, os
import face_recognition as fr
from IPython.display import Image, display
from matplotlib import pyplot as pit

# 이미지 파일을 로드하여 list 생성
person_list = []
person_list.append(fr.load_image_file("image_path"))
person_list.append(fr.load_image_file("image_path"))
person_list.append(fr.load_image_file("image_path"))
person_list.append(fr.load_image_file("image_path"))

face_list = []
for person in person_list:
  # 얼굴좌표 파악 및 cut과정
  top, right, bottom, left = fr.face_locations(person)[0] #첫번째로 발견된 얼굴(독사진이니까..)
  face_image = person[top:bottom, left:right] #배열로 이미지 전체를 저장

  #list에 저장
  face_list.append(face_image)

#저장한 얼굴 출력
for face in face_list:
  pit.imshow(face)
  pit.show()
  
# load unknown
unknown = fr.load_image_file("image_path")

# cut face
top, right, bottom, left = fr.face_locations(unknown)[0]
unknown_face = unknown[top:bottom, left:right]

# display with title :: unknown
pit.title("unknown")
pit.imshow(unknown_face)
pit.show()

# encoding unknown face
enc_unknown_face = fr.face_encodings(unknown_face)

# display
pit.imshow(enc_unknown_face)
pit.show()

# compare with regstered faces
for face in face_list:
  # encoding 128-demensinal face
  enc_face= fr.face_encodings(face)

  # get distance with unknown
  distance = fr.face_distance(enc_face, enc_unknown_face[0])

  # display with distance value
  pit.title("distance :: "+str(distance))
  pit.imshow(face)
  pit.show()
