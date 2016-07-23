# imagecrossfade

Combine two images by fading from one to the other horizontally.


## Prerequisites:

Install python, pip, and virtualenv if you do not already have them.

`virtualenv env`
`. env/bin/activate`
`pip install -r requirements.txt`


## Usage:


Print usage string:
`python crossfade_cli.py`
> usage: crossfade_cli.py [-h] [--offset OFFSET] [-o OUTPUT] leftimage rightimage


Only fade the middle 70%:

`python crossfade_cli.py path-to-image1 path-to-image2 --offset .3`


Pick output file:

`python crossfade_cli.py path-to-image1 path-to-image2 -o faded.png`
