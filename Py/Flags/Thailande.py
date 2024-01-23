import Main

def Thailande():
    img = Main.createImg((600,300),(165, 25, 49))
    img = Main.getBande(0, 600, 49,251, (244, 245, 248), img)
    img = Main.getBande(0, 600, 99,201, (45, 42, 74), img)
    return img