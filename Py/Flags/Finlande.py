import Main

def Finlande () :
    img = Main.createImg((600,300),(255,255,255))
    img = Main.getBande(170, 260, 0, 300, (0, 53, 128), img)
    img = Main.getBande(0, 600, 109,191, (0, 53, 128), img)

    return img

