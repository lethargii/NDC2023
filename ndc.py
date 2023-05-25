import pyxel

# Reste à faire :
# Rajouter un knockback de plus en plsu grand quand un joueur attaque l'autre
# Un joueur doit gagner quand l'autre quitte la zone de combat
# Rajouter l'orientation des personnages


class Jeu():

    '''
    Voici notre jeu : Spartacus bros brawl super ultra ultimate !!!!
    Ce jeu est un smash bros like qui se joue à 2 joueurs.
    LES JOUEURS NE SONT PAS DES OISEAUX.
    Le joueur 1 utilise les touches ZQSD pour se déplacer et la barre espace pour attaquer.
    Le joueur 2 utilise les flèches du clavier pour se déplacer et la touche entrée pour attaquer.
    '''



    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.j1x = 15
        self.j1y = 60
        self.j2x = 30
        self.j2y = 60
        self.jumpj1 = "Ground"
        self.jumpj2 = "Ground"
        self.j1hp = 5
        self.j2hp = 5
        self.j1sword = False
        self.j2sword = False
        pyxel.load("theme.pyxres")
        pyxel.playm(0, loop = True)
        pyxel.run(self.update, self.draw)


    def collision_j1(self):
        if self.j2sword:
            if (self.j1x > self.j2x-5 or self.j1x < self.j2x-10):
                print("coucou")



    def update(self):


        # Déplacement joueur 1
        if pyxel.btn(pyxel.KEY_D):
            self.j1x += 1
        if pyxel.btn(pyxel.KEY_Q):
            self.j1x -= 1
        if pyxel.btnr(pyxel.KEY_SPACE):
            self.j1sword = not self.j1sword


        # Déplacement joueur 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.j2x += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.j2x -= 1
        if pyxel.btnr(pyxel.KEY_RETURN):
            self.j2sword = not self.j2sword


        # Saut et gravité
        if pyxel.btn(pyxel.KEY_UP) and self.jumpj2 == "Ground":
            self.jumpj2 = "Jump"
        if self.jumpj2 == "Jump":
            self.j2y -= 2
        if self.j2y < 30:
            self.jumpj2 = "Fall"
        if self.jumpj2 == "Fall":
            self.j2y += 2
        if self.j2y >= 60:
            self.jumpj2 = "Ground"

        if pyxel.btn(pyxel.KEY_Z) and self.jumpj1 == "Ground":
            self.jumpj1 = "Jump"
        if self.jumpj1 == "Jump":
            self.j1y -= 2
        if self.j1y < 30:
            self.jumpj1 = "Fall"
        if self.jumpj1 == "Fall":
            self.j1y += 2
        if self.j1y >= 60:
            self.jumpj1 = "Ground"
        
        self.collision_j1()


    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,128,128,0)
        pyxel.blt(self.j1x, self.j1y, 0, 2, 0, 6, 8, 0)
        pyxel.blt(self.j2x, self.j2y, 0, 2, 8, -6, 8, 0)
        if self.j1sword:
            pyxel.blt(self.j1x+5, self.j1y, 0, 8, 24, 5, 8, 0)
        if self.j2sword:
            pyxel.blt(self.j2x-4, self.j2y, 0, 8, 24, -5, 8, 0)







Jeu()