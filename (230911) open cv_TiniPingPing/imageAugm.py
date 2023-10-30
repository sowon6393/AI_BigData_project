import os, glob
from utill import ImageAugumentation
filepathList = ['images\\layout_rawdata_\\']

for path_ in filepathList:
    fileList = glob.glob(path_+'*')

    for imagePath in fileList:
        print(imagePath)
        imageAug = ImageAugumentation(imagePath, 200, 200)
        imageAug.integralData()
        imageAug.createFile("images\\{}_augment_5\\".format(path_.split('\\')[1]),imagePath.split('\\')[-1])





 