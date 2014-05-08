import re

def subreddits(components):
    links = []
    response = ''
    subreddit_pattern = re.compile(r"(.*)\/r\/(\w+)", re.IGNORECASE)
    reddit_com_pattern = re.compile(r"reddit\.com", re.IGNORECASE)
    
    words = components['arguments'].split()
    for word in words:
        match = subreddit_pattern.search(word)
        if match:
            subreddit = match.groups()[1]
            submatch = reddit_com_pattern.search(match.groups()[0])
            if not submatch:
                links.append('http://www.reddit.com/r/%s' % subreddit)
    
    if links:
        response = 'Subreddit links: ' + ", ".join(links)
    return response
