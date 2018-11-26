import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from model import HopfieldModel
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-v', action='store_true')
    parser.add_argument('training', nargs='+')
    args = parser.parse_args()

    return args.training, args.v

def convert_image(file_name):
    return np.array(Image.open(file_name).convert('L'), dtype='int64')

def main():
    files, debug = parse_args()

    patterns = []

    for file in files:
        patterns.append(convert_image(file))

    model = HopfieldModel()

    model.memorize_patterns(patterns, debug = debug)

    if debug:
        print('Displaying weight patterns...')
        model.display()

    print("Beginning restoration...")

    print('Type the file path of the unknown image to resolve')
    corrupted = convert_image(str(input()))

    plt.subplot(211)
    plt.imshow(corrupted, cmap=plt.cm.BuPu_r, interpolation='none')
    plt.title('Corrupted image')

    updated = model.update(corrupted)

    count = 1
    while corrupted.all() != updated.all():
        print(f"update #{count}")
        corrupted = updated
        updated = model.update(corrupted)
        count += 1

    plt.subplot(212)
    plt.imshow(updated, cmap=plt.cm.BuPu_r, interpolation='none')
    plt.title('Restored image')

    plt.show()

if __name__ == '__main__':
    main()