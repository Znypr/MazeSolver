import cv2


def img_to_binary(img, t):

    for x in img:
        for y in img[x]:
            if y >= t:
                y = 1
            else:
                y = 0

    return img


img = cv2.imread("../media/mini_maze.png", 0)
blur = cv2.GaussianBlur(img, (5, 5), 0)
canny = cv2.Canny(blur, 100, 200)

binary = img_to_binary(canny, 100)

cv2.imshow(binary)
