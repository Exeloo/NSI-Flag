import Main
def Danemark () :
    img = Main.createImg((600,300),(198,12,48))
    img = Main.getBande(175, 225, 0, 300, (255,255,255), img)
    img = Main.getBande(0, 600, 130,180, (255,255,255), img)

    return img


