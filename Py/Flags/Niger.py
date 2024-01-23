import Main

def Niger():
    img = Main.createImg((600,300),(255,255,255))
    img = Main.getBande(0, 600, 0, 100, (224,82,6), img)
    img = Main.getBande(0, 600, 200,300, (13,176,43), img)
    img = Main.round(300, 150, 42, (224,82,6), img)
    return img