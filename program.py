import random
l=['Rock','Paper','Scissor']
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game started...Lets Play
1.Yes
2.No|Exit        '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1.Rock
2.Paper
3.Scissor       '''))
            if userInput==1:
                uchoice="Rock"
            elif userInput==2:
                uchoice="Paper"
            elif userInput==3:
                uchoice="Scissor"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value:",Cchoice)
                print("User Value:",uchoice)
                print("Result: Game Draw")
            elif (uchoice=="Rock" and Cchoice=="Scissor") or (uchoice=="Paper" and Cchoice=="Rock") or (uchoice=="Scissor" and Cchoice=="Paper"):
                print("Computer Value:",Cchoice)
                print("User Value:",uchoice)
                print("Result: You Win")
                ucount=ucount+1
            else:
                print("Computer Value:",Cchoice)
                print("User Value:",uchoice)
                print("Result: Computer Win")
                ccount=ccount+1

        if ucount==ccount:
            print(">>> Now, The Final Result: Game Draw")
            print("User Score:",ucount)
            print("Computer Score:",ccount)
        elif ucount>ccount:
            print(">>> Now, The Final Result: You Win The Game")
            print("User Score:",ucount)
            print("Computer Score:",ccount) 
        else:
            print(">>> Now, The Final Result: Computer Win The Game")
            print("User Score:",ucount)
            print("Computer Score:",ccount) 
    else:
        break