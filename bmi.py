import math
import tkinter as tk


def lbs_to_kg(lbs):
    return lbs * 0.453592


def feet_to_meters(feet):
    return feet * 0.3048


def inches_to_meters(inches):
    return inches * 0.0254


def calculate_bmi():
    try:
        # Get weight values
        weight_input = float(weight_entry.get())
        weight_unit = weight_unit_var.get().lower()

        if weight_unit == "lbs":
            weight_kg = lbs_to_kg(weight_input)
        elif weight_unit == "kg":
            weight_kg = weight_input
        else:
            result_label.config(text="Invalid weight unit.")
            return

        # Get height values
        height_input = float(height_entry.get())
        height_unit = height_unit_var.get().lower()

        if height_unit == "feet":
            height_m = feet_to_meters(height_input)
        elif height_unit == "inches":
            height_m = inches_to_meters(height_input)
        elif height_unit == "meters":
            height_m = height_input
        else:
            result_label.config(text="Invalid height unit.")
            return

        if height_m <= 0:
            result_label.config(text="Height must be greater than zero.")
            return

        # Calculate BMI
        bmi = weight_kg / (math.pow(height_m, 2))

        # Determine BMI category
        if bmi < 16:
            category = "Your shadow is starting to argue with you about who's thinner."
        elif 16 <= bmi < 17:
            category = "You could slip through a picket fence, but maybe grab a sandwich first?"
        elif 17 <= bmi < 18.5:
            category = "The wind whispers your name...and almost carries you away."
        elif 18.5 <= bmi < 25:
            category = "You're perfectly average, in a wonderfully un-alarming way."
        elif 25 <= bmi < 30:
            category = "You're not fat, you're just...extra huggable."
        elif 30 <= bmi < 35:
            category = "You've got a lot of personality...and a bit more of everything"
        elif 35 <= bmi < 40:
            category = "You're living proof that more is more...more cushion, more to love!"
        else:
            category = "You're not just big, you're a whole mood."

        result_label.config(text=f"BMI: {bmi:.2f}\n{category}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter numeric values.")


# Create main window
window = tk.Tk()
window.title("BMI Calculator")

# Weight section
weight_frame = tk.LabelFrame(window, text="Weight Information", padx=10, pady=10)
weight_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

weight_label = tk.Label(weight_frame, text="Your Weight:")
weight_label.grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(weight_frame)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

weight_unit_label = tk.Label(weight_frame, text="Unit:")
weight_unit_label.grid(row=0, column=2, padx=5, pady=5)
weight_unit_var = tk.StringVar(value="kg")
weight_unit_menu = tk.OptionMenu(weight_frame, weight_unit_var, "kg", "lbs")
weight_unit_menu.grid(row=0, column=3, padx=5, pady=5)

# Height section
height_frame = tk.LabelFrame(window, text="Height Information", padx=10, pady=10)
height_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

height_label = tk.Label(height_frame, text="Your Height:")
height_label.grid(row=0, column=0, padx=5, pady=5)
height_entry = tk.Entry(height_frame)
height_entry.grid(row=0, column=1, padx=5, pady=5)

height_unit_label = tk.Label(height_frame, text="Unit:")
height_unit_label.grid(row=0, column=2, padx=5, pady=5)
height_unit_var = tk.StringVar(value="meters")
height_unit_menu = tk.OptionMenu(height_frame, height_unit_var, "meters", "feet", "inches")
height_unit_menu.grid(row=0, column=3, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, pady=10)

# Result label
result_label = tk.Label(window, text="", wraplength=300)
result_label.grid(row=3, column=0, pady=10)

window.mainloop()