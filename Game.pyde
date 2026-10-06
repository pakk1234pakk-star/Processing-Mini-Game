add_library('minim')


def setup():
    size(500,500)
    global cat,x,y,bg,speed1,speed2,speed3,speed4,box2,key1,key2,randomFood,food,startTime,win,getFood,stageNum,catbox,cat3,catWin,timeIsUp,time,true
    global noFood
    global inst,arrow,arrow2,arrow3
    global timeCat,cTime
    global modeGreen
    global score
    global again,exit_X
    again=loadImage("again.png")
    exit_X=loadImage("exit_X.png")

    #box
    global x1,x2,x3,y1,y2,y3
    global b50,bspeed1,bspeed2,bspeed3
    timeCat=loadImage("timeCat.png")
    inst=loadImage("inst.png")
    arrow=loadImage("arrow.png")
    arrow2=loadImage("arrow2.png")
    arrow3=loadImage("arrow3.png")
    cat = loadImage("cat.png")
    bg=loadImage("bg.png")
    box2=loadImage("box2.png")
    key1=loadImage("key.png")
    key2=loadImage("key2.png")
    food=loadImage("catFood.png")
    win=loadImage("win.png")
    cat3= loadImage("cat3.png")
    modeGreen=0
    x=110
    y=390
    speed1=10
    speed2=10
    speed3=10
    speed4=10
    randomFood=int (random(1,6))
    getFood=0
    stageNum=-1
    catbox=0
    catWin=0
    noFood=0
#box---------------------------------------------------------------------------------------------------------------------
    x1=160
    x2=245
    x3=60
    y1=395
    y2=290
    y3=220
    b50=50
    #right
    bspeed1=1
    #in the room(3=max. speed)
    bspeed2=1
    #left
    bspeed3=1
#time and score---------------------------------------------------------------------------------------------------------------------
    timeIsUp=0
    time=0
    startTime=0
    true=0
    cTime=0
    
    global coin,visible_coin1,visible_coin2,visible_coin3
    score=0
    coin=loadImage("coin.png")
    visible_coin1=True
    visible_coin2=True
    visible_coin3=True

#mode---------------------------------------------------------------------------------------------------------------------
    global mode_x,mode_a
    mode_x=[]
    mode_x.append(50)
    mode_x.append(200)
    mode_x.append(350)
    mode_a=[]
    mode_a.append("  easy")   
    mode_a.append("normal")
    mode_a.append("  hard")
#the mini game(door)---------------------------------------------------------------------------------------------------------------------
    global password,inputPassword,decimal_places,Digits
    global password1,password2,password3
    global st,nd,rd
    global windoor
    windoor=False

    password1=int(random(0,10))
    password2=int(random(0,10))
    password3=int(random(0,10))
    st=0
    nd=0
    rd=0

    inputPassword=[]
    decimal_places =True
    Digits=0
#the mini game(paper)---------------------------------------------------------------------------------------------------------------------
    global paper
    paper=loadImage("paper.png")
#music---------------------------------------------------------------------------------------------------------------------
    global minim, player 
    minim = Minim(this)    
    player = minim.loadFile("song.mp3")
    global nosound,speaker
    nosound=loadImage("nosound.png")
    speaker=loadImage("speaker.png")
    global stop_or_resume
    stop_or_resume=10

#DRAW========================================================================

def draw():
    global c,b,getFood,x,y,z,stageNum,g,catbox,catWin
    global speed1,speed2,speed3,speed4
    global x1,x2,x3,y1,y2,y3,b50,bspeed1,bspeed2,bspeed3
    global windoor
    
#time---------------------------------------------------------------------------------------------------------------------
    global startTime,timeIsUp,time,true,cTime
    if stageNum==2 and startTime==0:
        startTime=millis()
    if startTime != 0:
        time=(millis()-startTime)/1000
    if time>=60:
        cTime=10
    print("Time="+str(time))
    
        


#image---------------------------------------------------------------------------------------------------------------------
    image(bg,0,0,width,height)
    image(cat,x,y,25,50)
    image(box2,x1,y1,b50,b50)
#play again(button)---------------------------------------------------------------------------------------------------------------------
    fill(255)
    ellipse(450,50,50,50)
    image(again,425,25,50,50)
    if dist(450, 50, mouseX, mouseY) < 50/2 and stageNum==2:
        stopminim()
        fill(255)
        textSize(20)
        text("play again",400,100)
        

