from cmu_graphics import *

app.background = "darkBlue"
app.stepsPerSecond = 20
app.movable = Group()
map = Group(Circle(200,200,600,fill=gradient("darkGreen", "green","lightGreen","gold")))
obstaclespawn = Circle(200,200,230,fill=None)
ballspawn = Circle(200,200,130,fill=None)
explosion = Group(Star(200,200,240,20,fill=gradient("yellow","orange","red","red")),Label("Bad luck",200,160,size=25))
explosion.visible=False
minimap = Rect(330,20,50,50,fill=None,border="black")
icon = Rect(350,40,10,10)
drowning = Group(Rect(0,0,400,400,fill="blue",opacity=40),Label("Maybe try breathing air next time",200,160,size=25))
drowning.visible = False
Reset = Label("Press Space to go back to menu",200,300,size=20,visible = False)
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
score = Label(0,200,330,size=20)
winner = Group(Label("Congratulations",200,120,size=30),Star(70,70,50,15,fill=gradient("lime","yellow")),Star(340,70,50,15,fill=gradient("lime","yellow")))
winner.visible = False
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
app.obstacle = Group()
app.movable.add(map,obstaclespawn,ballspawn,app.collectible,app.bullets,app.obstacle)
app.topY1 = -400
app.botY1= 800
app.leftX1 = -400
app.leftX2 = 200
app.rightX1 = 200
app.rightX2 = 800
#menu
blue = Rect(0,0,400,400,fill="lightblue")
start = Rect(140,60,120,40,fill="orange",border="black")
Menu = Group(blue, start,Label("START",200,80,size=25),Label("Disaster Survival",200,30,size=30,bold=True),
Label("Use WASD to move across the island",200,260,size=20),Label("Use the ball people to turn off the bomb",200,300,size=20),
Label("Shoot the switches with SPACE",200,340,size=20),Label("Try not to drown :)",200,380,size=18),
Rect(302,205,3,12,rotateAngle=155),Rect(296,205,3,12,rotateAngle=215),
Rect(297.5,195,5,12),Circle(300,190,5),Rect(307,190,3,12,rotateAngle=240),Rect(290,190,3,12,rotateAngle=120),
Rect(80,190,20,20,fill="red",border="black"),Circle(200,202,5),
Circle(198, 200,1,fill="white"),Circle(203, 200,1,fill="white"))
def makeObstacle(difficulty,x,y):
    numrows = difficulty
    numcols = difficulty
    obstacle = makeList(numrows,numcols)
    for row in range(numrows):
        for col in range(numcols):
            bruh = Rect(x + row * 25, y + col*25,20,20,fill="red",border="black")
            app.obstacle.add(bruh)
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
            Menu.visible = False
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
    if app.gameOver == False and app.drowned == False and app.win == False and app.started == True:
        if key == "space" and app.numballs > 0:
            shoot(app.direction)
    if app.gameOver == True or app.drowned == True or app.win == True:
        if key == "space":
            app.gameOver = False 
            app.drowned = False
            app.win = False 
            app.started = False
            Menu.visible = True
            explosion.visible = False
            man.rotateAngle = 0
            drowning.visible = False
            app.numballs = 3
            app.numhearts = 3
            app.collectible.clear()
            spawnBalls(20)
            app.obstacle.clear()
            app.buttons = 0
            spawnObstacles()
            timer.visible = True
            score.visible = True
            app.time = 900
            app.movable.centerX = 200
            app.movable.centerY = 200
            Reset.visible = False
            winner.visible = False
def onStep():
    if app.gameOver == False and app.drowned == False and app.win == False and app.started == True:
        if app.buttons == 0:
            app.win = True
        timer.value = "Island detonation in " + str(app.time // 20)
        score.value = "Turn off " + str(app.buttons) +" switches"
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
            for obstacle in app.obstacle.children:
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
        explosion.visible = True
        man.rotateAngle = 90
        score.visible = False
        timer.visible = False
        Reset.visible = True
    elif app.drowned == True:
        man.rotateAngle = 180
        drowning.visible = True
        score.visible = False
        timer.visible = False
        Reset.visible = True
    elif app.win == True:
        winner.visible = True
        score.visible = False
        timer.visible = False
        Reset.visible = True


cmu_graphics.run()