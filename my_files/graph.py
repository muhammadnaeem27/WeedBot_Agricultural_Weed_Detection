import csv
import matplotlib.pyplot as plt

def generate_pie_chart(labels, sizes):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.savefig('D:\\Finalyearproject\\yolov5-20230513T175146Z-001\\yolov5\\graph\\pie_chart.png')
    plt.show()

# Read CSV file and extract column values
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