#coin---------------------------------------------------------------------------------------------------------------------
    global visible_coin1
    global visible_coin2
    global visible_coin3
    global score
    

    #coin1(down)
    if visible_coin1==True:
        image(coin,100,300,25,25)
    if x>=90 and x<90+25 and y>=270 and y<=310 and visible_coin1==True:
        visible_coin1=False
        score=score+1
    #coin2(room)
    if visible_coin2==True:
        image(coin,350,245,25,25)
    if x>=340 and x<340+25 and y>=215 and y<215+40 and visible_coin2==True:
        visible_coin2=False
        score=score+1
    #coin3(up)
    if visible_coin3==True:
        image(coin,178,215,25,25)    
    if x>=168 and x<168+25 and y>185 and y<185+40 and visible_coin3==True:
        visible_coin3=False
        score=score+1
        
#boxMovement---------------------------------------------------------------------------------------------------------------------

    #box1
    if y1>=395:
        bspeed1=-bspeed1
        y1 = 394
    if y1<=170:
        bspeed1=-bspeed1
        y1 = 171
    if y1<=395 and y1>=170:
        y1=y1-bspeed1

    #box2
    #right:x2=380,245;or:330
    image(box2,x2,y2,b50,b50)
    if x2<=380 and x2>=245:
        x2=x2+bspeed2
    if x2>=380:
        bspeed2= -bspeed2
        x2 = 379
    if x2<=245:
        bspeed2= -bspeed2
        x2 = 246
    #box3
    #left:60,200;or:100
    image(box2,x3,y3,b50,b50)
    if x3<=200 and x3>=60:
        x3=x3+bspeed3
    if x3>=200:
        bspeed3= -bspeed3
        x3 = 199
    if x3<=60:
        bspeed3= -bspeed3
        x3 =61

#hints picture---------------------------------------------------------------------------------------------------------------------
    image(key2,290,60,200,200)
    image(key2,260,60,200,200)
    image(key2,380,60,200,200)
    image(key2,50,10,200,200)
    image(key2,200,20,200,200)

#mini game(paper)---------------------------------------------------------------------------------------------------------------------
    image(paper,380,340,55,40)
    if x>=380 and x<420 and y>=310 and y<360:
        fill(255)
        ellipse(400,350,30,30)
        fill(0)
        textSize(20)
        text("R",395,358)
    if x>=380 and x<420 and y>=310 and y<360 and key == 'r' :
        drawPaper()

#hints-food---------------------------------------------------------------------------------------------------------------------
    print randomFood
    #key1
    if x>69 and x<91 and y==170 and randomFood==1 and key=='s':
        getFood=10  
        drawWin()
    elif x>69 and x<91 and y==170 and key=='s'and randomFood>1:
        drawNth()
        
    #key2  
    if x>209 and x<221 and y==170 and randomFood==2 and key=='s':
        getFood=10
        drawWin()

    elif x>209 and x<221 and y==170 and key=='s' and randomFood!=2:
        drawNth()
    #key3
    if x>279 and x<291 and y<220 and randomFood==3 and key=='s':
        getFood=10
        drawWin()

    elif x>279 and x<291 and y<220 and randomFood!=3 and key=='s':
        drawNth()
    #key4
    if x>309 and x<321 and y<220 and randomFood==4 and key=='s':
        getFood=10
        drawWin()
        

    elif x>309 and x<321 and y<220 and randomFood!=4 and key=='s':
        drawNth()
    #key5
    if x>389 and y<220 and randomFood==5 and key=='s':
        getFood=10
        drawWin()
    elif x>389 and y<220 and randomFood!=5 and key=='s':
        drawNth()
#Hints-food(remind player presse s to search)---------------------------------------------------------------------------------------------------------------------     
    if x>69 and x<91 and y==170:
        drawRemind_S(85,170,80,178)
    if x>209 and x<221 and y==170:
        drawRemind_S(233,170,228,178)
    if x>279 and x<291 and y<220:
        drawRemind_S(295,220,290,228)
    if x>309 and x<321 and y<220:
        drawRemind_S(327,220,322,228)
    if x>389 and y<220:
        drawRemind_S(415,220,410,228)
        
#DOOR(remind player presse d to leave the door)---------------------------------------------------------------------------------------------------------------------     
    if x>89 and x<141 and y==390:
        fill(255)
        ellipse(135,430,30,30)
        fill(0)
        textSize(20)
        text("D",130,438)
#WIN DOOR(game)---------------------------------------------------------------------------------------------------------------------     
    if x>89 and x<141 and y==390 and key=='d' and getFood==10:
        windoor=True
        drawDoorGame()

