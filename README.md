Image Augmentation Tool

Overview
image-augmentation-tool is a cutting-edge image augmentation tool aimed at enhancing machine learning datasets with a wide array of image transformations. This powerful tool allows for the automated enhancement of image data, making it more versatile and increasing the robustness of machine learning models. By applying random but realistic modifications such as flipping, rotation, scaling, and noise addition, image-augmentation-tool helps in achieving better generalization and performance in image recognition tasks.

Installation
To get started with image-augmentation-tool, follow these simple installation steps:

-Clone the Repository:
First, clone the repository to your local machine using Git. Open your terminal, and run the following command:

git clone https://github.com/izzyxnac/image-augmentation-tool.git

-Set Up a Virtual Environment (optional but recommended):
Navigate to the cloned directory and set up a Python virtual environment. This step ensures that the dependencies for the project do not interfere with your other Python projects.

For Windows:
cd image-augmentation-tool
python -m venv venv
.\venv\Scripts\activate

For macOS/Linux:
cd image-augmentation-tool
python3 -m venv venv
source venv/bin/activate

Install Dependencies:
With the virtual environment activated, install the project dependencies using pip:
pip install -r requirements.txt

-Quick Start Guide
After installing image-augmentation-tool, you can quickly start augmenting your images with the following steps:

Configure Paths:
Open ImageAugmanter.py in a text editor and update the input_dir and output_base_dir variables to point to the directories containing your original images and where you want the augmented images to be saved, respectively.

Run the Script:
Execute the augmentation script from your terminal to begin processing your images:
python ImageAugmanter.py

Review the Results:
Once the script finishes running, navigate to your specified output_base_dir to review the augmented images. Each original image from the input_dir will now have a set of augmented variants in its corresponding output directory, expanding your dataset for improved machine learning model training.
By following these simple steps, you can easily enhance your image datasets with image-augmentation-tool's comprehensive suite of augmentation techniques, tailored to meet the diverse needs of modern machine learning applications.
