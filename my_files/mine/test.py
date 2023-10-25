import csv
import csv
import matplotlib.pyplot as plt
import os


filename = 'D:\\Finalyearproject\\yolov5-20230513T175146Z-001\\yolov5\\results.txt'

if not os.path.isfile(filename):
    with open(filename, 'w') as f:
        # Adding headers
        f.write('x1 \ty1 \tx2 \ty2 \tw \th \tconf \tcls \tname \tdate \ttime')
        f.write('\n')

# make function f1:
def f1():
    def replace_text_in_file(filename):
        with open('D:\\Finalyearproject\\yolov5-20230513T175146Z-001\\yolov5\\results.txt', 'r') as file:
            text = file.read()

        modified_text = text.replace("nut grass", "nut_grass")
        modified_text = text.replace("parthenium hysterophorus", "parthenium")
        modified_text = text.replace("lamb-s quarter", "lambsquarter")


        with open('D:\\Finalyearproject\\yolov5-20230513T175146Z-001\\yolov5\\results.txt', 'w') as file:
            file.write(modified_text)

    # Usage:
    replace_text_in_file('D:\\Finalyearproject\\yolov5-20230513T175146Z-001\\yolov5\\results.txt')


def f2():
    # Read the data from the text file
    with open(r'D:\\Finalyearproject\\yolov5-20230513T175146Z-001\\yolov5\\results.txt', 'r') as file:
        data = file.read().split('\n')[0:]  # Exclude the header

    # Split each row and create a list of lists
    data = [row.split(' ') for row in data]

    # Write the data to a new CSV file
    with open('D:\\Finalyearproject\\yolov5-20230513T175146Z-001\\yolov5\\output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def generate_pie_chart(labels, sizes):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('D:\\Finalyearproject\\yolov5-20230513T175146Z-001\\yolov5\\graph\\pie_chart.png')
    plt.show()


def f3():
    cls_values = []

    with open('D:\\Finalyearproject\\yolov5-20230513T175146Z-001\\yolov5\\output.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cls_values.append(row['cls'])

    # Define mapping of class labels to weed names
    weed_names = {
        '0': 'Borh',
        '1': 'Lamb\'s Quater',
        '2': 'Nut Grass',
        '3': 'Parthenium'
    }

    # Calculate weed occurrence percentages
    total_count = len(cls_values)
    weed_counts = {}
    for cls in cls_values:
        if cls in weed_counts:
            weed_counts[cls] += 1
        else:
            weed_counts[cls] = 1

    weed_labels = []
    weed_sizes = []

    for cls, count in weed_counts.items():
        weed_labels.append(weed_names[cls])  # Use weed names instead of class labels
        weed_sizes.append((count / total_count) * 100)

    # Generate pie chart
    generate_pie_chart(weed_labels, weed_sizes)



f1()
f2()
# f3()
