import Main

def Colombie():
    img = Main.createImg((600,300),(255,205,0))
    img = Main.getBande(0, 600, 150,225, (0,48,135), img)
    img = Main.getBande(0, 600, 225,300, (200,16,46), img)
    return img