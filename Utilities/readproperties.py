from configparser import RawConfigParser

config = RawConfigParser()
config.read("D:\\Local Disk\\Automation PROJECTS\\chaitanya_orangeHRM\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get("common data", "Url")
        return url

    @staticmethod
    def get_username():
        username = config.get("common data", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("common data", "password")
        return password
