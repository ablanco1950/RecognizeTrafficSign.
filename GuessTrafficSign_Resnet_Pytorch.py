# -*- coding: utf-8 -*-
"""

 Alfonso Blanco García , Jun 2023
"""

######################################################################
# PARAMETERS
######################################################################

######################################################################
#TabTrafficSign=['AM General Hummer SUV 2000', 'Acura Integra Type R 2001', 'Acura RL Sedan 2012', 'Acura TL Sedan 2012', 'Acura TL Type-S 2008', 'Acura TSX Sedan 2012', 'Acura ZDX Hatchback 2012', 'Aston Martin V8 Vantage Convertible 2012', 'Aston Martin V8 Vantage Coupe 2012', 'Aston Martin Virage Convertible 2012', 'Aston Martin Virage Coupe 2012', 'Audi 100 Sedan 1994', 'Audi 100 Wagon 1994', 'Audi A5 Coupe 2012', 'Audi R8 Coupe 2012', 'Audi RS 4 Convertible 2008', 'Audi S4 Sedan 2007', 'Audi S4 Sedan 2012', 'Audi S5 Convertible 2012', 'Audi S5 Coupe 2012', 'Audi S6 Sedan 2011', 'Audi TT Hatchback 2011', 'Audi TT RS Coupe 2012', 'Audi TTS Coupe 2012', 'Audi V8 Sedan 1994', 'BMW 1 Series Convertible 2012', 'BMW 1 Series Coupe 2012', 'BMW 3 Series Sedan 2012', 'BMW 3 Series Wagon 2012', 'BMW 6 Series Convertible 2007', 'BMW ActiveHybrid 5 Sedan 2012', 'BMW M3 Coupe 2012', 'BMW M5 Sedan 2010', 'BMW M6 Convertible 2010', 'BMW X3 SUV 2012', 'BMW X5 SUV 2007', 'BMW X6 SUV 2012', 'BMW Z4 Convertible 2012', 'Bentley Arnage Sedan 2009', 'Bentley Continental Flying Spur Sedan 2007', 'Bentley Continental GT Coupe 2007', 'Bentley Continental GT Coupe 2012', 'Bentley Continental Supersports Conv. Convertible 2012', 'Bentley Mulsanne Sedan 2011', 'Bugatti Veyron 16.4 Convertible 2009', 'Bugatti Veyron 16.4 Coupe 2009', 'Buick Enclave SUV 2012', 'Buick Rainier SUV 2007', 'Buick Regal GS 2012', 'Buick Verano Sedan 2012', 'Cadillac CTS-V Sedan 2012', 'Cadillac Escalade EXT Crew Cab 2007', 'Cadillac SRX SUV 2012', 'Chevrolet Avalanche Crew Cab 2012', 'Chevrolet Camaro Convertible 2012', 'Chevrolet Cobalt SS 2010', 'Chevrolet Corvette Convertible 2012', 'Chevrolet Corvette Ron Fellows Edition Z06 2007', 'Chevrolet Corvette ZR1 2012', 'Chevrolet Express Cargo Van 2007', 'Chevrolet Express Van 2007', 'Chevrolet HHR SS 2010', 'Chevrolet Impala Sedan 2007', 'Chevrolet Malibu Hybrid Sedan 2010', 'Chevrolet Malibu Sedan 2007', 'Chevrolet Monte Carlo Coupe 2007', 'Chevrolet Silverado 1500 Classic Extended Cab 2007', 'Chevrolet Silverado 1500 Extended Cab 2012', 'Chevrolet Silverado 1500 Hybrid Crew Cab 2012', 'Chevrolet Silverado 1500 Regular Cab 2012', 'Chevrolet Silverado 2500HD Regular Cab 2012', 'Chevrolet Sonic Sedan 2012', 'Chevrolet Tahoe Hybrid SUV 2012', 'Chevrolet TrailBlazer SS 2009', 'Chevrolet Traverse SUV 2012', 'Chrysler 300 SRT-8 2010', 'Chrysler Aspen SUV 2009', 'Chrysler Crossfire Convertible 2008', 'Chrysler PT Cruiser Convertible 2008', 'Chrysler Sebring Convertible 2010', 'Chrysler Town and Country Minivan 2012', 'Daewoo Nubira Wagon 2002', 'Dodge Caliber Wagon 2007', 'Dodge Caliber Wagon 2012', 'Dodge Caravan Minivan 1997', 'Dodge Challenger SRT8 2011', 'Dodge Charger SRT-8 2009', 'Dodge Charger Sedan 2012', 'Dodge Dakota Club Cab 2007', 'Dodge Dakota Crew Cab 2010', 'Dodge Durango SUV 2007', 'Dodge Durango SUV 2012', 'Dodge Journey SUV 2012', 'Dodge Magnum Wagon 2008', 'Dodge Ram Pickup 3500 Crew Cab 2010', 'Dodge Ram Pickup 3500 Quad Cab 2009', 'Dodge Sprinter Cargo Van 2009', 'Eagle Talon Hatchback 1998', 'FIAT 500 Abarth 2012', 'FIAT 500 Convertible 2012', 'Ferrari 458 Italia Convertible 2012', 'Ferrari 458 Italia Coupe 2012', 'Ferrari California Convertible 2012', 'Ferrari FF Coupe 2012', 'Fisker Karma Sedan 2012', 'Ford E-Series Wagon Van 2012', 'Ford Edge SUV 2012', 'Ford Expedition EL SUV 2009', 'Ford F-150 Regular Cab 2007', 'Ford F-150 Regular Cab 2012', 'Ford F-450 Super Duty Crew Cab 2012', 'Ford Fiesta Sedan 2012', 'Ford Focus Sedan 2007', 'Ford Freestar Minivan 2007', 'Ford GT Coupe 2006', 'Ford Mustang Convertible 2007', 'Ford Ranger SuperCab 2011', 'GMC Acadia SUV 2012', 'GMC Canyon Extended Cab 2012', 'GMC Savana Van 2012', 'GMC Terrain SUV 2012', 'GMC Yukon Hybrid SUV 2012', 'Geo Metro Convertible 1993', 'HUMMER H2 SUT Crew Cab 2009', 'HUMMER H3T Crew Cab 2010', 'Honda Accord Coupe 2012', 'Honda Accord Sedan 2012', 'Honda Odyssey Minivan 2007', 'Honda Odyssey Minivan 2012', 'Hyundai Accent Sedan 2012', 'Hyundai Azera Sedan 2012', 'Hyundai Elantra Sedan 2007', 'Hyundai Elantra Touring Hatchback 2012', 'Hyundai Genesis Sedan 2012', 'Hyundai Santa Fe SUV 2012', 'Hyundai Sonata Hybrid Sedan 2012', 'Hyundai Sonata Sedan 2012', 'Hyundai Tucson SUV 2012', 'Hyundai Veloster Hatchback 2012', 'Hyundai Veracruz SUV 2012', 'Infiniti G Coupe IPL 2012', 'Infiniti QX56 SUV 2011', 'Isuzu Ascender SUV 2008', 'Jaguar XK XKR 2012', 'Jeep Compass SUV 2012', 'Jeep Grand Cherokee SUV 2012', 'Jeep Liberty SUV 2012', 'Jeep Patriot SUV 2012', 'Jeep Wrangler SUV 2012', 'Lamborghini Aventador Coupe 2012', 'Lamborghini Diablo Coupe 2001', 'Lamborghini Gallardo LP 570-4 Superleggera 2012', 'Lamborghini Reventon Coupe 2008', 'Land Rover LR2 SUV 2012', 'Land Rover Range Rover SUV 2012', 'Lincoln Town Car Sedan 2011', 'MINI Cooper Roadster Convertible 2012', 'Maybach Landaulet Convertible 2012', 'Mazda Tribute SUV 2011', 'McLaren MP4-12C Coupe 2012', 'Mercedes-Benz 300-Class Convertible 1993', 'Mercedes-Benz C-Class Sedan 2012', 'Mercedes-Benz E-Class Sedan 2012', 'Mercedes-Benz S-Class Sedan 2012', 'Mercedes-Benz SL-Class Coupe 2009', 'Mercedes-Benz Sprinter Van 2012', 'Mitsubishi Lancer Sedan 2012', 'Nissan 240SX Coupe 1998', 'Nissan Juke Hatchback 2012', 'Nissan Leaf Hatchback 2012', 'Nissan NV Passenger Van 2012', 'Plymouth Neon Coupe 1999', 'Porsche Panamera Sedan 2012', 'Ram C-V Cargo Van Minivan 2012', 'Rolls-Royce Ghost Sedan 2012', 'Rolls-Royce Phantom Drophead Coupe Convertible 2012', 'Rolls-Royce Phantom Sedan 2012', 'Scion xD Hatchback 2012', 'Spyker C8 Convertible 2009', 'Spyker C8 Coupe 2009', 'Suzuki Aerio Sedan 2007', 'Suzuki Kizashi Sedan 2012', 'Suzuki SX4 Hatchback 2012', 'Suzuki SX4 Sedan 2012', 'Tesla Model S Sedan 2012', 'Toyota 4Runner SUV 2012', 'Toyota Camry Sedan 2012', 'Toyota Corolla Sedan 2012', 'Toyota Sequoia SUV 2012', 'Volkswagen Beetle Hatchback 2012', 'Volkswagen Golf Hatchback 1991', 'Volkswagen Golf Hatchback 2012', 'Volvo 240 Sedan 1993', 'Volvo C30 Hatchback 2012', 'Volvo XC90 SUV 2007', 'smart fortwo Convertible 2012']
#creating dictionary to label all traffic sign classes.
TabTrafficSign =[ 'Speed limit (20km/h)',
            'Speed limit (30km/h)',      
            'Speed limit (50km/h)',       
            'Speed limit (60km/h)',      
            'Speed limit (70km/h)',    
            'Speed limit (80km/h)',      
            'End of speed limit (80km/h)',     
            'Speed limit (100km/h)',    
            'Speed limit (120km/h)',     
            'No passing',   
            'No passing veh over 3.5 tons',     
            'Right-of-way at intersection',     
            'Priority road',    
            'Yield',     
            'Stop',       
            'No vehicles',       
            'Veh > 3.5 tons prohibited',       
            'No entry',       
            'General caution',     
            'Dangerous curve left',      
            'Dangerous curve right',   
            'Double curve',      
            'Bumpy road',     
            'Slippery road',       
            'Road narrows on the right',  
            'Road work',    
            'Traffic signals',      
            'Pedestrians',     
            'Children crossing',     
            'Bicycles crossing',       
            'Beware of ice/snow',
            'Wild animals crossing',      
            'End speed + passing limits',      
            'Turn right ahead',     
            'Turn left ahead',       
            'Ahead only',      
            'Go straight or right',      
            'Go straight or left',      
            'Keep right',     
            'Keep left',      
            'Roundabout mandatory',     
            'End of no passing',      
            'End no passing veh > 3.5 tons' ]
