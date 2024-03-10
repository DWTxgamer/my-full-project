import os
import tkinter as tk
import tkinter.filedialog as fd
from tkinter import ttk
import webview

root = tk.Tk()
root.geometry("800x600")
root.title("Desktop App")

# create a ttk Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# ask user to select the HTML file
html_file_path = fd.askopenfilename(filetypes=[("HTML Files", "*.html")])
if not html_file_path:
    exit()

# get the directory of the HTML file
html_dir = os.path.dirname(html_file_path)

# create a ttk Frame widget for the HTML page
html_frame = ttk.Frame(notebook)
notebook.add(html_frame, text="HTML")

# create a WebView widget and pack it into the HTML frame
html_view = webview.create_window(html_frame.winfo_id())
html_view.load_url(html_file_path)

# ask user to select the CSS file
css_file_path = fd.askopenfilename(filetypes=[("CSS Files", "*.css")])
if not css_file_path:
    exit()

# get the directory of the CSS file
css_dir = os.path.dirname(css_file_path)

# create a ttk Frame widget for the CSS page
css_frame = ttk.Frame(notebook)
notebook.add(css_frame, text="CSS")

# create a WebView widget and pack it into the CSS frame
css_view = webview.create_window(css_frame.winfo_id())
css_view.load_url(css_file_path)

# ask user to select the image file
img_file_path = fd.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
if not img_file_path:
    exit()

# get the directory of the image file
img_dir = os.path.dirname(img_file_path)

# create a ttk Frame widget for the image
img_frame = ttk.Frame(notebook)
notebook.add(img_frame, text="Image")

# create a Label widget and pack it into the image frame
img = tk.PhotoImage(file=img_file_path)
img_label = tk.Label(img_frame, image=img)
img_label.pack()

root.mainloop()
