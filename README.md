# LABEL-CONVERT
This project includes the conversion of various data set labels
## InriaToYolov5.py
This file converts INRIAPerson labels((Xmin, Ymin) - (Xmax, Ymax)) to yolov5 format labels(centerx,centery,w,h).  Both the labels of INRIAPerson and YoloV5 datasets are stored in TXT files

The Train dataset of INRIAPerson as follows:  
![image](https://github.com/JIHON/LABEL-CONVERT/blob/main/img/Inria.png)
- Labels are in the Annotations folder and corresponding images are in the pos folder. The same is true for the Test dataset  
- Each image has a corresponding TXT file. The same is true for the Test dataset  


## Yolov5ToCoco.py
This file is used to convert YOLOV5 labels(txt) into COCO labels(json).The labels for YOLOV5 are stored in TXT files. The coco format data set stores all the training set labels in one JSON file and all the validation set labels in another JSON file.

## UscToYolov5.py
This file is used to convert dataset labels in USC format to YOLO V5 dataset labels. The dataset labels in USC format are XML files. The format of the content in the XML file is as follows:  
![image](https://github.com/JIHON/LABEL-CONVERT/blob/main/img/uscxml.png)
- Each image in the USC dataset corresponds to an XML label file in. BMP format  
- x, y in the USC dataset label XML represent the coordinates of the upper-left corner of the target box, and height and width represent the height and width of the target box 
- The XML labels and images of the USC training set are mixed together in a folder. as follows:  
![image](https://github.com/JIHON/LABEL-CONVERT/blob/main/img/usc.png)

## CitypersonToYolov5.py
This file is used to convert Cityperson dataset labels to YOLO V5 data set labels. Cityperson dataset labels are as follows:  
![image](https://github.com/JIHON/LABEL-CONVERT/blob/main/img/cityperson.png)
- The Cityperson datasets are labeled json files, and each graph corresponds to a JSON-formatted label file
- The Cityperson dataset image is located in the leftImg8bit folder and the corresponding label is located in the gtBboxCityPersons folder  

## VocToYoloV5.py
This file is used to convert voc dataset labels into YOLO V5 data set labels. Voc dataset labels are XML files. The contents of the XML file are as follows:  
![image](https://github.com/JIHON/LABEL-CONVERT/blob/main/img/vocxml.png)
- Datasets in VOC format are labeled AS XML files, one for each graph
