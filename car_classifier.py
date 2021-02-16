import torchvision.transforms as tr
import torchvision.models
from PIL import Image
import torch
import torch.nn as nn
import cv2
import numpy as np

def predict_car(path_to_model, path_to_image):

    net = cv2.dnn.readNetFromDarknet('yolo-coco/yolov3.cfg', 'yolo-coco/yolov3.weights')

    image = cv2.imread(path_to_image)
    (H, W) = image.shape[:2]

    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
                              swapRB=True, crop=False)
    net.setInput(blob)
    layerOutputs = net.forward(ln)
    boxes = []
    confidences = []
    classIDs = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > 0.5:
                box = detection[0:4] * np.array([W, H, W, H])
                (centerX, centerY, width, height) = box.astype("int")

                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))

                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.3)

    bboxs = []
    list_of_cars = []

    if len(idxs) > 0:
        for i in idxs.flatten():
            bbox = []
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            if classIDs[i] == 2:
                bbox.append(x)
                bbox.append(y)
                bbox.append(w)
                bbox.append(h)
                bboxs.append(bbox)
                image_crop = image[bboxs[0][1]:bboxs[0][1] + bboxs[0][3], bboxs[0][0]:bboxs[0][0] + bboxs[0][2]]
                list_of_cars.append(image_crop)

    clases = ['AM General Hummer SUV 2000',
 'Acura Integra Type R 2001',
 'Acura RL Sedan 2012',
 'Acura TL Sedan 2012',
 'Acura TL Type-S 2008',
 'Acura TSX Sedan 2012',
 'Acura ZDX Hatchback 2012',
 'Aston Martin V8 Vantage Convertible 2012',
 'Aston Martin V8 Vantage Coupe 2012',
 'Aston Martin Virage Convertible 2012',
 'Aston Martin Virage Coupe 2012',
 'Audi 100 Sedan 1994',
 'Audi 100 Wagon 1994',
 'Audi A5 Coupe 2012',
 'Audi R8 Coupe 2012',
 'Audi RS 4 Convertible 2008',
 'Audi S4 Sedan 2007',
 'Audi S4 Sedan 2012',
 'Audi S5 Convertible 2012',
 'Audi S5 Coupe 2012',
 'Audi S6 Sedan 2011',
 'Audi TT Hatchback 2011',
 'Audi TT RS Coupe 2012',
 'Audi TTS Coupe 2012',
 'Audi V8 Sedan 1994',
 'BMW 1 Series Convertible 2012',
 'BMW 1 Series Coupe 2012',
 'BMW 3 Series Sedan 2012',
 'BMW 3 Series Wagon 2012',
 'BMW 6 Series Convertible 2007',
 'BMW ActiveHybrid 5 Sedan 2012',
 'BMW M3 Coupe 2012',
 'BMW M5 Sedan 2010',
 'BMW M6 Convertible 2010',
 'BMW X3 SUV 2012',
 'BMW X5 SUV 2007',
 'BMW X6 SUV 2012',
 'BMW Z4 Convertible 2012',
 'Bentley Arnage Sedan 2009',
 'Bentley Continental Flying Spur Sedan 2007',
 'Bentley Continental GT Coupe 2007',
 'Bentley Continental GT Coupe 2012',
 'Bentley Continental Supersports Conv. Convertible 2012',
 'Bentley Mulsanne Sedan 2011',
 'Bugatti Veyron 16.4 Convertible 2009',
 'Bugatti Veyron 16.4 Coupe 2009',
 'Buick Enclave SUV 2012',
 'Buick Rainier SUV 2007',
 'Buick Regal GS 2012',
 'Buick Verano Sedan 2012',
 'Cadillac CTS-V Sedan 2012',
 'Cadillac Escalade EXT Crew Cab 2007',
 'Cadillac SRX SUV 2012',
 'Chevrolet Avalanche Crew Cab 2012',
 'Chevrolet Camaro Convertible 2012',
 'Chevrolet Cobalt SS 2010',
 'Chevrolet Corvette Convertible 2012',
 'Chevrolet Corvette Ron Fellows Edition Z06 2007',
 'Chevrolet Corvette ZR1 2012',
 'Chevrolet Express Cargo Van 2007',
 'Chevrolet Express Van 2007',
 'Chevrolet HHR SS 2010',
 'Chevrolet Impala Sedan 2007',
 'Chevrolet Malibu Hybrid Sedan 2010',
 'Chevrolet Malibu Sedan 2007',
 'Chevrolet Monte Carlo Coupe 2007',
 'Chevrolet Silverado 1500 Classic Extended Cab 2007',
 'Chevrolet Silverado 1500 Extended Cab 2012',
 'Chevrolet Silverado 1500 Hybrid Crew Cab 2012',
 'Chevrolet Silverado 1500 Regular Cab 2012',
 'Chevrolet Silverado 2500HD Regular Cab 2012',
 'Chevrolet Sonic Sedan 2012',
 'Chevrolet Tahoe Hybrid SUV 2012',
 'Chevrolet TrailBlazer SS 2009',
 'Chevrolet Traverse SUV 2012',
 'Chrysler 300 SRT-8 2010',
 'Chrysler Aspen SUV 2009',
 'Chrysler Crossfire Convertible 2008',
 'Chrysler PT Cruiser Convertible 2008',
 'Chrysler Sebring Convertible 2010',
 'Chrysler Town and Country Minivan 2012',
 'Daewoo Nubira Wagon 2002',
 'Dodge Caliber Wagon 2007',
 'Dodge Caliber Wagon 2012',
 'Dodge Caravan Minivan 1997',
 'Dodge Challenger SRT8 2011',
 'Dodge Charger SRT-8 2009',
 'Dodge Charger Sedan 2012',
 'Dodge Dakota Club Cab 2007',
 'Dodge Dakota Crew Cab 2010',
 'Dodge Durango SUV 2007',
 'Dodge Durango SUV 2012',
 'Dodge Journey SUV 2012',
 'Dodge Magnum Wagon 2008',
 'Dodge Ram Pickup 3500 Crew Cab 2010',
 'Dodge Ram Pickup 3500 Quad Cab 2009',
 'Dodge Sprinter Cargo Van 2009',
 'Eagle Talon Hatchback 1998',
 'FIAT 500 Abarth 2012',
 'FIAT 500 Convertible 2012',
 'Ferrari 458 Italia Convertible 2012',
 'Ferrari 458 Italia Coupe 2012',
 'Ferrari California Convertible 2012',
 'Ferrari FF Coupe 2012',
 'Fisker Karma Sedan 2012',
 'Ford E-Series Wagon Van 2012',
 'Ford Edge SUV 2012',
 'Ford Expedition EL SUV 2009',
 'Ford F-150 Regular Cab 2007',
 'Ford F-150 Regular Cab 2012',
 'Ford F-450 Super Duty Crew Cab 2012',
 'Ford Fiesta Sedan 2012',
 'Ford Focus Sedan 2007',
 'Ford Freestar Minivan 2007',
 'Ford GT Coupe 2006',
 'Ford Mustang Convertible 2007',
 'Ford Ranger SuperCab 2011',
 'GMC Acadia SUV 2012',
 'GMC Canyon Extended Cab 2012',
 'GMC Savana Van 2012',
 'GMC Terrain SUV 2012',
 'GMC Yukon Hybrid SUV 2012',
 'Geo Metro Convertible 1993',
 'HUMMER H2 SUT Crew Cab 2009',
 'HUMMER H3T Crew Cab 2010',
 'Honda Accord Coupe 2012',
 'Honda Accord Sedan 2012',
 'Honda Odyssey Minivan 2007',
 'Honda Odyssey Minivan 2012',
 'Hyundai Accent Sedan 2012',
 'Hyundai Azera Sedan 2012',
 'Hyundai Elantra Sedan 2007',
 'Hyundai Elantra Touring Hatchback 2012',
 'Hyundai Genesis Sedan 2012',
 'Hyundai Santa Fe SUV 2012',
 'Hyundai Sonata Hybrid Sedan 2012',
 'Hyundai Sonata Sedan 2012',
 'Hyundai Tucson SUV 2012',
 'Hyundai Veloster Hatchback 2012',
 'Hyundai Veracruz SUV 2012',
 'Infiniti G Coupe IPL 2012',
 'Infiniti QX56 SUV 2011',
 'Isuzu Ascender SUV 2008',
 'Jaguar XK XKR 2012',
 'Jeep Compass SUV 2012',
 'Jeep Grand Cherokee SUV 2012',
 'Jeep Liberty SUV 2012',
 'Jeep Patriot SUV 2012',
 'Jeep Wrangler SUV 2012',
 'Lamborghini Aventador Coupe 2012',
 'Lamborghini Diablo Coupe 2001',
 'Lamborghini Gallardo LP 570-4 Superleggera 2012',
 'Lamborghini Reventon Coupe 2008',
 'Land Rover LR2 SUV 2012',
 'Land Rover Range Rover SUV 2012',
 'Lincoln Town Car Sedan 2011',
 'MINI Cooper Roadster Convertible 2012',
 'Maybach Landaulet Convertible 2012',
 'Mazda Tribute SUV 2011',
 'McLaren MP4-12C Coupe 2012',
 'Mercedes-Benz 300-Class Convertible 1993',
 'Mercedes-Benz C-Class Sedan 2012',
 'Mercedes-Benz E-Class Sedan 2012',
 'Mercedes-Benz S-Class Sedan 2012',
 'Mercedes-Benz SL-Class Coupe 2009',
 'Mercedes-Benz Sprinter Van 2012',
 'Mitsubishi Lancer Sedan 2012',
 'Nissan 240SX Coupe 1998',
 'Nissan Juke Hatchback 2012',
 'Nissan Leaf Hatchback 2012',
 'Nissan NV Passenger Van 2012',
 'Plymouth Neon Coupe 1999',
 'Porsche Panamera Sedan 2012',
 'Ram C-V Cargo Van Minivan 2012',
 'Rolls-Royce Ghost Sedan 2012',
 'Rolls-Royce Phantom Drophead Coupe Convertible 2012',
 'Rolls-Royce Phantom Sedan 2012',
 'Scion xD Hatchback 2012',
 'Spyker C8 Convertible 2009',
 'Spyker C8 Coupe 2009',
 'Suzuki Aerio Sedan 2007',
 'Suzuki Kizashi Sedan 2012',
 'Suzuki SX4 Hatchback 2012',
 'Suzuki SX4 Sedan 2012',
 'Tesla Model S Sedan 2012',
 'Toyota 4Runner SUV 2012',
 'Toyota Camry Sedan 2012',
 'Toyota Corolla Sedan 2012',
 'Toyota Sequoia SUV 2012',
 'Volkswagen Beetle Hatchback 2012',
 'Volkswagen Golf Hatchback 1991',
 'Volkswagen Golf Hatchback 2012',
 'Volvo 240 Sedan 1993',
 'Volvo C30 Hatchback 2012',
 'Volvo XC90 SUV 2007',
 'smart fortwo Convertible 2012']

    transforms = tr.Compose([tr.ToPILImage(),
                             tr.Resize((224, 224)),
                             tr.ToTensor(),
                             tr.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

    model = torchvision.models.resnet101(pretrained=False)
    model.fc = nn.Linear(2048, 196)
    model.load_state_dict(torch.load(path_to_model, map_location=torch.device('cpu')))
    model.eval()

    cars_on_photo = []
    for i in list_of_cars:
        image = i
        image = transforms(image).float()
        image = torch.autograd.Variable(image.view(3, 224, 224))
        image = image.unsqueeze(0)
        pred = model(image)
        _, predict = torch.max(pred.data, 1)
        car_class = clases[predict.item()]
        cars_on_photo.append(car_class)
    return cars_on_photo

cars_on_photo = predict_car('C:/Users/esus/Desktop/model_stat_dict.pt', 'C:/Users/esus/Desktop/3.jpg')
print(cars_on_photo)