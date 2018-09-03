play_more=True
while play_more:
    print('Welcome to the texting game! In this game your name is Katlin and you will text your best friend, Lea and she will reply back! Lea: Good morning! :)')
    hey =int(input('7 you too, 8 its bad, 9 hey!'))
    if hey == 7:
        print('Lea: Nice! After being your friend for this long THIS is my greeting!')
        Yay =int(input('10 Stop being so sensitive!, 11 Shut up already!, 12 cool it Lea!'))
        if Yay == 10:
            print ('Lea: We are no longer friends have a nice life(not).')
        if Yay == 11:
            print ('Lea: At least my voice is not annoying jerk! You have 1 hour to appologize or else.')
            Stupid =int(input('18 no, 19 Bye Mom.'))
            if Stupid == 18:
                print ('LeaLeaBear14 has blocked you.')
            if Stupid == 19:
                print ('I hope you die.')
        if Yay == 12:
            print ('Lea: OK. Look sorry Katlin. So are you invited to that party? Justin is hosting it at his house. Justin: Hey Katlin my house 2moro 5 itz my party.')
            da =int(input('28 Yes. Please do not block me! :(, 29 No.'))
            if da == 28:
                print ('I am not mad but, tell me EVERY detail!!!!')
            if da == 29:
                print ('Stop lying! We are no longer friends!')
    if hey == 8:
        print ('Lea: Life is bad! *sobs in pillow.')
        Tod =int(input('13 Lol!, 14 Lea, you are the best!, 15 Shut up your life is perfect!'))
        if Tod == 13:
            print ('Lea: I know right!')
            Farting =int(input('20 yep., 21 you are such a bragger.'))
            if Farting == 20:
                print ('Lea: Well I am a comidian.')
            if Farting == 21:
                print ('LeiaOrganaSkywalker has blocked you.')
                if Tod == 14:
                    print ('Lea: Aw thanks!')
                    Claire =int(input('22 no problem., 23 good night.'))
                    if Claire == 22:
                        print ('Lea: Well my phones getting taken away. So I guess this is bye. Mom said I could text you one last time. Um so yea thanks for being such a GREAT friend. Bye. :( See you next year.')
                    if Claire == 23:
                        print ('Lea: Good night see you tommorow.')
        if Tod == 15:
            print ('The person you are trying to reach has blocked you.')
    if hey == 9:
        print ('Lea: So what are you doing?')
        cop =int(input('16 nothing, 17 hanging with April, 18 texting you'))
        if cop == 16:
            print ('Lea: Do you want to come over to my place.')
            Water =int(input('24 Ok, 25 Um sorry I lied. :( Please forgive me.'))
            if Water == 24:
                print ('Lea: See you at my place. Good night Katlin. :)')
            if Water == 25:           
                print ('LitLea32 has blocked you.')       
        if cop == 17:
            print ('Lea: I guess you have a new best friend then.')
        if cop == 18:
            print ('Lea: Haha and I thought I was a comedian!!!!')
            Lit =int(input('26 Thank you!, 27 Choose to  not thank Lea.'))
            if Lit == 27:
                print ('I actually have feelings :(. I am going to tell Kay to make you unpopular.')
    
  
                   
    #See if they want to play again
    uinput = input ('type y if you want to play again or q if you want to quit ')
    play_more =uinput.lower() == 'y'
    if uinput =='q':
        break
