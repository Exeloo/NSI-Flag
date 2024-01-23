import Main

def Gabon():
    img = Main.createImg((600,300),(0, 158, 96))
    img = Main.getBande(0, 600, 100, 200, (252, 209, 22), img)
    img = Main.getBande(0, 600, 200,300, (58, 117, 196), img)
    return img