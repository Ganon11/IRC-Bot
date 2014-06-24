import config
from functions import *

CMD_STRING = config.cmd_char + 'quit ' # note the trailing space!

def quit(socket, components): # !quit [chan_name]+ -> PART #channel
   '''Returns a string for quitting the bot from a channel(or more) or from all
   channels if no arguments are supplied

   If the user is found in the owners list then the bot is closed, otherwise a
   message is sent to the channel
   If an argument is an invalid channel name it is simply ignored
   If there are no more channels active the bot closes
   '''
   response = ''
   leave = []
   registered = is_registered(socket, components['sender'])

   if registered is None:
      response = 'An unexpected error occurred while fetching data!'
   else:
      if components['sender'] in config.owner and registered:
         response = []
         response.append('PART')

         quit_command = components['arguments'].split(CMD_STRING)

         if 2 == len(quit_command): # arguments supplied
            arg_channels = quit_command[1].lstrip().split(' ')

            for chan in arg_channels:
               chan = chan.strip('\r')
               for curr_chan in config.channels:
                  print "have chan %s and curr_chan %s" % (chan, curr_chan)
                  print "comparing %s and %s" % (chan.lower(), curr_chan.lower())
                  if chan.lower() in curr_chan.lower(): # valid channel
                     leave.append(chan)
                     config.channels.remove(curr_chan)

            if len(leave):
               response.append(','.join(leave))
               response.append('\r\nPRIVMSG ' + components['action_args'][0] + ' :Left: {0}'.format(', '.join(leave)))
               else:
                  response = 'Invalid channel names!'

            else: # no arguments supplied, quitting all channels
               response.append(','.join(config.channels))
               config.channels[:] = []
      else:
         response = 'This command can be run only by the owners!'

   return response
