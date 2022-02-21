class TimedValue():
    def __init__(self, value):
        self.target = value
        self.v = 0

    def value(self):
        if self.v < self.target:
            self.v += 1
        return self.v