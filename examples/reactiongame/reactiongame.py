import explorerhat
from time import sleep
from gpiozero import Button
import random

#initiate the buttons on GPIO pins 7 and 10
button1 = Button(10)
button2 = Button(7)

#set the initial scores and the winning score
p1Score = 0
p2Score = 0
topScore = 3

# this function counts down from 3 - 0 to Go! with random delays between each count
def countdown():
    print('Ready?')
    sleep(0.5)
    print('3')
    sleep(0.5)
    print('2')
    sleep(0.5)
    print('1')
    sleep(0.5)
    print()
    print('GO')

def totaliser(player):
    print('P%d was first' % player)
    sleep(0.5)
    print ("New scores...")
    print ('P1 - %d' % p1Score)
    print ('P2 - %d' % p2Score)
    print()

def whoWins(player):
    print('We have a winner!')
    if player == 1:
        print('Player 1 wins')
    else:
        print('Player 2 wins')

# here's our initial countdown
countdown()

#check if we have a winner yet
while p1Score < topScore and  p2Score < topScore:
    if button1.is_pressed:
        #increase the player's score by one
        p1Score += 1
        totaliser(1)
        #if no one has won, run another countdown
        if p1Score < topScore:
            countdown()    
    elif button2.is_pressed:
        p2Score += 1
        totaliser(2)
        if p2Score < topScore:
            countdown()

# work out who won and start the celebrations!
if p1Score > p2Score:
    whoWins(1)
else:
    whoWins(2)