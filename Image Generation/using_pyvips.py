#https://stackoverflow.com/a/51808242/20269629

import pyvips


# To install 'pyvips' refers to https://pypi.org/project/pyvips/
#  1. Intall libvips shared library from https://jcupitt.github.io/libvips/install.html
#  2. Set the PATH variable.
#  3. run pip install pyvips

def generate_tweet_image():
    cnum = 1
    output_file = "tweet_file.png"
    text = u''
    with open("hindi.txt", "r", encoding='UTF-8') as filestream:
        for l in filestream.readlines():
            text = text + f'{cnum}) {l}'
            cnum += 1

    MAX_W, MAX_H = 1500, 1500

    # See for API https://jcupitt.github.io/pyvips/vimage.html#pyvips.Image.text

    # font file: ARIALUNI.TTF
    image = pyvips.Image.text(text, width=MAX_W, height=MAX_H, font='Arial Unicode MS', dpi=96)
    image.write_to_file(output_file)
    print(f'File Written at : {output_file}')


generate_tweet_image()