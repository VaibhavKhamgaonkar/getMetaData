# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:55:16 2019

@author: 10657561
"""
import subprocess
import os, numpy as np
import PIL
from PIL import Image, ExifTags



""" 
Class to provide the metadata of the images or any other file.
3 Modes are mentioned below by which user can fetch the meta data from the image.

Mode = 1. using ExifToo : 
    The recomened apporach to get the metatdata from any kind of file format.
    it is so far the best way to get the metada data. it gives more tags than anyother method.
    It a command line tool which is open sourced and can be downlaoded for windows and mac 
     "https://www.sno.phy.queensu.ca/~phil/exiftool/" 
    for linux, user have to get it by this command : sudo apt install libimage-exiftool-perl
Mode = 2. Using PIL package in python: 
    It is only used for images and no other file types are supported. It gives less 
    information  compared to other modes.
Mode = 3. using Hachoir metadata extraction process:
    just like Exiftool, it is also a command line tool which can be installed using 
    "pip install hachoir". It can give metadat from most of the file  formats but gives less information than
    Exif tool. 
    
    Recommend is mode 1
    
"""

class GetImageMetadata():
    def __init__(self, exifToolPath = 'D:/Projects/ImageMetaData/exiftool.exe', 
                 osType= 'windows'):
        
        if str(osType).lower() =='windows':
            self.exifToolPath = exifToolPath
        else:
            self.exifToolPath = "exiftool"
        
    def getMetadata(self, imgPath, mode=1):
        ''' get the metadata from the image whoese path is given as an argument '''
        infoDict = {}
        #print(f'mode={mode}')
        if mode == 1:
            ''' use Exif tool to get the metadata '''
            process = subprocess.Popen([self.exifToolPath,imgPath],
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            ''' get the tags in dict '''
            for tag in process.stdout:
                line = tag.strip().split(':')
                infoDict[line[0].strip()] = line[-1].strip()
            
            return infoDict
        
        elif mode == 2:
            ''' use PIL package to get the meta data  '''
            ''' get the Extension of the file as PIL method  only works for Images'''
            if imgPath.split('.')[-1]  not in ['png','jpg','jpeg']:
                print('\nWRONG MODE OF OPERATION SELECTED AS THIS MODE IS ONLY FOR THE IAMGE FILE..!! ')
                mode = str(input('Select the Mode again between 1 = Exiftool extration & 3 = hachoir metadata extraction:- \n'))
                if mode in ['1','3']:
                    return self.getMetadata(imgPath=imgPath,mode=int(mode))
                    #print(len(x))
                else:
                    print('Wrong entry. please run the application again..!')
                    return None
            else:
                img = Image.open(imgPath)
                infoDict = { ExifTags.TAGS[k]: v for k, v in img.getexif().items() if k in ExifTags.TAGS }
                return infoDict
        
        elif mode == 3:
            ''' using hachoir-metadata extraction module '''
            exeProcess = "hachoir-metadata"
            process = subprocess.Popen([exeProcess,imgPath],
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
            ''' get the tags in dict '''
            for tag in process.stdout:
                line = tag.strip().split(':')
                infoDict[line[0].strip()] = line[-1].strip()
            
            return infoDict
        
        else:
            print('Wrong Mode entered. Please run the application again..!')
            return None


# ------------------------------------------------------------------------------



if __name__ == '__main__':
    obj = GetImageMetadata(osType = 'Windows')
    meta = obj.getMetadata(imgPath='D:/Projects/ImageMetaData/Images/asian2.jpg', mode=1)

    ''' print the data on console '''
    for k,v in meta.items():
        print(k,':', v)
