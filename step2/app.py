import pyxel
from timedValue import TimedValue

# Step 2 - Encapsulation
# Where the value moves into a class as an instance variable
# and is updated through a member function.

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
        pyxel.text(10, 10, str(round(self.y.value()*100)/100), 10)


    def update(self):
        self.y.update(-0.1)

App(TimedValue(200))