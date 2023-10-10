import cv2
import os
from path import user_input_path, user_output_path



def demosaic_image(input_path, output_path):
    # Get the absolute paths
    input_path = os.path.abspath(input_path)
    output_path = os.path.abspath(output_path)

    # Load the raw image
    raw_image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    if raw_image is None:
        print(f"Failed to load the image from {input_path}")
        return

    # Perform demosaicing using the OpenCV function
    demosaiced_image = cv2.cvtColor(raw_image, cv2.COLOR_BayerGR2BGR)

    # Save the demosaiced image
    cv2.imwrite(output_path, demosaiced_image)

if __name__ == "__main__":
    

    demosaic_image(user_input_path, user_output_path)
