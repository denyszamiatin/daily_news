import configparser
config = configparser.ConfigParser()
config['WEBSITES'] = {'bbc': 'http://www.bbc.com/news',
                      'sky.com': 'https://news.sky.com/world',
                      'cnn': 'http://edition.cnn.com/',
                      'nbcnews': 'https://www.nbcnews.com/news/world',
                      'globalnews': 'https://globalnews.ca/world/'}
config['key_words'] = {'1': 'ukraine'}
with open('config.ini', 'w') as configfile:
  config.write(configfile)