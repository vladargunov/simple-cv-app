import torch
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights
from torchvision.io import read_image


def run_classification(img : torch.Tensor):
    # Step 1: Initialize model with the best available weights
    weights = MobileNet_V2_Weights.IMAGENET1K_V1
    model = mobilenet_v2(weights=weights)
    model.eval()

    # Step 2: Initialize the inference transforms
    preprocess = weights.transforms()

    # Step 3: Apply inference preprocessing transforms
    batch = preprocess(img).unsqueeze(0)

    # Step 4: Use the model and print the predicted category
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]

    return f"{category_name}: {100 * score:.1f}%"
