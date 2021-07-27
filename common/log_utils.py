import os
import logging
import time


current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, '../logs')


class LogUtils(object):
    def __init__(self, logger=None):
        self.log_name = os.path.join(log_path, 'UITest_%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(level=logging.INFO)

        self.fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        self.fh.setLevel(level=logging.INFO)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(level=logging.INFO)

        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    # def get_log(self):
    #     return self.logger


logger = LogUtils().logger

if __name__=='__main__':
    logger.info( 'newdream' )