#Time&Score------------------------------------------------------------------------------------------------------------
    #Time
    fill(300,100,10)
    textSize(30)
    text("Time:"+str(time)+"s",10,30)
    fill(300,100,10)

    #Score
    fill(300,100,10)
    textSize(30)
    text("Score:"+str(score),10,60)

    if cTime == 10:
        drawTime()
#WIN DOOR---------------------------------------------------------------------------------------------------------------------     

    if catWin==10:
        drawWin2()
    #'d' the DOOR without obtaining the food  
    if x>89 and x<141 and y==390 and key=='d' and getFood!=10:
        drawNoFood()
        
#START---------------------------------------------------------------------------------------------------------------------
    if stageNum ==0:
        drawStart1()
    if stageNum==1:
        drawStart2()
    if stageNum==-1:
        drawMode()
#prevent cat walk through the wall---------------------------------------------------------------------------------------------------------------------
    #left wall
    if x<71:
        speed4=0
    elif x>=71:
        speed4=10
    #up wall
    if y<180:
        speed1=0
    elif y>=180:
        speed1=10
        
    #middle up wall(->)
    if x>215 and y<260:
        speed3=0
    elif x<=215 or y>=260:
        speed3=10
        
    #midle up wall (<-)
    if x==280 and y>110 and y<261:
        speed4=0
    elif x>280 and y>110 and y<261:
        speed4=10
        
    #middle wall middle up    
    if x>220 and x<280 and y==260:
        speed1=0
    elif x<=220 and x>=280 and y<260:
        speed1 = 10

    
    if x>215 and y>300 and x<300:
        speed3=0
    elif x<=215 and y<=300 and x>=300:
        speed3=10
    
    #room table up
    if x>220 and y>300 and x<300:
        speed2=0
    elif x<220 or y<300 or x>300:
        speed2=10
    
    #room table right
    if x>280 and x<310 and y>310:
        speed4=0
    elif x<=280 and x>=310 and y<=310:
        speed4=10
    
    #room down wall
    if x>309 and y==340:
        speed2=0
    elif x<=309 and y<340:
        speed=10
        
    #right wall
    if x==400 and y>170 and y<341:
        speed3=0
    elif x<400 and x>250 and y>169 and y<341:
        speed3=10
    #down wall
    if y==390:
        speed2=0
    elif y<390 and x<200:
        speed2=10
#box games over--------------------------------------------------------------------------------------------------------

    #box1
    #if x>=150 and x<=150+50 and y>=310 and y<=310+50:
    #    catbox=10
    if x>=150 and x<=150+50 and y>= y1-10 and y<=y1-10+50:
        catbox=10

    #box2
    #if x>=320 and x<=320+50 and y>=280 and y<=280+50:
        #catbox=10
    if x>=x2-10 and x<=x2-10+50 and y>=280 and y<=280+50:
        catbox=10

    #box3
    #if x>=90 and x<=90+50 and y>=210 and y<=210+50:
        #catbox=10
    if x>=x3-10 and x<=x3-10+50 and y>=210 and y<=210+50:
        catbox=10

        
#box games over--------------------------------------------------------------------------------------------------------
       
#prevent the cat move before game start--------------------------------------------------
#prevent the boxes move after game----------------------------------------------------------------------------------------------------
    if stageNum<2:
        x=110
        y=390
        x1=160
        x2=245
        x3=60
        y1=395
        y2=290
        y3=220

        
        
    #games over   
    if catbox==10:
        drawBox()
#music------------------------------------------------------------------------------------------------------------
    if stop_or_resume == 10 and stageNum>=2 and catbox!=10 and catWin!=10 and cTime!=10:
        fill(255)
        ellipse(390, 50, 50, 50)
        image(speaker, 368, 28, 45, 50)
        player.play()
    elif stop_or_resume == -10 and stageNum>=2 and catbox!=10 and catWin!=10 and cTime!=10:
        fill(255)
        ellipse(390, 50, 50, 50)
        image(nosound, 368, 28, 30, 45)
        strokeWeight(5)
        line(372, 30, 405, 70)
        strokeWeight(1)
        if player.isPlaying():
            player.pause()
#------------------------------------------------------------------------------------------------------------
        
    #print mouseX,mouseY
    #print x,y
    print password1,password2,password3
    print inputPassword
    #print windoor
    print("catbox="+str(catbox))
    print("catWin="+str(catWin))
    print("cTime="+str(cTime))

    
    
    





    
