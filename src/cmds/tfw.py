import thefuckingweather as tfw

def tfw(components):
    loc = components['arguments'].split('!tfw ')[1]
    print '"%s"' % loc
    tfw_result = None
    try:
        tfw_result = tfw.get_weather(loc)
    except:
        return 'Could not get weather for "%s"' % loc
        
    location = tfw_result['location']
    print '"%s"' % location
    weather = tfw_result['current']
    print '"%s"' % weather
    response = '%s - %s%s F - %s (%s)' % (location, weather['temperature'], tfw.DEGREE_SYMBOL, ' '.join(weather['weather']), weather['remark'])
    print '"%s"' % response
    return response