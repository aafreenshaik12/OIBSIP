import tkinter as tk
from tkinter import messagebox

# ---------- BMI Calculation ----------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#FFD54F"
            compliment = "You are lighter than the healthy range. A balanced diet can help you stay healthy!"
        elif bmi < 25:
            category = "Normal Weight"
            color = "#81C784"
            compliment = "Excellent! Your BMI is in the healthy range. Keep maintaining your healthy lifestyle!"
        elif bmi < 30:
            category = "Overweight"
            color = "#FFB74D"
            compliment = "You're doing well! A little more exercise and a balanced diet can help you reach your goal."
        else:
            category = "Obese"
            color = "#EF5350"
            compliment = "Every journey starts with one step. Stay positive and focus on healthy habits!"

        result_frame.config(bg=color)
        result_label.config(
            text=f"BMI : {bmi:.2f}\nCategory : {category}",
            bg=color,
            fg="white"
        )

        compliment_label.config(
            text=compliment,
            bg=color,
            fg="white"
        )

    except:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid positive numbers."
        )

# ---------- Reset ----------
def reset():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_frame.config(bg="#F5F5F5")
    result_label.config(text="", bg="#F5F5F5")
    compliment_label.config(text="", bg="#F5F5F5")


# ---------- Window ----------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("430x520")
root.configure(bg="#E3F2FD")
root.resizable(False, False)

# ---------- Heading ----------
title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Segoe UI", 22, "bold"),
    bg="#E3F2FD",
    fg="#1565C0"
)
title.pack(pady=20)

# ---------- Weight ----------
tk.Label(
    root,
    text="Weight (kg)",
    font=("Segoe UI", 12),
    bg="#E3F2FD"
).pack()

weight_entry = tk.Entry(
    root,
    font=("Segoe UI", 13),
    justify="center",
    width=18
)
weight_entry.pack(pady=8)

# ---------- Height ----------
tk.Label(
    root,
    text="Height (m)",
    font=("Segoe UI", 12),
    bg="#E3F2FD"
).pack()

height_entry = tk.Entry(
    root,
    font=("Segoe UI", 13),
    justify="center",
    width=18
)
height_entry.pack(pady=8)

# ---------- Buttons ----------
button_frame = tk.Frame(root, bg="#E3F2FD")
button_frame.pack(pady=20)

calc_btn = tk.Button(
    button_frame,
    text="Calculate BMI",
    font=("Segoe UI", 11, "bold"),
    bg="#1976D2",
    fg="white",
    padx=15,
    command=calculate_bmi
)
calc_btn.grid(row=0, column=0, padx=10)

reset_btn = tk.Button(
    button_frame,
    text="Reset",
    font=("Segoe UI", 11, "bold"),
    bg="#757575",
    fg="white",
    padx=20,
    command=reset
)
reset_btn.grid(row=0, column=1)

# ---------- Result Box ----------
result_frame = tk.Frame(
    root,
    bg="#F5F5F5",
    width=340,
    height=170,
    bd=2,
    relief="groove"
)
result_frame.pack(pady=20)

result_frame.pack_propagate(False)

result_label = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI", 16, "bold"),
    bg="#F5F5F5"
)
result_label.pack(pady=(25,10))

compliment_label = tk.Label(
    result_frame,
    text="",
    font=("Segoe UI", 11),
    wraplength=300,
    justify="center",
    bg="#F5F5F5"
)
compliment_label.pack()

# ---------- Footer ----------
footer = tk.Label(
    root,
    text="Stay Healthy • Stay Happy",
    font=("Segoe UI", 10, "italic"),
    bg="#E3F2FD",
    fg="#546E7A"
)
footer.pack(side="bottom", pady=10)

root.mainloop()