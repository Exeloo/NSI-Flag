import Main

def Maurice():
    img = Main.createImg((600,300),(239,51,64))
    img = Main.getBande(0, 600, 75,150 , (0,94,184), img)
    img = Main.getBande(0, 600, 150,225, (255,209,0), img)
    img = Main.getBande(0, 600, 225,300, (0,150,57), img)
    return img