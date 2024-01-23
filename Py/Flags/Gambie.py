import Main

def Gambie():
    img = Main.createImg((600,300),(255,255,255))
    img = Main.getBande(0, 600, 0,100 , (206, 17, 38), img)
    img = Main.getBande(0, 600, 115,185, (12, 28, 140), img)
    img = Main.getBande(0, 600, 200,300, (58, 119, 40), img)
    return img