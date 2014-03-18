##################################################################################################
##################################################################################################
###                  _       __     __                             ______                      ###
###                 | |     / /__  / /________  ____ ___  ___     /_  __/___                   ###
###                 | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \     / / / __ \                  ###
###                 | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/    / / / /_/ /                  ###
###                 |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/    /_/  \____/                   ###
###      ___           ___                   ___           ___           ___          ___      ###
###     /\  \         /\__\      ___        /\__\         /\  \         /\  \        /\  \     ###
###    /::\  \       /:/  /     /\  \      /::|  |       /::\  \       /::\  \       \:\  \    ###
###   /:/\ \  \     /:/  /      \:\  \    /:|:|  |      /:/\:\  \     /:/\:\  \       \:\  \   ###
###  _\:\-\ \  \   /:/  /       /::\__\  /:/|:|__|__   /::\-\:\__\   /:/  \:\  \      /::\  \  ###
### /\ \:\ \ \__\ /:/__/     __/:/\/__/ /:/ |::::\__\ /:/\:\ \ |__| /:/__/ \:\__\    /:/\:\__\ ###
### \:\ \:\ \/__/ \:\  \    /\/:/  /    \/__/--/:/  / \:\-\:\/:/  / \:\  \ /:/  /   /:/  \/__/ ###
###  \:\ \:\__\    \:\  \   \::/__/           /:/  /   \:\ \::/  /   \:\  /:/  /   /:/  /      ###
###   \:\/:/  /     \:\  \   \:\__\          /:/  /     \:\/:/  /     \:\/:/  /   /:/  /       ###
###    \::/  /       \:\__\   \/__/         /:/  /       \::/  /       \::/  /   /:/  /        ###
###     \/__/         \/__/                 \/__/         \/__/         \/__/    \/__/         ###
###                                                                                            ###
###-------SlimBOT is a simple, easy to understand learning tool for both IRC and Python!-------###
##################################################################################################
##################################################################################################

#imports
import socket
from random import *

#Globals Variables (your methods may need them to use some, if so put them below!)
beenShot = False
count = randint(0,5)

##################################################################################################
###---------------------THE BASICS (network, channel, nick, and socket)------------------------###
##################################################################################################

#Change these to whatever suits your needs
network = 'irc.installgentoo.com'  #<---------------------------------------------CHANGE ME!
channel = "#test"  #<--------------------------------------------CHANGE ME!
nick = 'slimBOT'  #<-------------------------------------------------YOU CAN CHANGE ME IF YOU WANT

#You should never have to change the port for a basic setup
#port 6667 is the default port for IRC
port = 6667

#Setting up the socket below, this too you should not ever have to change
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((network, port))

#This prints all incoming data from the IRC server

##################################################################################################
###-------------------------------CONNECTING AND COMMAND MUSTS---------------------------------###
##################################################################################################

irc.send('NICK ' + nick + '\r\n')
irc.send('USER ' + nick + ' ' + nick + ' ' + nick + ' ' + ':A Simple Python IRC\r\n')
irc.send('JOIN ' + channel + '\r\n')

# Once the bot has joined the channel
irc.send('PRIVMSG ' + channel + ' :Hello World, I\'m ' + nick + '\r\n')

while True:
    #The number is the Buffer (how many characters socket takes in at a time)
    #HINT: The Buffer should be about as many characters are in the input string from the socket 
    # + some room for longer usernames + the longest command 
    #When in doubt, too long is better than too short
    data = irc.recv(64)

    #Prints all incoming data from the IRC to the console
    print data

    if data.find('PING') != -1:
        irc.send('PONG ' + data.split()[1] + '\r\n')

    #Auto rejoins to kicked
    if data.find('KICK') != -1:
        irc.send('JOIN ' + channel + '\r\n')

    #Tells the bot to quit the channel
    if data.find('!Bot quit') != -1:
        irc.send('PRIVMSG ' + channel + ' :Alright, I\'ll quit then...\r\n')
        irc.send('QUIT\r\n')

    #Says hello back
    if data.find('!hello' or '!hi') != -1:
        irc.send('PRIVMSG ' + channel + ' :Hello\r\n')

    if data.find('!help' or '!Help') != -1:
        irc.send('PRIVMSG ' + channel + ' :All commands begin with ! and are as follows: '
                                        'hi, hello, slaps, and  8ball or 8b\r\n')

    ###################################################################################################
    ###-------------------------------COMMAND CHECKS & CALLS BELOW----------------------------------###
    ###################################################################################################

    if data.find('!slaps') != -1:
        irc.send('PRIVMSG ' + channel + ' :Come on man, why you got to be like that?\r\n')

    if data.find('!8b' or '!8ball') != -1:
        eightBall()

    if data.find('!rr' or '!russianRoulette') != -1:
        russianRoulette()

    ##################################################################################################
    ###---------------------------------METHODS / FUNCTIONS BELOW----------------------------------###
    ##################################################################################################

    def eightBall():
        ball_responses = ["Yes.", "Reply hazy, try again.", "Without a doubt.", "My sources say no.",
                          "As I see it, yes.", "You may rely on it.", "Concentrate and ask again.",
                          "Outlook not so good.", "It is decidedly so.", "Better not tell you now.",
                          "Very doubtful.", "Yes, definitely.", "It is certain.", "Cannot predict now.",
                          "Most likely.", "Ask again later.", "My reply is no.", "Outlook good.",
                          "Don\'t count on it."]

        #Prints to the IRC chat
        irc.send('PRIVMSG ' + channel + ' ' + random.choice(ball_responses) + '\r\n')

        ## END OF eightBall ##

    def russianRoulette():
        global count
        global beenShot
        # Indexs of list... 0           1          2          3          4         5
        gun_responces = ['*Click*', '*Click*', '*Click*', '*Click*', '*Click*', '*BANG*']

        #If the gun has "been shot" then we put a new bullet in the chamber and spin it.
        if beenShot:
            irc.send('PRIVMSG ' + channel + ' *Reloading*\r\n')
            count = randint(0, 5);
            beenShot = False

        #Prints to the IRC chat
        irc.send('PRIVMSG ' + channel + ' ' + gun_responces[count] + '\r\n')

        #If we printed the list at index 5 then we printed the BANG and the gun has been shot
        if count == 5:
            beenShot = True
        #If the gun has not been shot then we pass it on to another player the advance to the
        #next chamber
        else:
            count += 1

        ## END OF russianRoulette ##







