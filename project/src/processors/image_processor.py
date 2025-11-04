import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image
import pandas as pd
import numpy as np


class ImageProcessor:
    def __init__(self):
        """Initialize image processor with pre-trained ResNet50 model."""
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = torchvision.models.resnet50(pretrained=True)
        self.model.eval()
        self.model.to(self.device)
        
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
    
    def process_image(self, image_path):
        """
        Process an image and extract features.
        
        Args:
            image_path: Path to image file or file-like object
            
        Returns:
            numpy array of extracted features
        """
        if isinstance(image_path, str):
            image = Image.open(image_path).convert('RGB')
        else:
            # Handle file-like object (e.g., from Flask upload)
            image = Image.open(image_path).convert('RGB')
        
        tensor = self.transform(image).unsqueeze(0).to(self.device)
        
        with torch.no_grad():
            features = self.model(tensor)
        
        return features.cpu().numpy()
    
    def batch_process(self, image_paths):
        """Process multiple images at once."""
        results = []
        for path in image_paths:
            features = self.process_image(path)
            results.append(features.flatten())
        return np.array(results)

