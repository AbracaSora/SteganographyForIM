import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import os
import random
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.tensorboard import SummaryWriter

def getData(data_dir):
    truncate_path = data_dir + ('%05d' % 3755)
    image_names=[]
    for root, sub_folder, file_list in os.walk(data_dir):
        if root < truncate_path:
            # 每张图片的地址的数组
            image_names += [os.path.join(root, file_path) for file_path in file_list]
    labels = [int(file_name[len(data_dir):].split(os.sep)[0]) for file_name in image_names]
    random.seed(2)
    random.shuffle(image_names)
    random.seed(2)
    random.shuffle(labels)
    return image_names, labels

class GJCTV(Dataset):
    '''
        @param
        resize：将图片大小根据网络结构适配
        mode：train或者test模式
    '''
    def __init__(self, images, labels, mode):
        super(GJCTV, self).__init__()
        self.images = images
        self.labels = labels
        if mode == 'train': # 80%
            self.images = self.images[:int(0.9*len(self.images))]
            self.labels = self.labels[:int(0.9*len(self.labels))]
        elif mode == 'val': # 20%
            self.images = self.images[int(0.9*len(self.images)):]
            self.labels = self.labels[int(0.9*len(self.labels)):]

    def __len__(self):
        return len(self.images)

    def __getitem__(self,idx):
        img, label = self.images[idx],self.labels[idx]
       # print('1:\n',img)
        img = Image.open(img).convert('RGB')
       # print('2:\n',img)
        mean = [0.485, 0.456, 0.406]
        std = [0.229, 0.224, 0.225]
        tf = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=mean,std=std)
        ])
        img=tf(img)
        label = torch.tensor(label)
        return img, label

class OCR_model(nn.Module):
    def __init__(self,num_classes,**kwargs):
        super().__init__()
        self.backbone=nn.Sequential(
            nn.Conv2d(3, 64, 3, 1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2, padding=1),
            nn.Conv2d(64, 128, 3, 1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2, padding=1),
            nn.Conv2d(128, 256, 3, 1, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2, padding=1),
            nn.Conv2d(256, 512, 3, 1, padding=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2, 2, padding=1),
        )
        self.linear = nn.Linear(12800, num_classes, bias=True)

    def forward(self, x):
        x = self.backbone(x)
        x = torch.flatten(x, 1)
        x = self.linear(x)
        return x