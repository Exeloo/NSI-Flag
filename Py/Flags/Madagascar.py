import Main

def Madagascar():
    img = Main.createImg((600,300),(255 ,255,255))
    img = Main.getBande(200, 600, 0, 150, (249,66,58), img)
    img = Main.getBande(200, 600, 150,300, (0,132,61), img)
    return img