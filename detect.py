import cv2
import numpy as np

path = "./images/maz3.jpg"

def scale(img, p):

    width = int(img.shape[1] * p)
    height = int(img.shape[0] * p)

    dsize = (width, height)

    return cv2.resize(img, dsize)

def filter(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(11,11),0)

    # binary
    bi = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

    # canny
    img_canny = cv2.Canny(img,100,300)

    # sobel
    img_sobelx = cv2.Sobel(blur,cv2.CV_8U,1,0,ksize=5)
    img_sobely = cv2.Sobel(blur,cv2.CV_8U,0,1,ksize=5)
    img_sobel = img_sobelx + img_sobely


    # prewitt
    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    img_prewittx = cv2.filter2D(blur, -1, kernelx)
    img_prewitty = cv2.filter2D(blur, -1, kernely)

    return [img, blur, bi, img_canny, img_sobelx, img_sobely, img_sobel, img_prewittx, img_prewitty, img_prewittx+img_prewitty]

if __name__=="__main__":

    img = cv2.imread(path, 1)

    arr = filter(img)

    for i in range(len(arr)):
        cv2.imwrite("./output/"+str(i)+".jpg", scale(arr[i], 0.5))

