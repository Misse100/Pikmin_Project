# Fill me in!
app.background = "darkBlue"
app.movable = Group()
map = Group(Circle(200,200,600,fill=gradient("lightgrey","lightBlue","darkGreen", "green","lightGreen","lightBlue",start="top")))
obstaclespawn = Circle(200,200,280,fill="aqua")
ballspawn = Circle(200,200,180,fill="blue")
#player
leftleg = Rect(202,205,3,12,rotateAngle=155)
leftleg.a = 0.5
rightleg = Rect(196,205,3,6,rotateAngle=215)
rightleg.a = -0.5
body = Rect(197.5,195,5,12)
man = Group(Circle(200,190,5),body,Rect(207,190,3,12,rotateAngle=240),
Rect(190,190,3,12,rotateAngle=120),leftleg,rightleg)
#variables
app.numballs = 3
app.numhearts = 3
app.hearts = Group()
app.balls = Group()
app.collectible = Group()
app.bullets = Group()
app.direction = "up"
app.bulletspeed = 15
app.speed = 10
app.gameOver = False
app.Obstacle = Group()
app.movable.add(map,obstaclespawn,ballspawn,app.collectible,app.bullets,app.Obstacle)
app.topY1 = -400
app.botY1= 800
app.leftX1 = -400
app.leftX2 = 200
app.rightX1 = 200
app.rightX2 = 800

def makeObstacle(difficulty,x,y):
    place = Group()
    numrows = difficulty
    numcols = difficulty
    obstacle = makeList(numrows,numcols)
    for row in range(numrows):
        for col in range(numcols):
            bruh = Rect(x + row * 25, y + col*25,20,20,fill="lightgrey",border="black")
            app.Obstacle.add(bruh)
            
def spawnObstacles():
    #left
    for i in range(1):
        x = randrange(app.leftX1,app.leftX2)
        y = randrange(app.topY1,app.botY1)
        while map.contains(x,y) == False or obstaclespawn.contains(x,y) == True:
            x = randrange(app.leftX1,app.leftX2)
            y = randrange(app.topY1,app.botY1)
        makeObstacle(1,x,y)
        
        x = randrange(app.leftX1,app.leftX2)
        y = randrange(app.topY1,app.botY1)
        while map.contains(x,y) == False or obstaclespawn.contains(x,y) == True:
            x = randrange(app.leftX1,app.leftX2)
            y = randrange(app.topY1,app.botY1)
        makeObstacle(2,x,y)
        
        x = randrange(app.leftX1,app.leftX2)
        y = randrange(app.topY1,app.botY1)
        while map.contains(x,y) == False or obstaclespawn.contains(x,y) == True:
            x = randrange(app.leftX1,app.leftX2)
            y = randrange(app.topY1,app.botY1)
        makeObstacle(3,x,y)
    #right
    for i in range(1):
        x = randrange(app.rightX1,app.rightX2)
        y = randrange(app.topY1,app.botY1)
        while map.contains(x,y) == False or obstaclespawn.contains(x,y) == True:
            x = randrange(app.rightX1,app.rightX2)
            y = randrange(app.topY1,app.botY1)
        makeObstacle(1,x,y)
        x = randrange(app.rightX1,app.rightX2)
        y = randrange(app.topY1,app.botY1)
        while map.contains(x,y) == False or obstaclespawn.contains(x,y) == True:
            x = randrange(app.rightX1,app.rightX2)
            y = randrange(app.topY1,app.botY1)
        makeObstacle(2,x,y)
        x = randrange(app.rightX1,app.rightX2)
        y = randrange(app.topY1,app.botY1)
        while map.contains(x,y) == False or obstaclespawn.contains(x,y) == True:
            x = randrange(app.rightX1,app.rightX2)
            y = randrange(app.topY1,app.botY1)
        makeObstacle(3,x,y)
spawnObstacles()

def spawnBalls(num):
    #left
    for i in range(num):
        x = randrange(app.leftX1,app.leftX2)
        y = randrange(app.topY1,app.botY1)
        while map.contains(x,y) == False or ballspawn.contains(x,y) == True:
            x = randrange(app.leftX1,app.leftX2)
            y = randrange(app.topY1,app.botY1)
        app.collectible.add(Circle(x,y,5))
    #right
    for i in range(num):
        x = randrange(app.rightX1,app.rightX2)
        y = randrange(app.topY1,app.botY1)
        while map.contains(x,y) == False or ballspawn.contains(x,y) == True:
            x = randrange(app.rightX1,app.rightX2)
            y = randrange(app.topY1,app.botY1)
        app.collectible.add(Circle(x,y,5))
        
def endGame():
    app.gameOver = True

def adjustBalls(balls):
    for i in range(app.numballs):
        app.balls.add(Circle(215 + 10*i,214,4))

def adjustHearts(hearts):
    if app.numhearts == 0:
        endGame()
    for i in range(app.numhearts):
        app.hearts.add(Circle(215 + 10*i,15,4))
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
    if app.gameOver == False:
        if map.containsShape(body) == True:
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
        else:
            app.movable.centerX = 200
            app.movable.centerY = 200
            app.numhearts -= 1
def onKeyPress(key):
    if app.gameOver == False:
        if key == "space" and app.numballs > 0:
            shoot(app.direction)
    

def onStep():
    if app.gameOver == False:
        app.balls.clear()
        adjustBalls(app.numballs)
        app.hearts.clear()
        adjustHearts(app.numhearts)
        for bul in app.bullets.children:
            for obstacle in app.Obstacle.children:
                if bul.hitsShape(obstacle) and obstacle.fill == "lightgrey":
                    app.bullets.remove(bul)
                    obstacle.fill = "red"
                    
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