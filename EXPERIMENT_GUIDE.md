# Image Warping Experiment - Quick Start Guide

## 🎯 Experiment Overview

**AIM**: To perform image warping using geometric transformations such as scaling, rotation, translation, and perspective transformation.

**OBJECTIVE**: 
- Understand geometric transformation techniques
- Apply affine/perspective transformations to modify image shape and orientation  
- Observe how pixel mapping and interpolation affect the warped output

## 📁 Files Generated

| File | Description |
|------|-------------|
| `image_warping_experiment.py` | Main experiment script with all transformations |
| `custom_image_example.py` | Example showing how to use your own images |
| `requirements.txt` | Python package dependencies |
| `README.md` | Detailed documentation and theory |
| `image_warping_results.png` | Grid showing all transformation results |
| `interpolation_comparison.png` | Comparison of interpolation methods |
| `test_image.png` | Sample geometric test image |

## 🚀 How to Run

### Method 1: Using Sample Images (Default)
```bash
python image_warping_experiment.py
```

### Method 2: Using Your Own Image
```python
from image_warping_experiment import ImageWarping

# Initialize with your image
warper = ImageWarping("path/to/your/image.jpg")

# Run all transformations
warper.display_results()
warper.demonstrate_interpolation_methods()
warper.analyze_transformation_effects()
```

### Method 3: Using the Custom Example
```bash
python custom_image_example.py
```

## 🔧 Transformations Implemented

### 1. **Affine Transformations** (2×3 matrix)
- ✅ **Translation**: Shift image by (tx, ty) pixels
- ✅ **Scaling**: Resize by factors (sx, sy)  
- ✅ **Rotation**: Rotate by angle around center point
- ✅ **Shear**: Skew along x or y axis
- ✅ **Combined**: Multiple transformations in sequence

### 2. **Perspective Transformation** (3×3 matrix)
- ✅ **4-Point Mapping**: Map corners to create perspective effect
- ✅ **Homogeneous Coordinates**: Full projective transformation

### 3. **Interpolation Methods**
- ✅ **Nearest Neighbor**: Fastest, blocky results
- ✅ **Bilinear**: Good speed/quality balance
- ✅ **Bicubic**: Smoother results
- ✅ **Lanczos**: Highest quality

## 📊 Expected Output

### Console Output Example:
```
============================================================
IMAGE WARPING EXPERIMENT
============================================================
Creating sample checkerboard image...
Image loaded successfully. Dimensions: 400x400
Applying translation: tx=50, ty=30
Applying scaling: scale_x=1.5, scale_y=1.2
Applying rotation: angle=30°, scale=1.0
...
Translation Matrix (tx=50, ty=30):
[[ 1.  0. 50.]
 [ 0.  1. 30.]]
============================================================
```

### Visual Output:
- **Grid of 7 images**: Original + 6 transformations
- **Interpolation comparison**: 4 different methods
- **High-resolution PNG files** saved automatically

## 🎛️ Customization Options

You can modify parameters in the script:

```python
# Translation parameters
translated_img, _ = warper.apply_translation(tx=100, ty=50)

# Scaling parameters  
scaled_img, _ = warper.apply_scaling(scale_x=2.0, scale_y=0.5)

# Rotation parameters
rotated_img, _ = warper.apply_rotation(angle=45, scale=1.2)

# Shear parameters
sheared_img, _ = warper.apply_shear(shear_x=0.5, shear_y=0.2)
```

## 🔍 Key Learning Points

1. **Matrix Operations**: Understanding how 2×3 and 3×3 matrices control image transformations
2. **Coordinate Systems**: How pixel coordinates are mapped during transformation
3. **Interpolation Effects**: Quality vs. speed trade-offs in different methods
4. **Practical Applications**: Real-world uses in computer vision and image processing

## 📈 Experiment Extensions

Try these advanced experiments:

1. **Interactive GUI**: Add sliders for real-time parameter adjustment
2. **Performance Testing**: Benchmark different transformation speeds
3. **Quality Metrics**: Implement PSNR/SSIM for quantitative analysis
4. **Custom Transformations**: Create barrel distortion, fisheye effects
5. **Video Warping**: Apply transformations to video frames

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Import errors | Run: `pip install -r requirements.txt` |
| Images not displaying | Install matplotlib GUI backend |
| Memory errors | Use smaller images or reduce resolution |
| Transformation artifacts | Adjust interpolation method |

## ✅ Success Criteria

The experiment is successful when you can:
- [x] Generate all 7 transformation types
- [x] Compare 4 interpolation methods  
- [x] Analyze transformation matrices
- [x] Save high-quality result images
- [x] Understand the mathematical principles

---

**🎉 Experiment Complete!** 

You now have a comprehensive image warping toolkit that demonstrates all major geometric transformations used in computer vision and image processing applications.