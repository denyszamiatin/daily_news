import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def get_section(section):
    if section not in config:
        return {}
    return {option:config.get(section, option) for option in options}


websites = get_section('WEBSITES')
key_words = get_section('key_words')


if __name__ == '__main__':
    print(websites)
    print(key_words)