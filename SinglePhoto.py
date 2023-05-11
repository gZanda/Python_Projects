import cv2

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # Upload Classifier
impImg1 = cv2.VideoCapture("Me and Rato 3.jpg") # Upload image

res, img = impImg1.read()  # Try to read ( img ) and store the dimensions ( res )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Convert to Gray Scale img

faces = detect.detectMultiScale(gray, 1.3, 5)   # x, y, Width and Height ( coordenates )

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0), 2) # img, coordinates, wid and hei, color, thickness

cv2.imshow("Face Tracker", img)
cv2.waitKey(0)  # Image will be oppened untill closed
impImg1.release()
cv2.destroyAllWindows()