import configparser


def read_config(path):
    if type(path) is not str:
        raise Exception('illegal args!, please input correct config file path... ...')

    config = configparser.ConfigParser()
    config.read(path)

    if config.sections():
        return config
    else:
        raise Exception('config file is not exist, or file content is empty')


def get_chinese_characters(config):
    return config.get('chinese.characters', 'cc')



if __name__ == '__main__':

    config = read_config('../setup.cfg')
    cc = get_chinese_characters(config)

    print(cc)

    # TODO 乱序排列中文
    # TODO 生成文字图片
    # TODO 保存至文件夹
