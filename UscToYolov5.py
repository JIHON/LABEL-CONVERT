# -*- coding:utf-8 -*-
import xml.dom.minidom
import os
from PIL import Image

def convert_annotation(image_add):
    lenimg=len(image_add)
    image_add = image_add[0:image_add.find('.', lenimg-7)]  # 删除后缀.gt.xml，现在只有文件名没有后缀
    print("image_add:",image_add)
    # 现在传进来的只有图片名没有后缀

    in_file = open('F:/LJH/DATASETS/USC/PedestrianMultiViewTestSet/GT/' + image_add + '.gt.xml')  # 为USC标签的目录
    out_file = open('F:/LJH/DATASETS/USC/test/%s.txt' % (image_add), 'w')  # 修改为标签的存放目录
    img_fullname = os.path.join("F:/LJH/DATASETS/USC/PedestrianMultiViewTestSet/"+image_add + '.bmp') #USC图片路径
    img = Image.open(img_fullname)
    img_w, img_h = img.size
    print("img_w:",img_w," img_h", img_h)
    dom=xml.dom.minidom.parse(in_file)
    root = dom.documentElement
    datalist=root.getElementsByTagName('Rect')
    for data in datalist:
        x=int(data.getAttribute("x"))/img_w
        y=int(data.getAttribute("y"))/img_h
        w=int(data.getAttribute("width"))/img_w
        h=int(data.getAttribute("height"))/img_h
        b='0'+" " + " "+str(x)+" " + " "+str(y)+" " + " "+str(w)+" " + " "+str(h)
        out_file.write(b+'\n')


rootdir = 'F:/LJH/DATASETS/USC/PedestrianMultiViewTestSet/GT'  # 修改为USC数据集的标签路径

list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(0, len(list)):
    path = os.path.join(rootdir, list[i])

    if os.path.isfile(path):
        if list[i].endswith(".xml"):
            print("list[i]:",list[i])
            convert_annotation(list[i])