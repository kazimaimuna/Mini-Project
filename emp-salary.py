import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Employee Payroll System")
root.geometry("700x600")
root.configure(bg="#202A44")

employees = [
    {"name": "Anil", "salary": 25000},
    {"name": "Priya", "salary": 30000},
    {"name": "Sona", "salary": 28000},
    {"name": "Jay", "salary": 35000},
    {"name": "Veer", "salary": 40000}
]

def display_employees():
    employee_list.delete(0, tk.END)

    for e in employees:
        employee_list.insert(
            tk.END,
            f'{e["name"]}       Rs. {e["salary"]}'
        )

def view_salary():
    selected = employee_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select an employee!"
        )
        return

    e = employees[selected[0]]

    annual = e["salary"] * 12

    messagebox.showinfo(
        "Payroll Details",
        f'Employee: {e["name"]}\n'
        f'Monthly Salary: Rs. {e["salary"]}\n'
        f'Annual Salary: Rs. {annual}'
    )

def total_salary():
    total = sum(e["salary"] for e in employees)

    messagebox.showinfo(
        "Total Payroll",
        f"Total Monthly Salary: Rs. {total}\n"
        f"Total Annual Salary: Rs. {total * 12}"
    )

# Main Heading
heading = tk.Label(
    root,
    text="EMPLOYEE PAYROLL SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#202A44",
    fg="#FFD166"
)
heading.pack(pady=25)

# Subtitle
tk.Label(
    root,
    text="Employee Salary Details",
    font=("Arial", 14, "bold"),
    bg="#202A44",
    fg="white"
).pack(pady=10)

# Employee List
employee_list = tk.Listbox(
    root,
    font=("Arial", 14),
    width=40,
    height=10,
    bg="#F1F5F9",
    fg="#202A44",
    selectbackground="#06A77D",
    selectforeground="white",
    bd=0
)
employee_list.pack(pady=20)

# View Salary Button
tk.Button(
    root,
    text="VIEW EMPLOYEE SALARY",
    font=("Arial", 12, "bold"),
    bg="#06A77D",
    fg="white",
    width=25,
    command=view_salary
).pack(pady=8)

# Total Salary Button
tk.Button(
    root,
    text="TOTAL PAYROLL",
    font=("Arial", 12, "bold"),
    bg="#457B9D",
    fg="white",
    width=25,
    command=total_salary
).pack(pady=8)

# Refresh Button
tk.Button(
    root,
    text="REFRESH LIST",
    font=("Arial", 12, "bold"),
    bg="#E9A23B",
    fg="black",
    width=25,
    command=display_employees
).pack(pady=8)

# Exit Button
tk.Button(
    root,
    text="EXIT",
    font=("Arial", 12, "bold"),
    bg="#D9534F",
    fg="white",
    width=25,
    command=root.destroy
).pack(pady=8)

display_employees()

root.mainloop()