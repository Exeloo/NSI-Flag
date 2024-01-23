import Main

def Suède():
    img = Main.createImg((600,300),(0, 106, 167))
    img = Main.getBande(170, 260, 0, 300, (254, 204, 0), img)
    img = Main.getBande(0, 600, 109,191, (254,204,0), img)
    return img