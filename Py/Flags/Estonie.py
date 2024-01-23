import Main

def Estonie () :
    img = Main.createImg((600,300),(0,0,0))
    img = Main.getBande(0, 600, 0, 100, (0, 114, 206), img)
    img = Main.getBande(0, 600, 200,300, (255,255,255), img)

    return img