import torch
from torch import nn
import os
import re

import cv2

import numpy as np
import keras
import functools  
import time
inicio=time.time()

from torchvision import datasets, transforms, models
import torchvision.models as models
from PIL import Image

#model = models.resnet34(pretrained=True)
model = models.resnet50(pretrained=True)

# https://stackoverflow.com/questions/53612835/size-mismatch-for-fc-bias-and-fc-weight-in-pytorch
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 43)

#TabCarBrand=[]
def load_checkpoint(filepath):

    checkpoint = torch.load(filepath)
    
    #model.load_state_dict(checkpoint['state_dict'])
    model.load_state_dict(checkpoint['state_dict'], strict=False)
    #model.class_to_idx = checkpoint['class_to_idx']
    
    return model

#model_path= "my_checkpoint1.pth"
model_path= "checkpoint20epoch.pth"


model = load_checkpoint('checkpoint20epoch.pth')
# Checking model i.e. should have 196 output units in the classifier
#print(model)
#DataPath='C:\\archiveKaggle\\cars_train\\cars_train' + '\\'

def find_classes(dir):
    classes = os.listdir(dir)
    classes.sort()
    class_to_idx = {classes[i]: i for i in range(len(classes))}
    return classes, class_to_idx
#classes, c_to_idx = find_classes(data_dir+"/train")
classes, c_to_idx = find_classes('Dir_TrafficSign_Resnet/train')


