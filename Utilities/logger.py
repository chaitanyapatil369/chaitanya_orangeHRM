import inspect
import logging


class logGen:
    @staticmethod
    def loggen():
        classname = inspect.stack()[1][3]
        logger = logging.getLogger(classname)
        file = logging.FileHandler("D:\\Local Disk\\Automation PROJECTS\\chaitanya_orangeHRM\\logs\\OrangeHRM_Automation.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s :  %(name)s : %(funcName)s: %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger

#FileHandler file location
#Formatter format
#file--->format setFormatter
#addHandler logger--->file
#setLevel logger----->INFO
#inspect.stack()[1][3]   get classname
#
#return logger