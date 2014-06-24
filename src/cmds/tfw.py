from config import cmd_char
import thefuckingweather as tfw

CMD_STRING = cmd_char + 'tfw ' # note the trailing space!
USAGE_STRING = 'Usage: %stfw <location>' % cmd_char

def tfw(components):
    args = components['arguments'].split(CMD_STRING)
    if len(args) == 1:
        return USAGE_STRING
    loc = args[1]
    tfw_result = None
    try:
        tfw_result = tfw.get_weather(loc)
    except:
        return 'Could not get weather for "%s"' % loc
        
    location = tfw_result['location']
    weather = tfw_result['current']
    response = '%s - %s%s F - %s (%s)' % (location, weather['temperature'], tfw.DEGREE_SYMBOL, ' '.join(weather['weather']), weather['remark'])
    return response