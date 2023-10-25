from tkinter import Tk, filedialog
from roboflow import Roboflow
import os
import matplotlib.pyplot as plt
import numpy as np

rf = Roboflow(api_key="rU5VcejA2EM9BIMmdbWr")
project = rf.workspace().project("weed-classification")
model = project.version(8).model

def get_matrix_index(x1, y1, x2, y2, image_width, image_height, num_rows, num_cols):
    cell_width = image_width / num_cols
    cell_height = image_height / num_rows
    
    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2
    
    x_index = min(int(x_center / cell_width), num_cols - 1)
    y_index = min(int(y_center / cell_height), num_rows - 1)
    
    return x_index, y_index

def get_matrix_index2(x1, y1, x2, y2, image_width, image_height, num_rows, num_cols):
    cell_width = image_width / num_cols
    cell_height = image_height / num_rows

    # Calculate the center coordinates of the detected object
    x_center = (x1 + x2) / 2
    y_center = (y1 + y2) / 2

    # Calculate the indices based on the center coordinates
    x_index = int(x_center // cell_width)
    y_index = int(y_center // cell_height)

    # Ensure the indices stay within the range of the matrix
    x_index = min(x_index, num_cols - 1)
    y_index = min(y_index, num_rows - 1)

    return x_index, y_index


def visualize_image(image_path):
    image_width = 416
    image_height = 416
    num_rows = 4
    num_cols = 4

    # Create an empty matrix
    matrix = np.zeros((num_rows, num_cols))

    # Predict on the image
    result = model.predict(image_path, confidence=20, overlap=30).json()

    # Write matrix indices for each detected object to a text file
    with open('indexes.txt', 'w') as f:
        for obj in result['predictions']:
            x1, y1, w, h = obj['x'], obj['y'], obj['width'], obj['height']

            x2, y2 = x1 + w, y1 + h
            x_index, y_index = get_matrix_index2(x1, y1, x2, y2, image_width, image_height, num_rows, num_cols)

            # Write the indices for this detected object
            f.write(f'{x_index} {y_index} ')

            # Update the matrix with the detected object's index
            matrix[y_index, x_index] += 1

        # Write a newline character to separate the indices for different images
        f.write('\n')

    # Read the matrix indices from the output file
    with open('indexes.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            indices = [int(i) for i in line.strip().split()]

            # Highlight the cell corresponding to the index with a yellow color
            matrix[indices[1], indices[0]] += 10

    # Plot the matrix using matplotlib
    fig, ax = plt.subplots()
    ax.imshow(matrix, cmap='YlOrBr', interpolation='nearest')

    # Add index labels to the cells
    for i in range(num_rows):
        for j in range(num_cols):
            ax.text(j, i, int(matrix[i, j]), ha='center', va='center', color='k')

    # Hide axis ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('image')

    # Show the plot
    plt.show()

    # Visualize your prediction
    result = model.predict(image_path, confidence=20, overlap=30)
    print(result)

def browse_image():
    # Create Tkinter root window
    root = Tk()

    # Hide the root window
    root.withdraw()

    # Ask the user to browse an image file
    image_path = filedialog.askopenfilename(title="Select Image", filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")))

    # Check if the user selected an image file
    if image_path:
        visualize_image(image_path)
    else:
        print("No image selected.")

browse_image()
