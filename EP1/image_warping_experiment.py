import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

class ImageWarping:
    def __init__(self, image_path=None):
        """Initialize the ImageWarping class with an image"""
        if image_path and os.path.exists(image_path):
            self.original_image = cv2.imread(image_path)
            self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
        else:
            # Create a sample image if no image is provided
            self.original_image = self.create_sample_image()
        
        self.height, self.width = self.original_image.shape[:2]
        print(f"Image loaded successfully. Dimensions: {self.width}x{self.height}")
    
    def create_sample_image(self):
        """Create a sample checkerboard image for demonstration"""
        print("Creating sample checkerboard image...")
        img = np.zeros((400, 400, 3), dtype=np.uint8)
        
        # Create checkerboard pattern
        for i in range(0, 400, 50):
            for j in range(0, 400, 50):
                if (i//50 + j//50) % 2 == 0:
                    img[i:i+50, j:j+50] = [255, 255, 255]  # White squares
                else:
                    img[i:i+50, j:j+50] = [0, 0, 0]  # Black squares
        
        # Add some colored elements for better visualization
        cv2.circle(img, (100, 100), 30, (255, 0, 0), -1)  # Red circle
        cv2.rectangle(img, (250, 250), (350, 350), (0, 255, 0), -1)  # Green rectangle
        cv2.circle(img, (300, 100), 25, (0, 0, 255), -1)  # Blue circle
        
        return img
    
    def apply_translation(self, tx=50, ty=30):
        """Apply translation transformation"""
        print(f"Applying translation: tx={tx}, ty={ty}")
        
        # Define translation matrix (2x3)
        translation_matrix = np.float32([[1, 0, tx],
                                       [0, 1, ty]])
        
        # Apply transformation
        translated_image = cv2.warpAffine(self.original_image, translation_matrix, 
                                        (self.width, self.height))
        
        return translated_image, translation_matrix
    
    def apply_scaling(self, scale_x=1.5, scale_y=1.2):
        """Apply scaling transformation"""
        print(f"Applying scaling: scale_x={scale_x}, scale_y={scale_y}")
        
        # Define scaling matrix (2x3)
        scaling_matrix = np.float32([[scale_x, 0, 0],
                                   [0, scale_y, 0]])
        
        # Calculate new dimensions
        new_width = int(self.width * scale_x)
        new_height = int(self.height * scale_y)
        
        # Apply transformation
        scaled_image = cv2.warpAffine(self.original_image, scaling_matrix, 
                                    (new_width, new_height))
        
        return scaled_image, scaling_matrix
    
    def apply_rotation(self, angle=30, center=None, scale=1.0):
        """Apply rotation transformation"""
        print(f"Applying rotation: angle={angle}°, scale={scale}")
        
        if center is None:
            center = (self.width // 2, self.height // 2)
        
        # Get rotation matrix using cv2.getRotationMatrix2D
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
        
        # Apply transformation
        rotated_image = cv2.warpAffine(self.original_image, rotation_matrix, 
                                     (self.width, self.height))
        
        return rotated_image, rotation_matrix
    
    def apply_shear(self, shear_x=0.3, shear_y=0.1):
        """Apply shear transformation"""
        print(f"Applying shear: shear_x={shear_x}, shear_y={shear_y}")
        
        # Define shear matrix (2x3)
        shear_matrix = np.float32([[1, shear_x, 0],
                                 [shear_y, 1, 0]])
        
        # Apply transformation
        sheared_image = cv2.warpAffine(self.original_image, shear_matrix, 
                                     (self.width, self.height))
        
        return sheared_image, shear_matrix
    
    def apply_perspective_transform(self, src_points=None, dst_points=None):
        """Apply perspective transformation using 4-point mapping"""
        print("Applying perspective transformation...")
        
        if src_points is None:
            # Default source points (corners of the image)
            src_points = np.float32([[0, 0],
                                   [self.width-1, 0],
                                   [self.width-1, self.height-1],
                                   [0, self.height-1]])
        
        if dst_points is None:
            # Default destination points (create perspective effect)
            offset = 50
            dst_points = np.float32([[offset, offset],
                                   [self.width-1-offset, offset//2],
                                   [self.width-1-offset//2, self.height-1-offset//2],
                                   [offset//2, self.height-1-offset]])
        
        # Get perspective transformation matrix (3x3)
        perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        
        # Apply transformation
        perspective_image = cv2.warpPerspective(self.original_image, perspective_matrix,
                                              (self.width, self.height))
        
        return perspective_image, perspective_matrix, src_points, dst_points
    
    def apply_combined_affine_transform(self):
        """Apply a combination of affine transformations"""
        print("Applying combined affine transformations...")
        
        # Center point for transformations
        center = (self.width // 2, self.height // 2)
        
        # Get rotation matrix
        rotation_matrix = cv2.getRotationMatrix2D(center, 15, 0.8)
        
        # Add translation to the rotation matrix
        rotation_matrix[0, 2] += 20  # translate x
        rotation_matrix[1, 2] += 10  # translate y
        
        # Apply combined transformation
        combined_image = cv2.warpAffine(self.original_image, rotation_matrix,
                                      (self.width, self.height))
        
        return combined_image, rotation_matrix
    
    def display_results(self):
        """Display all transformation results in a grid"""
        print("Generating transformation results...")
        
        # Apply all transformations
        translated_img, _ = self.apply_translation()
        scaled_img, _ = self.apply_scaling()
        rotated_img, _ = self.apply_rotation()
        sheared_img, _ = self.apply_shear()
        perspective_img, _, _, _ = self.apply_perspective_transform()
        combined_img, _ = self.apply_combined_affine_transform()
        
        # Create a figure with subplots
        fig, axes = plt.subplots(2, 4, figsize=(16, 8))
        fig.suptitle('Image Warping Experiment Results', fontsize=16, fontweight='bold')
        
        # Display images
        images = [
            (self.original_image, "Original Image"),
            (translated_img, "Translation"),
            (scaled_img, "Scaling"),
            (rotated_img, "Rotation"),
            (sheared_img, "Shear"),
            (perspective_img, "Perspective"),
            (combined_img, "Combined Affine"),
            (np.zeros_like(self.original_image), "")  # Empty for layout
        ]
        
        for i, (img, title) in enumerate(images):
            row = i // 4
            col = i % 4
            if i < 7:  # Don't show the empty image
                axes[row, col].imshow(img)
                axes[row, col].set_title(title, fontweight='bold')
                axes[row, col].axis('off')
            else:
                axes[row, col].axis('off')
        
        plt.tight_layout()
        plt.savefig('image_warping_results.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Results saved as 'image_warping_results.png'")
    
    def demonstrate_interpolation_methods(self):
        """Demonstrate different interpolation methods"""
        print("Demonstrating different interpolation methods...")
        
        # Apply rotation with different interpolation methods
        center = (self.width // 2, self.height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.5)
        
        interpolation_methods = [
            (cv2.INTER_NEAREST, "Nearest Neighbor"),
            (cv2.INTER_LINEAR, "Bilinear"),
            (cv2.INTER_CUBIC, "Bicubic"),
            (cv2.INTER_LANCZOS4, "Lanczos")
        ]
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        fig.suptitle('Interpolation Methods Comparison', fontsize=16, fontweight='bold')
        
        for i, (method, name) in enumerate(interpolation_methods):
            row = i // 2
            col = i % 2
            
            # Apply transformation with specific interpolation
            warped = cv2.warpAffine(self.original_image, rotation_matrix,
                                  (self.width, self.height), flags=method)
            
            axes[row, col].imshow(warped)
            axes[row, col].set_title(name, fontweight='bold')
            axes[row, col].axis('off')
        
        plt.tight_layout()
        plt.savefig('interpolation_comparison.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Interpolation comparison saved as 'interpolation_comparison.png'")
    
    def analyze_transformation_effects(self):
        """Analyze and display transformation matrix effects"""
        print("\n" + "="*50)
        print("TRANSFORMATION MATRIX ANALYSIS")
        print("="*50)
        
        # Translation analysis
        _, trans_matrix = self.apply_translation(50, 30)
        print(f"\nTranslation Matrix (tx=50, ty=30):")
        print(trans_matrix)
        print("Effect: Shifts image by (50, 30) pixels")
        
        # Scaling analysis
        _, scale_matrix = self.apply_scaling(1.5, 1.2)
        print(f"\nScaling Matrix (sx=1.5, sy=1.2):")
        print(scale_matrix)
        print("Effect: Scales image by factor 1.5 in x and 1.2 in y")
        
        # Rotation analysis
        _, rot_matrix = self.apply_rotation(30)
        print(f"\nRotation Matrix (30°):")
        print(rot_matrix)
        print("Effect: Rotates image by 30° around center")
        
        # Perspective analysis
        _, persp_matrix, src_pts, dst_pts = self.apply_perspective_transform()
        print(f"\nPerspective Transformation Matrix:")
        print(persp_matrix)
        print(f"Source points: {src_pts}")
        print(f"Destination points: {dst_pts}")
        print("Effect: Creates perspective/3D viewing effect")
        
        print("\n" + "="*50)

def main():
    """Main function to run the image warping experiment"""
    print("="*60)
    print("IMAGE WARPING EXPERIMENT")
    print("="*60)
    print("AIM: To perform image warping using geometric transformations")
    print("Transformations: scaling, rotation, translation, perspective")
    print("="*60)
    
    # Initialize with sample image (you can replace with your image path)
    # warper = ImageWarping("your_image_path.jpg")  # Use your own image
    warper = ImageWarping()  # Uses sample checkerboard image
    
    # Display all transformation results
    warper.display_results()
    
    # Demonstrate interpolation methods
    warper.demonstrate_interpolation_methods()
    
    # Analyze transformation effects
    warper.analyze_transformation_effects()
    
    print("\n" + "="*60)
    print("EXPERIMENT COMPLETED SUCCESSFULLY!")
    print("Check the generated PNG files for visual results.")
    print("="*60)

if __name__ == "__main__":
    main()