from PIL import Image

def createImg(taille, color):
    """Cette fonction crée une image"""
    img=Image.new("RGB",taille,color)
    return img

def show(img) :
    """Cette fonction montre une image"""
    img.show()

def coef(x1, x2, y1, y2) :
    """Cette fonction calcul un coefficiant"""
    return (y2-y1)/(x2-x1)

def getBande(x1, x2, y1, y2, color, img):
    """Cette fonction dessine une bande"""
    for x in range (x1, x2) :
        for y in range (y1, y2) :
            img.putpixel((x,y),color)
    return img

def triangleBG(x1, x2, y1, y2, color, img):
    """Cette fonction dessine un triangle rectangle avec l'angle droit
    en bas à gauche"""
    a = coef(x1, x2, y1, y2)
    for x in range (x1, x2) :
        for y in range (y1, y2) :
            if y-y1 >= (x-x1)*a :
                img.putpixel((x,y),color)
    return img

def triangleBD(x1, x2, y1, y2, color, img):
    """Cette fonction dessine un triangle rectangle avec l'angle droit
    en bas à droite"""
    a = coef(x1, x2, y1, y2)
    for x in range (x2, x1) :
        for y in range (y1, y2) :
            if y-y1 >= (x-x1)*a :
                img.putpixel((x,y),color)
    return img

def triangleHG(x1, x2, y1, y2, color, img):
    """Cette fonction dessine un triangle rectangle avec l'angle droit
    en haut à gauche"""
    a = coef(x1, x2, y1, y2)
    for x in range (x1, x2) :
        for y in range (y2, y1) :
            if y-y1 <= (x-x1)*a :
                img.putpixel((x,y),color)
    return img

def triangleHD(x1, x2, y1, y2, color, img):
    """Cette fonction dessine un triangle rectangle avec l'angle droit
    en haut à droite"""
    a = coef(x1, x2, y1, y2)
    for x in range (x2, x1) :
        for y in range (y2, y1) :
            if y-y1 <= (x-x1)*a :
                img.putpixel((x,y),color)
    return img



def round(a, b, r, color, img):
    """Cette fonction dessine un rond"""
    for x in range (a-r,a+r) :
        for y in range (b-r, b+r) :
            if (x-a)**2 + (y-b)**2 <= r**2 :
                img.putpixel((x,y),color)
    return img


def getDefaultFlag() :
    return Image.open("Error.jpg")