import Main

def Norvège () :
    img = Main.createImg((600,300),(186, 12, 47))
    img = Main.getBande(150, 250, 0, 300, (255,255,255), img)
    img = Main.getBande(0, 600, 112,188, (255,255,255), img)
    img = Main.getBande(0, 600, 131,169, (0, 32, 91), img)
    img = Main.getBande(175, 225, 0,300, (0, 32, 91), img)

    return img



