class TimedValue():
    def __init__(self, value):
        self.v = value

    def update(self, v):
        self.v += v

    def value(self):
        return self.v