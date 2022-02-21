import pytweening

class TimedValue():
    def __init__(self, value, clock, duration=60, f="linear"):
        self.target = value
        self.duration = duration
        self.clock = clock
        self.birth = clock.now()
        self.interpolator = getattr(pytweening, f)


    def value(self):
        e = self.now() - self.birth
        p = e / self.duration
        if p > 1:
            p = 1
        return self.interpolator(p) * self.target

    def now(self):
        return self.clock.now()
    
    def reset(self):
        self.birth = self.now()