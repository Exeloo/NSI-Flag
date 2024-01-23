import Main
def Irlande () :
    img = Main.createImg((600,300),(255,255,255))
    img = Main.getBande(0, 200, 0, 300, (22, 155, 98), img)
    img = Main.getBande(400, 600, 0,300, (255,136,62), img)

    return img

