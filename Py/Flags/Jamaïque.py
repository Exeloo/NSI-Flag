import Main

def Jamaïque():
    img = Main.createImg((600, 300), (255, 184, 28))
    img = Main.triangleBG(0, 250, 25, 150, (45,41,38), img)
    img = Main.triangleBD(600, 350,25, 150,  (45,41,38), img)
    img = Main.triangleHG(0, 250, 270, 150,(45,41,38), img)
    img = Main.triangleHD(600,350 , 270, 150, (45,41,38), img)
    img = Main.triangleHD(300,50 , 125, 0, (0,119,73), img)
    img = Main.triangleHG(300,550 , 125, 0, (0,119,73), img)
    img = Main.triangleBD(300,50 , 175, 300, (0,119,73), img)
    img = Main.triangleBG(300,550 , 175, 300, (0,119,73), img)
    return img