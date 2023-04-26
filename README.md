
# GUI math practice

It is an application that helps kids, like my daughter, learn mathematical operations, focusing on negative and positive integer numbers.



## Documentation

 - [pythonguis](https://www.pythonguis.com/faq/adding-images-to-pyqt5-applications/)
 - [PyQt](https://wiki.python.org/moin/PyQt)


## Imported Modules

```python
import os
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QColor, QPalette, QImage, QBrush
from PyQt5.QtCore import QSize, Qt
```


## Features

- Math practice on a positive way
- Apply again
- Customizable according to user name
- Archive Example /dist/math_practiceGUI.exe


## Installation

To run the code be sure to install PyQt5

```bash
pip install PyQt5
```


## Deployment

To deploy this project run

Into the archive path
```bash
pyinstaller --onefile --windowed math_practices.py
```
In case, you want to change the code after create the application you have to use
```bash
pyinstaller math_practicesGUI.spec
```
## Screenshots

![App Screenshot 1](https://github.com/Jbaruz/mathpractice/blob/master/images/display1.png?raw=true)

![App Screenshot 2](https://github.com/Jbaruz/mathpractice/blob/master/images/display2.png?raw=true)

![App Screenshot 3](https://github.com/Jbaruz/mathpractice/blob/master/images/display3.png?raw=true)

![App Screenshot 4](https://github.com/Jbaruz/mathpractice/blob/master/images/dispplay4.png?raw=true)

## Feedback

If you have any feedback, please reach out to us at jbaruz@gmail.com

