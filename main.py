import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
CHICK_INTERVAL = 15

class Chick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isAnim = False
    
    def update(self):
        if self.y < SCREEN_HEIGHT:
            self.y += 1 + (self.x % 3)
        
        if pyxel.frame_count % (CHICK_INTERVAL - (self.x % 5)) == 0:
            self.isAnim ^= True

    def draw(self):
        #ひよころ
        if self.isAnim:
            pyxel.blt(self.x, self.y, 0, 32, 0, 16, 16, pyxel.COLOR_BLACK)
        else:
            pyxel.blt(self.x, self.y, 0, 48, 0, 16, 16, pyxel.COLOR_BLACK)


class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="ひよころパラダイス")
        pyxel.load("my_resource.pyxres")
        self.chicks = []
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if pyxel.frame_count % 12 == 0:
            self.chicks.append(Chick(pyxel.rndi(0, SCREEN_WIDTH - 16), 0))
        if pyxel.frame_count % 15 == 0:
            self.chicks.append(Chick(pyxel.rndi(0, SCREEN_WIDTH - 16), 0))
        if pyxel.frame_count % 24 == 0:
            self.chicks.append(Chick(pyxel.rndi(0, SCREEN_WIDTH - 16), 0))

        for chick in self.chicks.copy():
            chick.update()
            if chick.y >= SCREEN_HEIGHT:
                self.chicks.remove(chick)

    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        #ひよころ
        for chick in self.chicks:
            chick.draw()

        #ひなころ
        pyxel.blt(pyxel.mouse_x - 8, SCREEN_HEIGHT - 16, 0, 16, 0, 16, 16, pyxel.COLOR_BLACK)

App()