print(classes, c_to_idx) 


def loadimagesTest():
    imgpath = "Dir_TrafficSign_Resnet\\valid\\"

    print("Reading imagenes from ",imgpath)

    TabDirName=[]
    for root, dirnames, filenames in os.walk(imgpath):
         for dirname in dirnames:  
             print(dirname)
             if len(dirname) < 2:
                 dirnameTo= "0" + dirname
             else:
                  dirnameTo=  dirname    
             TabDirName.append(dirnameTo)

    TotImages=0
   
    TotImagesValid=0
    TabImagePath = []
    NameImages=[]
    Y=[]
    
    for i in range(len(TabDirName)):
    
        imgpath1=imgpath+ str(TabDirName[i])+"\\"
        #print(imgpath1)
        
        # https://stackoverflow.com/questions/62137343/how-to-get-full-path-with-os-walk-function-in-python
        for root, dirnames, filenames in os.walk(imgpath1):
            for filename in filenames:  
                #print(filename)
                #if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            
                filepath = os.path.join(root, filename)
                # https://stackoverflow.com/questions/51810407/convert-image-into-1d-array-in-python
            
                #image = cv2.imread(filepath)
                #cv2.imshow("image",image)
                #cv2.waitKey(0)
                #images.append(image)
                TabImagePath.append(filepath)
                NameImages.append(filename)
                Y.append(TabDirName[i])       
                TotImages+=1
       
    print( " Total images to test "  + str(TotImages))     

    return TabImagePath, Y, NameImages


