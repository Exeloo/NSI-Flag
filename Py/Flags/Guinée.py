import Main

def Guinée():
    img = Main.createImg((600,300),(255,209,0))
    img = Main.getBande(0, 200, 0,300, (239,51,64), img)
    img = Main.getBande(400, 600, 0,300, (0,150,57), img)
    return img