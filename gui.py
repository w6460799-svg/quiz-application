import tkinter as tk
from tkinter import ttk

from backend import (
    get_questions,
    get_result_message,
    get_percentage,
    calculate_score,
)


class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Quiz Application")
        self.geometry("900x650")
        self.minsize(800, 550)
        self.configure(bg="#f4f7fb")

        self.questions = get_questions()
        self.current_index = 0
        self.selected_answers = {}
        self.selected_answer = None

        self.configure_styles()
        self.build_ui()
        self.show_question()

    def configure_styles(self):
        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        self.style.configure("TFrame", background="#f4f7fb")
        self.style.configure(
            "Header.TLabel",
            background="#f4f7fb",
            foreground="#1f2937",
            font=("Segoe UI", 26, "bold"),
        )
        self.style.configure(
            "Question.TLabel",
            background="#f4f7fb",
            foreground="#111827",
            font=("Segoe UI", 18, "bold"),
            wraplength=760,
        )
        self.style.configure(
            "SubLabel.TLabel",
            background="#f4f7fb",
            foreground="#4b5563",
            font=("Segoe UI", 12),
        )
        self.style.configure(
            "Score.TLabel",
            background="#f4f7fb",
            foreground="#2563eb",
            font=("Segoe UI", 14, "bold"),
        )
        self.style.configure(
            "Option.TButton",
            font=("Segoe UI", 12),
            padding=(18, 12),
            background="#ffffff",
            foreground="#111827",
        )
        self.style.map(
            "Option.TButton",
            background=[("active", "#dbeafe"), ("pressed", "#bfdbfe")],
            foreground=[("active", "#111827"), ("pressed", "#111827")],
        )
        self.style.configure(
            "Primary.TButton",
            font=("Segoe UI", 12, "bold"),
            background="#2563eb",
            foreground="white",
        )
        self.style.map(
            "Primary.TButton",
            background=[("active", "#1d4ed8"), ("pressed", "#1e40af")],
            foreground=[("active", "white"), ("pressed", "white")],
        )
        self.style.configure(
            "Secondary.TButton",
            font=("Segoe UI", 12),
            background="#e5e7eb",
            foreground="#111827",
        )
        self.style.map(
            "Secondary.TButton",
            background=[("active", "#d1d5db"), ("pressed", "#c2c7cf")],
            foreground=[("active", "#111827"), ("pressed", "#111827")],
        )
        self.style.configure("Card.TFrame", background="#ffffff", relief="flat", borderwidth=1)

    def build_ui(self):
        container = ttk.Frame(self, padding=24)
        container.pack(fill="both", expand=True)

        top_bar = ttk.Frame(container, style="TFrame")
        top_bar.pack(fill="x", pady=(0, 12))

        self.title_label = ttk.Label(
            top_bar,
            text="Python Quiz Challenge",
            style="Header.TLabel",
            anchor="w",
        )
        self.title_label.pack(side="left", fill="x", expand=True)

        self.score_label = ttk.Label(
            top_bar,
            text="Score: 0",
            style="Score.TLabel",
            anchor="e",
        )
        self.score_label.pack(side="right")

        self.progress_frame = ttk.Frame(container, style="TFrame")
        self.progress_frame.pack(fill="x", pady=(0, 10))

        self.progress_label = ttk.Label(
            self.progress_frame,
            text="Progress: 0 / 10",
            style="SubLabel.TLabel",
            anchor="w",
        )
        self.progress_label.pack(side="left", fill="x", expand=True)

        self.progress_var = tk.DoubleVar(value=0)
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            variable=self.progress_var,
            maximum=100,
            length=650,
            mode="determinate",
        )
        self.progress_bar.pack(side="right", fill="x", expand=True, padx=(12, 0))

        self.card = ttk.Frame(container, style="Card.TFrame", padding=20)
        self.card.pack(fill="both", expand=True)

        self.question_number_label = ttk.Label(
            self.card,
            text="Question 1",
            style="SubLabel.TLabel",
            anchor="w",
        )
        self.question_number_label.pack(anchor="w", pady=(0, 12))

        self.question_label = ttk.Label(
            self.card,
            text="",
            style="Question.TLabel",
            justify="left",
            anchor="nw",
        )
        self.question_label.pack(anchor="nw", fill="x", pady=(0, 18))

        self.options_frame = ttk.Frame(self.card, style="TFrame")
        self.options_frame.pack(fill="both", expand=True)

        self.option_buttons = []

        for i in range(4):
            btn = ttk.Button(
                self.options_frame,
                text="",
                style="Option.TButton",
                command=lambda idx=i: self.select_option(idx),
            )
            btn.pack(fill="x", pady=4)
            self.option_buttons.append(btn)

        self.navigation_frame = ttk.Frame(container, style="TFrame")
        self.navigation_frame.pack(fill="x", pady=(18, 0))

        self.next_button = ttk.Button(
            self.navigation_frame,
            text="Next",
            style="Primary.TButton",
            command=self.next_question,
        )
        self.next_button.pack(side="right")

    def show_question(self):
        if self.current_index >= len(self.questions):
            self.show_results()
            return

        question_data = self.questions[self.current_index]
        current_question_number = self.current_index + 1

        self.question_number_label.config(text=f"Question {current_question_number}")
        self.question_label.config(text=question_data["question"])

        for idx, option_text in enumerate(question_data["options"]):
            self.option_buttons[idx].config(text=option_text)
            self.option_buttons[idx].state(["!disabled"])

        self.selected_answer = None
        self.next_button.config(state="disabled")

        answered = self.selected_answers.get(self.current_index)
        if answered is not None:
            self.select_option(self.option_index_for_letter(answered), update_button_only=True)

        self.update_progress()

    def option_index_for_letter(self, letter):
        letter_map = {"A": 0, "B": 1, "C": 2, "D": 3}
        return letter_map.get(letter.upper(), 0)

    def select_option(self, index, update_button_only=False):
        for i, button in enumerate(self.option_buttons):
            if i == index:
                button.state(["pressed"])
                button.configure(style="Primary.TButton")
            else:
                button.state(["!pressed"])
                button.configure(style="Option.TButton")

        self.selected_answer = self.get_letter_for_index(index)
        if not update_button_only:
            self.next_button.config(state="normal")

    def get_letter_for_index(self, index):
        letters = ["A", "B", "C", "D"]
        return letters[index]

    def next_question(self):
        if self.selected_answer is None:
            return

        self.selected_answers[self.current_index] = self.selected_answer

        if self.current_index < len(self.questions) - 1:
            self.current_index += 1
            self.show_question()
        else:
            self.show_results()

    def update_progress(self):
        answered_count = len(self.selected_answers)
        total_questions = len(self.questions)
        percent = (answered_count / total_questions) * 100 if total_questions else 0
        self.progress_var.set(percent)
        self.progress_label.config(text=f"Progress: {answered_count} / {total_questions}")
        self.score_label.config(text=f"Score: {self.calculate_current_score()}")

    def calculate_current_score(self):
        score = 0
        for index, question in enumerate(self.questions):
            user_answer = self.selected_answers.get(index)
            if user_answer and user_answer == question["answer"]:
                score += 1
        return score

    def show_results(self):
        self.card.pack_forget()
        self.progress_frame.pack_forget()
        self.navigation_frame.pack_forget()

        results_frame = ttk.Frame(self, padding=30, style="TFrame")
        results_frame.pack(fill="both", expand=True)

        title = ttk.Label(results_frame, text="Quiz Complete!", style="Header.TLabel")
        title.pack(pady=(0, 10))

        total_questions = len(self.questions)
        final_score = calculate_score(
            [self.selected_answers.get(i, "") for i in range(total_questions)],
            self.questions,
        )
        percentage = get_percentage(final_score, total_questions)
        message = get_result_message(final_score, total_questions)

        ttk.Label(results_frame, text=f"Your score: {final_score} / {total_questions}", style="Question.TLabel").pack(pady=6)
        ttk.Label(results_frame, text=f"Percentage: {percentage}%", style="Question.TLabel").pack(pady=6)
        ttk.Label(results_frame, text=message, style="SubLabel.TLabel").pack(pady=(16, 8))

        correct_answers_frame = ttk.LabelFrame(results_frame, text="Correct Answers", padding=16)
        correct_answers_frame.pack(fill="x", pady=(10, 16))

        for index, question_data in enumerate(self.questions, start=1):
            ttk.Label(
                correct_answers_frame,
                text=f"{index}. {question_data['answer']}",
                font=("Segoe UI", 12),
                background="#ffffff",
            ).pack(anchor="w", pady=3)

        button_frame = ttk.Frame(results_frame, style="TFrame")
        button_frame.pack(pady=(18, 0))

        restart_btn = ttk.Button(
            button_frame,
            text="Restart Quiz",
            style="Primary.TButton",
            command=self.restart_quiz,
        )
        restart_btn.pack(side="left", padx=(0, 10))

        exit_btn = ttk.Button(
            button_frame,
            text="Exit",
            style="Secondary.TButton",
            command=self.destroy,
        )
        exit_btn.pack(side="left")

    def restart_quiz(self):
        self.current_index = 0
        self.selected_answers = {}
        self.selected_answer = None
        self.progress_var.set(0)
        self.score_label.config(text="Score: 0")

        if hasattr(self, "card") and self.card.winfo_ismapped():
            self.card.pack_forget()

        self.build_ui()
        self.show_question()


if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
