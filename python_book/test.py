

class Bomba:
    def __init__(self):
        self.color = 'fire'

    def fire(self):
        print('boom')

class Dynamite(Bomba):
    s = 'rare'
    def __init__(self):
        Bomba.__init__(self)
        self.coloring = self.color*3
    
    


b = Dynamite()

print(b.coloring)