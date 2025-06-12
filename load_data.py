import kagglehub
import shutil
import os

# Download latest version with force download to clear cache
path = kagglehub.dataset_download("philosopher0808/real-vs-ai-generated-faces-dataset", force_download=True)

print("Path to dataset files:", path)

# Copy to current directory
current_dir = os.getcwd()
dataset_dir = os.path.join(current_dir, "real-vs-ai-generated-faces-dataset")

print(current_dir)
print(dataset_dir)
# Create the dataset directory if it doesn't exist
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Copy all files from cache to current directory
for item in os.listdir(path):
    src = os.path.join(path, item)
    dst = os.path.join(dataset_dir, item)
    if os.path.isdir(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copy2(src, dst)

print(f"Dataset copied to: {dataset_dir}")