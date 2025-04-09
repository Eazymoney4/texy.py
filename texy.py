import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        
        # Calculate simple interest
        interest = (principal * rate * time) / 100
        total_amount = principal + interest
        
        result_label.config(text=f"Calculated Interest: ${interest:.2f}\nTotal Amount: ${total_amount:.2f}")
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Interest Calculator")

# Create and place the input fields and labels
tk.Label(root, text="Principal Amount ($):").grid(row=0, column=0, padx=10, pady=10)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

tk.Label(root, text="Rate of Interest (%):").grid(row=1, column=0, padx=10, pady=10)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1)

tk.Label(root, text="Time (years):").grid(row=2, column=0, padx=10, pady=10)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1)

# Create the Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, columnspan=2, pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 10))
result_label.grid(row=4, columnspan=2)

# Start the Tkinter event loop
root.mainloop()