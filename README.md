# ImgToData
# Google Docs link : https://docs.google.com/document/d/1_941UJvFQzl9mt2E1sjzzEEjWv_k5TRgv1h18cNGpL4/edit?usp=sharing

## AIM:
The aim of this script is to digitise plots from an input image, allowing the user to interactively click on points on each axis or, alternatively, provide the coordinates of these points directly. The digitised data points can be saved to a CSV file, and an optional scatter plot can be generated.
## PROCEDURE:
The script reads the input image using the OpenCV library.
If the points parameter is not provided, it enters interactive mode, prompting the user to click on points on each axis by displaying the image using OpenCV.
If points are provided, they are directly used.
The script sorts the points by their x-coordinates.
The sorted points are written to a CSV file specified by the output_csv parameter.
If the output_plot parameter is specified, a scatter plot is generated using Matplotlib, and the plot is saved to the specified file.

## LIBRARIES USED:
OpenCV (cv2): A computer vision library used for image processing tasks, such as reading images and displaying them.
NumPy (np): A numerical computing library used for handling arrays and mathematical operations. It is often used in image processing for numerical operations on pixel values.
Matplotlib (plt): A 2D plotting library used for creating visualizations, such as scatter plots. In this script, it is used to generate a scatter plot of the digitized points.
Argparse: A Python library for parsing command-line arguments. It allows the script to accept input parameters from the command line.

## INPUT:
The input to the script is the path to an image file (D:\OSC\bargraph.png in this case).
The user can provide additional input through command-line arguments, including the output CSV file path (--output_csv), the output plot image path (--output_plot), and the coordinates of points on the axes (--points).
This script provides flexibility by allowing users to either interactively click on points or directly input them, making it useful for digitizing plots from images.

## OUTPUT:
The output of the script depends on the parameters provided and the execution mode:

CSV File:

If the --output_csv parameter is specified, the digitized data points (x, y coordinates) are saved to the specified CSV file (D:\OSC\output.csv by default).
Scatter Plot (Optional):

If the --output_plot parameter is specified, the script generates a scatter plot using Matplotlib, highlighting the digitized points. The plot is saved to the specified file (D:\OSC\output_plot.png by default) and displayed.
Interactive Mode (Points Clicked):

If the script is run without providing the --points parameter, it enters interactive mode, prompting the user to click on points on each axis. After clicking, the points are processed as described, and the CSV file and scatter plot are generated accordingly.
Direct Input Mode (Points Provided):

If the --points parameter is provided, the script uses the specified points directly without interactive clicking. The CSV file and scatter plot are generated based on these points.
