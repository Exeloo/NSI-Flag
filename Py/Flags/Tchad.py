import Main

def Tchad():
    img = Main.createImg((600,300),(255, 204, 0))
    img = Main.getBande(0, 200, 0,300, (0, 37, 105), img)
    img = Main.getBande(400, 600, 0,300, (	210, 15, 54), img)
    return img