import Main
def Lettonie () :
    img = Main.createImg((600,300),(255,255,255))
    img = Main.getBande(0, 600, 0, 125, (173,0,35), img)
    img = Main.getBande(0, 600, 175,300, (173,0,35), img)

    return img


