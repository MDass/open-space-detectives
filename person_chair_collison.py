# Adapted from: https://github.com/shu-nya/Object-Detection-using-YOLOv8-on-Custom-Dataset/blob/main/Object_Detection_using_YOLOv8_model_on_Custom_Guitar_Dataset.ipynb

import matplotlib.pyplot as plt
import cv2

def detect_overlap(box1, box2):
    # Convert YOLOv8 bounding box format to (x1, y1, x2, y2)
    box1_coords = yolo_to_coords(box1)
    box2_coords = yolo_to_coords(box2)
    
    # Calculate intersection area
    intersection_area = calculate_intersection_area(box1_coords, box2_coords)
    
    # Calculate areas of each bounding box
    box1_area = calculate_box_area(box1_coords)
    box2_area = calculate_box_area(box2_coords)
    
    # Calculate overlap percentage
    overlap_percentage = intersection_area / min(box1_area, box2_area)
    
    # Check if overlap percentage is at least 70%
    if overlap_percentage >= 0.7:
        return True
    else:
        return False

# Function to convert YOLOv8 bounding box format to (x1, y1, x2, y2)
def yolo_to_coords(box):
    x_center, y_center, width, height = box
    x1 = x_center - width / 2
    y1 = y_center - height / 2
    x2 = x_center + width / 2
    y2 = y_center + height / 2
    return (x1, y1, x2, y2)

# Function to calculate intersection area of two bounding boxes
def calculate_intersection_area(box1, box2):
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    # Calculate width and height of intersection rectangle
    width = max(0, x2 - x1)
    height = max(0, y2 - y1)
    
    # Calculate intersection area
    intersection_area = width * height
    return intersection_area

# Function to calculate area of a bounding box
def calculate_box_area(box):
    width = box[2] - box[0]
    height = box[3] - box[1]
    area = width * height
    return area

def plot_box(image, bboxes, labels):

    print(len(bboxes))
    print(len(labels))

    # Need the image height and width to denormalize the bounding box coordinates
    h, w, _ = image.shape
    for box_num, box in enumerate(bboxes):
        
        x1, y1, x2, y2 = yolo_to_coords(box)

        # Denormalize the coordinates.
        xmin = int(x1*w)
        ymin = int(y1*h)
        xmax = int(x2*w)
        ymax = int(y2*h)

        # calculate the thickness of the bounding box lines based on the image width
        # to make sure the boxes are visible in the plot.
        thickness = max(2, int(w/275))

        # draw a rectangle on the image
        image = cv2.rectangle(
            image,
            (xmin, ymin), (xmax, ymax),
            #  color (0, 0, 255) -> red
            color=(0, 0, 255) if labels[box_num] == "1" else (255, 0, 0),
            thickness=thickness
        )

        cv2.putText(image, 'occupiedchair' if labels[box_num] == "1" else "empty chair", (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255) if labels[box_num] == "1" else (255, 0, 0), 2)

    return image


image_path = "datasets/combined_dataset/test/images/frame232_jpg.rf.2491bca71662a7422e27f919ecc334f7.jpg"
label_path = "datasets/combined_dataset/test/labels/frame232_jpg.rf.2491bca71662a7422e27f919ecc334f7.txt"
image = cv2.imread(image_path)

chairs = []
people = []
file = open(label_path, "r")
lines = file.readlines()
for line in lines:
    label = line[0]
    bbox_string = line[2:]
    x_c, y_c, w, h = bbox_string.split(' ')
    x_c = float(x_c)
    y_c = float(y_c)
    w = float(w)
    h = float(h)

    if label == "0":
        people.append([x_c, y_c, w, h])
    else:
        chairs.append([x_c, y_c, w, h])

labels = []
for chair in chairs:
    continue_chair = True
    for person in people:
        if continue_chair:
            if detect_overlap(chair, person):
                labels.append("1")
                continue_chair = False
    if continue_chair:
        labels.append("0")
    
result_image = plot_box(image, chairs, labels)
plt.subplot(2, 2, 1)
plt.imshow(result_image[:, :, ::-1])
plt.subplots_adjust(wspace=1)
plt.tight_layout()
plt.show()

