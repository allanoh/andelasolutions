import requests

# A simple command line application to call the twitter profile of @gbabyz
link = 'https://twitter.com/@gbabyz'
page = requests.get(link)
print (page.content)