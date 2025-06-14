import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())   
        height = float(height_entry.get())      

        if weight <= 0 or height <= 0:         
            messagebox.showerror("Invalid input", "Please enter positive numbers.")
            return

        bmi = weight / (height ** 2)          
        bmi_value = f"{bmi:.2f}"                

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"Your BMI is: {bmi_value}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Fonts
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
# Add label and box for weight input
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# Add label and box for height input
tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Add button to calculate BMI
calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()



