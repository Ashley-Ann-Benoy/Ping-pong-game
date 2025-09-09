# computer project by Ashley, Devna and Pavani. Grade 11

# Ping pong game

#imported modules and packages
from tkinter import messagebox
from tkinter import *
import turtle
import winsound
import os
import sys


#initialising homepage
sc = Tk()
#screen formatting - front
sc.title('Welcome to Ping Pong saga')
sc.geometry('800x600')
sc['bg'] = 'white'

#setting background image
background1 = PhotoImage(file='HS-Final.png')

test_label2 = Label(sc, image=background1)
test_label2.place(x=0, y=0)

#input usernames
playerB=Text(sc,bg='#FFF1D6',width=20,height=2)
playerB.place(x=450,y=450)
playerA=Text(sc,bg='#FFF1D6',width=20,height=2)
playerA.place(x=450,y=400)

#global variables
global PA
global PB
global theme
global r
global quitim

# setting variable
r = IntVar()

# terms and conditions page
def tc():
    messagebox.showinfo('Terms and Conditions,', '''These terms apply to your download and/or access of Ping Pong Saga, whether on your computer, on a mobile device or any other website, device or platform. These terms also apply to any other services that we may provide in relation to the game or the website, such as customer support, social media, community channels and other websites that we may operate from time to time such as pingpongsaga.com (we refer to all our games and other services collectively as the "Services" in these terms). These terms are a legal agreement and contain important information about your rights and obligations in relation to our Services.

        If you do not agree to these terms or any future updated version of them then you must not access and/or use, and must cease all access and/or use of, any of our Services. If we require that any future update to these terms requires any action from you in order to accept the updated terms, then you may not be able to continue to use the Services until you have taken such action.

        The specific game rules, scoring rules, controls and guidelines for each game can be found within the game itself. Such rules, scoring rules, controls and guidelines form part of these terms and you agree that you shall comply with them in respect of each individual game which you choose to access and/or play.

        You are responsible for the internet connection and/or mobile charges that you may incur for accessing and/or using our Services. You should ask your mobile operator or internet service provider if you are unsure what these charges will be, before you access and/or use our Services.

        There may be times when our Services or any part of them are not available for technical or maintenance related reasons, whether on a scheduled or unscheduled basis.

        You must comply with the laws that apply to you in the location that you access our Services from. If any laws applicable to you restrict or prohibit you from using our Services, you must comply with those legal restrictions or, if applicable, stop accessing and/or using our Services.

        You promise that all the information you provide to us on accessing and/or using our Services is and shall remain true, accurate and complete at all times.
        Information, data, software, sound, photographs, graphics, video, messages, tags, or other materials may be sent, uploaded, communicated, transmitted or otherwise made available via our Services by you or another user (“Content”). You understand and agree that all Content that you may be sent when using our Services, whether publicly posted or privately sent, is the sole responsibility of the person that sent the Content. This means that you, not us, are entirely responsible for all Content that you may upload, communicate, transmit or otherwise make available via our Services.

        You acknowledge that all copyright, trade marks, and other intellectual property rights in and relating to our Services (other than Content which is contributed and owned by players) is owned by or licensed to us.

        Whilst you are in compliance with these terms, we grant you a non-exclusive, non-transferable, personal, revocable limited licence to access and/or use our Services (but not any related object and source code) for your own personal private use, in each case provided that such use is in accordance with these terms. You agree not to use our Services for anything else. These terms also apply to any update or patches which we may release or make available for any of the Services and any such update or patch shall be deemed part of the Services for the purposes of these terms''')


tc_button=Button(sc,bg='white', text='T & C',command=tc,)
tc_button.place(x=30,y=0)


def exit_pg():
    sys.exit()


#button images
play_buttonim=PhotoImage(file='CS.StartButton.png')
close_buttonim=PhotoImage(file='close.png')
go_buttonim=PhotoImage(file='play-button.png')

#exit home page button
exit_hb=Button(sc, bg='white', text='Quit', command=exit_pg, height=10, width=10, image=close_buttonim)
exit_hb.place(x=0,y=0)


