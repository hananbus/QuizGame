from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QuizApp")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(height=250, width=400, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(200, 125, width=380, text="", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 20, "italic"), fg="white")
        self.score_label.grid(row=0, column=1)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.right_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_correct_answer = self.quiz.check_answer("True")
        self.give_feedback(is_correct_answer)

    def false_pressed(self):
        is_correct_answer = self.quiz.check_answer("False")
        self.give_feedback(is_correct_answer)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
