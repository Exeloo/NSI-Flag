import Main

def Kuwait():
    img = Main.createImg((600,300), (239, 51, 64))
    img = Main.getBande(150, 600, 0, 100, (0,150,57), img)
    img = Main.getBande(150, 600, 100,200, (255, 255, 255), img)
    img = Main.getBande(150, 600,200,300, (0, 0, 0), img)
    return img