import random
import tkinter as tk



def computer_choice():
    return random.choice(["Kamień", "Papier", "Nożyce"])


def play(user_choice):
    comp_choice = computer_choice()
    result = ""
    if user_choice == comp_choice:
        result = "Remis!"
    elif (user_choice == "Papier" and comp_choice == "Kamień") or \
        (user_choice == "Kamień" and comp_choice == "Nożyce") or \
        (user_choice == "Nożyce" and comp_choice == "Papier"):
        result = "Wygrałeś"
    else:
        result = "Przegrałeś!"

    user_label.config(text=f"Twój wybór: {user_choice}", font="Times 15")
    computer_label.config(text=f"Wybór komputera: {comp_choice}", font="Times 15")
    result_label.config(text=result, font="Times 15 bold")


root = tk.Tk()
root.title("Kamień-Papier-Nożyce")
root.geometry("800x500")

user_label = tk.Label(root, text="Twój wybór: ", font="Times 15")
user_label.pack(pady=20)
computer_label = tk.Label(root, text="Wybór komputera: ", font="Times 15")
computer_label.pack(pady=20)
result_label = tk.Label(root, text="", font="Times 15")
result_label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=30)

rock_button = tk.Button(buttons_frame, text="Kamień", font="Times 15", bg="pink", command=lambda: play("Kamień"))
rock_button.grid(row=0, column=0, padx=10)
paper_button = tk.Button(buttons_frame, text="Papier", font="Times 15", bg="pink", command=lambda: play("Papier"))
paper_button.grid(row=0, column=1, padx=10)
scissors_button = tk.Button(buttons_frame, text="Nożyce", font="Times 15", bg="pink", command=lambda: play("Nożyce"))
scissors_button.grid(row=0, column=2, padx=10)
quit_button = tk.Button(root, text="Wyjście", font="Times 12", bg="grey", command=root.quit)
quit_button.pack(side="bottom", anchor="se", pady=10, padx=10)

root.mainloop()



