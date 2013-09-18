__author__ = 'matt'
__date__ = '9/17/13'

import urllib,json
data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=cat-pizza&api_key=dc6zaTOxFJmzC&limit=5").read())
# data['data'][0]['id']
# http://media1.giphy.com/media/11H2sYCtWyuTF6/giphy.gif
id_list = [ 'http://media1.giphy.com/media/%s/giphy.gif' % (gif_meta['id']) for gif_meta in data['data'] ]
print id_list