def keyPressed():
    global x,y,stageNum,catWin
    global speed1,speed2,speed3,speed4
    global bspeed1, bspeed2, bspeed3 
    if key == CODED:
        if keyCode == UP:
            y=y-speed1
        elif keyCode == DOWN:
            y=y+speed2
        elif keyCode == RIGHT:
            x=x+speed3
        elif keyCode == LEFT:
            x=x-speed4
    if key == 'g':
        stageNum=stageNum+1
    if catbox==10 and (key == 'a'):
        setup()
    if catWin==10 and (key =='a'):
        setup()
    if cTime==10 and (key =='a'):
        setup()

def drawNth():
    fill(255)
    rect(10,350,480,300)
    image(cat,20,360,120,150)
    fill(0)
    textSize(30)
    text("zi maa",160,378)
    textSize(20)
    text("meow(nothing here)",160,425)
    
def drawWin():
    fill(255)
    rect(10,350,480,300)
    image(cat,20,360,120,150)
    fill(0)
    textSize(30)
    text("zi maa",160,378)
    textSize(20)
    image(food,160,390,70,100)
    text("obtained",250,450)
    textSize(40)
    fill(300,100,100)

def drawWin2():
    global time
    background(255)
    image(win,-70,100)
    textSize(70)
    fill(300,100,100)
    text("YOU WIN!",125,100)
    textSize(40)
    # fill(0)
    # text("presse 'a' to play again",10,450)
    # textSize(30)
    text("score="+str(score),230,490)
    
    #try again button
    fill(0,200,50)
    stroke(40)
    ellipse(180,268,100,100)
    image(again,120,220,120,100)
    #close the game button
    fill(200,0,50)
    ellipse(350,268,100,100)
    image(exit_X,293,227,120,80)
    stroke(20)
    stopminim()

def drawStop():
    speed1=0
    speed2=0
    speed3=0
    speed4=0
def drawStart1():
    background(255)
    image(cat,175,175,175,250)
    textSize(40)
    fill(0)
    text("Instruction:",10,40)
    textSize(20)
    text("Move cat when you presses the arrow keys",10,80)
    text("presse 's' to search",10,100)
    text("presse 'd' to leave the house after obtaining food",10,120)
    text("presse 'r' to read the paper",10,140)
    fill(300,100,100)
    text("time limitation:60s",10,160)
    textSize(40)
    fill(0)
    text("presse 'g' to next page",50,450)
def drawStart2():
    background(255)
    image(inst,10,10,480,480)
    #BOX
    image(arrow,250,300,100,50)
    fill(255)
    rect(210,150,220,50)
    fill(0)
    textSize(20)
    text("place to search ",220,175)
    #hints
    image(arrow2,95,155,100,50)
    fill(255)
    rect(210,240,220,50)
    fill(0)
    text("Don't touch the box",220,270)

    #door
    image(arrow3,100,360,50,100)
    fill(255)
    rect(20,350,250,50)
    fill(0)
    text("place to leave the house",30,390)
    textSize(40)
    fill(255)
    text("press 'g' to start",90,50)
    
    #papper
    image(paper,380,340,55,40)
    image(arrow,300,350,100,50)
    fill(255)
    rect(210,390,220,50)
    fill(0)
    textSize(20)
    text("press 'r' to read",220,420)


    
def drawBox():
    global time
    background(255)
    image (box2,90,168)
    image(cat3,170,200,180,100)
    textSize(30)
    text("Opps!",240,110)
    text("It seems that zi maa",130,150) 
    text("is attracted to the Carton Box",50,190)
    fill(0)
    textSize(50)
    text("Games Over",150,50)
    textSize(30)
    text("score="+str(score),230,490)
    #restart button
    fill(0,200,50)
    stroke(40)
    ellipse(180,400,100,100)
    image(again,120,352,120,100)
    #close the game button
    fill(200,0,50)
    ellipse(350,400,100,100)
    image(exit_X,293,359,120,80)
    stopminim()
def drawNoFood():
    fill(255)
    rect(10,350,480,300)
    image(cat,20,360,120,150)
    fill(0)
    textSize(30)
    text("zi maa",160,378)
    textSize(20)
    text("meow",160,425)
    text("(i can't leave this house without",160,445)
    text(" food)",160,465)
