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
import random

##################################################################################################
###---------------------THE BASICS (network, channel, nick, and socket)------------------------###
##################################################################################################

#Change these to whatever suits your needs
network = 'CHANGE THIS TO YOUR NETWORK'
channel = "#CHANGE THIS TO YOUR CHANNEL"
nick = 'slimBOT'

#You should never have to change the port for a basic setup
port = 6667

#Setting up the socket below, this too you should not ever have to change
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((network,port ))

#This prints all incoming data from the IRC server
#The number is the Buffer (how many characters socket takes in at a time
print irc.recv(4096)

##################################################################################################
###-------------------------------CONNECTING AND COMMAND MUSTS---------------------------------###
##################################################################################################

irc.send('NICK ' + nick + '\r\n')
irc.send('USER ' + nick + ' ' + nick + ' ' + nick + ' ' + ':A Simple Python IRC\r\n')
irc.send('JOIN ' + channel + '\r\n')

irc.send('PRIVMSG ' + channel + ' :Hello World, I\'m ' + nick + '\r\n')

while True:
    data = irc.recv(4096)
    if data.find('PING') != -1:
        irc.send('PONG ' + data.split()[1] + '\r\n')

    #Auto rejoins to kicked
    if data.find('KICK') != -1:
        irc.send('JOIN ' + channel + '\r\n')

    #Tells the bot to quit the channel
    if data.find('!Bot quit') != -1:
        irc.send ('PRIVMSG ' + channel + ' :Fine, if you don\'t want me here...\r\n' )
        irc.send('QUIT\r\n')

    #Says hello back
    if data.find('!hello' or '!hi') != -1:
        irc.send('PRIVMSG ' + channel + ' :Hello\r\n')


    ###################################################################################################
    ###-------------------------------COMMAND CHECKS & CALLS BELOW----------------------------------###
    ###################################################################################################

    if data.find('!slaps') != -1:
        irc.send('PRIVMSG ' + channel + ' :Look mother fucker, I don\'t have time for your shit...\r\n')

    if data.find('!angry8' or '!a8ball') != -1:
        angry8ball()


    ##################################################################################################
    ###--------------------------------------METHODS BELOW-----------------------------------------###
    ##################################################################################################

    def angry8ball():
        ball_responses = ["Try again, wanker!", "Meh, kinda", "Fuckin' a right!", "Shit yeah",
                      "yes", "No", "Bitch, please", "Shit, idk", "Who cares", "How the fuck am I supposed to know?",
                      "I'm hazy, try again", "Without a doubt, you queer", "Idk, prob", "IDK TRY HARDER NEXT TIME",
                      "Fuck no", "Outlook good, now fuck off", "Don't fuckin' count on it",
                      "Cannot predict now, what am I, an fucking geanie?", "Yes definitely, now piss off",
                      "Better not tell you now, you'll piss yourself", "Outlook not good. Don't be a pussy, roll again."]

        #Prints to the IRC chat
        irc.send('PRIVMSG ' + channel + ' ' + random.choice(ball_responses) + '\r\n')