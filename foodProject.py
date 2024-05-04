from pygame import *
import random

init()
width=1398
height=766
screen = display.set_mode((width,height))

clock = time.Clock()
running = True
mx=0
my=0
button=0
typ=""
ingMem=[]
ing=""

#windows
infoBox=False
dialog=False

font = font.SysFont("Comic Sans MS", 50)

page=3;

#the pic with 2 at the end is the version that is being clicked

#title page
titlePage=image.load("img/1.png")
titlePage= transform.scale(titlePage, (width,height))



buttonInfox1=width/16
buttonInfox2=width/2
buttonInfoy1=height/9
buttonInfoy2=height/5



buttonStartx1=width/16
buttonStartx2=width/2
buttonStarty1=height/3.6
buttonStarty2=height/2.52



buttonQuitx1=width/16
buttonQuitx2=width/2
buttonQuity1=height/2.07
buttonQuity2=height/1.59

infoWindow=image.load("img/18.png")
infoWindow= transform.scale(infoWindow, (width,height))





#kitchen background
kitchenBackground=image.load("img/0.png")
kitchenBackground= transform.scale(kitchenBackground, (width,height))
kitchenBackground2=image.load("img/0.png")
kitchenBackground2= transform.scale(kitchenBackground2, (width,height))
kitchen2=image.load("img/7.png")
kitchen2= transform.scale(kitchen2, (width,height))

#some character emotion images randomized
character=image.load("img/7.png")
character= transform.scale(character, (width,height))

dialogBox=image.load("img/12.png")#apperar in 135
dialogBox= transform.scale(dialogBox, (width,height))

leftArrow=image.load("img/20.png")#in all 12345
leftArrow= transform.scale(leftArrow, (width,height))
leftArrow2=image.load("img/20.png")#in all 12345
leftArrow2= transform.scale(leftArrow2, (width,height))

leftArrowx1=width/174.7
leftArrowx2=width/14.9
leftArrowy1=height/1.21
leftArrowy2=height/1.04

rightArrow=image.load("img/15.png")#in 135
rightArrow= transform.scale(rightArrow, (width,height))
rightArrow2=image.load("img/15.png")#in 135
rightArrow2= transform.scale(rightArrow2, (width,height))

rightArrowx1=width/1.1
rightArrowx2=width/1.03
rightArrowy1=height/1.21
rightArrowy2=height/1.04

buttonIng=image.load("img/30.png")
buttonIng= transform.scale(buttonIng, (width,height))

buttonEggx1=90
buttonEggx2=330
buttonEggy1=157
buttonEggy2=230

buttonRicex1=385
buttonRicex2=622
buttonRicey1=171
buttonRicey2=229

#page 3 items
allRecipe=image.load("img/17.png")
allRecipe= transform.scale(allRecipe, (width,height))

allRecipex1=width/4.17
allRecipex2=width/3.25
allRecipey1=height/1.54
allRecipey2=height/1.22

searchBox=image.load("img/19.png")
searchBox= transform.scale(searchBox, (width,height))

searchBoxx1=width/1.75
searchBoxx2=width/1.44
searchBoxy1=height/4.9
searchBoxy2=height/4.14

#page 4 items
searchWindow=image.load("img/21.png")
searchWindow= transform.scale(searchWindow, (width,height))
helpIngredientList=image.load("img/13.png")
helpIngredientList= transform.scale(helpIngredientList, (width,height))

upArrow=image.load("img/10.png")
upArrow= transform.scale(upArrow, (width,height))
downArrow=image.load("img/8.png")
downArrow= transform.scale(downArrow, (width,height))


leftShiftArrow=image.load("img\9.png")#also in 5
leftShiftArrow= transform.scale(leftShiftArrow, (width,height))
rightShiftArrow=image.load("img/2.png")#also in 5
rightShiftArrow= transform.scale(rightShiftArrow, (width,height))
recipeSheet=image.load("img/4.png")
recipeSheet= transform.scale(recipeSheet, (width/2,height/2))

#pagee 5 itmes
characterInBox=image.load("img/6.png")
characterInBox= transform.scale(character, (width,height))
characterAndStepBox=image.load("img/5.png")
characterAndStepBox= transform.scale(characterAndStepBox, (width,height))

imageRect = titlePage.get_rect(center=(width/2, height/2))
leftRect = titlePage.get_rect(center=(width/9, height/1.01))
rightRect = titlePage.get_rect(center=(width/0.97, height/1.01))

leftArrowRect = titlePage.get_rect(center=(width/9.4, height/2))
rightArrowRect = titlePage.get_rect(center=(width/1.03, height/2))

#get quotes
quoteList=[]
quotes = open("text\quotes.txt", "r")
using = True
while using == True:
    texteachline = quotes.readline()
    texteachline=texteachline.strip() 

    if texteachline == "":
        using = False
        break
    
    quoteList.append(texteachline)

quotes.close()

quoteRandom=random.choice(quoteList)

def startPage():
    screen.blit(titlePage,imageRect)

    
    if infoBox==True:
        screen.blit(infoWindow,imageRect)
    

