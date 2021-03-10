from cv2 import cv2               

def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          # convert caputre live image to gray color
    img_gray_blur = cv2.GaussianBlur(img_gray,(9,9), 0)         # blur the image to clear it
    canny_edge = cv2.Canny(img_gray_blur, 10, 80)               # edge detection using canny 
    ret, mark = cv2.threshold(canny_edge, 70, 235, cv2.THRESH_BINARY)          # store the capture image im mark and show it
    return mark

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    cv2.imshow("our live sketch " , sketch(frame))
    if cv2.waitKey(1) == 13:
        break

cam.release()
cv2.destroyAllWindows()