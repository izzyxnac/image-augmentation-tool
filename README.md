# Image Augmentation Tool

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Customizing Augmentations](#customizing-augmentations)
- [Examples](#Examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

The Image Augmentation Tool is a Python-based application designed to enrich machine learning datasets with advanced image processing techniques. Through various transformations, it enhances model robustness and generalization in image recognition tasks.

## Key Features

- **Wide Range of Augmentations**: Supports flipping, rotation, scaling, noise addition, and more.
- **Batch Processing**: Efficient processing of entire directories with random augmentations applied to each image.
- **Customizable Parameters**: Flexibility to tweak augmentation parameters for specific dataset enhancement needs.
- **Progress Tracking**: Utilizes a progress bar to monitor the augmentation process.

## Getting Started

### Prerequisites

- Python 3.8 or later.

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/izzyxnac/image-augmentation-tool.git
   ```
2. Navigate to the project directory:
   ```
   cd image-augmentation-tool
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

Update `input_dir` and `output_base_dir` in `ImageAugmanter.py` to your paths and run:

```
python ImageAugmanter.py
```

## Customizing Augmentations

Modify the `augmentations` list in the script for tailored dataset enhancement, adding or removing techniques as needed.

## Examples

The following image demonstrates different augmentation effects applied to a single original image of a chimpanzee. Each effect showcases a unique transformation that this tool is capable of:

![Augmentation Examples](https://github.com/izzyxnac/image-augmentation-tool/blob/main/examples/monkey-noise.png)

_Descriptions for each effect from left to right:_

1. **Gaussian Noise**: Adds Gaussian noise to the image, simulating the effect of camera sensor noise.
2. **Local Variance**: Applies noise with local variance, often used for texture enhancement.
3. **Poisson Noise**: Simulates Poisson-distributed noise, typically from photon-counting statistics.
4. **Salt**: Introduces white pixels randomly, representing the 'salt' effect.
5. **Pepper**: Introduces black pixels randomly, representing the 'pepper' effect.
6. **Salt & Pepper**: Combines both 'salt' and 'pepper' effects in one image.
7. **Speckle**: Applies multiplicative noise, creating a 'speckled' look.

## Contributing

Contributions to improve or extend the tool's capabilities are welcome. Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to `imgaug` and `imageio` libraries.
- Created by NACIRI Issam, © 2024.
