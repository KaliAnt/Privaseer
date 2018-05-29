import os
import sys

def create_csv(image_path):
    try:
        imgs = os.listdir(image_path)
        csv = os.open("data.csv", os.O_CREAT | os.O_WRONLY)
        for img in imgs:
            print(img)
            line = image_path + '/' + img + ';' + '0' + '\n'
            os.write(csv, line)
            
    except OSError:
        print("Invalid path name: " + image_path)
        exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        create_csv(sys.argv[1])
    else:
        print("usage:   ./script_name path_to_dir")
    