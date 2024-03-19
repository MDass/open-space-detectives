# Adapted from: https://github.com/shu-nya/Object-Detection-using-YOLOv8-on-Custom-Dataset/blob/main/Object_Detection_using_YOLOv8_model_on_Custom_Guitar_Dataset.ipynb

import matplotlib.pyplot as plt
import cv2

# Function to convert bounding boxes in YOLO format to x_min, y_min, x_max, y_max.

def yolo2bbox(bboxes):

    xmin, ymin = bboxes[0]-bboxes[2]/2, bboxes[1]-bboxes[3]/2
    xmax, ymax = bboxes[0]+bboxes[2]/2, bboxes[1]+bboxes[3]/2
    return xmin, ymin, xmax, ymax

def plot_box(image, bboxes, labels):

    print(len(bboxes))
    print(len(labels))

    # Need the image height and width to denormalize the bounding box coordinates
    h, w, _ = image.shape
    for box_num, box in enumerate(bboxes):
        
        x1, y1, x2, y2 = yolo2bbox(box)

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
            color=(0, 0, 255) if labels[box_num] == "1" else (255, 0, 0),
            thickness=thickness
        )

        cv2.putText(image, 'occupiedchair' if labels[box_num] == "1" else "empty chair", (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255) if labels[box_num] == "1" else (255, 0, 0), 2)

    return image

def plot(image_path, label_path, num_samples):
    """
    Arguments:  image_paths - the path to the folder containing the images.
                label_paths - the path to the folder containing the label files for the corresponding images.
                num_samples - the number of random samples to visualize.
    The function helps to visualize a random selection of images along with their bounding boxes and labels.
    """



    plt.figure(figsize=(15, 12))    # create a plot of 15x12 inches

    image = cv2.imread(image_path)   # read the image corresponding to the index j.

    # open the label file associated with the selected image (based on the image name)
    # read the bounding box coordinates and labels for each object present in the image.
    with open(label_path, 'r') as f:
        bboxes = []     # initialize an empty list to store the bounding box coordinates that are extracted from the label files.
        labels = []     # initialize an empty list to store the labels that are extracted from the label files.
        label_lines = f.readlines()
        for label_line in label_lines:
            label = label_line[0]
            bbox_string = label_line[2:]
            x_c, y_c, w, h = bbox_string.split(' ')
            x_c = float(x_c)
            y_c = float(y_c)
            w = float(w)
            h = float(h)
            bboxes.append([x_c, y_c, w, h])
            labels.append(label)
    result_image = plot_box(image, bboxes, labels)  # call the plot_box function to draw the bounding boxes and labels on the image.
    plt.subplot(2, 2, 1)
    plt.imshow(result_image[:, :, ::-1])    # reverse the order of color channels. OpenCV uses BGR color order. Matplotlib uses RGB color order.
    plt.axis('off')
    plt.subplots_adjust(wspace=1)
    plt.tight_layout()
    plt.show()

plot(
    image_path='datasets/sec.v5i.yolov8_mod/test/images/frame232_jpg.rf.2491bca71662a7422e27f919ecc334f7.jpg',
    label_path='datasets/sec.v5i.yolov8_mod/test/labels/frame232_jpg.rf.2491bca71662a7422e27f919ecc334f7.txt',
    num_samples=1,
)