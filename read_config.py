import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

websites = ConfigSectionMap('WEBSITES')
key_words = ConfigSectionMap('key_words')

print(websites)
print(key_words)