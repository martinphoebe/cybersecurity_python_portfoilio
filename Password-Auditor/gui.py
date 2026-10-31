import tkinter as tk
from tkinter import ttk
from main import check_password

# Main application window
root = tk.Tk()
root.title("Password Auditor")
root.geometry("520x580")
root.configure(bg="#111827")
root.resizable(False, False)

# Colours
BG = "#111827"
PANEL = "#1F2937"
ACCENT = "#38BDF8"
WHITE = "#F9FAFB"
GREY = "#9CA3AF"

# Title
title = tk.Label(
    root,
    text="PASSWORD AUDITOR",
    font=("Arial", 22, "bold"),
    bg=BG,
    fg=ACCENT
)
title.pack(pady=(30, 5))

subtitle = tk.Label(
    root,
    text="Cybersecurity Password Assessment Tool",
    font=("Arial", 10),
    bg=BG,
    fg=GREY
)
subtitle.pack(pady=(0, 30))

# Main panel
panel = tk.Frame(root, bg=PANEL, padx=25, pady=25)
panel.pack(padx=30, fill="x")

# Password label
tk.Label(
    panel,
    text="Enter password to analyse",
    font=("Arial", 11, "bold"),
    bg=PANEL,
    fg=WHITE
).pack(anchor="w", pady=(0, 10))

# Password input
password_entry = tk.Entry(
    panel,
    font=("Arial", 14),
    show="*",
    bg="#374151",
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)
password_entry.pack(fill="x", ipady=10)

# Show / hide password
show_password = tk.BooleanVar()

def toggle_password():
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

tk.Checkbutton(
    panel,
    text="Show password",
    variable=show_password,
    command=toggle_password,
    bg=PANEL,
    fg=GREY,
    selectcolor=PANEL,
    activebackground=PANEL,
    activeforeground=WHITE
).pack(anchor="w", pady=10)

# Results section
results = tk.Frame(root, bg=PANEL, padx=25, pady=20)
results.pack(padx=30, pady=20, fill="both", expand=True)

strength_label = tk.Label(
    results,
    text="Strength: Not assessed",
    font=("Arial", 15, "bold"),
    bg=PANEL,
    fg=WHITE
)
strength_label.pack(pady=10)

score_label = tk.Label(
    results,
    text="Security score: --/6",
    font=("Arial", 11),
    bg=PANEL,
    fg=GREY
)
score_label.pack(pady=5)

# Progress bar
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Custom.Horizontal.TProgressbar",
    troughcolor="#374151",
    background=ACCENT,
    bordercolor=PANEL
)

progress = ttk.Progressbar(
    results,
    style="Custom.Horizontal.TProgressbar",
    length=350,
    maximum=6
)
progress.pack(pady=15)

# Recommendations
recommendations = tk.Label(
    results,
    text="Enter a password to begin your assessment.",
    font=("Arial", 10),
    bg=PANEL,
    fg=GREY,
    justify="left",
    wraplength=380
)
recommendations.pack(anchor="w", pady=10)

# Analyse password
def analyse_password():
    password = password_entry.get()

    if not password:
        strength_label.config(
            text="Please enter a password",
            fg="#F87171"
        )
        return

    score, strength, feedback = check_password(password)

    colours = {
        "Weak": "#F87171",
        "Moderate": "#FBBF24",
        "Strong": "#34D399"
    }

    strength_label.config(
        text=f"Strength: {strength}",
        fg=colours[strength]
    )

    score_label.config(
        text=f"Security score: {score}/6"
    )

    progress["value"] = score

    if feedback:
        message = "Recommendations:\n\n"
        message += "\n".join("- " + item for item in feedback)
    else:
        message = "No basic improvements identified."

    recommendations.config(text=message)

# Analyse button
analyse_button = tk.Button(
    panel,
    text="ANALYSE PASSWORD",
    command=analyse_password,
    font=("Arial", 11, "bold"),
    bg=ACCENT,
    fg="#111827",
    activebackground="#0EA5E9",
    relief="flat",
    cursor="hand2"
)
analyse_button.pack(fill="x", pady=(15, 0), ipady=10)

# Footer
tk.Label(
    root,
    text="Educational security tool | Python",
    font=("Arial", 9),
    bg=BG,
    fg=GREY
).pack(pady=12)

# Start application
root.mainloop()