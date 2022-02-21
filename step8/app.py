import pyxel
from timedValue import TimedValue

# Step 8 - Functions are things
# Where we select the interpolator dynamically

class App:

    def __init__(self):

        pyxel.init(
            320,
            240,
            fps=60,
            quit_key=pyxel.KEY_TAB,
        )

        # Delay construction to avoid unfortunate coincidence
        self.start = 60*1

        pyxel.run(self.update,self.draw)
    
    def now(self):
        return pyxel.frame_count
    
    def draw(self):
        pyxel.cls(0)
        if pyxel.frame_count < self.start: return
        pyxel.text(10, 10, str(round(self.y.value()*100)/100), 10)
        pyxel.rect(10, 20, 20 + self.y.value(), 20 + self.y.value(), 10)
        pyxel.rect(300, 20 + self.y.value(), 2, 2, 8)

    def update(self):
        if pyxel.frame_count == self.start:
            self.y = TimedValue(200, self, 60*3, f="easeInOutBack")
        
        if pyxel.btn(pyxel.KEY_R):
            self.y.reset()

App()