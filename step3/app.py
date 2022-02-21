import pyxel
from timedValue import TimedValue

# Step 3 - Slow value
# Where the target value takes time to be reached

class App:

    def __init__(self, y):

        pyxel.init(
            320,
            240,
            fps=60,
            quit_key=pyxel.KEY_TAB,
        )
        self.y = y

        pyxel.run(self.update,self.draw)
    
    def draw(self):
        pyxel.cls(0)
        curY = self.y.value()
        pyxel.text(10, 10, str(round(curY*100)/100), 10)
        pyxel.rect(10,20,curY,curY,10)
        pyxel.rect(300,curY,2,2,10)

    def update(self):
        pass

App(TimedValue(200))