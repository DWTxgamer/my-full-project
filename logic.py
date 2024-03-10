import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()
window.title("My GUI")
window.geometry("400x300")

# Create a label widget
label = tk.Label(window, text="Hello World!", font=("Arial", 16))
label.pack(pady=20)

# Create a button widget
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

# Run the GUI event loop
window.mainloop()
