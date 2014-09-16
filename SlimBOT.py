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

"""
It is generally considered a bad programming practice to have global variables in python for many
reasons.  I decided to do it here because it was the simplest way to keep track of these variables
and I also wanted to show how it can be done and where they would go.  It is best to avoid this
in practice unless you have a good reason to otherwise.
"""

beenShot = False
count = randint(0, 5)

##################################################################################################
###---------------------THE BASICS (network, channel, nick, and socket)------------------------###
##################################################################################################

"""
Below are the three main things that allow this bot online.  The network (sometimes called the
server) is the main entry point for any IRC.  There are many popular networks for IRC such as
FreeNode and IRCnet but all of these networks use the same format for logging on:
irc.*networkName*.com and can be done so using the /connect command.

A channel is the next login point once on the server and is more or less just another name for a
chatroom. They always start with a # and can be joined by using the /join command with:
#*channelName*

Your nick is just the name other users will see when you send a message, it's short for nickname.
To change your nick in chat you would use the /nick command.
"""

#Change these to whatever suits your needs
network = 'irc.installgentoo.com'  # <--------------------------------------------------CHANGE ME!
channel = "#testing"  # <---------------------------------------------------------------CHANGE ME!
nick = 'SlimBOT'  # <------------------------------------------------YOU CAN CHANGE ME IF YOU WANT

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
    """
    The number inside irc.recv() is the buffer (how many characters we receive at a time).
    The Buffer should be about as many characters are in the input string from the socket + some
    room for longer usernames + the longest command.  When in doubt, too long is better than
    too short.

    There are certainly better ways to do this but for the sake a keeping it simple and "Slim"
    I decided to keep it lower level and easy so that we can see how it works.  If you decide to
    build a full and powerful IRC bot with python a good starting place would be to look at the
    Twisted networking library.
    """
    data = irc.recv(128) # <----------------------------------------------------------Buffer Size

    #Prints all incoming data from the IRC to the console
    print data

    if data.find('PING') != -1:
        irc.send('PONG ' + data.split()[1] + '\r\n')

    #Auto rejoins to kicked
    if data.find('KICK') != -1:
        irc.send('JOIN ' + channel + '\r\n')

    #Tells the bot to quit the channel
    if data.find('!bot quit') != -1:
        irc.send('PRIVMSG ' + channel + ' :Alright, I\'ll quit then...\r\n')
        irc.send('QUIT\r\n')

    #Says hello back
    if data.find('!hello' or '!hi') != -1:
        irc.send('PRIVMSG ' + channel + ' :Hello\r\n')

    if data.find('!help') != -1:
        irc.send('PRIVMSG ' + channel + ' :All commands begin with ! and are as follows: '
                                        'hi / hello, slap, 8ball / 8b, and russianRoulette / rr\r\n')

    ##################################################################################################
    ###---------------------------------METHODS / FUNCTIONS BELOW----------------------------------###
    ##################################################################################################

    def ask():
        ask_responses = ["Yes", "No"]
        #Prints to the IRC chat
        irc.send('PRIVMSG ' + channel + ' :' + choice(ask_responses) + '\r\n')

        ## END OF ask ##

    def eightBall():
        ball_responses = ["Yes.", "Reply hazy, try again.", "Without a doubt.", "My sources say no.",
                          "As I see it, yes.", "You may rely on it.", "Concentrate and ask again.",
                          "Outlook not so good.", "It is decidedly so.", "Better not tell you now.",
                          "Very doubtful.", "Yes, definitely.", "It is certain.", "Cannot predict now.",
                          "Most likely.", "Ask again later.", "My reply is no.", "Outlook good.",
                          "Don\'t count on it."]

        #Prints to the IRC chat
        irc.send('PRIVMSG ' + channel + ' :' + choice(ball_responses) + '\r\n')

        ## END OF eightBall ##

    def russianRoulette():
        global count
        global beenShot
        # Indexes of list... 0           1          2          3          4         5
        gun_responces = ['*Click*', '*Click*', '*Click*', '*Click*', '*Click*', '*BANG*']

        #If the gun has "been shot" then we put a new bullet in the chamber and spin it.
        if beenShot:
            irc.send('PRIVMSG ' + channel + ' *Reloading*\r\n')
            count = randint(0, 5)
            beenShot = False

        #Prints to the IRC chat
        irc.send('PRIVMSG ' + channel + ' :' + gun_responces[count] + '\r\n')

        #If we printed the list at index 5 then we printed the BANG and the gun has been shot
        if count == 5:
            beenShot = True
        #If the gun has not been shot then we pass it on to another player the advance to the
        #next chamber
        else:
            count += 1
            
        ## END OF russianRoulette ##

    ###################################################################################################
    ###-------------------------------COMMAND CHECKS & CALLS BELOW----------------------------------###
    ###################################################################################################

    if data.find('!slap') != -1:
        irc.send('PRIVMSG ' + channel + ' :Come on man, why you got to be like that?\r\n')

    if data.find('!ask' or '!a') != -1:
        ask()

    if data.find('!8b' or '!8ball') != -1:
        eightBall()

    if data.find('!rr' or '!russianRoulette') != -1:
        russianRoulette()




