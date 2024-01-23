import Main

def Grèce():
    img = Main.createImg((600,297),(13,94,175))
    img = Main.getBande(165, 600, 33, 66, (255,255,255), img)
    img = Main.getBande(165, 600, 99, 132, (255,255,255), img)
    img = Main.getBande(0, 600, 165, 198, (255,255,255), img)
    img = Main.getBande(0, 600, 231, 264, (255,255,255), img)
    img = Main.getBande(66, 99, 0, 165, (255,255,255), img)
    img = Main.getBande(0,165, 66,99, (255,255,255), img)
    return img