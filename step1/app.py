import pyxel

# Step 1 - Plain old Python value

class App:

    def __init__(self):

        pyxel.init(
            320,
            240,
            fps=60,
            quit_key=pyxel.KEY_TAB,
        )
        self.y = 200

        pyxel.run(self.update,self.draw)
    
    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, str(round(self.y*100)/100), 10)


    def update(self):
        self.y -= 0.1

App()