import os

# Remove irrelevant labels
delete = [0, 2, 3, 4, 6]

# Create mapping of labels that are relevant to be 0-indexed
mapping = {1: 1, 5: 0}
dirs = ['test', 'train', 'valid']
new_dirs = ['test', 'train', 'valid']
for dir in dirs:
    for label_file in os.listdir(f'datasets/combined_dataset/{dir}/old_labels'):
        full_label_file_path = f'datasets/combined_dataset/{dir}/old_labels/{label_file}'
        file = open(full_label_file_path, "r")
        lines = file.readlines()
        new_lines = []
        for line in lines:
            if int(line[0]) not in delete:
                new_line = str(mapping[int(line[0])]) + line[1:]
                new_lines.append(new_line)
        new_label_file_path = f'datasets/combined_dataset/{dir}/labels/{label_file}'
        new_file = open(new_label_file_path, "w")
        new_file.writelines(new_lines)