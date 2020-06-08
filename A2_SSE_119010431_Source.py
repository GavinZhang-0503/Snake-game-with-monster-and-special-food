import turtle
import time
import copy
from random import randrange

def generatefood():
    global food
    foodall=[1,2,3,4,5,6,7,8,9]
    foodx=[]
    foody=[]
    same=False
    while True:
        if len(foodx)>=9:
            break
        x=randrange(-200,200,10)
        if foodx==[]:
            foodx.append(x)
        else:
            same=False
            for n in foodx:
                if n==x:
                    same=True
            if same==False:
                foodx.append(x)
            else:
                continue
            
    while True:
        if len(foody)>=9:
            break
        y=randrange(-200,200,10)
        if foody==[]:
            foody.append(y)
        else:
            same=False
            for n in foody:
                if n==y:
                    same=True
            if same==False:
                foody.append(y)
            else:
                continue
    food=[foodx,foody,foodall]
    print(food)
              
def showfood():
    global food
    for i in range(len(food[2])):
        position=turtle.pos()
        turtle.up()
        turtle.goto(food[0][i],food[1][i])
        turtle.down()
        turtle.write(food[2][i],align="left")
        turtle.up()
        turtle.goto(position)
        turtle.down()

def square(x,y,size,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()

def initialize():
    global snake
    global heading
    global food
    global monster
    global contnum
    global starttime
    contnum=0
    turtle.screensize(500,500)
    turtle.clear()
    monster=[0,0]
    monster[0]=randrange(-6,-4)*10
    monster[1]=randrange(-6,-4)*10
    square(monster[0],monster[1],10,"blue")
    
    snake=[[0,0],[0,10],[0,20],[0,30],[0,40]]
    square(snake[-1][0],snake[-1][1],10,"red")
    for body in snake[-2::-1]:
        square(body[0],body[1],10,"black")
    heading=[0,10]
    turtle.hideturtle()
    turtle.tracer(False)
    generatefood()
    showfood()
    position=turtle.pos()
    turtle.up()
    turtle.goto(-250,100)
    turtle.down()
    turtle.write("welcome to to the 'snake' game. \n in this game, you can use the 4 arrow keys to control the snake to move towards four directions. \n There will be a monster moving at the same direction of your snake.\n your goal is to eat all the food to get the victory. \n once you consume a food, your body will become longer for the number of the food. \n if you crash with the monster or move out of the screen, you fail.\n the screen is 500X500.\n Have fun!\n Clicl the screen to start the game",align="left")
    turtle.up()
    turtle.goto(position)
    turtle.down()
    starttime=time.time()
    turtle.listen()
    turtle.onkey(lambda: changedirection(10, 0), "Right")  # 右
    turtle.onkey(lambda: changedirection(-10, 0), "Left")  # 左
    turtle.onkey(lambda: changedirection(0, 10), "Up")  # 上
    turtle.onkey(lambda: changedirection(0, -10), "Down")  # 下
    turtle.onkey(initialize,"r")
    turtle.onscreenclick(main,btn=1,add=None)
    
def changedirection(x,y):
    heading[0]=x
    heading[1]=y

def monstermove():
    global heading
    global monster
    x=randrange(-10,20,10)
    y=randrange(-10,20,10)
    if (monster[0]<-250):
        monster=[-250,monster[1]]      
    elif monster[0]>250:
        monster=[250,monster[1]]
    elif monster[1]<-250:
        monster=[monster[0],-250]
    elif monster[1]>250:
        monster=[monster[0],250]
    else:
        monster=[monster[0]+x,y]
    
    turtle.update()

def UI():
    global currenttime
    contact()
    position=turtle.pos()
    turtle.up()
    turtle.goto(0,250)
    turtle.down()
    turtle.write("contact="+str(contnum)+","+"Time = "+str(int(currenttime-starttime)),align="center")
    turtle.up()
    turtle.goto(position)
    turtle.down()

def contact():
    global monster
    global snake
    global contnum
    for body in snake:
        if (body[0]==monster[0]) and (body[1]==monster[1]):
            contnum+=1
        else:
            pass
    return(contnum)

def failcheck():
    global head,monster
    if (head[0]<-250)or (head[1]<-250) or (head[0]>250) or (head[1]>250)or(head==monster):
        turtle.down()
        turtle.write("Game over,Press'R'to restart")
        return False

def wincheck():
    global food
    xwin=False
    ywin=False
    win=False
    for x in food[0]:
        if x==1000:
            xwin=True
        else: 
            xwin=False
            break
    for y in food[1]:
        if y==1000:
            ywin=True
        else:
            ywin=False
            break
    if (xwin==True) and (ywin==True):
        win=True
    else:
        win=False
    return win

def foodcheck():
    global head,food
    global onefood
    isfood=False
    isfoodx=False
    isfoody=False
    onefood=[]
    for x in food[0]:
        if head[0]==x:
            isfoodx=True
            break
        else:
            isfoody=False
    for y in food[1]:
        if head[1]==y:
            isfoody=True
            break
        else: isfoody=False
    if (isfoodx==True) and (isfoody==True):
        isfood=True
        onefood.append(x)
        onefood.append(y)
    return isfood

def pausecheck():
    global nowpause
    if nowpause==False:
        nowpause=True
    else: nowpause=False
    return nowpause

def snakemove():
    global snake,head,monster
    global heading
    global food,onefood,remain,remain1
    global monster
    global currenttime
    global starttime
    global nowpause
    currenttime=time.time()
    head=snake[-1]
    
    if failcheck()==False:
        return
    if wincheck()==True:
        turtle.down
        turtle.write("congratulation,you win!!! if you want to restart, please press'R'")
        return
    if foodcheck()==True:
        remain=food[0].index(onefood[0])
        food[0][remain]=1000
        food[1][remain]=1000
        remain=food[2][remain]
        remain1 = remain +remain1
        print(food)
        
    if remain1==0:
        head=copy.deepcopy(snake[-1])
        head=[head[0]+heading[0],head[1]+heading[1]]
        snake.append(head)
        snake.pop(0)
    elif remain1>0:
        head=copy.deepcopy(snake[-1])
        head=[head[0]+heading[0],head[1]+heading[1]]
        snake.append(head)
        remain1-=1
    
    turtle.clear()
    
    showfood()
    square(snake[-1][0],snake[-1][1],10,"red")
    for body in snake[-2::-1]:
        square(body[0],body[1],10,"black")
    square(monster[0],monster[1],10,"blue")
    UI()
    
    turtle.update()
    turtle.ontimer(monstermove,randrange(10,310))
    turtle.ontimer(snakemove,300) 
    
def main(x,y):
    turtle.clear()
    snakemove()
    
remain1=0
remain=0

initialize()
turtle.done()