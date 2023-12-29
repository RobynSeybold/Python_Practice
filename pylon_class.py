class Pylon:
    pyloncount = 0
    def __init__(self, front):
        self.front = front
        print("Pylon constructed.")
        Pylon.pyloncount = Pylon.pyloncount+1
        if Pylon.pyloncount < 5:
            print("You must construct additional Pylons!")
    
    def protoss_warp(self, base):
        for unit, number in base.items():
            #print(unit, number)
            if unit != "Probe":
                base[unit] = 0
                self.front.setdefault(unit, 0)
                self.front[unit] += number
        return base, self.front
