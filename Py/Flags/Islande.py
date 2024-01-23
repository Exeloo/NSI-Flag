import Main
def Islande () :
    img = Main.createImg((600,300),(0,56,151))
    img = Main.getBande(168, 264, 0, 300, (255,255,255), img)
    img = Main.getBande(0, 600, 119,187, (255,255,255), img)
    img = Main.getBande(0, 600, 136,170, (215,40,40), img)
    img = Main.getBande(192, 240, 0,300, (215,40,40), img)

    return img

