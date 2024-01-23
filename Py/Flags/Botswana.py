import Main

def Botswana():
    img = Main.createImg((600,300),(171, 202, 233))
    img = Main.getBande(0, 600, 111,190 , (255,255,255), img)
    img = Main.getBande(0, 600, 125,176, (0,0,0), img)
    return img