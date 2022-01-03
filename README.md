# LABEL-CONVERT
This project includes the conversion of various data set labels
## InriaToYolov5.py
This file converts INRIAPerson labels((Xmin, Ymin) - (Xmax, Ymax)) to yolov5 format labels(centerx,centery,w,h).  

The Train dataset of INRIAPerson as follows: 
- Labels are in the Annotations folder and corresponding images are in the pos folder. The same is true for the Test dataset  

![image](https://github.com/JIHON/LABEL-CONVERT/blob/main/img/Inria.png)
