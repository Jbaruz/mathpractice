import os
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QColor, QPalette, QImage, QBrush
from PyQt5.QtCore import QSize, Qt

class CustomButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def sizeHint(self):
        size = super().sizeHint()
        return QSize(size.width() * 2, size.height() * 2)  # Adjust the size as desired


class MathPracticeApp(QMainWindow):
    operation_to_key = {
    '+': 'addition',
    '-': 'subtraction',
    '*': 'multiplication'
    }
    
    def generate_question(self,user_weaknesses):
        total_weaknesses = sum(user_weaknesses.values())
        if total_weaknesses == 0:
            operation = random.choice(["+", "-", "*"])
        else:
            operation = random.choices(
                ["+", "-", "*"],
                weights=[user_weaknesses["addition"], user_weaknesses["subtraction"], user_weaknesses["multiplication"]],
                k=1
            )[0]

        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        answer = eval(f" {num1} {operation} {num2}")

        return {
            'question': f"What is {num1} {operation} {num2}?",
            'answer': round(answer, 2),
            'operation': operation
        }
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Math Practice")
        self.setGeometry(100, 100, 560, 400)

        image_path = self.resource_path("ava.png")


        self.layout = QVBoxLayout()

        self.label = QLabel("Enter your name\nAva is watching you:")
        self.layout.addWidget(self.label)

        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        self.start_button = QPushButton("Start Math Practice")
        self.layout.addWidget(self.start_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Add your name to the bottom of the application
        self.credit_label = QLabel("Created by Jbaruz")
        self.credit_label.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.credit_label)

        self.start_button.clicked.connect(self.start_math_practice)

        # Customizations
        self.customize_widgets()
    
    def start_math_practice(self):
        self.user_name = self.name_input.text()
        self.score = 0
        self.current_question = 0

        self.layout.removeWidget(self.label)
        self.label.deleteLater()
        self.layout.removeWidget(self.name_input)
        self.name_input.deleteLater()
        self.layout.removeWidget(self.start_button)
        self.start_button.deleteLater()

        self.question_label = QLabel()
        self.layout.addWidget(self.question_label)

        self.answer_input = QLineEdit()
        self.layout.addWidget(self.answer_input)

        self.submit_button = QPushButton("Submit Answer")
        self.layout.addWidget(self.submit_button)

        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)

        # Set font for the new widgets
        custom_font = QFont("Arial", 16)
        self.question_label.setFont(custom_font)
        self.result_label.setFont(custom_font)

        self.user_weaknesses = {"addition": 0, "subtraction": 0, "multiplication": 0}
        self.questions = [self.generate_question(self.user_weaknesses) for _ in range(10)]

        self.submit_button.clicked.connect(self.check_answer)

        self.show_question()

        
        # Initialize user_name attribute
        self.user_name = ""

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def customize_widgets(self):
        # Set font
        custom_font = QFont("Arial", 16)
        self.label.setFont(custom_font)


        # Set text color
        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, QColor("blue"))
        self.label.setPalette(palette)

        # Set background color
        palette = self.central_widget.palette()
        palette.setColor(QPalette.Background, QColor(173, 216, 230, 128))
        self.central_widget.setAutoFillBackground(True)
        self.central_widget.setPalette(palette)

        # Set background image
        image_path = self.resource_path("ava.png")
        image = QImage(image_path)
        image = image.scaled(560, 400)  # Adjust the size of the image to fit the window
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(image))
        self.setPalette(palette)

    # Method to show the current question or display the final score
    def show_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            # Display the current question
            self.question_label.setText(f"Operation {self.current_question + 1}: {question['question']}")
        else:
            # If all questions have been answered, display the user's score
            if self.score >= 7:
                self.question_label.setText(f"Congratulations, {self.user_name}! Your score is {self.score}/{len(self.questions)}. Keep up the good work!")
            else:
                self.question_label.setText(f"{self.user_name}, your score is {self.score}/{len(self.questions)}. Don't give up, keep practicing!")

            # Create and display the "Play Again" button
            self.play_again_button = QPushButton("Play Again")
            self.layout.addWidget(self.play_again_button)
            self.play_again_button.clicked.connect(self.reset_app)
            
    def check_answer(self):
        user_answer = self.answer_input.text()

        try:
            user_answer = float(user_answer)
        except ValueError:
            self.result_label.setText(
                f"{self.user_name}, invalid input. Please enter a number")
            return

        question = self.questions[self.current_question]
        if round(user_answer, 2) == question['answer']:
            self.result_label.setText(
                f"Unbeliavable {self.user_name} it was correct!")
            self.score += 1
        else:
            self.result_label.setText(
                f"Sorry {self.user_name} it is incorrect!. The correct answer is {question['answer']}.")
            self.user_weaknesses[self.operation_to_key[question["operation"]]] += 1

        
        self.current_question += 1
        self.show_question()
        self.answer_input.clear()

        
    def reset_app(self):
        # Remove the current widgets from the layout
        self.layout.removeWidget(self.question_label)
        self.question_label.deleteLater()
        self.layout.removeWidget(self.answer_input)
        self.answer_input.deleteLater()
        self.layout.removeWidget(self.submit_button)
        self.submit_button.deleteLater()
        self.layout.removeWidget(self.result_label)
        self.result_label.deleteLater()
        self.layout.removeWidget(self.play_again_button)
        self.play_again_button.deleteLater()

        # Recreate the initial widgets and set up the layout
        self.label = QLabel("Enter your name:")
        self.layout.addWidget(self.label)
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)
        self.start_button = QPushButton("Start Math Practice")
        self.layout.addWidget(self.start_button)
        self.start_button.clicked.connect(self.start_math_practice)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        QPushButton {
            background-color: lightblue;
            font-size: 24px;
            font-family: 'Comic Sans MS';
            color: yellow;
            padding: 10px 5px;
            border-radius: 5px;
            font-weight: bold;
            margin: 30px 74px 0px 74px;
        }
        QPushButton:hover {
            background-color: blue;
        }
        QLabel {
            color: darkblue;
            font-family: 'Comic Sans MS';
            font-size: 20px;
        }
        QLineEdit {
            background-color: white;
            color: darkblue;
            font-family: 'Comic Sans MS';
            font-size: 20px;
            border: 1px solid lightblue;
            border-radius: 5px;
            padding: 5px;
            margin: 10px 95px 0px 95px;
        }
    """)

    main_window = MathPracticeApp()
    main_window.show()
    sys.exit(app.exec_())