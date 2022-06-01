from cmu_graphics import *

app.background = "darkBlue"
app.stepsPerSecond = 30
app.movable = Group()
map = Group(Circle(200,200,600,fill=gradient("darkGreen", "green","lightGreen","lightBlue")))
obstaclespawn = Circle(200,200,230,fill=None)
ballspawn = Circle(200,200,130,fill=None)
Explosion = Star(200,200,240,20,fill=gradient("yellow","orange","red","red"),visible=False)
minimap = Rect(330,20,50,50,fill=None,border="black")
icon = Rect(350,40,10,10)
drowning = Rect(0,0,400,400,fill="blue",opacity=40,visible = False)
#player
leftleg = Rect(202,205,3,12,rotateAngle=155)
leftleg.a = 0.5
rightleg = Rect(196,205,3,6,rotateAngle=215)
rightleg.a = -0.5
body = Rect(197.5,195,5,12)
man = Group(Circle(200,190,5),body,Rect(207,190,3,12,rotateAngle=240),
Rect(190,190,3,12,rotateAngle=120),leftleg,rightleg)
#Labels
timer = Label(5,200,30,size=25)
Score = Label(0,200,330,size=20)
winner = Label("Congratulations",200,160,size=30,visible = False)
#variables
app.time = 900
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
app.started = False
app.drowned = False
app.win = False
app.buttons = 0
app.Obstacle = Group()
app.movable.add(map,obstaclespawn,ballspawn,app.collectible,app.bullets,app.Obstacle)
app.topY1 = -400
app.botY1= 800
app.leftX1 = -400
app.leftX2 = 200
app.rightX1 = 200
app.rightX2 = 800
#menu
blue = Rect(0,0,400,400,fill="lightblue")
start = Rect(140,40,120,40,fill="orange",border="black")
Menu = Group(blue, start)
def makeObstacle(difficulty,x,y):
    numrows = difficulty
    numcols = difficulty
    obstacle = makeList(numrows,numcols)
    for row in range(numrows):
        for col in range(numcols):
            bruh = Rect(x + row * 25, y + col*25,20,20,fill="red",border="black")
            app.Obstacle.add(bruh)
            app.buttons += 1
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
        
def adjustBalls():
    for i in range(app.numballs):
        app.balls.add(Circle(215 + 10*i,214,5),
        Circle(213 + 10 * i, 212,1,fill="white"),Circle(218 + 10 * i, 212,1,fill="white"))

def adjustHearts():
    if app.numhearts == 0:
        app.drowned = True
    for i in range(app.numhearts):
        app.hearts.add(Oval(15 + i * 15,15,12,5,rotateAngle=45,fill="red",border="black",borderWidth=1),
        Oval(20 + i * 15,15,12,5,rotateAngle=-45,fill="red",border="black",borderWidth=1))
spawnBalls(20)

def onMousePress(mouseX,mouseY):
    if app.started == False:
        if start.hits(mouseX,mouseY):
            app.started = True
            Menu.clear()
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
    if app.gameOver == False and app.drowned == False and app.win == False and app.started == True:
        if map.hitsShape(body) == True:
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
    if app.gameOver == False and app.drowned == False and app.win == False and app.started == True:
        timer.value = "Island detonation in " + str(app.time // 30)
        Score.value = "Turn off " + str(app.buttons) +" switches"
        if app.time < 1:
            app.gameOver = True
        else:
            app.time -= 1
        icon.centerX = 364 - (app.movable.centerX/22)
        icon.centerY = 54 - (app.movable.centerY/22)
        app.balls.clear()
        adjustBalls()
        app.hearts.clear()
        adjustHearts()
        for bul in app.bullets.children:
            for obstacle in app.Obstacle.children:
                if bul.hitsShape(obstacle) and obstacle.fill == "red":
                    app.bullets.remove(bul)
                    obstacle.fill = "lightgrey"
                    app.buttons -= 1
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
    elif app.gameOver == True:
        Explosion.visible = True
        man.rotateAngle = 90
        Score.visible = False
        timer.visible = False
    elif app.drowned == True:
        man.rotateAngle = 180
        drowning.visible = True
        Score.visible = False
        timer.visible = False
    elif app.win == True:
        winner.visible = True
        Score.visible = False
        timer.visible = False

cmu_graphics.run()