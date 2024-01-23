import Main
def Bahamas () :
    img = Main.createImg((600, 300), (0, 119, 139))
    img = Main.getBande(0, 600, 100, 200, (255, 199, 44), img)
    img = Main.triangleBG(0, 260, 0, 150, (0, 0, 0), img)
    img = Main.triangleHG(0, 260, 300, 150, (0, 0, 0), img)
    return img