def drawTime():
    global timeCat
    background(255)
    image(timeCat,130,150,250,150)
    textSize(50)
    fill(0)
    text("Games Over",100,50)
    fill(300,100,100)
    text("Time Out",135,100)
    fill(0)
    textSize(30)
    text("score="+str(score),210,410)
    
    #try again button
    fill(0,200,50)
    stroke(40)
    ellipse(180,340,100,100)
    image(again,120,292,120,100)
    #close the game button
    fill(200,0,50)
    ellipse(350,340,100,100)
    image(exit_X,293,299,120,80)
    stopminim()
def drawMode():
    #background(0)
    image(bg,0,0,500,500)
    for i in range(len(mode_x)):
        fill(255)
        rect(100,mode_x[i],300,100)
        fill(0)
        textSize(50)
        text(mode_a[i],175,mode_x[i]+60)
        fill(300,100,100)
        textSize(30)
        text("presse 'g' to next page",80,480)
    if modeGreen ==1:
        fill(0,40,0,100)
        rect(100,mode_x[0],300,100)
    if modeGreen ==2:
        fill(0,40,0,100)
        rect(100,mode_x[1],300,100)
    if modeGreen ==3:
        fill (0,40,0,100)
        rect(100,mode_x[2],300,100)
        
def mousePressed():
    global bspeed1, bspeed2, bspeed3
    global mode_x
    global stageNum
    global modeGreen
    global catbox,catWin,cTime
#music------------------------------------------------------------------------
    global stop_or_resume
    if dist(390, 50, mouseX, mouseY) < 50/2 and stageNum==2:
        stop_or_resume=-stop_or_resume
        
#play again(during the game)------------------------------------------------------------------------
    if dist(450, 50, mouseX, mouseY) < 50/2 and stageNum==2:
        if player.isPlaying():
            player.pause()
            player.rewind() 
        setup()
#win page------------------------------------------------------------------------
    #try again button(win page)
    if dist(180, 268, mouseX, mouseY) < 100/2 and catWin==10:
        setup()
    #close the game button(win page)
    if dist(350, 268, mouseX, mouseY) < 100/2 and catWin==10:
        exit()
#game over(time) page------------------------------------------------------------------------
    #try again button
    if dist(180, 340, mouseX, mouseY) < 100/2 and cTime==10:
        setup()
    #close the game button
    if dist(350, 340, mouseX, mouseY) < 100/2 and cTime==10:
        exit()
#game over(box) page------------------------------------------------------------------------
    #try again button
    if dist(180, 400, mouseX, mouseY) < 100/2 and catbox==10:
        setup()
    #close the game button
    if dist(350, 400, mouseX, mouseY) < 100/2 and catbox==10:
        exit()
#Mode------------------------------------------------------------------------
    for i in range(len(mode_x)):
        if mode_x[i] <= mouseY and  mode_x[i] + 100 >= mouseY and 100 <= mouseX and  400 >= mouseX and stageNum==-1:
            if i == 0:
                bspeed1=1
                bspeed2=1
                bspeed3=1
                modeGreen=1
            elif i == 1:
                bspeed1=3
                bspeed2=2
                bspeed3=3
                modeGreen=2
            elif i == 2:
                bspeed1=5
                bspeed2=3
                bspeed3=5
                modeGreen=3
            break
#the mini game(door)---------------------------------------------------------------------------------------------------------------------
    global inputPassword,Digits
    global st,nd,rd
    global decimal_places
    #del
    if windoor==True:
        if mouseX>25 and mouseX<25+50 and mouseY>400 and mouseY<400+50:
            inputPassword = []
            Digits=0
            decimal_places=True
    #add number        
    if windoor==True:
        if decimal_places == True:
            drawAddNum(125,200,125,200,7)
            drawAddNum(125,200,225,300,4)                                
            drawAddNum(125,200,325,400,1)
            drawAddNum(225,300,125,200,8)       
            drawAddNum(225,300,225,300,5)
            drawAddNum(225,300,325,400,2)
            drawAddNum(225,300,425,500,0)     
            drawAddNum(325,400,125,200,9)
            drawAddNum(325,400,225,300,6)                                
            drawAddNum(325,400,325,400,3)
                            
#---------------------------------------------------------------------------------
                
    if Digits==1:
        drawDigits1(125,200,125,200,7)
        drawDigits1(125,200,225,300,4)
        drawDigits1(125,200,325,400,1)
        drawDigits1(225,300,125,200,8)
        drawDigits1(225,300,225,300,5)
        drawDigits1(225,300,325,400,2)
        drawDigits1(225,300,425,500,0)
        drawDigits1(325,400,125,200,9)
        drawDigits1(325,400,225,300,6)
        drawDigits1(325,400,325,400,3)

