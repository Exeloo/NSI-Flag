import Main

def Roumanie () :
    img = Main.createImg((600,300),(252,209,22))
    img = Main.getBande(0, 200, 0, 300, (0,43,127), img)
    img = Main.getBande(400, 600, 0,300, (206,17,38), img)

    return img


