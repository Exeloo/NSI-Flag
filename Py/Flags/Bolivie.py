import Main

def Bolivie():
    img = Main.createImg((600,300),(213,43,30))
    img = Main.getBande(0, 600, 100, 200, (252,209,22), img)
    img = Main.getBande(0, 600, 200,300, (0,121,52), img)
    return img