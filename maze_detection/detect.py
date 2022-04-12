import cv2
import numpy as np
from PIL import Image


def img_to_binary(img, t):
    """ 
    img value over threshold t: 255, else 0 
    """

    sy, sx = img.shape
    binary = np.zeros((sy, sx))

    for i in range(0, sy):
        for j in range(0, sx):
            if img[i, j] >= t:
                binary[i, j] = 255
            else:
                binary[i, j] = 0
    return binary

def pil_to_cv2(img):
    pil_image = img.convert('RGB')
    open_cv_image = np.array(pil_image)
    # Convert RGB to BGR
    img = open_cv_image[:, :, ::-1].copy()

    return img

### Resizing Image
img = Image.open("MazeSolver/media/maze.jpg")
small = img.resize((150, 75))
img = pil_to_cv2(small)

### Blurring Image
blur = cv2.GaussianBlur(img, (7, 7), 0)

### Sharpening Image
k = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
k2 = np.array([[-2, -2, -2], [-2, 17, -2], [-2, -2, -2]])
k3 = np.array([[-3, -3, -3], [-3, 25, -3], [-3, -3, -3]])
k4 = np.array([[-4, -4, -4], [-4, 33, -4], [-4, -4, -4]])

#sharp = cv2.filter2D(blur, -1, k4)

### Thresholding Image
canny = cv2.Canny(blur, 60, 390)

### Saving Image
cv2.imwrite("MazeSolver/media/img.jpg", img)
#cv2.imwrite("MazeSolver/media/sharp.jpg", sharp)
cv2.imwrite("MazeSolver/media/canny.jpg", canny)
cv2.imwrite("MazeSolver/media/blur.jpg", blur)
