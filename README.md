# Simulate Colorblindness and Correct Colors for People with Colorblindness

This Script simulates images based on how people with colorblindness would perceive it naturally. You can also vary the degree of colorblindness for simulating. This script can also be used to correct images, making differenciation of certain colors in an image easier for people with colorblindness.

* **Easy** to setup and run!
* Simulate **Protanopia, Deutranopia, Tritanopia and Hybrid Colorblindess (Protanopia+Deutranopia).**
* **Correct colors** in images for **Protanopia, Deutranopia and Hybrid Colorblindness.**
* **Vary the degree of colorblindness** for both Simulation and Correction!
* Extremly **fast.**
* Use it from the **command line (super easy)**, or use it as a **library (advanced users).**
* Supports **Daltonization and HSV Shifting algorithm.**

```
### Installing dependencies

To run this script, you need to install three libraries for python. Use pip or conda (or any package manager of your choice) to download PIL, Numpy and OpenCV.
```shell
sudo pip install Pillow numpy opencv-python
```

### Verifying the installation

Once you have successfully downloaded the scripts, and installed the dependencies, we can verify the installation.
The *~/Examples_Check/* folder contains a sample image containing a number of Ishihara plate images. 
We want to run the script on this example image and see if everything is working fine.

```shell
# Go to the directory where you downloaded the scripts.
cd <dir where scripts are downloaded>/Simulate-Correct-Colorblindness

# Now run the examples script.
python run_examples.py
```

This will run all the available algorithms on the example image, and save the processed images in the *Examples_Check/* directory.
Check the directory and see if you have 5 processed + 1 original image. The processed (verified) and the original image are tagged in this readme file. If you want to verify further, have a look at the images in your computer and the images here.


  

### *How to run the script*

Go to the directory
```shell
cd ~/Simulate-Correct-ColorBlindness
```

Run the script with flags.
Let's say we want to simulate only tritanopia, and correct the image 
for protanopia and deutranopia. We run the below command.
```shell
python recolor.py
  -input /Users/example_user/pictures/sample.jpg
  -output /Users/example_user/pictures/sample_dir/
  -protanopia_degree 0.9
  -deutranopia_degree 0.6
  -tritanopia_degree 0.5 
  -sim_tritanopia
  -correct_colors
```
  
 If you want to run all the operations, you can also use the -all flag. 
 We will keep the degrees as default (1.0) this time to focus on -run_all flag.
 ```shell
 python recolor.py
  -input /Users/example_user/pictures/sample.jpg
  -output /Users/example_user/pictures/sample_dir/
  -run_all
```
  
If you want to run correction for only protanopia, 
you can set the deutranopia_degree value to 0. 
Essentially forcing the algorithm to not assume deutranopia.
```shell
 python recolor.py
   -input /Users/example_user/pictures/sample.jpg
   -output /Users/example_user/pictures/sample_dir/
   -deutranopia_degree 0
   -correct_colors
```





