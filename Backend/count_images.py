import os

def count_images_in_folder(folder_path):
    """Count the number of image files in a given folder and its subfolders."""
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return 0
    
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif', '.gif', '.webp'}
    image_count = 0
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_count += 1
    
    return image_count

def count_images_in_train_folder():
    """Count images in the train folder."""
    train_folder = os.path.join(os.getcwd(), "real-vs-ai-generated-faces-dataset", "train")
    count = count_images_in_folder(train_folder)
    print(f"Images in train folder: {count}")
    return count

def count_images_in_test_folder():
    """Count images in the test folder."""
    test_folder = os.path.join(os.getcwd(), "real-vs-ai-generated-faces-dataset", "test")
    count = count_images_in_folder(test_folder)
    print(f"Images in test folder: {count}")
    return count

if __name__ == "__main__":
    # Run the counting functions when script is executed directly
    print("--- Image Counts ---")
    print("\n--- Train/Test Split ---")
    count_images_in_train_folder()
    count_images_in_test_folder() 

    