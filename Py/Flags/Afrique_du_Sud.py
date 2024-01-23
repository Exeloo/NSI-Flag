import Main

def Afrique_du_Sud():
    img = Main.createImg((600, 300), (255, 255, 255))
    img = Main.getBande(0, 600, 100, 200, (255, 255, 255), img)
    img = Main.getBande(275, 600, 0, 100, (224, 60, 49), img)
    img = Main.getBande(275, 600, 200, 300, (0, 20, 137), img)
    img = Main.getBande(0, 600, 116, 184, (0, 119, 73), img)
    img = Main.getBande(0, 60, 0, 300, (0, 119, 73), img)
    img = Main.triangleBG(60, 325, 0, 150, (0, 119, 73), img)
    img = Main.triangleHG(60, 325, 300, 150, (0, 119, 73), img)
    img = Main.triangleBG(0, 195, 40, 150, (255, 184, 28), img)
    img = Main.triangleHG(0, 195, 260, 150, (255, 184, 28), img)
    img = Main.triangleBG(0, 170, 55, 150, (0,0,0), img)
    img = Main.triangleHG(0, 170, 245, 150, (0,0,0), img)
    img = Main.triangleHD(275, 95, 100, 0, (224, 60, 49), img)
    img = Main.triangleBD(275, 95, 200, 300, (0, 20, 137), img)

    return img