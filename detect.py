import cv2

img_path = r"./images_maze/maze2.jpg"

def read_img(path):

    img = cv2.imread(path, 0)
    
    return img




if __name__ == '__main__':

    img = cv2.imread(img_path,1)

    edged = cv2.Canny(img, 30, 200)


    contours, hierarchy = cv2.findContours(edged,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    edged = cv2.resize(edged, (1920,1080))
    cv2.imshow("maze", edged)
    cv2.waitKey(0)