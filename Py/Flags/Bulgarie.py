import Main

def Bulgarie():
    img = Main.createImg((600,300),(208, 28, 31))
    img = Main.getBande(0, 600, 0, 100, (255,255,255), img)
    img = Main.getBande(0, 600, 100,200, (0, 155, 117), img)
    return img