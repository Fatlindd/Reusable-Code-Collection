"""
Note: Fakeuser-agent knowns about: Chrome, Edge, Firefox and Safari. Other browsers are not popular
"""

from fake_useragent import UserAgent
ua = UserAgent()
print(dir(ua))

# Get a random browser user-agent string
# print(ua.random)

# Or get user-agent string from a specific browser
# print(ua.chrome)
# print(ua.google)
# print(ua['google chrome'])
# print(ua.firefox)
# print(ua.safari)


# If you want to specify your own operating systems, you can do that via the os argument 
ua = UserAgent(os='linux')
# print(ua.random)

"""
You can also specify the type of platforms you want to use, you can do that via the platforms argument 
(default is ["pc", "mobile", "tablet"]
"""
# ua = UserAgent(platforms=['pc'])
# ua = UserAgent(platforms=['mobile'])
ua = UserAgent(platforms=['tablet'])
# print(ua.random)


"""
If you want to return more recent user-agent strings, you can play with the min_version argument 
(default is: 0.0, meaning all user agents will match).
"""
ua = UserAgent(min_version=129.0)
# print(ua.random)

# User-agent Python Dictionary
print(ua.getRandom)