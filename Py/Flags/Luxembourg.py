import Main

def Luxembourg():
    img = Main.createImg((600,300),(199, 63, 74))
    img = Main.getBande(0, 600, 100, 200, (255, 255, 255), img)
    img = Main.getBande(0, 600, 200,300, (0, 137, 182), img)
    return img