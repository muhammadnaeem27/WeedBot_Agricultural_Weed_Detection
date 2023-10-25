import tkinter as tk
from PIL import ImageTk, Image
import subprocess

def run_test_program():
    #test.py program
    subprocess.call(["python", r"D:\Finalyearproject\yolov5-20230513T175146Z-001\yolov5\testt.py"])
    print("Test program completed.")

def run_roboflow_program():
    #roboflow_api.py program
    subprocess.call(["python", r"D:\Finalyearproject\yolov5-20230513T175146Z-001\yolov5\roboflow_api.py"])
    print("Roboflow program completed.")

def quit_program():
    # Close the GUI window
    root.destroy()

# HUI MAIN CODE
root = tk.Tk()

# our title
root.title("AGRO AI")

# Set the window size
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load the image
image_path = r"D:\FYP documnets\yolov5-flask updated\yolov5-flaskl\templates\web\images\agro_small_logo.png"
image = Image.open(image_path)
image = image.resize((window_width // 2, window_height))
image_tk = ImageTk.PhotoImage(image)


image_label = tk.Label(root, image=image_tk)# Create a label to display the image
image_label.pack(side=tk.LEFT, padx=10, pady=10)


button_frame = tk.Frame(root)# Create a frame for the buttons
button_frame.pack(side=tk.LEFT, padx=10, pady=10)


btn_test = tk.Button(button_frame, text="Generate Results", command=run_test_program, height=2, width=30)#  "Generate Results" button
btn_test.pack(pady=10)


btn_roboflow = tk.Button(button_frame, text="Find Coordinates", command=run_roboflow_program, height=2, width=30)# "Find Coordinates" button
btn_roboflow.pack(pady=10)


btn_quit = tk.Button(button_frame, text="Quit", command=quit_program, height=2, width=30)# "Quit" button
btn_quit.pack(pady=10)


root.mainloop()# Run the GUI event loop beacuse we want continous display of the window
