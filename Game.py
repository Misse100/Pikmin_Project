from cmu_graphics import *
# Fill me in!
app.movable = Group()
map = Group(Circle(200,200,300,fill=gradient("white","red","blue")))
leftleg = Rect(202,205,3,12,rotateAngle=155)
leftleg.a = 0.5
rightleg = Rect(196,205,3,6,rotateAngle=215)
rightleg.a = -0.5
man = Group(Circle(200,190,5),Rect(197.5,195,5,12),Rect(207,190,3,12,rotateAngle=240),
Rect(190,190,3,12,rotateAngle=120),leftleg,rightleg)
app.numballs = 3
app.balls = Group()
app.collectible = Group(Circle(30,30,5),Circle(230,30,5))
app.bullets = Group()
app.movable.add(map,app.collectible)
app.direction = "up"
def makeThrow():
    pass

def adjustBalls(balls):
    for i in range(app.numballs):
        app.balls.add(Circle(215 + 10*i,214,4))




'''
app.rows = 3
app.cols = 4
list = makeList(app.rows,app.rows)

def onMouseDrag(mouseX,mouseY):
    target = list.hitTest(mouseX,mouseY)
    for row in range(app.rows):
        for col in range(app.cols):
            list[row][col] = bob
            if target == bob:
                lightup(row,col)
                
def lightup(row,col):
    list[row][col].fill = "lightGreen"
    bob.timer = 30

def onStep():
    bob.timer -1
    for bob in list:
        if bob.timer > 0:
            bob.fill = "lightgreen"
'''
def shoot(direction):
    if direction == "down":
        x = 200
        y = 220
        speedX = 0
        speedY = 10
    elif direction == "up":
        x = 200
        y = 180
        speedX = 0
        speedY = -10
    elif direction == "right":
        x = 220
        y = 200
        speedX = 10
        speedY = 0
    elif direction == "left":
        x = 180
        y = 200
        speedX = -10
        speedY = 0
    bullet = Circle(x,y,3)
    bullet.dy = speedY
    bullet.dx = speedX
    app.bullets.add(bullet)
    app.numballs -= 1
def legmove():
    if leftleg.height > 12 or leftleg.height < 6:
        leftleg.a *= -1
        rightleg.a *= -1
    leftleg.height += leftleg.a
    rightleg.height += rightleg.a
    
def onKeyHold(keys):
    if "w" in keys:
        app.movable.centerY += 10
        app.direction = "up"
    if "a" in keys:
        app.movable.centerX += 10
        app.direction = "left"
    if "s" in keys:
        app.movable.centerY -= 10
        app.direction = "down"
    if "d" in keys:
        app.movable.centerX -= 10
        app.direction = "right"
def onKeyPress(key):
    if key == "space" and app.numballs > 0:
        shoot(app.direction)
    legmove()

def onStep():
    app.balls.clear()
    adjustBalls(app.numballs)
    for dot in app.collectible:
        if dot.hitsShape(man):
            app.collectible.remove(dot)
            app.numballs += 1
    for i in app.bullets:
        i.centerX += i.dx
        i.centerY += i.dy
        



cmu_graphics.run()