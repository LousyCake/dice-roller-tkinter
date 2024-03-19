import tkinter as tk
import random

class DiceRollerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Roller")
        self.master.configure(bg="#d8b9c3")
        self.master.geometry("300x200")
        
        self.dice = [1, 2, 3, 4, 5, 6]

        self.roll_button = tk.Button(master, text="Roll Dice", command=self.roll_dice, bg="#7d529e", fg="white", font=("Arial", 12, "bold"))
        self.roll_button.pack(pady=10)

        self.clear_button = tk.Button(master, text="Clear Result", command=self.clear_result, bg="#7d529e", fg="white", font=("Arial", 12, "bold"))
        self.clear_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", bg="#d8b9c3", fg="#4c337c", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

    def roll_dice(self):
        value1 = random.choice(self.dice)
        value2 = random.choice(self.dice)
        result = f"Dice 1: {value1}\nDice 2: {value2}"
        self.result_label.config(text=result)

    def clear_result(self):
        self.result_label.config(text="")

def main():
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
