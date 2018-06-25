# Image-Forensics-Tool
A tool to detect whether an image forgery.


## A linux command line tool developed and tested on Ubuntu 16.04


### Requirements
* Python(version 2.7)
  - Installation: $ sudo apt install python2.7 python-pip
  
* PIL 
  - Installation: $ sudo apt install python-pil

* SKLearn/scikit-learn 
  - Installation: $ pip install scikit-learn==0.18.1

* Numpy 
  - Installation: $ pip install numpy

* Scipy 
  - Installation: $ pip install scipy 

* tqdm 
  - Installation: $ pip install tqdm

### USAGE
#### 1. Command to run the image edit detection tool:
+ Go to the folder ImageForensicsTool
+ Open Terminal
+ $ chmod +x ImageForensicsTool 
+ $ ./ImageForensicsTool fullImageFilename

Test: ./ImageForensicsTool testImages/a.jpg

Input Image:

<img src="https://raw.githubusercontent.com/sejaljain1194/image-forensics-tool/master/screenshots/a.png" width="200">

Terminal: The image seems to be edited.

Copy Move detected Image: 

<img src="https://raw.githubusercontent.com/sejaljain1194/image-forensics-tool/master/screenshots/20180623_031816_lined_a.jpg" width="200">

#### 2. Command to run ELA tool:
+ Go to the folder ela/dist/ela
+ Open Terminal
+ $ ./ela originalimage fakeimage

Expected Output:


