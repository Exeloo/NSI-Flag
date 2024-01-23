import Main

def Seychelles():
    img = Main.createImg((600, 300), (210,38,48))
    img = Main.triangleBD(600,0 , 100, 300, (255,255,255), img)
    img = Main.triangleBD(600,0 , 200, 300, (0,122,51), img)
    img = Main.triangleHG(0,400 ,300, 0, (254,209,65), img)
    img = Main.triangleHG(0,200 ,300, 0, (0,47,108), img)
    return img