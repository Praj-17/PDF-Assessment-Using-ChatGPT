## How to setup the code

### Step-1: Setup Envirnoment
Create a python envirnoment preferrably `3.9.0` and install all the requirements as stated in `requirements.txt`. Using the following command

```
pip install -r requirements.txt
```

### Step-2: Install Tesseract

This is a required dependancy to perform the OCR using Tesseract.

Download and install tesseract-OCR from the following link

```
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
```
### Step-3: Set path for Tesseract

Navigate to `C://Program Files//Tesseract-OCR` and add it to your system envirnoment variable.

### Step-4: Install Poppler

Unzip the `Release 23.11.0` folder and move the  `Poppler 23.11.0` folder to `C://Program Files`

### Step-5: Set path for Poppler

Navigate to `C:\Program Files\poppler-23.10.0\Library\bin` copy the path and set it as the envirnoment variable.

___

## Running the code

Navigate to the directory and run 

```
python main.py
```
By default it will take a pdf from the data folder and perform OCR using both `tesseract` and `easyocr` you can customize this in the code. 

Also a `Speeach Recognition` module is been integrated which runs after the OCR code. By default it accepts voice as input and does not accept a `.mp3` or any other sort of `audio ` file. 

___ 
## Examples

Refer the `output` folder to checkout the OCR extraction output. It is not very good as of now. 
