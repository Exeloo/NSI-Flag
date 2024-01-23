import Main

def Tchéquie():
    img = Main.createImg((600, 300), (255, 255, 255))
    img = Main.getBande(0, 600, 150, 300, (255, 20, 20), img)
    img = Main.triangleBG(0, 260, 0, 150, (20, 83, 255), img)
    img = Main.triangleHG(0, 260, 300, 150, (20, 83, 255), img)
    return img
