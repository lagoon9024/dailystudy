import cv2
import numpy as np
from matplotlib import pyplot as pit

#이미지 버퍼 생성
buffer = np.full((256,256,3),255,np.uint8)

#이미지 버퍼 가공
cv2.line(buffer,(0,0),(250,250),(255,0,0),3)
# line(가공대상, 시작점, 끝점, color(RGB255), pixel(두께))
cv2.circle(buffer,(50,200),30,(0,0,255),-1)
# circle(가공대상, 원점, 반지름, color, 두께(0보다 작은수 => 채우기))
cv2.rectangle(buffer, (200,50),(250,100),(0,255,0),1)
# rectangle(가공대상, 시작점, 끝점, color, 두께(0보다 작은수 => 채우기))
cv2.ellipse(buffer,(128,128),(100,50),0,0,180,(128,0,128),1)
# 가공대상, 중점, (장축,단축), 시작각도, 끝각도, 호 비율(0~360), color, 두께)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(buffer,[pts],True,(0,255,255))
# 폴리곤. 점위치설정 & 그리기

#이미지 버퍼 출력
pit.imshow(buffer)
pit.show()
