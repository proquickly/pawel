"""
add:
torch
torchvision
Pillow
"""
import torch
from torchvision import models, transforms
from torchvision.models import ResNet50_Weights
from PIL import Image
import json

# Load the pre-trained ResNet-50 model
model = models.resnet50(weights=ResNet50_Weights.IMAGENET1K_V1)
model.eval()

# Define the image transformations
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

# Load the labels for the ImageNet dataset
with open("src/pawel/imagenet_classes.json") as f:
    labels = json.load(f)


def recognize_image(image_path):
    # Load the image
    image = Image.open(image_path).convert("RGB")  # Convert to RGB
    image = preprocess(image)
    image = image.unsqueeze(0)

    # Perform the prediction
    with torch.no_grad():
        outputs = model(image)

    # Get the predicted class
    _, predicted = outputs.max(1)
    label = labels[predicted.item()]  # Use integer index

    return label


if __name__ == "__main__":
    image_path = "/Users/andy/ws/lessons/pawel/src/pawel/xxx.png"
    label = recognize_image(image_path)
    print(f"The image is recognized as: {label}")
