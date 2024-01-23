import Main

def Russie () :
    img = Main.createImg((600,300),(0, 57,166))
    img = Main.getBande(0,600,0,100, (255,255,255), img)
    img = Main.getBande(0, 600, 200,300, (213,43, 30), img)

    return img

