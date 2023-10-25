import csv

def f1():
    def replace_text_in_file(filename):
        with open(filename, 'r') as file:
            text = file.read()

            modified_text = text.replace("lamb-s quarter", "lambs_quarter")
            modified_text = modified_text.replace("nut grass", "nut_grass")
            modified_text = modified_text.replace("parthenium hysterophorus", "parthenium_hysterophorus")

        with open(filename, 'w') as file:
            file.write(modified_text)

    # Usage:
    replace_text_in_file('results.txt')



def f2():
    # Read the data from the text file
    with open(r'results.txt', 'r') as file:
        data = file.read().split('\n')[1:]  # Exclude the header

    # Split each row and create a list of lists
    data = [row.split(' ') for row in data]

    # Write the data to a new CSV file
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
def f3():
    import csv

    def add_csv_header(filename, header):
        # Check if the file already has a header
        with open(filename, 'r') as file:
            first_line = file.readline().strip()
            if first_line == ','.join(header):
                # The header is already present, so
                return

        # Read the content of the CSV file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Insert the header as the first line
        lines.insert(0, ','.join(header) + '\n')

        # Overwrite the file with the modified content
        with open(filename, 'w') as file:
            file.writelines(lines)

    # Define the header row
    header = ['x1', 'y1', 'x2', 'y2', 'w', 'h', 'conf', 'cls', 'name','date', 'time']

    # Specify the filename of the existing CSV file
    filename = 'output.csv'

    # Call the function to add the header to the CSV file if it doesn't already exist
    add_csv_header(filename, header)

def f4():
    import csv
    import matplotlib.pyplot as plt

    def generate_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.savefig('graph/pie_chart.png')
        plt.show()

    # Read CSV file and extract column values
    cls_values = []

    with open('output.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cls = row['cls']
            if cls is not None:  # Skip None values
                cls_values.append(cls)

    # Define mapping of class labels to weed names
    weed_names = {
        0: 'Borh',
        1: 'Lamb\'s Quater',
        2: 'Nut Grass',
        3: 'Parthenium'
    }

    # Calculate weed occurrence percentages
    total_count = len(cls_values)
    weed_counts = {}
    for cls in cls_values:
        cls = int(float(cls))  # Convert class label to integer
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
f3()
f4()
