# Demosaicing_Python

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)

## Introduction
This Python script is designed for demosaicing raw images captured by digital cameras. Demosaicing is the process of converting raw sensor data into a full-color image by interpolating missing color information. This script uses the OpenCV library to perform the demosaicing.

## Features
- Demosaicing of raw sensor data into full-color images.
- Support for various Bayer patterns, such as BGGR, RGGB, etc.
- Simple and easy-to-use Python script.
- Option to specify input and output image paths.

## Usage
1. **Clone the Repository:**

    - Clone this repository to local machine using the following command: git clone https://github.com/Kaishays/Demosaicing_Python

2. **Install OpenCV**

    - Make sure OpenCV is installed in your Python environment. Install using `pip`: pip3 install opencv-python

3. **Configure path.py**

    - Set user_input_path = "path/to/image.jpg"
    - Set user_output_path = "path/to/output"

- **If steps were correctly followed Demosaic.py will convert raw sensor data into full-color images.**
   

   
### Dynamic Control UI Documentation

#### Overview
Dynamic Control UI is a versatile interface designed for the AltiView software, enabling users to interact with various controls using a Controller, as well as full support for keyboard and mouse inputs. This UI leverages path data and View Models to arrange a circular design with 8 buttons, enhancing the interaction through visual feedback and dynamic content changes.

#### Organization
The Dynamic Control UI is organized across two main files: `XboxUI.xaml` and `XboxUI.xaml.cs`. The latter is categorized into several sections to streamline development and maintenance:

1. **General Variables**: Defines the backbone variables used throughout the UI.
2. **Color Variables**: Allows customization of the UI's color scheme.
   - Adjust these variables to change the color themes of the buttons and other UI elements.
3. **Sub Classes**:
   - **XboxUIEventArgs**: Stores essential data for each button including content, button number, page number, and associated events.
   - **ViewModel**: Connects path data to each button, facilitating dynamic updates and interactions.
4. **General Controls**: Manages input from both the keyboard, mouse, and controller.
5. **Keyboard and Mouse Controls**: Specific methods and event handlers for mouse and keyboard interactions.
6. **Controller Controls**: Specialized controls tailored for game controller inputs.

The Dynamic Control UI uses a system of 8 buttons per page, where only 8 button objects are ever created. Multiple button configurations are simulated by adjusting the displayed data on these objects. Two index systems organize button selection:

- **Full Index**: A zero-based index that represents the total number of button instances within the UI, primarily used for querying within `XboxUIEventArgs`.
- **Visible Index**: A one-based index that offers an intuitive understanding of which button is selected, using a combination of a page number (1–n) and a button number (1–8).

#### Getter and Setter Methods
These methods provide ways to manipulate the content displayed by the Dynamic Control UI using the visible index system.

1. **Get Button Content**
   - Description: Retrieves the content of a button at a specified button number and page number.
   - Parameters:
     - `int buttonNum`: The number of the button.
     - `int pageNum`: The page number where the button is located.
   - Returns: `string` - The content of the button.

2. **Get Content Location**
   - Description: Searches for all occurrences of specific content within `XboxUIEventArgs` and returns their locations.
   - Parameters:
     - `string content`: The content to search for.
   - Returns: `List<(int, int)>` - A list of tuples containing button numbers and page numbers where the content is found.

3. **Replace Button**
   - Description: Replaces the content of a button at the specified visible index.
   - Parameters:
     - `int buttonNum`: The button number.
     - `int pageNum`: The page number.
     - `string newContent`: The new content to set for the button.

4. **Replace All Buttons**
   - Description: Replaces the content of all buttons according to a list of new contents.
   - Parameters:
     - `List<string> contentList`: A list containing new content for each button, sequentially.

5. **Add Button**
   - Description: Adds a new button with specified content at a given position.
   - Parameters:
     - `int buttonNum`: The button number on the current page.
     - `int pageNum`: The page number.
     - `string newContent`: The content for the new button.

6. **Add Buttons**
   - Description: Adds multiple new buttons on a specified page starting from a specific button number.
   - Parameters:
     - `int buttonNum`: The starting button number on the current page.
     - `int pageNum`: The page number.
     - `List<string> contentList`: A list of contents for the new buttons.

7. **Delete Button**
   - Description: Deletes a button by its content or by its position.
   - Overloads:
     - By content: `void DeleteButton(string content)`
     - By position: `void DeleteButton(int buttonNum, int pageNum)`
