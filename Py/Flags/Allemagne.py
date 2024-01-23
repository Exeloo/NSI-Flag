import Main

def Allemagne() :
    img = Main.createImg((600,300),(208,0,0))
    img = Main.getBande(0, 600, 0, 100, (0,0,0), img)
    img = Main.getBande(0, 600, 200,300, (255,206,0), img)

    return img