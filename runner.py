import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from model import HopfieldModel
from argparse import ArgumentParser

def parse_args():
    """
    Parses command line arguments

    'training': list of image files to train the model
    '-v': optional verbose output
    """
    parser = ArgumentParser()
    parser.add_argument('-v', action='store_true')
    parser.add_argument('training', nargs='+')
    args = parser.parse_args()

    return args.training, args.v

def convert_image(file_name):
    """
    Converts an image using the Image library to a numpy array
    """
    return np.array(Image.open(file_name).convert('L'), dtype='int64')

def main():
    """
    Main script
    """

    files, debug = parse_args()

    patterns = []

    for file in files:
        # process each image file
        patterns.append(convert_image(file))

    model = HopfieldModel()

    # memorize all the converted files
    model.memorize_patterns(patterns, debug = debug)

    if debug:
        print('Displaying weight patterns...')
        model.display()

    print("Beginning resolution ...")

    # Allows the user to specify the image they want to resolve
    print('Type the file path of the unknown image to resolve')
    corrupted = convert_image(str(input()).strip())

    # Displays the unknown image on top of what the model believes it should
    # look like

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