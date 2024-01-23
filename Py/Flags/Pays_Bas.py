import Main

def Pays_Bas():
    img = Main.createImg((600,300),(174, 28, 40))
    img = Main.getBande(0, 600, 100, 200, (255, 255, 255), img)
    img = Main.getBande(0, 600, 200,300, (33, 70, 139), img)
    return img