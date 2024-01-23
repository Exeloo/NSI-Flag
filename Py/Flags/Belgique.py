import Main
def Belgique ():
    img = Main.createImg((600,300),(255, 233, 54))
    img = Main.getBande(0, 200, 0,300, (0,0,0), img)
    img = Main.getBande(400, 600, 0,300, (255, 15, 33), img)
    return img
