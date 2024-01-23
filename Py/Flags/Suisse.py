import Main

def Suisse () :
    img = Main.createImg((400,400),(255,0,0))
    img = Main.getBande(66, 334, 162, 237, (255,255,255), img)
    img = Main.getBande(162, 237, 66,334, (255,255,255), img)

    return img


