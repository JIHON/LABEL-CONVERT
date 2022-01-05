import xml.etree.ElementTree as ET
import os

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_add,rootdir,labeldst):
    # image_add进来的是只带名字不带路径的.jpg
    image_add = image_add[0:image_add.find('.', 1)]  # 删除后缀，现在只有文件名没有后缀
    # 现在传进来的只有图片名没有后缀

    in_file = open(rootdir+'/' + image_add + '.xml')  # 修改为你自己的输入目录
    out_file = open(labeldst+'%s.txt' % (image_add), 'w')  # 修改为你自己的输出目录

    tree = ET.parse(in_file) #读取xml文件的方式
    root = tree.getroot()

    if root.find('size'):

        size = root.find('size')
        # 获取图像的宽高
        w = int(size.find('width').text)  # 偶尔xml标记出错，width或height设置为0了
        h = int(size.find('height').text)  # 需要标记出来，便于单独处理
        if w == 0:
            print("出错！ width或height为0:  " + image_add)
            return
        for obj in root.iter('object'):
            # iter()方法可以递归遍历元素/树的所有子元素，一个object表示一个标记框
            difficult = obj.find('difficult').text #寻找xml中difficult标签对应的值
            cls = obj.find('name').text #寻找xml中name标签对应的值，也就是标记的类别
            # 如果训练标签中的类别不在程序预定类别，或者difficult = 1，跳过此object
            if cls not in classes or int(difficult) == 1:
                continue
            # cls_id 只等于1
            cls_id = classes.index(cls) # 获取类别对应的索引
            xmlbox = obj.find('bndbox')
            # b是每个Object中，一个bndbox上下左右像素的元组
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    else:
        print("出错！xml缺少size:  " + image_add)  #xml缺少size的情况，打印输出，单独处理

if __name__ == '__main__':
    classes = ["mask", "no_mask"]  ##修改为自己的类别
    rootdir = 'D:/DATASETS/Mask/Annotations'  #VOC数据集目录
    labeldst="D:/DATASETS/Mask/label/" #转换后需要保存到的目录

    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        print(path)
        if os.path.isfile(path):
            convert_annotation(list[i],rootdir,labeldst)