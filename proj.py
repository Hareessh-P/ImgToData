import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import csv

def plot_digitizer(image_path, output_csv, output_plot=None, points=None):
    # Read the input image using OpenCV
    img = cv2.imread(image_path)

    # If points are not provided, use interactive mode
    if points is None:
        # Prompt the user to click on points on each axis
        print("Click on points on each axis.")
        print("Press any key to continue after clicking.")
        
        # Create an empty list to store the clicked points
        points = []
        
        # Display the image using OpenCV
        cv2.imshow('image', img)
        
        # Wait for a key press (0 means wait indefinitely until a key is pressed)
        cv2.waitKey(0)
        
        # Close the image window
        cv2.destroyAllWindows()
    else:
        # If points are provided, use them directly
        # Convert the string coordinates to tuples of integers
        points = [tuple(map(int, p.split(','))) for p in points]

    # Sort points by x-coordinate
    sorted_points = sorted(points, key=lambda p: p[0])

    # Example: Dumping points to a CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['X', 'Y'])

        # Write each point to the CSV file
        for x, y in sorted_points:
            csv_writer.writerow([x, y])

    # If output_plot is specified, create a scatter plot using Matplotlib
    if output_plot:
        plt.scatter(*zip(*sorted_points), color='red')
        plt.savefig(output_plot)  # Save the plot to a file
        plt.show()  # Display the plot

if __name__ == "__main__":
    # Set up a command-line argument parser
    parser = argparse.ArgumentParser(description='Digitize plots')
    
    # Define command-line arguments
    parser.add_argument('--output_csv', type=str, help='Path to the output CSV file')
    parser.add_argument('--output_plot', type=str, help='Path to the output plot image')
    parser.add_argument('--points', nargs='+', type=str, help='Coordinates of points in the format x1,y1 x2,y2 ...')

    # Specify the default image path
    default_image_path = r'D:\OSC\bargraph.png'
    
    # Parse command-line arguments
    args = parser.parse_args()

    # Call the plot_digitizer function with the specified image path and other arguments
    plot_digitizer(default_image_path, args.output_csv, args.output_plot, args.points)




