import Main

def Mali():
    img = Main.createImg((600,300),(252,209,22))
    img = Main.getBande(0, 200, 0,300, (20,181,58), img)
    img = Main.getBande(400, 600, 0,300, (206-17-38), img)
    return img