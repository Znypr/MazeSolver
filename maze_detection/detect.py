import cv2 as cv
import numpy as np
import sys
sys.path.append('c:/Users/jonat/Documents/GitHub/MazeSolver')
import solver.entities as nt

def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv.imshow('image', img)

def correct_perspective(image, refPoints):
    #order reference points so they are warped correctly
    rect = order_points(refPoints)
    (tl, tr, br, bl) = rect

    #compute the size of the new image which consists of the maximum dimensions of the original image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    
    #determine the corner points of the resulting image
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")

    #warp the image using the transformation matrix calculated using the reference points
    M = cv.getPerspectiveTransform(rect, dst)
    warped = cv.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped
    
def order_points(points):
    #order the reference points in the order of top left, top right, bottom right, bottom left
    rect = np.zeros((4,2), dtype="float32")
    
    sum = points.sum(axis = 1)
    rect[0] = points[np.argmin(sum)]
    rect[2] = points[np.argmax(sum)]

    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]
    rect[3] = points[np.argmax(diff)]

    return rect

def detect_walls(img):
    imgBlue =  img[:,:,0]
    imgGreen = img[:,:,1]
    imgRed = img [:,:,2]

    imgBin = np.logical_and(np.logical_and(np.logical_or(np.logical_or(imgBlue < 200, imgRed < 200), imgGreen < 200), imgRed > 1.35 * imgBlue), imgBlue > 65).astype(np.uint8)

    return imgBin

def sumUpImage(img):
    sumX = np.zeros(img.shape[1])
    sumY = np.zeros(img.shape[0])

    for index, line in enumerate(img):
        sumY[index] = np.sum(line)

    for index, column in enumerate(img.transpose()):
        sumX[index] = np.sum(column)

    return (sumX, sumY)

def calculateLabDims(imgBin):
    sumX, sumY = sumUpImage(imgBin)

    sumX = sumX > 150
    sumY = sumY > 150

    dimX = 0
    dimY = 0

    for i in range(sumX.shape[0]-1):
        if(sumX[i+1] and sumX[i]):
            sumX[i] = False

    for column in sumX:
        if column:
            dimX += 1

    for i in range(sumY.shape[0]-1):
        if(sumY[i+1] and sumY[i]):
            sumY[i] = False

    for row in sumY:
        if row:
            dimY += 1

    dimX -= 1
    dimY -= 1

    return (dimX, dimY)

def detect_lab(filepath):
    img = np.array(cv.imread(filepath))
    img = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)), interpolation = cv.INTER_AREA)

    #show initial labyrinth
    cv.imshow("image", img)
    cv.setMouseCallback('image', click_event)
    k = cv.waitKey(0)

    refPoints = np.array([(376, 42), (1221, 45), (310,719), (1281, 716)])
    img = correct_perspective(img, refPoints)

    #show labyrinth with corrected perspective
    cv.imshow("image", img)
    k = cv.waitKey(0)

    img = cv.medianBlur(img, 5)

    #show blurred image
    cv.imshow("image", img)
    k = cv.waitKey(0)

    imgBin = detect_walls(img)

    #show binary image of walls
    cv.imshow("image", imgBin*255)
    k = cv.waitKey(0)

    imgBin = cv.medianBlur(imgBin, 9)

    #show blurred binary image of walls
    cv.imshow("image", imgBin*255)
    k = cv.waitKey(0)

    dims = calculateLabDims(imgBin)
    print(dims)

    cells = np.empty(dims, dtype=object)

    #calculate how large the cells are by dividing the image dimensions by the number of cells
    cellWidth = imgBin.shape[1] / dims[0]
    cellHeight = imgBin.shape[0] / dims[1]

    print(cellWidth, cellHeight)

    #run through all cells and look at their middle point in the image
    for i in range(dims[1]):
        yPos = int(cellHeight/2 + cellHeight * i)
        for j in range(dims[0]):
            xPos = int(cellWidth/2 + cellWidth * j)

            #from the middle point of the cell check towards all sides in order to find walls

            #top
            startTop = yPos - int(cellHeight * 0.6)
            if(startTop < 0): startTop = 0
            topPoints = imgBin[startTop:yPos, xPos]
            topWall = topPoints.sum() > 0
            
            #right
            endRight = xPos + int(cellWidth * 0.6)
            if(endRight >= imgBin.shape[1]): endRight = imgBin.shape[1] - 1
            rightPoints = imgBin[yPos, xPos:endRight]
            rightWall = rightPoints.sum() > 0

            #bottom
            endBottom = yPos + int(cellHeight * 0.6)
            if(endBottom >= imgBin.shape[0]): endBottom = imgBin.shape[0] -1
            bottomPoints = imgBin[yPos: endBottom, xPos]
            bottomWall = bottomPoints.sum() > 0

            #left
            startLeft = xPos - int(cellWidth * 0.6)
            if(startLeft < 0): startLeft = 0
            leftPoints = imgBin[yPos, startLeft:xPos]
            leftWall = leftPoints.sum() > 0

            cells[j, i] = nt.Cell(topWall, rightWall, bottomWall, leftWall, j, i)

    maze = nt.Maze(dims, cells)

    return maze