import Main

def Sierra_Leone():
    img = Main.createImg((600,300),(67,176,42))
    img = Main.getBande(0, 600, 100, 200, (255,255,255), img)
    img = Main.getBande(0, 600, 200,300, (105,179,231), img)
    return img