def mainPage():
    screen.blit(kitchen2,imageRect)
    screen.blit(character,imageRect)
    
    screen.blit(leftArrow,leftRect )
    screen.blit(rightArrow,rightRect )        
     
    if dialog==True:
        screen.blit(dialogBox,imageRect)

        textRect = Rect(width/9.2, height/1.21, width/1.22, height/9.24) #text surface
        quoteText = font.render(quoteRandom, 1,(0,0,0))
    
        screen.blit(quoteText, textRect)    
       
                
    
def kitchenPage():
    screen.blit(kitchenBackground,imageRect)
    screen.blit(allRecipe,imageRect)
    screen.blit(searchBox,imageRect)
    
    screen.blit(leftArrow,leftRect )   
    
def inputIngredient():
    
    screen.blit(kitchenBackground2,imageRect)
    screen.blit(searchBox,imageRect)
    screen.blit(searchWindow,imageRect)
    
    screen.blit(leftArrow,leftRect )
    screen.blit(rightArrow,rightRect )    
    
    textIng = font.render(typ, 1, (0,0,0))
    screen.blit(textIng, Rect(width/9.2, height/1.21, width/1.22, height/9.24))
      
    ingT = font.render(ing, 1, (0,0,0))
    screen.blit(ingT, Rect(width/9.2, height/1.21, width/1.22, height/9.24))    
    
    screen.blit(buttonIng, imageRect);                        
    
    black = (0, 0, 0);    
        
     
def recipePage():
    screen.blit(kitchenBackground,imageRect)
    for i in range(2):
        for j in range (3):
            screen.blit(recipeSheet,recipeSheet.get_rect(center=(width/2.7+j*width/4,height/3.4+i*height/2.3)))
            
    screen.blit(leftShiftArrow,leftArrowRect )
    screen.blit(rightShiftArrow,rightArrowRect )    
    
    screen.blit(leftArrow,leftRect)  
            
    
def steps():
    screen.blit(kitchen2,imageRect)
    screen.blit(characterAndStepBox,imageRect)
    
    #the 
    screen.blit(leftShiftArrow,imageRect)
    screen.blit(rightShiftArrow,imageRect)
    
    screen.blit(characterInBox,imageRect)
    
    screen.blit(leftArrow,leftRect )
    screen.blit(rightArrow,rightRect ) 
   
    screen.blit(buttonIng, imageRect);                        

while running:
    for e in event.get(): #checks all possible events
        mx, my = mouse.get_pos()
         
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:   
            if page==0:
                #info button
                if infoBox==True:
                    infoBox=False
                else:
                    if mx>buttonInfox1 and mx<buttonInfox2 and my>buttonInfoy1 and my<buttonInfox2:
                            infoBox=True
                        
                    if  mx>buttonStartx1 and mx<buttonStartx2 and my>buttonStarty1 and my<buttonStarty2:
                        page=1
                        
            if page ==1 or page ==2 or page ==3 or page ==4 or page ==5:
                if mx>leftArrowx1 and mx<leftArrowx2 and my>leftArrowy1 and my<leftArrowy2:
                    page-=1  
                    
                elif page ==1 or page ==3:
                    if  mx>rightArrowx1 and mx<rightArrowx2 and my>rightArrowy1 and my<rightArrowy2:
                        page+=1   
                        
                        if page==4:
                            writeIng = open("text/Ingredients.txt", "w")
                            for i in range(len(ingMem)):
                                writeIng.write(ingMem[i]+"\n")
                            
                            writeIng.close()                            
                    
                    elif page==1:
                        if dialog==True:
                            dialog=False
                        else:
                            dialog=True     
                            
                        quoteRandom=random.choice(quoteList)
                        
                elif page==2:
                    if  mx>allRecipex1 and mx<allRecipex2 and my>allRecipey1 and my<allRecipey2:
                        page=4
                    elif mx>searchBoxx1 and mx<searchBoxx2 and my>searchBoxy1 and my<searchBoxy2:
                        page=3
                        ingMem=[]
                        
                elif page==3:
                    if  mx>buttonEggx1 and mx<buttonEggx2 and my>buttonEggy1 and my<buttonEggy2:
                        #if the egg button was pressed
                        ingMem.append("Egg")
                    elif mx>buttonRicex1 and mx<buttonRicex2 and my>buttonRicey1 and my<buttonRicey2:
                        #if the rice button was pressed
                        ingMem.append("Rice")
                 
                        
                elif page==5:
                    if  mx>rightArrowx1 and mx<rightArrowx2 and my>rightArrowy1 and my<rightArrowy2:
                        page=0
                        
                        
                
              

                    #pygame.drawRect(100, 40, 100, 100);
                   # if  mx>allRecipex1 and mx<allRecipex2 and my>allRecipey1 and my<allRecipey2:
                       # page=4;
                        
                    
                        
                    #if e.key == K_BACKSPACE: 
                       # if len(typ) > 0:
                            #typ = typ[:-1]
                    #elif len(typ)<=19 and e.key != K_SPACE:
                       # typ += e.unicode
                    #elif e.key == K_ENTER and typ!="":
                       # IngMem.append(typ)
                       # ing+=typ+"\n"
                       # typ=""                
                
    
            
    
    if page==0: startPage()   
    elif page==1: mainPage()  
    elif page==2: kitchenPage()  
    elif page==3: inputIngredient()
    elif page==4: recipePage()
    elif page==5:steps()
    else :running==False
    display.update()

    print("%i, %i"%(mx,my))

    
 
quit()
