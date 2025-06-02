import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="ひなころボンバー")
        pyxel.load("my_resource.pyxres")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()


    def draw(self):
        pyxel.cls(pyxel.COLOR_DARK_BLUE)
        #石
        pyxel.blt(SCREEN_WIDTH/2, 0, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK)
        #プレイヤー
        pyxel.blt(SCREEN_WIDTH/2, SCREEN_HEIGHT * 4 / 5, 0, 16, 0, 16, 16, pyxel.COLOR_BLACK)

App()