import kagglehub

# Download latest version
path = kagglehub.dataset_download("philosopher0808/real-vs-ai-generated-faces-dataset")

print("Path to dataset files:", path)