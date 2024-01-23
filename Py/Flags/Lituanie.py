import Main

def Lituanie () :
    img = Main.createImg((600,300),(0,100,0))
    img = Main.getBande(0, 600, 0, 100, (255,202,24), img)
    img = Main.getBande(0, 600, 200,300, (255,0,0), img)

    return img


