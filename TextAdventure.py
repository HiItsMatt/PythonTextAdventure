correct = False
Gameover = False
playing = True
#this loop will restart the game if the player wants to
while playing == True:
    gameover = False
    correct = False
    valid = False

    #Scene 1 - Work Scene
    #show text
    print("┏━━━┓  ┏┓             ┏┓┏┓     ┏┓  ┏━┓")
    print("┃┏━┓┃  ┃┃            ┏┛┗┫┃     ┃┃  ┃┏┛")
    print("┃┃ ┃┃┏━┛┣━━┳┓ ┏┓┏┳━┓ ┗┓┏┫┗━┳━━┓┃┃┏┳┛┗┳━━┓")
    print("┃┗━┛┃┃┏┓┃┏┓┃┃ ┃┃┣┫┏┓┓ ┃┃┃┏┓┃┃━┫┃┃┣╋┓┏┫┃━┫")
    print("┃┏━┓┃┃┗┛┃┏┓┃┗━┛┃┃┃┃┃┃ ┃┗┫┃┃┃┃━┫┃┗┫┃┃┃┃┃━┫")
    print("┗┛ ┗┛┗━━┻┛┗┻━┓┏┛┗┻┛┗┛ ┗━┻┛┗┻━━┛┗━┻┛┗┛┗━━┛")
    print("           ┏━┛┃")
    print("           ┗━━┛")
    print("a story that may or may not be about the creation of this program")
    print("---------------------------------------------------------------------------------------------------")
    print("")
    print("you wake up. it is 12:30pm")
    print("you are worried for a moment, but then you remember you're an IT student - this is early for you")
    print("you get onto your computer to begin work on your assignment. it is due tomorrow")
    print("you encounter an error and cannot seem to find the solution")
    #keep asking action
    #this loop will ensure that the question can be answered again if the first answer is invalid
    while correct == False:
        print("")
        print("What do you do?")
        print("1. Find a 10 year old stackoverflow post and copy the code [correct]")
        print("2. Attempt to solve the problem yourself [incorrect]")
        print("3. Give up and go back to sleep for a few hours [incorrect]")
        question1_answer = input("Answer 1, 2 or 3: ")
        #try checks whether the function is doable or not. since we have int a word will return as invalid
        try:
            #if checks whether the number recieved is an acceptable answer
            if int(question1_answer) == 1:
                correct = True
                print("")
                print("the 10 year old answer works flawlessly")
            elif int(question1_answer) == 2:
                print("")
                print("your are stupid and therefore unsuccessful")
            elif int(question1_answer) == 3:
                print("")
                print("You overslept and failed the assignment")
                gameover = True
                break
            else:
                print("Not an accepted answer, Try again")
        except:
            print("Not an accepted answer, Try again")
    correct = False
    #while loop ensures that invalid answers can be corrected
    while gameover == True:
        print("")
        play_again = input("Gameover! Would you like to play again? y/n: ")
        #checks whether answer is valid or not
        if play_again in ['y','n']:
            #cannot break out of nested loop, so logic on whether to break out of next loop needs to be done after breaking out of this one
            break
        else:
            print("not an accepted answer. Try again")
    #break out of loop or not based on if the player wants to play again.
    if gameover == True:
        if play_again in ["y"]:
            #this continue will restart the game
            continue
        elif play_again in ["n"]:
            #this break will end the game
            break
    print("")
    print("you have been working for a while and decide to take a break")
    print("")
    #Scene 2 - Game Scene
    print("instead of going outside you decide to play video games like any self respecting IT student")
    print("you have seen this free new video game on YouTube and want to try it out")
    print("as a broke uni student, you appreciate the pricetag and download the game")
    print("The game wants you to create a character - it asks for a username")
    print("")
    #get the name of the player
    name = input("Username: ")
    print("")
    print("The devs are trying to collect usage data to improve their game")
    print("It is asking for what graphics card you have")
    #get the player's weapon
    print("when you bought your graphics card, all of them were out of stock except:")
    print("1. 3080")
    print("2. 2080")
    print("3. 1080")
    #while loop ensures that invalid answers can be corrected
    while valid == False:
        print("")
        weapon = input("so you are using (answer 1, 2 or 3): ")
        #breaks out of loop if answer is valid, asks again if answer is invalid
        try:
            if int(weapon) == 1:
                weapon = 3080
                valid = True
            elif int(weapon) == 2:
                weapon = 2080
                valid = True
            elif int(weapon) == 3:
                weapon = 1080
                valid = True
            else:
                print("")
                print("this answer is not valid. Try again")
        except:
            print("")
            print("this answer is not valid. Try again")
    valid = False
    #Scene 3
    print("")
    #Show text
    print("Your friend Noah calls you on Discord")
    print("he saw your discord status change and wants to play with you")
    #while loop ensures that invalid answers can be corrected
    while correct == False:
        print("")
        print("do you want to play with him?")
        print("1. Yes")
        print("2. No")
        print("")
        question2_answer = input("Answer 1 or 2: ")
        #checks for invalid input.
        try:
            if int(question2_answer) == 1:
                correct = True
                print("")
                print("you tell noah that you were just thinking of playing with him [correct answer]")
            elif int(question2_answer) == 2:
                print("")
                print("you tell noah that you just feel like playing solo for now [game over]")
                gameover = True
                break
            else:
                print("")
                print("this answer is not valid. Try again")
        except:
            print("this answer is not valid. Try again")
    correct = False
    #while loop insures that invalid answers can be corrected
    while gameover == True:
        play_again = input("Gameover! Would you like to play again? y/n: ")
        #checking if answer is valid -if it is then break out of nested loop
        if play_again in ['y','n']:
            #cannot break out of higher loops when in a nested one. logic on whether to break out of higher loop has to be handled there so save the values and move on
            break
        else:
            print("not an accepted answer. Try again")
    #logic of whether to break out of loop - breaking will end the game.
    if gameover == True:
        if play_again in ["y"]:
            #this continue will restart the game
            continue
        elif play_again in ["n"]:
            #this break will end the game
            break
    #Scene 4
    #show text
    print("you get into the game and play strategically")
    #have a line show based on previous decisions
    if int(weapon) == 3080:
        print("your powerful GPU is able to run the game smoothly with no issues")
    elif int(weapon) == 2080:
        print("your middle aged GPU is able to run the game smoothly on lower settings")
    elif int(weapon) == 1080:
        print("your older GPU means the game stutters and drops frames. oh well")
    #repeating action
    print("")
    print("you run into the first opponent on the enemy team")
    enemy1_health = 100
    #loop that allows multiple hits to hit the same target. this way we can have a health system as opposed to 1 shot or no damage
    while True:
        print("")
        print("they are facing away from you. what will you do?")
        print("")
        print("1. Miss your shots because you suck [0 damage]")
        print("2. Take your time to align your crosshair with their head [one-shot]")
        print("3. Spray in their general direction and hope you hit them [medium damage]")
        question3_answer = input("Answer 1, 2 or 3: ")
        #ensure that input is valid
        try:
            if int(question3_answer) == 1:
                print("")
                print("Noah tells you that you suck. 0 Damage dealt")
                print("enemy has " + str(enemy1_health) + " health left")
            elif int(question3_answer) == 2:
                print("")
                print("Noah tells you that was a good shot. 100 Damage Dealt")
                enemy1_health = enemy1_health - 100
                print("enemy has " + str(enemy1_health) + " health left")
                #take away health from the enemy and report current health
            elif int(question3_answer) == 3:
                print("")
                print("Noah tells you that was... something? 50 damage dealt")
                enemy1_health = enemy1_health - 50
                print("enemy has " + str(enemy1_health) + " health left")
                #take away health from the enemy and report current health
            else:
                print("not an accepted answer. Try again")
        except:
            print("not an accepted answer. Try again")
        #check if enemy is dead - end loop if he is
        if enemy1_health < 1:
            break
    print("that was the only kill you got during the entire match. this is because you suck")
    print("")
    #scene 5
    #show text
    print("you decide to return to the assignment you were doing before.")
    print("you are pretty tired. you check the clock. It reads 12am")
    #series of repeating actions (multiple enemies combat)
    print("your assignment has a few bugs that you need to fix before you can submit it tomorrow though, so you power through")
    enemy2_health = 100
    #loop that allows multiple hits to hit the same target. this way we can have a health system as opposed to 1 shot or no damage
    while True:
        print("")
        print("Bug no.1")
        print("this bug is really bothering you. What will you do?")
        print("")
        print("1. use epic hollywood hacking montage to remove them [small damage]")
        print("2. think logically about where the error would originate from [high damage]")
        print("3. attempt to follow the confusing error message that is returned [medium damager]")
        question3_answer = input("Answer 1, 2 or 3: ")
        #ensure that the input is valid
        try:
            if int(question3_answer) == 1:
                print("")
                print("this is real life, but you somehow managed to hurt the code's feelings. 5 Damage dealt")
                enemy2_health = enemy2_health - 5
                print("enemy has " + str(enemy2_health) + " health left")
                #calculate damage and print current health
            elif int(question3_answer) == 2:
                print("")
                print("good job. bug squashed. 100 Damage Dealt")
                enemy2_health = enemy2_health - 100
                print("enemy has " + str(enemy2_health) + " health left")
                #calculate damage and print current health
            elif int(question3_answer) == 3:
                print("")
                print("The bug has changed, so I guess you did something. 42.7 damage dealt")
                enemy2_health = enemy2_health - 42.7
                print("enemy has " + str(enemy2_health) + " health left")
                #calculate damage and print current health
            else:
                print("not an accepted answer. Try again")
        except:
            print("not an accepted answer. Try again")
        if enemy2_health < 1:
            break
        #check if enemy is dead
    print("That's the first bug done, only 3 more left")
    enemy3_health = 100
    while True:
        print("")
        print("Bug no.2")
        print("this bug is really bothering you. What will you do?")
        print("")
        print("1. use epic hollywood hacking montage to fix it [small damage]")
        print("2. think logically about where the error would originate from [high damage]")
        print("3. attempt to follow the confusing error message that is returned [medium damager]")
        question4_answer = input("Answer 1, 2 or 3: ")
        #ensure that the input is valid
        try:
            if int(question4_answer) == 1:
                print("")
                print("this is real life, but you somehow managed to hurt the bug's feelings. 5 Damage dealt")
                enemy3_health = enemy3_health - 5
                print("enemy has " + str(enemy3_health) + " health left")
                #calculate damage and print current health
            elif int(question4_answer) == 2:
                print("")
                print("good job. bug squashed. 100 Damage Dealt")
                enemy3_health = enemy3_health - 100
                print("enemy has " + str(enemy3_health) + " health left")
                #calculate damage and print current health
            elif int(question4_answer) == 3:
                print("")
                print("The bug has changed, so I guess you did something. 42.7 damage dealt")
                enemy3_health = enemy3_health - 42.7
                print("enemy has " + str(enemy3_health) + " health left")
                #calculate damage and print current health
            else:
                print("not an accepted answer. Try again")
        except:
            print("not an accepted answer. Try again")
        if enemy3_health < 1:
            break
        #check if enemy is dead
    print("That's the second bug done, only 2 more left")
    enemy4_health = 100
    while True:
        print("")
        print("Bug no.3")
        print("this bug is really bothering you. What will you do?")
        print("")
        print("1. use epic hollywood hacking montage to fix it [small damage]")
        print("2. think logically about where the error would originate from [high damage]")
        print("3. attempt to follow the confusing error message that is returned [medium damager]")
        question5_answer = input("Answer 1, 2 or 3: ")
        #ensure that the input is valid
        try:
            if int(question5_answer) == 1:
                print("")
                print("this is real life, but you somehow managed to hurt the bug's feelings. 5 Damage dealt")
                enemy4_health = enemy4_health - 5
                print("enemy has " + str(enemy4_health) + " health left")
                #calculate damage and print current health
            elif int(question5_answer) == 2:
                print("")
                print("good job. bug squashed. 100 Damage Dealt")
                enemy4_health = enemy4_health - 100
                print("enemy has " + str(enemy4_health) + " health left")
                #calculate damage and print current health
            elif int(question5_answer) == 3:
                print("")
                print("The bug has changed, so I guess you did something. 42.7 damage dealt")
                enemy4_health = enemy4_health - 42.7
                print("enemy has " + str(enemy4_health) + " health left")
                #calculate damage and print current health
            else:
                print("not an accepted answer. Try again")
        except:
            print("not an accepted answer. Try again")
        if enemy4_health < 1:
            break
        #check if enemy is dead
    print("That's the third bug done, only 1 more left")
    enemy5_health = 100
    while True:
        print("")
        print("Bug no.4")
        print("this bug is really bothering you. What will you do?")
        print("")
        print("1. use epic hollywood hacking montage to fix it [small damage]")
        print("2. think logically about where the error would originate from [high damage]")
        print("3. attempt to follow the confusing error message that is returned [medium damager]")
        question6_answer = input("Answer 1, 2 or 3: ")
        #ensure that the input is valid
        try:
            if int(question6_answer) == 1:
                print("")
                print("this is real life, but you somehow managed to hurt the bug's feelings. 5 Damage dealt")
                enemy5_health = enemy5_health - 5
                print("enemy has " + str(enemy5_health) + " health left")
                #calculate damage and print current health
            elif int(question6_answer) == 2:
                print("")
                print("good job. bug squashed. 100 Damage Dealt")
                enemy5_health = enemy5_health - 100
                print("enemy has " + str(enemy5_health) + " health left")
                #calculate damage and print current health
            elif int(question6_answer) == 3:
                print("")
                print("The bug has changed, so I guess you did something. 42.7 damage dealt")
                enemy5_health = enemy5_health - 42.7
                print("enemy has " + str(enemy5_health) + " health left")
                #calculate damage and print current health
            else:
                print("not an accepted answer. Try again")
        except:
            print("not an accepted answer. Try again")
        if enemy5_health < 1:
            break
        #check if enemy is dead
    #text (optional)
    print("That's all the bugs fixed! Congratulations")
    print("")
    #scene 6
    #show text
    print("you look at the clock. it reads 3:51am")
    print("you are incredibly tired, but your work is done and all you want to do is sleep")
    print("")
    #action (with 2 alternatives)
    print("1. Go to bed and submit the assignment in the morning [incorrect]")
    print("2. Fend off your fatigue and submit the assignment now [correct]")
    print("3. Go on your phone and relax for a while before bed [incorrect]")
    final_question = input("Answer 1, 2 or 3: ")
    #while loop ensures that invalid answers can be corrected
    while True:
        #checks whetehr input is valid
        try:
            #show text (depends on alternatives)
            if int(final_question) == 1:
                print("----------------------------------------------------------------------------------------")
                print("      You turn off your computer as you fall into bed. satisfied by your work.")
                print("   only you have forgotton one thing. The floppy disk shaped button in the top left")
                print("  Commonly referred to as the save button. something that you have forgotton to click")
                print("           you wake up the next morning, prepared to submit your work")
                print("            you suddenly discover the horrific nature of you mistake")
                print("                                    GAME OVER")
                print("----------------------------------------------------------------------------------------")
                break
            elif int(final_question) == 2:
                print("----------------------------------------------------------------------------------------")
                print("   with begrudging effort, you fend off your tiredness and begin to submit your code")
                print("       very soon you discover that you didnt save once during this entire session")
                print("              'Crisis Averted' you think, as you finalise the submission")
                print("         finally, you just need a name... what could you call this project?")
                print("                            'a day in the life' works i guess")
                print("                                       YOU WIN")
                print("----------------------------------------------------------------------------------------")
                break
            elif int(final_question) == 3:
                print("----------------------------------------------------------------------------------------------------------")
                print("                        You save your work before you exit your computer, thankfully")
                print("                  as your computer shuts down, you bring up your favorite youtuber to watch")
                print("                    a few minutes turns into a few hours, as you lie in bed, entertained")
                print("        suddenly, you look outside and see the sun already risen as you begin to drop off to sleep")
                print("     you wake, hours later. In darkness, you check the clock. 12:01am. You have missed the deadline")
                print("                                               GAME OVER")
                print("----------------------------------------------------------------------------------------------------------")
                break
            else:
                print("not an accepted answer. Try again")
        except:
            print("not an accepted answer. Try again")
    play_again = input("would you like to play again? y/n")
    if play_again in ["y"]:
        continue
    elif play_again in ["n"]:
        break