# Image Detection and Relaxation - EP2

## Overview
This experiment demonstrates image detection techniques and relaxation methods to refine detected features. The notebook implements multiple detection algorithms and applies iterative relaxation to improve the consistency of detected regions.

## Objective
- Detect edges/features using various operators (Sobel, Canny, Harris, LoG, DoG)
- Apply relaxation techniques to remove noise and improve detection consistency
- Understand iterative refinement of binary/feature maps
- Compare different detection and relaxation strategies

## Features Implemented

### Detection Methods
1. **Sobel Edge Detection**: Detects edges using gradients in X and Y directions
2. **Canny Edge Detection**: Advanced edge detection with noise suppression
3. **Harris Corner Detection**: Identifies corner features in images
4. **LoG (Laplacian of Gaussian)**: Blob detection using LoG operator
5. **DoG (Difference of Gaussians)**: Efficient blob detection approximation

### Relaxation Techniques
1. **Majority Voting**: Updates pixels based on neighborhood majority
2. **Weighted Relaxation**: Uses weighted neighborhood influence
3. **Morphological Relaxation**: Applies morphological operations
4. **Iterative Relaxation**: Applies relaxation until convergence

### Analysis Features
- Parameter sensitivity analysis
- Convergence behavior tracking
- Statistical comparison of methods
- Visual overlays and comparisons

## Files
- `image_detection_relaxation.ipynb` - Main experiment notebook
- `requirements.txt` - Required Python packages
- `README.md` - This documentation

## Setup Instructions

1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook image_detection_relaxation.ipynb
   ```

3. Run all cells to execute the complete experiment

## Key Concepts Demonstrated

### Image Detection
- Edge detection using differential operators
- Corner detection for feature identification
- Blob detection for circular features
- Multi-scale analysis techniques

### Relaxation Methods
- Neighborhood-based pixel updating
- Majority voting for noise reduction
- Weighted influence schemes
- Iterative refinement until convergence

### Parameter Optimization
- Neighborhood size effects (3×3, 5×5, 7×7)
- Threshold sensitivity analysis
- Weight parameter tuning
- Convergence criteria evaluation

## Expected Results

The experiment will demonstrate:
1. Different detection methods capture different types of features
2. Relaxation reduces noise while preserving important features
3. Parameter choices significantly affect final results
4. Iterative approaches provide better consistency
5. Combined strategies often outperform single methods

## Learning Outcomes

After completing this experiment, you will understand:
- How various image detection operators work
- The importance of noise reduction in computer vision
- Iterative refinement techniques
- Parameter tuning for optimal results
- Comparative analysis of different approaches

## Extensions

You can extend this experiment by:
- Testing with different types of images
- Implementing additional detection operators
- Developing adaptive relaxation schemes
- Adding real-time processing capabilities
- Combining with machine learning approaches