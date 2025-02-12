import tkinter as tk
import time

# Define 10 different alien-style digit sets
alien_digit_sets = [
    {'0': '☀', '1': '☾', '2': '✺', '3': '☽', '4': '✧', '5': '✡', '6': '☍', '7': '☼', '8': 'CaCo2', '9': '✶'},
    {'0': '◎', '1': '●', '2': '★', '3': '✵', '4': '⚪', '5': '⨀', '6': '⨁', '7': '⬦', '8': '⊗', '9': '⟁'},
    {'0': '☾', '1': '♒', '2': '☯', '3': '✡', '4': '☽', '5': '⌘', '6': '⨀', '7': '⌘', '8': '☾', '9': '♈'},
    {'0': '0', '1': '⮌', '2': '⨅', '3': '⟁', '4': '⊗', '5': '⚛', '6': '⍈', '7': '⍂', '8': '⎈', '9': '⨐'},
    {'0': '⭥', '1': '♒', '2': '⟁', '3': '⨘', '4': '⍂', '5': '⩠', '6': '⊠', '7': '⨉', '8': '⍷', '9': '9'},
    {'0': '⊙', '1': '⩔', '2': 'O3', '3': '⨙', '4': '⨖', '5': '☿', '6': '⨏', '7': '⨤', '8': '8', '9': '⨉'},
    {'0': '⮌', '1': '⍋', '2': '⚗', '3': '⩯', '4': '⮛', '5': 'Au', '6': 'H2O', '7': '⩠', '8': '⟊', '9': '⩡'},
    {'0': '⏚', '1': '⊹', '2': '⩱', '3': '⍁', '4': '⨠', '5': '⨦', '6': '⩥', '7': '⨏', '8': '⭛', '9': 'Fe'},
    {'0': '✶', '1': '⚙', '2': '⧫', '3': '⨞', '4': 'K', '5': 'Mg', '6': '⩯', '7': '⊙', '8': '☽', '9': '⍂'},
    {'0': '⚒', '1': '⨎', '2': '⨿', '3': '⨳', '4': '⩯', '5': '⨈', '6': '⪧', '7': '⮟', '8': '!', '9': '⩩'}
]

# Function to convert time to alien-style using a custom set of symbols
def convert_to_alien_style(time_str, alien_set):
    return ''.join(alien_set.get(ch, ch) for ch in time_str)

# Function to update clocks
def update_clocks():
    current_time = time.localtime()
    time_str = time.strftime("%H:%M:%S", current_time)

    # Update each clock with its own alien symbols
    for i, clock_label in enumerate(clock_labels):
        alien_time_str = convert_to_alien_style(time_str, alien_digit_sets[i])
        clock_label.config(text=alien_time_str)

    # Call update_clocks again after 1 second
    root.after(1000, update_clocks)

# Create the main window
root = tk.Tk()
root.title("Alien Style Clocks")

# Create a frame to hold the clocks
frame = tk.Frame(root)
frame.pack(padx=30, pady=30)

# Create labels for 10 clocks (arranging them in 4 rows and 3 columns, with one in the last row)
clock_labels = []
for i in range(10):
    label = tk.Label(frame, font=("Courier", 30), fg="green", bg="black", width=15, height=2)
    label.grid(row=i//3, column=i%3, padx=20, pady=20)
    clock_labels.append(label)

# Start updating clocks
update_clocks()

# Start the Tkinter main loop
root.mainloop()
