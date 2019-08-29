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
    #turn on all the lights on the explorerHat
    explorerhat.light.yellow.on()
    explorerhat.light.blue.on()
    explorerhat.light.red.on()

    #then turn them off, but with a random delay between each light for added tension / fun
    explorerhat.light.green.off()
    sleep(random.randint(1,20)/10)
    explorerhat.light.blue.off()
    sleep(random.randint(1,20)/10)
    explorerhat.light.yellow.off()
    sleep(random.randint(1,20)/10)
    explorerhat.light.red.off()
    explorerhat.light.green.on()

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
        explorerhat.motor.one.forward()
    else:
        print('Player 2 wins')
        explorerhat.motor.two.forward()

def flashPlayer(player, duration):
    if player == 1:
        for i in range(duration):
            explorerhat.light.blue.on()
            sleep(0.1)
            explorerhat.light.blue.off()
            sleep(0.1)
    else:
        for i in range(duration):
            explorerhat.light.yellow.on()
            sleep(0.1)
            explorerhat.light.yellow.off()
            sleep(0.1)

# here's our initial countdown
countdown()

while p1Score < topScore and  p2Score < topScore:
    if button1.is_pressed:
        p1Score += 1
        totaliser(1)
        if p1Score < topScore:
            flashPlayer(1,10)
            countdown()    
    elif button2.is_pressed:
        p2Score += 1
        totaliser(2)
        if p2Score < topScore:
            flashPlayer(2,10)
            countdown()

# work out who won and start the celebrations!
if p1Score > p2Score:
    whoWins(1)
    flashPlayer(1,50)
else:
    whoWins(2)
    flashPlayer(2,50)

# Now clean up after ourselves
sleep(3)
explorerhat.explorerhat_exit()