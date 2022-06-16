import cv2
cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

cacaoCascade = cv2.CascadeClassifier('./traindata/cascade.xml')

while True:
	
	ret,frame = cap.read()	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	height, width, _ = frame.shape
	cx = int(width / 2)
	cy = int(height / 2)


	# Pick pixel value
	pixel_center = gray[cy, cx]
	hue_value = pixel_center[0]

	color = "Undefined"
	
	if hue_value < 11 and hue_value > 0:
		color = "RED"
	elif hue_value < 40:
		color = "ORANGE"
	elif hue_value < 72:
		color = "YELLOW"
	elif hue_value < 165:
		color = "GREEN"
	elif hue_value < 262:
		color = "BLUE"
	elif hue_value < 324:
		color = "VIOLET"
	elif hue_value <255:
		color = "RED"
	pixel_center_bgr = frame[cy, cx]
	b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

	obj = cacaoCascade.detectMultiScale(gray,
	scaleFactor = 4,
        minNeighbors = 80,
        minSize=(200,100))

	for (x,y,w,h) in obj:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		cv2.putText(frame,'Cacao',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
		cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
		cv2.circle(frame, (x+150,y+100), 5, (25, 25, 25), 3)

	cv2.imshow('frame',frame)
	
	if cv2.waitKey(1) == 27:
		break
cap.release()
cv2.destroyAllWindows()