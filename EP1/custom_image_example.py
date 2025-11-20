"""
Example script showing how to use your own image with the Image Warping Experiment
"""

from EP1.image_warping_experiment import ImageWarping
import cv2
import numpy as np

def run_with_custom_image(image_path):
    """Run the warping experiment with a custom image"""
    try:
        # Initialize with your custom image
        warper = ImageWarping(image_path)
        
        # Run all the demonstrations
        warper.display_results()
        warper.demonstrate_interpolation_methods()
        warper.analyze_transformation_effects()
        
        print(f"Successfully processed: {image_path}")
        
    except Exception as e:
        print(f"Error processing image: {e}")
        print("Make sure the image path is correct and the file exists.")

def create_test_image():
    """Create a test image with geometric patterns for better visualization"""
    img = np.zeros((300, 400, 3), dtype=np.uint8)
    
    # Add background gradient
    for i in range(300):
        for j in range(400):
            img[i, j] = [i//3, j//4, (i+j)//5]
    
    # Add geometric shapes for reference points
    cv2.rectangle(img, (50, 50), (150, 150), (255, 255, 255), 3)  # White rectangle
    cv2.circle(img, (300, 100), 40, (0, 255, 255), -1)  # Yellow circle
    cv2.line(img, (0, 0), (400, 300), (255, 0, 255), 5)  # Magenta diagonal
    cv2.putText(img, "TEST", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
    
    # Save the test image
    cv2.imwrite('test_image.png', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    print("Created test_image.png")
    
    return 'test_image.png'

if __name__ == "__main__":
    print("Image Warping with Custom Images")
    print("-" * 40)
    
    # Option 1: Create and use a test image
    print("Creating a test image...")
    test_img_path = create_test_image()
    print(f"Running experiment with test image: {test_img_path}")
    run_with_custom_image(test_img_path)
    
    # Option 2: Instructions for using your own image
    print("\n" + "=" * 50)
    print("TO USE YOUR OWN IMAGE:")
    print("=" * 50)
    print("1. Place your image file in the same folder as this script")
    print("2. Uncomment and modify the line below with your image path:")
    print("   # run_with_custom_image('your_image.jpg')")
    print("3. Supported formats: .jpg, .jpeg, .png, .bmp, .tiff")
    print("=" * 50)
    
    # Uncomment the line below and replace with your image path
    # run_with_custom_image('your_image.jpg')