def process_image(image):
    
    # Process a PIL image for use in a PyTorch model
  
    # Converting image to PIL image using image file path
    pil_im = Image.open(f'{image}')

    """

    # Building image transform
    transform = transforms.Compose([transforms.Resize((244,244)),
                                    #transforms.CenterCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406], 
                                                         [0.229, 0.224, 0.225])]) 
    """
    transform = transforms.Compose([transforms.Resize((30,30)),
                                            transforms.CenterCrop(30),
                                            transforms.ToTensor(),
                                            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])


    # Transforming image for use with network
    pil_tfd = transform(pil_im)
    
    # Converting to Numpy array 
    array_im_tfd = np.array(pil_tfd)
    
    return array_im_tfd

def predict(image_path, model, topk=5):
    # Implement the code to predict the class from an image file   
    
    # Loading model - using .cpu() for working with CPUs
    loaded_model = load_checkpoint(model).cpu()
    # Pre-processing image
    img = process_image(image_path)
    # Converting to torch tensor from Numpy array
    img_tensor = torch.from_numpy(img).type(torch.FloatTensor)
    # Adding dimension to image to comply with (B x C x W x H) input of model
    img_add_dim = img_tensor.unsqueeze_(0)

    # Setting model to evaluation mode and turning off gradients
    loaded_model.eval()
    with torch.no_grad():
        # Running image through network
        output = loaded_model.forward(img_add_dim)
        
    #conf, predicted = torch.max(output.data, 1)   
    probs_top = output.topk(topk)[0]
    predicted_top = output.topk(topk)[1]
    
    # Converting probabilities and outputs to lists
    conf = np.array(probs_top)[0]
    predicted = np.array(predicted_top)[0]
        
    #return probs_top_list, index_top_list
    return conf, predicted


    
###########################################################
# MAIN
##########################################################

from tensorflow.keras.models import load_model


#TabImagePath_test, Y_test, imageName_test=loadimagesTest()
TabImagePath, Y_test, imageName_test=loadimagesTest()

TotalHits=0
TotalFailures=0
with open( "ModelsResults.txt" ,"w") as  w:
    
    
    
    for i in range(len(TabImagePath)):
        
                
        TabP=[]
        TabModel=[]
        TabPredictions1=[]
        

        conf, predicted1=predict(TabImagePath[i], model_path, topk=5)
        NameTrafficSignPredicted=TabTrafficSign[predicted1[0]]
        NameTrafficSignTrue=TabTrafficSign[int(Y_test[i])-1]
        IntClassPredicted= predicted1[0]
        ClassPredicted=str(IntClassPredicted)
        if len(ClassPredicted) < 2 : ClassPredicted="0"+ClassPredicted
        
        if Y_test[i]!=ClassPredicted:
            TotalFailures=TotalFailures + 1
            print("ERROR " + imageName_test[i]+ " is assigned Model " + str(ClassPredicted)+ NameTrafficSignPredicted
                  + "  True Model " + str(Y_test[i])+ NameTrafficSignTrue)
                  
        else:
            print("HIT " + imageName_test[i]+ " is assigned model " + str(ClassPredicted)+  NameTrafficSignPredicted)
                
          
                 
          
            TotalHits=TotalHits+1
        lineaw=[]
        lineaw.append(imageName_test[i]) 
        lineaw.append(str(Y_test[i]))
        lineaw.append(NameTrafficSignTrue)
        lineaw.append(str(ClassPredicted))
        lineaw.append(NameTrafficSignPredicted)
        lineaWrite =','.join(lineaw)
        lineaWrite=lineaWrite + "\n"
        w.write(lineaWrite)

    
print("")
print("Total hits = " + str(TotalHits))  
print("Total failures = " + str(TotalFailures) )     
print("Accuracy = " + str(TotalHits*100/(TotalHits + TotalFailures)) + "%") 
