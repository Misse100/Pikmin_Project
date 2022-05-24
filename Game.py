from cmu_graphics import *
app.movable = Group()

map = Group(Circle(200,200,400,fill=gradient("darkGreen", "green","lightGreen","lightBlue","blue","darkBlue")))
spawn = Circle(200,200,140,fill=None)
#player
leftleg = Rect(202,205,3,12,rotateAngle=155)
leftleg.a = 0.5
rightleg = Rect(196,205,3,6,rotateAngle=215)
rightleg.a = -0.5
man = Group(Circle(200,190,5),Rect(197.5,195,5,12),Rect(207,190,3,12,rotateAngle=240),
Rect(190,190,3,12,rotateAngle=120),leftleg,rightleg)
#variables
app.numballs = 3
app.balls = Group()
app.collectible = Group()
app.bullets = Group()
app.movable.add(map,app.collectible,spawn,app.bullets)
app.direction = "up"
app.bulletspeed = 15
app.speed = 10
def spawnBalls(num):
    #left
    for i in range(num):
        x = randrange(-400,200)
        y = randrange(-400,800)
        while map.contains(x,y) == False or spawn.contains(x,y) == True:
            x = randrange(-400,200)
            y = randrange(-400,800)
        app.collectible.add(Circle(x,y,5))
    #right
    for i in range(num):
        x = randrange(200,800)
        y = randrange(-400,800)
        while map.contains(x,y) == False or spawn.contains(x,y) == True:
            x = randrange(200,800)
            y = randrange(-400,800)
        app.collectible.add(Circle(x,y,5))
        
        

def adjustBalls(balls):
    for i in range(app.numballs):
        app.balls.add(Circle(215 + 10*i,214,4))


spawnBalls(20)


def shoot(direction):
    if direction == "down":
        x = 200
        y = 220
        speedX = 0
        speedY = app.bulletspeed
    elif direction == "up":
        x = 200
        y = 180
        speedX = 0
        speedY = -app.bulletspeed
    elif direction == "right":
        x = 220
        y = 200
        speedX = app.bulletspeed
        speedY = 0
    elif direction == "left":
        x = 180
        y = 200
        speedX = -app.bulletspeed
        speedY = 0
    elif direction == "topleft":
        x = 180
        y = 180
        speedX = -app.bulletspeed
        speedY = -app.bulletspeed
    elif direction == "topright":
        x = 220
        y = 180
        speedX = app.bulletspeed
        speedY = -app.bulletspeed
    elif direction == "downleft":
        x = 180
        y = 220
        speedX = -app.bulletspeed
        speedY = app.bulletspeed
    elif direction == "downright":
        x = 220
        y = 220
        speedX = app.bulletspeed
        speedY = app.bulletspeed
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
    if "w" in keys and "a" in keys:
        app.direction = "topleft"
        app.movable.centerY += app.speed
        app.movable.centerX += app.speed
    elif "w" in keys and "d" in keys:
        app.direction = "topright"
        app.movable.centerY += app.speed
        app.movable.centerX -= app.speed
    elif "s" in keys and "a" in keys:
        app.direction = "downleft"
        app.movable.centerY -= app.speed
        app.movable.centerX += app.speed
    elif "s" in keys and "d" in keys:
        app.direction = "downright"
        app.movable.centerY -= app.speed
        app.movable.centerX -= app.speed
        
    elif "w" in keys:
        app.movable.centerY += app.speed
        app.direction = "up"
    elif "a" in keys:
        app.movable.centerX += app.speed
        app.direction = "left"
    elif "s" in keys:
        app.movable.centerY -= app.speed
        app.direction = "down"
    elif "d" in keys:
        app.movable.centerX -= app.speed
        app.direction = "right"
    legmove()
def onKeyPress(key):
    if key == "space" and app.numballs > 0:
        shoot(app.direction)
    

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
        if i.centerX > 400 or i.centerX < 0:
            app.bullets.remove(i)
        if i.centerY > 400 or i.centerY < 0:
            app.bullets.remove(i)
cmu_graphics.run()