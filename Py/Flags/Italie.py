import Main

def Italie () :
    img = Main.createImg((600,300),(255,255,255))
    img = Main.getBande(0, 200, 0, 300, (0, 146, 70), img)
    img = Main.getBande(400, 600, 0,300, (206, 43, 55), img)

    return img


