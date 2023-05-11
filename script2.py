import cv2, glob # glob = module to acess varios images

all_images = glob.glob("*.jpg") # glob them all into the glob

detect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")   # Upload Classifier

for image in all_images:
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect.detectMultiScale(gray_img, 1.1, 5)

    for(x,y,w,h) in faces:
        final_img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0), 2)

    cv2.imshow("Face Detection", final_img)
    cv2.waitKey(0)  # Image will be oppened untill closed
    cv2.destroyAllWindows()

