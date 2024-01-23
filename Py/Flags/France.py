import Main

def France() :
    img = Main.createImg((600,300),(255,255,255))
    img = Main.getBande(0, 200, 0, 300, (0, 85, 164), img)
    img = Main.getBande(400, 600, 0,300, (239, 65, 53), img)

    return img