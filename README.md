Hopfield Image Processor + Classifer
---

Design
----
* `model.py` includes the HopfieldModel class, which creates a Hopfield model that makes and memorizes weight patterns, and uses matplotlib to show plots.

* `runner.py` contains the script that requires paths to images to be passed into train, and resolves a given unknown image by drawing what the model thinks the image should look like.

* The older folders are media files and contain jpg files

Usage
----
Ensure PIL, matplotlib, and numpy are installed in your Python environment.

Example: `./python3.7 runner.py colored/cafe_terrace_night.jpg colored/last_supper.jpg colored/mona_lisa.jpg -v`

* `-v` may be optionally supplied for verbose output
* Training files are specified as a list of files in the terminal window.