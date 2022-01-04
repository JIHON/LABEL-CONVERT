# -*- coding:utf-8 -*-
"""
YOLO 格式的数据集转化为 COCO 格式的数据集
classes.txt是需要在根目录下新建的一个文件，里面是类别名称，每行一个类别
"""

import os
import cv2
import json
from tqdm import tqdm

def yolo2coco(root_path,savepath):
    print("Loading data from ", root_path)

    assert os.path.exists(root_path)
    originLabelsDir = os.path.join(root_path, 'labels/train/') # 针对train数据集
    originImagesDir = os.path.join(root_path, 'images/train/') # 针对train数据集
    with open(os.path.join(root_path, 'classes.txt')) as f:
        classes = f.read().strip().split()
    # images dir name
    indexes = os.listdir(originImagesDir)

    dataset = {'categories': [], 'annotations': [], 'images': []}
    for i, cls in enumerate(classes, 0):
        dataset['categories'].append({'id': i, 'name': cls, 'supercategory': 'mark'})

    # 标注的id
    ann_id_cnt = 0
    for k, index in enumerate(tqdm(indexes)):
        # 支持 png jpg bmp格式的图片。
        txtFile = index.replace('images', 'txt').replace('.jpg', '.txt').replace('.png', '.txt').replace(".bmp",'.txt')
        # 读取图像的宽和高

        im = cv2.imread(originImagesDir + index)
        height, width, _ = im.shape
        # 添加图像的信息
        dataset['images'].append({'file_name': index,
                                  'id': k,
                                  'width': width,
                                  'height': height})
        if not os.path.exists(os.path.join(originLabelsDir, txtFile)):
            # 如没标签，跳过，只保留图片信息。
            print(index+"没标签")
            continue
        with open(os.path.join(originLabelsDir, txtFile), 'r') as fr:
            labelList = fr.readlines()
            for label in labelList:
                label = label.strip().split()
                x = float(label[1])
                y = float(label[2])
                w = float(label[3])
                h = float(label[4])

                # convert x,y,w,h to x1,y1,x2,y2
                H, W, _ = im.shape
                x1 = (x - w / 2) * W
                y1 = (y - h / 2) * H
                x2 = (x + w / 2) * W
                y2 = (y + h / 2) * H
                # 标签序号从0开始计算, coco2017数据集标号混乱，不管它了。
                cls_id = int(label[0])
                width = max(0, x2 - x1)
                height = max(0, y2 - y1)
                dataset['annotations'].append({
                    'area': width * height,
                    'bbox': [x1, y1, width, height],
                    'category_id': cls_id,
                    'id': ann_id_cnt,
                    'image_id': k,
                    'iscrowd': 0,
                    # mask, 矩形是从左上角点按顺时针的四个顶点
                    'segmentation': [[x1, y1, x2, y1, x2, y2, x1, y2]]
                })
                ann_id_cnt += 1

    # 保存结果
    folder = os.path.join(root_path, 'annotations')
    if not os.path.exists(folder):
        os.makedirs(folder)

    json_name = os.path.join(root_path, 'annotations/{}'.format(savepath))
    with open(json_name, 'w') as f:
        json.dump(dataset, f)
        print('Save annotation to {}'.format(json_name))

if __name__ == "__main__":
    rootdir="F:/LJH/DATASETS/INRIAPerson/" # 输入根路径
    savepath='./train.json' # 保存文件的名字
    yolo2coco(rootdir,savepath)