#---------------------------------------------------------------------------------
                
    if Digits==2:
        drawDigits2(125,200,125,200,7)
        drawDigits2(125,200,225,300,4)
        drawDigits2(125,200,325,400,1)
        drawDigits2(225,300,125,200,8)
        drawDigits2(225,300,225,300,5)
        drawDigits2(225,300,325,400,2)
        drawDigits2(225,300,425,500,0)
        drawDigits2(325,400,125,200,9)
        drawDigits2(325,400,225,300,6)
        drawDigits2(325,400,325,400,3)

#---------------------------------------------------------------------------------
                
    if Digits==3:
        drawDigits3(125,200,125,200,7)
        drawDigits3(125,200,225,300,4)
        drawDigits3(125,200,325,400,1)
        drawDigits3(225,300,125,200,8)
        drawDigits3(225,300,225,300,5)
        drawDigits3(225,300,325,400,2)
        drawDigits3(225,300,425,500,0)
        drawDigits3(325,400,125,200,9)
        drawDigits3(325,400,225,300,6)
        drawDigits3(325,400,325,400,3)            
def drawDoorGame():
    global inputPassword
    global decimal_places
    global catWin
    global bg
    image (bg,0,0,width,height)
    # background(255)
    fill(200)
    noStroke()
    rect(100,0,325,500)
    #input box
    fill(255)
    rect(125,25,275,75)
    fill(0)
    for i in range(len(inputPassword)):
        text(str(inputPassword[i]),150+50*i,75)
    print inputPassword
    #number box
    drawNumberBox(125,125,"7")
    drawNumberBox(125,225,"4")
    drawNumberBox(125,325,"1")
    drawNumberBox(225,125,"8")
    drawNumberBox(225,225,"5")
    drawNumberBox(225,325,"2")
    drawNumberBox(225,425,"0")
    drawNumberBox(325,125,"9")
    drawNumberBox(325,225,"6")
    drawNumberBox(325,325,"3")
    #3-digits
    if Digits ==3:
        decimal_places = False
    #correct answer
    if password1==st and password2==nd and password3==rd:
        print ("correct!")
        catWin=10
    else:
        print ("incorrect!")

        
    # print decimal_places
    # print Digits
    # print st,nd,rd
    #del button
    fill(255)
    stroke(10)
    rect(25,400,50,50)
    fill(0)
    rect(30,413,25,25)
    triangle(55,413,55,438,70,425.5)
    fill(255)
    ellipse(40,425,20,20)
    fill(0)
    textSize(15)
    text("X",36,430)

    
    
def drawNumberBox(x,y,num):
    textSize(50)
    fill(255)
    rect(x,y,75,75)
    fill(0)
    text(num,x+25,y+50)
def drawAddNum(addNum_x1,addNum_x2,addNum_y1,addNum_y2,Num):
    global Digits
    for i in range(1):
        if mouseX>addNum_x1 and mouseX<addNum_x2 and mouseY>addNum_y1 and mouseY<addNum_y2:
            inputPassword.append(Num)
            Digits=Digits+1
def drawDigits1(digits_x1,digits_x2,digits_y1,digits_y2,Num):
    global st
    for i in range(1):
            if mouseX>digits_x1 and mouseX<digits_x2 and mouseY>digits_y1 and mouseY<digits_y2:
                st=Num
def drawDigits2(digits_x1,digits_x2,digits_y1,digits_y2,Num):
    global nd
    for i in range(1):
            if mouseX>digits_x1 and mouseX<digits_x2 and mouseY>digits_y1 and mouseY<digits_y2:
                nd=Num
def drawDigits3(digits_x1,digits_x2,digits_y1,digits_y2,Num):
    global rd
    for i in range(1):
            if mouseX>digits_x1 and mouseX<digits_x2 and mouseY>digits_y1 and mouseY<digits_y2:
                rd=Num

def drawPaper():
    global password1,password2,password3
    print ("the password="+str(password1)+str(password2)+str(password3))
    image(paper,-50,20)
    fill(0)
    textSize(35)
    text("DOOR PASSWORD",125,120)
    textSize(100)
    text(str(password1)+str(password2)+str(password3),172,250)
def drawRemind_S(ex,ey,tx,ty):
    fill(255)
    ellipse(ex,ey,30,30)
    fill(0)
    textSize(20)
    text("s",tx,ty)
    
def stopminim():
    player.close()
    minim.stop()
