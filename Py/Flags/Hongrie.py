import Main

def Hongrie () :
    img = Main.createImg((600,300),(255,255,255))
    img = Main.getBande(0, 600, 0, 100, (204,0,8), img)
    img = Main.getBande(0, 600, 200,300, (0,102,43), img)

    return img

