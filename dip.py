import numpy as np
import math as math

# Costrast Stretching
def CS(img, scale):
    a, b = [50, 150]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if int(img[i, j]) < a:
                img[i, j] = 0
            elif int(img[i, j]) < b:
                img[i, j] = scale * (int(img[i, j]) - a)
            else:
                img[i, j] = scale * (b - a)
    return img

# Image Brightening
def IB(img, const):
    a, b = [0, 255]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if int(img[i,j]) + const > b:
                img[i,j] = 255
            elif int(img[i,j]) + const < a:
                img[i,j] = 0
            else:
                img[i,j] = int(img[i,j]) + const
    return img

# Negative image
def Negative(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i,j] = 255 - int(img[i,j])
    return img

# Scaling 
def Scaling(pic, scalex, scaley): 
    newsizex = round(scaley*pic.shape[0])
    newsizey = round(scalex*pic.shape[1])
    img = np.zeros((newsizex,newsizey),dtype=np.uint8)

    for i in range(newsizex-1):
        for j in range(newsizey-1):
            img[i,j] = pic[round(i/scaley),round(j/scalex)]
    return img

# Rotation
def Rotate(pic, Angle):
    Degree = math.radians(Angle%360)

    if (Degree < math.radians(360) and Degree >= math.radians(271)) or (Degree < math.radians(180) and Degree >= math.radians(90)):
        newsizex = round(abs(math.cos(Degree)*pic.shape[0] - math.sin(Degree)*pic.shape[1]))
        newsizey = round(abs(math.sin(Degree)*pic.shape[0] - math.cos(Degree)*pic.shape[1]))
        img = np.zeros((newsizex,newsizey),dtype=np.uint8)
        dif = round(pic.shape[0]*math.sin(Degree))

        for i in range(pic.shape[0]):
            for j in range(pic.shape[1]):
                x = round(i*math.cos(Degree) - j*math.sin(Degree))
                y = round(i*math.sin(Degree) + j*math.cos(Degree))
                if x< img.shape[0] and y - dif < img.shape[1]:
                    img[x, y-dif] = pic[i,j]
        
    else:
        newsizex = round(abs(math.cos(Degree)*pic.shape[0] + math.sin(Degree)*pic.shape[1]))
        newsizey = round(abs(math.sin(Degree)*pic.shape[0] + math.cos(Degree)*pic.shape[1]))
        print(pic.shape[1],pic.shape[0],newsizex, newsizey)
        img = np.zeros((newsizex,newsizey),dtype=np.uint8)
        dif = round(pic.shape[1]*math.sin(Degree))

        for i in range(pic.shape[0]):
            for j in range(pic.shape[1]):
                x = round(i*math.cos(Degree) - j*math.sin(Degree))
                y = round(i*math.sin(Degree) + j*math.cos(Degree))
                if x + dif < img.shape[0] and y < img.shape[1]:
                    img[x+dif, y] = pic[i,j]
    return img

# Translation
def Trans(pic, trlx, trly):
    trlx = int(trlx / 100 * pic.shape[1])
    trly = int(trly / 100 * pic.shape[0])
    if trlx>=0:
        for i in range(pic.shape[0]):
            for j in range(pic.shape[1]-1,-1,-1):
                if j-trlx >= 0:
                    pic[i,j] = int(pic[i,j-trlx])
                else:
                    pic[i,j] = 255
    else:
        for i in range(pic.shape[0]):
            for j in range(pic.shape[1]):
                if j-trlx <= pic.shape[1] - 1:
                    pic[i,j] = int(pic[i,j-trlx])
                else:
                    pic[i,j] = 255

    if trly>=0:
        for i in range(pic.shape[0]):
            for j in range(pic.shape[1]):
                if i+trly <= pic.shape[0] - 1:
                    pic[i,j] = int(pic[i+trly,j])
                else:
                    pic[i,j] = 255
    else:
        for i in range(pic.shape[0]-1,-1,-1):
            for j in range(pic.shape[1]):
                if i+trly >= 0:
                    pic[i,j] = int(pic[i+trly,j])
                else:
                    pic[i,j] = 255
    return pic

# Smoothen/Sharpen
def SS(pic,level):
    for i in range(pic.shape[0]):
        for j in range(pic.shape[1]):
            summ =+ pic[i,j]

    ave = summ/pic.shape[0]/pic.shape[1]

    if(level<0):
        level = abs(level)
        for i in range(pic.shape[0]):
            for j in range(pic.shape[1]):
                if(pic[i,j] + (ave - pic[i,j])*level*level > 255):
                    pic[i,j] = 255
                elif(pic[i,j] + (ave - pic[i,j])*level*level < 0):
                    pic[i,j] = 0
                else:
                    pic[i,j] += (ave - pic[i,j])*level*level
    
    elif(level>0):
        for i in range(pic.shape[0]):
            for j in range(pic.shape[1]):
                if(pic[i,j] + (pic[i,j] - ave)*level*level > 255):
                    pic[i,j] = 255
                elif(pic[i,j] + (pic[i,j] - ave)*level*level < 0):
                    pic[i,j] = 0
                else:
                    pic[i,j] += (pic[i,j] - ave)*level*level
    return pic



def PP(pic, Degree):
    Degree = math.radians(Degree%360)

    newsizex = round(abs(math.cos(Degree)*pic.shape[0]) + abs(math.sin(Degree)*pic.shape[1]))
    newsizey = round(abs(math.sin(Degree)*pic.shape[0]) + abs(math.cos(Degree)*pic.shape[1]))

    img = np.zeros((newsizex,newsizey),dtype=np.uint8)

    for i in range(pic.shape[0]):
        for j in range(pic.shape[1]):
            x = round(abs(i*math.cos(Degree)) + abs(j*math.sin(Degree)))
            y = round(abs(i*math.sin(Degree)) + abs(j*math.cos(Degree)))
            if x < img.shape[0] and y < img.shape[1]:
                img[x, y] = int(pic[i,j])
    return img
    
def PP2(pic, top, left):
    DegreeTop = math.radians(top%360)
    DegreeLeft = math.radians(left%360)

    newsizex = round(abs(math.cos(DegreeLeft)*pic.shape[0]) + abs(math.sin(DegreeLeft)*pic.shape[1]))
    newsizey = round(abs(math.sin(DegreeTop)*pic.shape[0]) + abs(math.cos(DegreeTop)*pic.shape[1]))

    img = np.zeros((newsizex,newsizey),dtype=np.uint8)

    for i in range(pic.shape[0]):
        for j in range(pic.shape[1]):
            x = round(abs(i*math.cos(DegreeLeft)) + abs(j*math.sin(DegreeLeft)))
            y = round(abs(i*math.sin(DegreeTop)) + abs(j*math.cos(DegreeTop)))
            if x < img.shape[0] and y < img.shape[1]:
                img[x, y] = int(pic[i,j])
    return img