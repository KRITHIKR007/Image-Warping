# Image Warping Experiment

## AIM
To perform image warping using geometric transformations such as scaling, rotation, translation, and perspective transformation.

## OBJECTIVE
- To understand geometric transformation techniques
- To apply affine/perspective transformations to modify image shape and orientation
- To observe how pixel mapping and interpolation affect the warped output

## THEORY

### Geometric Transformations

#### 1. Affine Transformations
Affine transformations preserve parallel lines and can be represented by a 2×3 matrix:
```
[x']   [a b c] [x]
[y'] = [d e f] [y]
                [1]
```

**Types of Affine Transformations:**

- **Translation**: Shifts the image by (tx, ty) pixels
  ```
  Matrix: [1 0 tx]
          [0 1 ty]
  ```

- **Scaling**: Changes the size by factors (sx, sy)
  ```
  Matrix: [sx 0  0]
          [0  sy 0]
  ```

- **Rotation**: Rotates by angle θ around a point
  ```
  Matrix: [cos(θ) -sin(θ) 0]
          [sin(θ)  cos(θ) 0]
  ```

- **Shear**: Skews the image along x or y axis
  ```
  Matrix: [1   shx 0]
          [shy 1   0]
  ```

#### 2. Perspective Transformation
Uses a 3×3 homogeneous matrix to map 4 points from source to destination, creating a perspective effect:
```
[x']   [a b c] [x]
[y'] = [d e f] [y]
[w']   [g h i] [1]
```

Final coordinates: x = x'/w', y = y'/w'

### Interpolation Methods

When transforming pixels, interpolation determines how to calculate pixel values at non-integer coordinates:

1. **Nearest Neighbor**: Uses the value of the closest pixel
2. **Bilinear**: Linear interpolation in both x and y directions
3. **Bicubic**: Uses 16 neighboring pixels for smoother results
4. **Lanczos**: High-quality resampling using sinc function

## IMPLEMENTATION

### Files Structure
```
LMS/
├── image_warping_experiment.py  # Main experiment script
├── requirements.txt             # Python dependencies
└── README.md                   # This documentation
```

### Key Classes and Methods

#### `ImageWarping` Class
- `__init__()`: Initialize with image or create sample
- `apply_translation()`: Translate image by (tx, ty)
- `apply_scaling()`: Scale image by (sx, sy) factors
- `apply_rotation()`: Rotate image by angle around center
- `apply_shear()`: Apply shear transformation
- `apply_perspective_transform()`: 4-point perspective mapping
- `apply_combined_affine_transform()`: Multiple transformations
- `display_results()`: Show all transformation results
- `demonstrate_interpolation_methods()`: Compare interpolation techniques

## PROCEDURE

1. **Setup Environment**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Experiment**
   ```bash
   python image_warping_experiment.py
   ```

3. **Expected Outputs**
   - `image_warping_results.png`: Grid showing all transformations
   - `interpolation_comparison.png`: Comparison of interpolation methods
   - Console output with transformation matrix analysis

## OBSERVATIONS

### Transformation Effects
1. **Translation**: Simple pixel shifting, no distortion
2. **Scaling**: Size changes, may cause pixelation or smoothing
3. **Rotation**: Introduces aliasing, some pixels may be lost
4. **Shear**: Creates parallelogram-like distortion
5. **Perspective**: Simulates 3D viewing angle changes

### Interpolation Impact
- **Nearest Neighbor**: Fastest, but creates blocky artifacts
- **Bilinear**: Good balance of speed and quality
- **Bicubic**: Smoother results, slower computation
- **Lanczos**: Best quality for upscaling, slowest

## APPLICATIONS

1. **Computer Vision**: Object recognition, feature matching
2. **Medical Imaging**: Registration, alignment correction
3. **Photography**: Perspective correction, image stabilization
4. **Augmented Reality**: Object tracking, overlay alignment
5. **Document Processing**: Skew correction, perspective normalization

## EXPERIMENTAL EXTENSIONS

To extend this experiment, try:

1. **Custom Image Input**: Replace sample image with your own
2. **Interactive Parameters**: Add GUI for real-time parameter adjustment
3. **Performance Analysis**: Measure transformation speeds
4. **Quality Metrics**: Implement PSNR, SSIM for quality assessment
5. **Advanced Transformations**: Barrel distortion, fisheye effects

## CONCLUSION

This experiment demonstrates the fundamental concepts of image warping through geometric transformations. Each transformation type serves specific purposes in image processing applications, and the choice of interpolation method significantly affects the quality of the output.

## REFERENCES

1. OpenCV Documentation: https://docs.opencv.org/
2. Digital Image Processing - Gonzalez & Woods
3. Computer Vision: Algorithms and Applications - Szeliski