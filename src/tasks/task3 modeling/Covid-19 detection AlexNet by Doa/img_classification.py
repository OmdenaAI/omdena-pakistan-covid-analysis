from PIL import Image
import torchvision.transforms as transforms
import cv2
import torch
import torchvision.models as models
import torch.nn as nn
import numpy as np

def Model_predict(img):
    AlexNet_model = torch.hub.load('pytorch/vision:v0.6.0', 'alexnet', pretrained=True)

    # check if CUDA is available
    use_cuda = torch.cuda.is_available()

    for param in AlexNet_model.features.parameters():
        param.requires_grad = False 

    #Updating the second classifier
    AlexNet_model.classifier[4] = nn.Linear(4096,1024)

    #Updating the third and the last classifier that is the output layer of the network. Make sure to have 2 output nodes 
    AlexNet_model.classifier[6] = nn.Linear(1024,2)

    
    # load the model that got the best validation accuracy 
    AlexNet_model.load_state_dict(torch.load('Model_AlexNet_Covid19_4.pt'))
    
    #224x224 images as input
    data_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))

    ])
    

    
    transformed_img = data_transform(img.convert('RGB'))
    #make the tensor 4D, instead of 3D
    transformed_img = transformed_img.unsqueeze(0)
    
    if use_cuda:
        transformed_img = transformed_img.cuda()
        
    output = AlexNet_model(transformed_img)
    
    if use_cuda:
        output = output.cpu()
        
    _, preds_tensor = torch.max(output, 1)
    preds = np.squeeze(preds_tensor.numpy()) if not use_cuda else np.squeeze(preds_tensor.cpu().numpy())
    #print(preds)

    classes = ['CT_COVID', 'CT_NonCOVID']
    pred_class = classes[preds]
        
    #print("Predicted Class : " , pred_class)
    return pred_class