def popup():
    #new page
    PA = playerA.get("1.0", "end-1c")
    PB=playerB.get("1.0", "end-1c")
    sc.title('Theme')
    sc.geometry('800x600')
    sc['bg'] = 'white'
    # setting background image
    backgroud = PhotoImage(file='Menu Screen MS.png')
    menu_label = Label(sc, image=backgroud)
    menu_label.place(x=0, y=0)

    normal_sel = Radiobutton(sc, text="default", variable=r, value=0, bg='white')
    beach_sel = Radiobutton(sc, text="beach", variable=r, value=1, bg='white')
    arcade_sel = Radiobutton(sc, text="arcade", variable=r, value=2, bg='white')

    normal_sel.place(x=385, y=270)
    beach_sel.place(x=385, y=290)
    arcade_sel.place(x=385, y=310)

    def clicked():
        global theme
        theme = r.get()
        # theme conditions
        if theme == 0:
            theme_mapping = {'backgrd': 'GS-Final.png', 'music': 'Headphones-In.wav', 'paddlecolor': '#F9D317',
                             'ballcolor': '#FFE135'}
        elif theme == 1:
            theme_mapping = {'backgrd': 'Beach GS.png', 'music': 'Oahu Beach Stroll.wav', 'paddlecolor': '#FF7C00',
                             'ballcolor': '#FFFFFF'}
        elif theme == 2:
            theme_mapping = {'backgrd': 'Arcade GS.png', 'music': 'Arcade Music.wav', 'paddlecolor': '#68F1FB',
                             'ballcolor': '#FFFFFF'}

        color_paddle = str(theme_mapping['paddlecolor'])
        color_ball = str(theme_mapping['ballcolor'])
        game_bg = theme_mapping['backgrd']
        bgm = theme_mapping['music']

        #instructions screen
        sc.title('instructions')
        sc.geometry('800x600')
        inst_page = PhotoImage(file='IS-Final.png')
        test_label = Label(sc, image=inst_page, bg='white')
        exit_hb = Button(sc, bg='white', text='Quit', command=exit_pg, height=10, width=10, image=close_buttonim)
        exit_hb.place(x=0, y=0)
        test_label.place(x=0, y=0)

        def go():
            # setting a message box
            messagebox.showinfo("hello", "hi there, please head over to game window to play")

            sc.destroy()

            #  turtle game screen
            wn = turtle.Screen()
            winsound.PlaySound(bgm, winsound.SND_ASYNC)
            wn.title("Ping Pong Saga ")
            wn.setup(width=800, height=600)
            wn.bgpic(game_bg)
            wn.bgcolor("#287635")  # japanese lurel green
            wn.tracer()

            # Score
            score_a = 0
            score_b = 0
            score_final = 3

            # Paddle A
            paddle_a = turtle.Turtle()
            paddle_a.speed(0)
            paddle_a.shape("square")
            paddle_a.shapesize(stretch_wid=5, stretch_len=1)
            paddle_a.color(color_paddle)
            paddle_a.penup()
            paddle_a.goto(-350, 0)

            # Paddle B
            paddle_b = turtle.Turtle()
            paddle_b.speed(0)
            paddle_b.shape("square")
            paddle_b.shapesize(stretch_wid=5, stretch_len=1)
            paddle_b.color(color_paddle)
            paddle_b.penup()
            paddle_b.goto(350, 0)

            # ball
            ball = turtle.Turtle()
            ball.speed(0)
            ball.shape("circle")
            ball.color(color_ball)
            ball.penup()
            ball.goto(0, 0)

            # rate of change of ball
            ball.dx = 2.0
            ball.dy = 2.0

            # Pen
            pen = turtle.Turtle()
            pen.speed(0)
            pen.color("black")
            pen.penup()
            pen.hideturtle()
            pen.goto(0, 260)

            # score board
            pen.color('black')
            pen.write("{}: 0         {}: 0".format(PA, PB), align="center", font=("Verdana", 20, "normal"))

            # function
            # moving paddles up and down
            def paddle_a_up():
                y = paddle_a.ycor()
                y += 20
                paddle_a.sety(y)

            def paddle_a_down():
                y = paddle_a.ycor()
                y -= 20
                paddle_a.sety(y)

            def paddle_b_up():
                y = paddle_b.ycor()
                y += 20
                paddle_b.sety(y)

            def paddle_b_down():
                y = paddle_b.ycor()
                y -= 20
                paddle_b.sety(y)

            # Keyboard binding
            wn.listen()
            wn.onkeypress(paddle_a_up, 'w')
            wn.onkeypress(paddle_a_down, 's')
            wn.onkeypress(paddle_b_up, 'Up')
            wn.onkeypress(paddle_b_down, 'Down')

            # Main game loop
            while True:
                wn.update()
                # condition to end game
                if score_a == score_final or score_b == score_final:
                    turtle.delay(50)
                    wn.bye()
                    winsound.PlaySound('Clapping Sound Effects.wav', winsound.SND_ASYNC)

                    sc3 = Tk()
                    sc3.title("Thank you for playing")
                    sc3.geometry('800x600')
                    sc3['bg'] = 'black'
                    background2 = PhotoImage(file='ES-Final.png')
                    test_label3 = Label(sc3, image=background2)
                    test_label3.place(x=0, y=0)


                    def close():
                        sys.exit()


                     # quit button
                    quitim=PhotoImage(file='close3.png')
                    close_button = Button(sc3, bg='white', text='Quit', command=close, height=70, width=70,image=quitim)
                    close_button.place(x=370, y=480)

                    # for stating the winner
                    if score_a == score_final:
                        winner_name = Label(sc3, text=PA, height=2, width=20, bg='white', font=('Arial Bold', 25))
                        winner_name.place(x=200, y=400)
                        sc3.mainloop()

                    elif score_b == score_final:
                        winner_name = Label(sc3, text=PB, height=2, width=20, bg='white', font=('Arial Bold', 25))
                        winner_name.place(x=200, y=400)
                        sc3.mainloop()

                # Move the ball
                xx = ball.xcor()
                yy = ball.ycor()
                DX = ball.dx
                DY = ball.dy
                move_x = int(xx + DX)
                move_y = int(yy + DY)
                ball.setposition((move_x, move_y))

                # Border Checking
                if ball.ycor() > 290:
                    # winsound.PlaySound(None, winsound.SND_ASYNC)
                    # winsound.PlaySound("ballbounce.wav", winsound.SND_ASYNC)
                    ball.sety(290)
                    ball.dy *= -1

                if ball.ycor() < -290:
                    # winsound.PlaySound(None, winsound.SND_ASYNC)
                    # winsound.PlaySound("ballbounce.wav", winsound.SND_ASYNC)
                    ball.sety(-290)
                    ball.dy *= -1

                if paddle_a.ycor() < -290:
                    paddle_a.sety(-289)

                if paddle_a.ycor() > 290:
                    paddle_a.sety(291)

                if paddle_b.ycor() < -290:
                    paddle_b.sety(-289)

                if paddle_b.ycor() > 290:
                    paddle_b.sety(291)

                # ball out of court
                if ball.xcor() > 390:
                    # winsound.PlaySound("point.wav", winsound.SND_ASYNC)
                    ball.goto(0, 0)
                    ball.dx *= -1
                    score_a += 1
                    pen.clear()

                    # score update for A
                    pen.write("{}: {}         {}: {}".format(PA, score_a, PB, score_b), align="center",
                              font=("Verdana", 20, "normal"))

                if ball.xcor() < -390:
                    # winsound.PlaySound("point.wav", winsound.SND_ASYNC)
                    ball.goto(0, 0)
                    ball.dx *= -1
                    score_b += 1
                    pen.clear()

                    # score update for B
                    pen.write("{}: {}         {}: {}".format(PA, score_a, PB, score_b), align="center",
                              font=("Verdana", 20, "normal"))

                # Paddle and ball collisions
                if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
                    # winsound.PlaySound("swoosh.wav", winsound.SND_ASYNC)
                    ball.dx *= -1

                elif ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
                    # winsound.PlaySound("swoosh.wav", winsound.SND_ASYNC)
                    ball.dx *= -1

        go_button = Button(sc, text='GO', command=go, bg='white', fg='white', height=60, width=60, image=go_buttonim)
        go_button.place(x=350, y=500)
        sc.mainloop()

    mybutton = Button(sc, text="Select", command=clicked, bg='#A5FF8B', width=8)
    mybutton.place(x=380, y=335)

    # for maintaining instructions
    sc.mainloop()


inst_button = Button(sc, text='play', command=popup, bg='black', fg='white', height=80, width=120, image=play_buttonim)
inst_button.place(x=380, y=500)

# for maintaining main screen
sc.mainloop()


