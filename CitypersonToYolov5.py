# -*- coding:UTF-8 -*-
import json
import os.path
import shutil

def convert_annotation(rootdir,image_name,cls,jsonsrc,txtdst):
    imgsrc=rootdir+"/"+cls+"/"+image_name#图片源路径
    imgdst="F:/LJH/DATASETS/cityperson/images/val"+"/"+image_name#图片目的地
    shutil.copyfile(imgsrc,imgdst)
    try:
        load_f = open(jsonsrc+cls+"/%s_gtBboxCityPersons.json" % (image_name[:-16]),'r')#读取源标签
    except:
        return
    load_dict = json.load(load_f)
    out_file = open(txtdst+'%s_leftImg8bit.txt' % (image_name[:-16]), 'w')  # 输出标签的地址
    W = load_dict['imgWidth']  # 原图的宽，用于归一化
    H = load_dict['imgHeight']
    objects = load_dict['objects']
    nums = len(objects)
    for i in range(0, nums):
        label, (x, y, w, h) = objects[i]['label'], objects[i]['bbox']
        label = labels.index(label)
        writeline = str(label)+' '+str((x+w/2)/W)+' '+str((y+(h/2))/H)+' '+str(w/W)+' '+str(h/H)+'\n'
        out_file.write(writeline)

if __name__ == '__main__':
    rootdir = 'F:/LJH/DATASETS/cityperson/leftImg8bit/val'  # cityperson图片的地址
    txtdst="F:/LJH/DATASETS/cityperson/labels/val/" #转换后的标签存放路径
    jsonsrc="F:/LJH/DATASETS/cityperson/gtBboxCityPersons/val/"# cityperson标签的路径
    labels = ['pedestrian', 'rider', 'sitting person', 'person (other)', 'ignore', 'person group']  # 标签的种类
    for cls in os.listdir(rootdir):
        imgdir=rootdir+'/'+cls
        for imgname in os.listdir(imgdir):
            print(imgdir+'/'+imgname)
            convert_annotation(rootdir,imgname,cls, jsonsrc,txtdst)
