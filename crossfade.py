from PIL import Image


def blendImages(image1_path, image2_path, offset_ratio=0, output_path=None):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    output = _blendImages(image1, image2, offset_ratio)
    output.save(output_path or 'output.png', 'PNG')


def _blendImages(image1, image2, offset_ratio):
    fade1 = fadeImage(image1, offset_ratio, True)
    fade2 = fadeImage(image2, offset_ratio, False)

    # uncomment to print debug images
    # fade1.save('fade1.png', 'PNG')
    # fade2.save('fade2.png', 'PNG')

    rect = 0, 0, image1.size[0], image1.size[1]
    copy2 = fade2.crop(rect)
    fade1.paste(copy2, rect, copy2)

    return fade1


def fadeImage(image, offset_ratio, leftToRight=True):
    image.putalpha(255)
    width, height = image.size
    pixels = image.load()

    # update each column
    for x in range(width):
        progress = 1.0 * x / width

        if progress < offset_ratio:
            progress = 0
        else:
            adjusted_start = width * offset_ratio
            adjusted_width = width - (2 * adjusted_start)
            progress = 1.0 * (x - adjusted_start) / adjusted_width

        # fade linearly
        alpha_float = 1.0 - progress if leftToRight else progress
        alpha = int(round(255 * alpha_float))

        # update all the pixels in this column
        for y in range(height):
            pixels[x, y] = pixels[x, y][:3] + (alpha,)

    return image


if __name__ == '__main__':
    print (
        '{} is just a library file. Use {} from the command line'.format(
            __file__,
            'crossfade_cli.py'
        )
    )
