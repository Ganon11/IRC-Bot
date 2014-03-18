import os
import os.path
import time
import logging

# some commands can be executed only if the user's nick is found in this list
owner = list(set([
    'mstark',
    'mstark|home',
    'aletheist',
]))

owner_email = {
    'mstark': 'stark3@gmail.com',
    'mstark|home': 'stark3@gmail.com',
}

# server to connect to
server = 'chat.freenode.net'
# server's port
port = 6667

# bot's nicknames
nicks = list(set(['WorfBot', 'WorfBot2', 'WorfBot3']))
# bot's real name
real_name = 'WorfBot, son of MoghBot'

# channels to join on startup
channels = list(set([
    '#mstark',
    #'#reddit-Christianity',
]))

cmds = {
    # core commands list, these commands will be run in the same thread as the bot
    # and will have acces to the socket that the bot uses
    'core': list(set([
        'quit',
        'join',
        'channels',
    ])),

    # normal commands list, the ones that are accessible to any user
    'user': list(set([
        'wiki',
        'about',
        'help',
        'honor',
        'weather',
        'google',
        'mball',
        'uptime',
    ])),

    # commands list that the bot will execute even if a human didn't request an
    # action
    'auto': list(set([
        'subreddits',
    ])),
}

# users should NOT modify below!
log = os.path.join(os.getcwd(), '..', 'logs', '')
logging_level = logging.DEBUG
start_time = time.time()
current_nick = ''
