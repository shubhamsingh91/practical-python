class Player:
    def __init__(self,name,x,y,health):
        self.name = name
        self.x = x
        self.y = y
        self.health = health
    
    def move(self,dx,dy):
        self.x+= dx
        self.y+= dy
    
    def damage(self,hit):
        self.health -= hit
    
    def print(self):
        print("Player: ", self.name)
        print("Pos = ", self.x, ",", self.y)
        print("health = ", self.health)
        print("\n")

if __name__ == "__main__":
    
    p1 = Player("A",23,45,100)
    p2 = Player("B",13,24,67)

    p1.print()
    p2.print()

    p1.damage(12)
    p2.damage(15)

    p1.move(1,2)
    p2.move(4,5)

    p1.print()
    p2.print()

