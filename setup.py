import configparser

config = configparser.RawConfigParser()

config['chinese.characters'] = {
    'cc':['你', '好']
}

with open('setup.cfg', 'w') as configfile:
    config.write(configfile)