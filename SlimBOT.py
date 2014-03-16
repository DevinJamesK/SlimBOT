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
network = 'CHANGE THIS TO YOUR NETWORK'  #<---------------------------------------------CHANGE ME!
channel = "#CHANGE THIS TO YOUR CHANNEL" #<---------------------------------------------CHANGE ME!
nick = 'slimBOT' #<--------------------------------------------------YOU CAN CHANGE ME IF YOU WANT

#You should never have to change the port for a basic setup
#port 6667 isa default port for IRC
port = 6667

#Setting up the socket below, this too you should not ever have to change
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((network,port ))

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
    if data.find('PING') != -1:
        irc.send('PONG ' + data.split()[1] + '\r\n')

    #Auto rejoins to kicked
    if data.find('KICK') != -1:
        irc.send('JOIN ' + channel + '\r\n')

    #Tells the bot to quit the channel
    if data.find('!Bot quit') != -1:
        irc.send ('PRIVMSG ' + channel + ' :Alright, I\'ll quit then...\r\n' )
        irc.send('QUIT\r\n')

    #Says hello back
    if data.find('!hello' or '!hi') != -1:
        irc.send('PRIVMSG ' + channel + ' :Hello\r\n')
        
    if data.find('!help' or '!Help') != -1:
        irc.send(('PRIVMSG ' + channel + ' :All commands begin with ! and are as follows:'  +
            'hi, hello, slaps, and  8ball or 8b\r\n')


    ###################################################################################################
    ###-------------------------------COMMAND CHECKS & CALLS BELOW----------------------------------###
    ###################################################################################################

    if data.find('!slaps') != -1:
        irc.send('PRIVMSG ' + channel + ' :Come on man, why you got to be like that?
        
    if data.find('!8b' or '!8ball') != -1:
        8ball()


    ##################################################################################################
    ###---------------------------------METHODS / FUNCTIONS BELOW----------------------------------###
    ##################################################################################################

    def 8ball():
        ball_responses = ["Yes.", "Reply hazy, try again.", "Without a doubt." "My sources say no.", 
        "As I see it, yes.", "You may rely on it.", "Concentrate and ask again.", "Outlook not so good.",
        "It is decidedly so.", "Better not tell you now.", "Very doubtful.", "Yes, definitely.", 
        "It is certain.", "Cannot predict now.", "Most likely.", "Ask again later.", "My reply is no.", 
        "Outlook good.", "Don\'t count on it."]

        #Prints to the IRC chat
        irc.send('PRIVMSG ' + channel + ' ' + random.choice(ball_responses) + '\r\n')
