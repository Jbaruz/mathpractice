
# GUI math practice

It is an application that helps kids, like my daughter, learn mathematical operations, focusing on negative and positive integer numbers (Multiplication, substraction, addition).

Aditionally, the application is adapted from the math practice according to the user's weaknesses used a simple ruled-based sistem.

The 'generate_question' method in the 'MathPracticeApp; class generates questions based on the user's poerformance in previous questions. If the use has a weakness in a certain operation (addition, subtraction or multiplication), the method will be more likely to generate questions with that operation. The reuled-based system is based on the user's incorrect answers, and the weights for each operation are adjusted accordingly in the 'user_weaknesses' dictionary.

## Features

1. The application starts by importing the necessary libraries and creating a MathPracticeApp class which inherits from QMainWindow.
2. The main window of the app is set up in the __init__ method with a QVBoxLayout layout and widgets for entering the user's name and starting the math practice.
3. The generate_question function is responsible for creating random math questions based on the user's weaknesses.
4. When the user clicks the "Start Math Practice" button, the start_math_practice method is called, which sets up the layout for the actual math practice, generates the questions, and connects the "Submit Answer" button to the check_answer method.
5. The check_answer method is called when the user submits an answer. It compares the user's answer to the correct answer, updates the user's score, and updates the user's weaknesses if the answer is incorrect.
6. The show_question method displays the next question or the final score and a "Play Again" button if all questions have been answered.
7. The reset_app method is called when the user clicks the "Play Again" button, resetting the application to its initial state.
Finally, the if __name__ == "__main__": block creates a QApplication instance, sets global styles for the application, creates and displays the main window, and starts the app's event loop.

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

![App Screenshot 5](https://github.com/Jbaruz/mathpractice/blob/master/images/display5.png?raw=true)

## Feedback

If you have any feedback, please reach out to us at jbaruz@gmail.com

