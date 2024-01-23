import Main

def Laos():
    img = Main.createImg((600,300),(239,51,64))
    img = Main.getBande(0, 600, 100, 200, (0,61,165), img)
    img = Main.round(300, 150, 40, (255,255,255), img)
    return img