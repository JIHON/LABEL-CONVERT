# LABEL-CONVERT
This project includes the conversion of various data set labels
## InriaToYolov5.py
This file converts INRIAPerson labels((Xmin, Ymin) - (Xmax, Ymax)) to yolov5 format labels(centerx,centery,w,h).  Both the labels of INRIAPerson and YoloV5 datasets are stored in TXT files

The Train dataset of INRIAPerson as follows: 
- Labels are in the Annotations folder and corresponding images are in the pos folder. The same is true for the Test dataset  
- Each image has a corresponding TXT file. The same is true for the Test dataset  

![image](https://github.com/JIHON/LABEL-CONVERT/blob/main/img/Inria.png)
## Yolov5ToCoco.py
This file is used to convert YOLOV5 labels(txt) into COCO labels(json).The labels for YOLOV5 are stored in TXT files. The coco format data set stores all the training set labels in one JSON file and all the validation set labels in another JSON file.
