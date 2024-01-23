import Main

def Pologne():
    img = Main.createImg((600,300),(255,255,255))
    img = Main.getBande(0, 600, 150, 300, (206, 43, 55), img)
    return img