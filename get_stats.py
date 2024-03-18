import os

dirs = ['test', 'train', 'valid']
new_dirs = ['test', 'train', 'valid']
for dir in dirs:
    iter = 0
    ones = 0
    zeros = 0
    for label_file in os.listdir(f'hand_dataset/{dir}/labels'):
        if ".txt" in label_file:
            iter += 1
            full_label_file_path = f'hand_dataset/{dir}/labels/{label_file}'
            file = open(full_label_file_path, "r")
            lines = file.readlines()
            new_lines = []
            for line in lines:
                if line[0] == "0":
                    zeros += 1
                else:
                    ones += 1

    print(iter)
    print(zeros)
    print(ones)
    print()

        
