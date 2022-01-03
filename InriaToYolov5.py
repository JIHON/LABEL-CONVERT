# coding=UTF-8
'''
INRIA label format:(Xmin, Ymin) - (Xmax, Ymax)
YOLOV5 label format: centerx,centery,w,h
'''
import os
import shutil
from PIL import Image

# 获取目标框的坐标
def text_create(name,bnd,img_src):
   im=Image.open(img_src+name + '.png')
   size=im.size[0],im.size[1]# 获取要查询的图片的w,h
   convert_size = convert(size, bnd)
   strlabel='0 ' + str(convert_size[0]) + ' ' + str(convert_size[1]) + ' ' + str(convert_size[2]) + ' ' + str(convert_size[3])+"\n"
   return strlabel

# 转换成yolo的X,Y,W,H并归一化
def convert(size, box):
   x = (box[0] + box[2])/2.0 # centerx
   y = (box[1] + box[3])/2.0 # centery
   w = box[2] - box[0] #目标检测框的宽
   h = box[3] - box[1] #目标检测框的高
   x = x/size[0] # 归一化
   w = w/size[0]
   y = y/size[1]
   h = h/size[1]
   return (x,y,w,h)

if __name__ == '__main__':
    annotations_src = "F:/LJH/DATASETS/INRIAPerson/Test/annotations" # INRIA标签路径
    img_src = "F:/LJH/DATASETS/INRIAPerson/Test/pos/" # INRIA图片路径
    img_dst = "F:/LJH/DATASETS/INRIAPerson/images/"  # 图片目标路径
    label_dst='F:/LJH/DATASETS/INRIAPerson/labels/val/' # YOLOV5标签目标路径
    annotations= os.listdir(annotations_src) #得到文件夹下的所有文件名称

    for file in annotations: #遍历文件夹
        str_name = file.replace('.txt', '')
        srcimg = img_src+str_name+".png"  # 源图片存放路径
        dstimg = img_dst+str_name+".png"# 目的图片存放路径
        shutil.copyfile(srcimg, dstimg) #将inria源图片复制到目标文件夹

        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            with open(annotations_src+"/"+file) as f : #打开inria标签文件
                iter_f = iter(f) #创建迭代器
                label=""
                for line in iter_f: #遍历文件，一行行遍历，读取文本
                    str_XY = "(Xmax, Ymax)"
                    if str_XY in line:
                        strlist = line.split(str_XY)
                        strlist1 = "".join(strlist[1:])    # 把list转为str
                        strlist1 = strlist1.replace(':', '')
                        strlist1 = strlist1.replace('-', '')
                        strlist1 = strlist1.replace('(', '')
                        strlist1 = strlist1.replace(')', '')
                        strlist1 = strlist1.replace(',', '')
                        b = strlist1.split()
                        bnd = (float(b[0]) ,float(b[1]) ,float(b[2]) ,float(b[3]))
                        print(str_name,":",bnd)
                        label=label+text_create(str_name, bnd, img_src)
                    else:
                        continue
                file = open(label_dst+str_name+'.txt', 'w')
                file.write(label)
                print(label)