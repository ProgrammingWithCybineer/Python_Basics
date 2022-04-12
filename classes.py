class Point:
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
#object is an instance of the class
point1 = Point()

point1.draw()
point1.move()

# can have attributes that can be set anywhere in the program
point1.x = 10 
point1.y = 20
print(point1.x)