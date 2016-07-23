"""
Combine two images by fading them together from left to right.
"""

import argparse
from crossfade import blendImages


parser = argparse.ArgumentParser()
parser.add_argument('leftimage', help='image on the left side')
parser.add_argument('rightimage', help='image on the right side')
parser.add_argument(
    '--offset',
    type=float,
    default=0,
    help='where to start the fade (0 - 1.0)'
)
parser.add_argument(
    '-o',
    '--output',
    default='output.png',
    help='where to save the output'
)


args = parser.parse_args()

blendImages(
    args.leftimage,
    args.rightimage,
    args.offset,
    args.output
)
