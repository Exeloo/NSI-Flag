import Main

def Soudan():
    img = Main.createImg((600,300),(200 ,16,46))
    img = Main.getBande(0, 600, 100, 200, (255, 255, 255), img)
    img = Main.getBande(0, 600, 200,300, (0,0,0), img)
    img = Main.triangleBG(0,200,0,150,(0,150,94), img)
    img = Main.triangleHG(0,200,300,150,(0,150,94), img)
    return img