class TimedValue():
    def __init__(self, value, clock, duration=60):
        self.target = value
        self.duration = duration
        self.clock = clock
        self.birth = clock.now()

    def value(self):
        e = self.now() - self.birth
        p = e / self.duration
        if p > 1:
            p = 1
        return p*self.target

    def now(self):
        return self.clock.now()