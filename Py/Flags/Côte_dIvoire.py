import Main

def Côte_dIvoire():
    img = Main.createImg((600,300),(	255, 255, 255))
    img = Main.getBande(0, 200, 0,300, (	247, 127, 0), img)
    img = Main.getBande(400, 600, 0,300, (	0, 158, 96), img)
    return img