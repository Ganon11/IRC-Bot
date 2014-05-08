import os
import os.path
import time
import logging

# some commands can be executed only if the user's nick is found in this list
owner = list(set([
<<<<<<< HEAD
    'paullik',
    'foobarfoo',
    'paullik-test',
=======
    'mstark',
    'mstark|home',
    'aletheist',
    'aletheia',
>>>>>>> upstream/WorfBot
]))

owner_email = {
    'foobarfoo': 'foobar@gmail.com',
}

# server to connect to
server = 'chat.freenode.net'
# server's port
port = 6667

# bot's nicknames
nicks = list(set(['PPyBot']))
# bot's real name
real_name = 'Paul Python Bot'

# channels to join on startup
channels = list(set([
<<<<<<< HEAD
    '#ppybbot',
    '#test-chan',
=======
    '#reddit-Christianity',
    '#mstark',
>>>>>>> upstream/WorfBot
]))

cmds = {
    # core commands list, these commands will be run in the same thread as the bot
    # and will have acces to the socket that the bot uses
    'core': list(set([
        'add',
        'channels',
        'join',
        'quit',
    ])),

    # normal commands list, the ones that are accessible to any user
    'user': list(set([
<<<<<<< HEAD
        'task',
        'wiki',
        'answer',
=======
>>>>>>> upstream/WorfBot
        'about',
        'bible',
        'help',
        'honor',
        'honour',
        'google',
        'mball',
        'uptime',
<<<<<<< HEAD
        'so',
        'twitter',
=======
        'weather',
        'wiki',
>>>>>>> upstream/WorfBot
    ])),

    # commands list that the bot will execute even if a human didn't request an
    # action
    'auto': list(set([
<<<<<<< HEAD
        'email_alert',
=======
        'subreddits',
>>>>>>> upstream/WorfBot
    ])),
}

# smtp server for email_alert
smtp_server = 'smtp.gmail.com'
smtp_port = 25
from_email_address = 'changeme@gmail.com'
from_email_password = 'p@s$w0rd'

# users should NOT modify below!
log = os.path.join(os.getcwd(), '..', 'logs', '')
logging_level = logging.INFO
start_time = time.time()
current_nick = ''
