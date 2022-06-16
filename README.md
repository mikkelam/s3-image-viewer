# s3-image-viewer

Simple utility to randomly shuffle the the newest images inserted into an S3 bucket (currently only jpeg is supported). 

First, launch firefox in kiosk mode:
```bash
firefox -kiosk index.html
```


To fetch the `N=5000` newest images.
```bash
python main.py -refresh --bucket my-bucket
```

then, to update update the displayed image
```bash
python main.py -show_random
```

`index.html` continually refreshes `show.jpeg`, so we should now see a new image