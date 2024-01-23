import Main

def Bénin():
    img = Main.createImg((600,300),(34 ,136,72))
    img = Main.getBande(200, 600, 0, 150, (253, 218, 36), img)
    img = Main.getBande(200, 600, 150,300, (238, 39, 55), img)
    return img