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


## Example

![image1.jpg](https://raw.githubusercontent.com/collingreen/imagecrossfade/master/example/image1.jpg)
![image2.jpg](https://raw.githubusercontent.com/collingreen/imagecrossfade/master/example/image2.jpg)

`python crossfade_cli.py example/image1.jpg example/image2.jpg --offset .3 -o example/faded.png`

![faded.png](https://raw.githubusercontent.com/collingreen/imagecrossfade/master/example/faded.png)


Example Images:
- forestfire - https://pixabay.com/en/wildfire-forest-fire-blaze-smoke-1105209/
- rays of light - https://pixabay.com/en/clouds-ray-of-light-light-sky-872143/
