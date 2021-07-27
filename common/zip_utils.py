#!/usr/bin/env python
# encoding: utf-8
# @author: Leo
# @time: 2021/7/25 16:07
# @E-mail: leo.liu@italki.com
import os
import zipfile


def zip_dir(dir_path, zip_path):
    """
    :param dir_path: 目标文件夹路径
    :param zip_path: 压缩后的文件夹路径
    :return:
    """
    zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
    for root, dirnames, filenames in os.walk(dir_path):
        file_path = root.replace(dir_path, '')  # 去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
        # 循环出一个个文件名
        for filename in filenames:
            zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
    zip.close()


# cur_path = os.path.dirname(__file__)
# dir_path = os.path.join(cur_path, '..', 'reports\禅道自动化测试报告V1.7')
# print(cur_path, dir_path)
# zip_dir(dir_path,
#         dir_path+'\禅道自动化测试报告V1.7.zip')
