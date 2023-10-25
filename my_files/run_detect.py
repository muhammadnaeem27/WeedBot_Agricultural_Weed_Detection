import tkinter as tk
from tkinter import filedialog
import subprocess
from PIL import ImageTk, Image

# def run_script():
#     # Get the values from the input fields
#     weights = entry_weights.get()
#     img_size = entry_img_size.get()
#     confidence = entry_confidence.get()
#     image_path = entry_image_path.get()

#     # Construct the command to run the script
#     # command = f"detectcoordinates.py --weights {weights} --img {img_size} --conf {confidence} --source {image_path}"
#     command = f"detectcoordinates.py --weights {weights} --img {img_size} --conf {confidence} --source {image_path}"

#     # Run the script
#     subprocess.call(command, shell=True)
#     print("Script completed.")
def run_script():
    # Get the values from the input fields
    weights = entry_weights.get()
    img_size = entry_img_size.get()
    confidence = entry_confidence.get()
    image_path = entry_image_path.get()

    # Construct the command to run the script
    command = f"python detectcoordinates.py --weights {weights} --img {img_size} --conf {confidence} --source {image_path}"
    print(f"Command: {command}")


    try:
        # Run the script
        subprocess.check_call(command, shell=True)
        print("Script completed.")
        # Move the results to the latest exp folder
        subprocess.call("mv runs/exp /path/to/latest/exp", shell=True)
        print("Results moved to the latest exp folder.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def run_results():
    # script path : E:\FYP\yolo\yolo checking\yolov5\gui_code.py
    #construct the command to run the script
    command = f"python gui_code2.py"

    # Run the script
    subprocess.call(command, shell=True)
    print("Script completed.")

def quit_program():
    # Close the GUI window
    root.destroy()

def adjust_confidence(event):
    # Get the current confidence value
    current_confidence = float(entry_confidence.get())
    
    # Get the key code of the pressed key
    key = event.keysym

    # Adjust the confidence value based on the pressed key
    if key == 'Up':
        current_confidence += 0.1
    elif key == 'Down':
        current_confidence -= 0.1

    # Ensure the confidence value stays within the range of 0.1 to 1.0
    current_confidence = max(0.1, min(1.0, current_confidence))

    # Update the confidence entry field
    entry_confidence.delete(0, tk.END)
    entry_confidence.insert(0, str(current_confidence))

def browse_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("JPEG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")))

    # Update the image path entry field
    entry_image_path.delete(0, tk.END)
    entry_image_path.insert(0, file_path)

# Create the main window
root = tk.Tk()

# Set the window title
root.title("AGRO AI")

# Create a frame for the left column (containing the image)
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=20, pady=20)

# Load and display the image
# image_path = "agro_small_logo.png"
image_path = "agro_small_logo.png"
image = Image.open(image_path)
image = image.resize((300, 300))
image_tk = ImageTk.PhotoImage(image)
label_image = tk.Label(frame_left, image=image_tk)
label_image.pack()

# Create a frame for the right column (containing the input fields and buttons)
frame_right = tk.Frame(root)
frame_right.pack(side=tk.LEFT, padx=20, pady=20)

# Create labels and entry fields for the script arguments
label_weights = tk.Label(frame_right, text="Weights:")
label_weights.pack()
entry_weights = tk.Entry(frame_right, width=50)
entry_weights.pack()
entry_weights.insert(0, "best.pt")  # Set default weights value

label_img_size = tk.Label(frame_right, text="Image Size:")
label_img_size.pack()
entry_img_size = tk.Entry(frame_right, width=50)
entry_img_size.pack()
entry_img_size.insert(0, "416")  # Set default image size value

label_confidence = tk.Label(frame_right, text="Confidence:")
label_confidence.pack()
entry_confidence = tk.Entry(frame_right, width=50)
entry_confidence.pack()
entry_confidence.insert(0, "0.6")  # Set default confidence value

label_image_path = tk.Label(frame_right, text="Image Path or IP Path:")
label_image_path.pack()
entry_image_path = tk.Entry(frame_right, width=50)
entry_image_path.pack()

# Create the "Browse Image" button
btn_browse = tk.Button(frame_right, text="Browse Image", command=browse_image, height=2, width=30)
btn_browse.pack(pady=10)

# Create the "Run Script" button
btn_run = tk.Button(frame_right, text="Run Script", command=run_script, height=2, width=30)
btn_run.pack(pady=10)

# Create the "Check Results" button
btn_run = tk.Button(frame_right, text="Check Results", command=run_results, height=2, width=30)
btn_run.pack(pady=10)

# Create the "Quit" button
btn_quit = tk.Button(frame_right, text="Quit", command=quit_program, height=2, width=30)
btn_quit.pack(pady=10)

# Bind the arrow keys to the confidence adjustment function
root.bind("<Up>", adjust_confidence)
root.bind("<Down>", adjust_confidence)

# Run the GUI event loop
root.mainloop()
