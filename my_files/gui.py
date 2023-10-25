import tkinter as tk
from tkinter import filedialog
import subprocess

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg")])
    entry_path.delete(0, tk.END)
    entry_path.insert(tk.END, filepath)

def run_detection():
    source_path = entry_path.get()
    cmd = f"python D:\Finalyearproject\yolov5-20230513T175146Z-001\yolov5\detect.py --weights D:\Finalyearproject\yolov5-20230513T175146Z-001\yolov5\best.pt --img 416 --conf 0.2 --source \"{source_path}\""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout
    # Display the output in a text box or any other suitable way

# Create the GUI window
window = tk.Tk()
window.title("Object Detection Application")

# Source path input and browse button
frame_input = tk.Frame(window)
frame_input.pack(pady=10)

label_path = tk.Label(frame_input, text="Source Path:")
label_path.pack(side=tk.LEFT)

entry_path = tk.Entry(frame_input, width=50)
entry_path.pack(side=tk.LEFT)

button_browse = tk.Button(frame_input, text="Browse", command=browse_file)
button_browse.pack(side=tk.LEFT)

# Run button
button_run = tk.Button(window, text="Run Detection", command=run_detection)
button_run.pack(pady=10)

# Output display (e.g., text box) - Add your desired widget here

# Start the GUI event loop
window.mainloop()
