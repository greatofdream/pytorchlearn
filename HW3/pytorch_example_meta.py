# import libraries
import argparse
import numpy as np
import torch
from utils_meta import *

# define settings
parser = argparse.ArgumentParser()
parser.add_argument('--num_metatrain_classes', type=int, default=1000, 
                    help='number of meta-train classes')
parser.add_argument('--num_samples_metatrain', type=int, default=20, 
                    help='number of samples per meta-train class used for meta-training')
parser.add_argument('--num_metatest_classes', type=int, default=50, 
                    help='number of meta-test classes')
parser.add_argument('--num_samples_metatest_train', type=int, default=1, 
                    help='number of samples per meta-test class used for meta-test-training, i.e., adapation')
parser.add_argument('--num_samples_metatest_test', type=int, default=10, 
                    help='number of samples per meta-test class used for final testing')
parser.add_argument('--seed',type=int, default=1, 
                    help='random seed')
args = parser.parse_args()
# in the meta-learning language, the above example is a 50-way-1-shot learning setting 

# define you model, loss functions, hyperparameters, and optimizers
### Your Code Here ###
meta_train_epochs = None
meta_test_epochs = None


# load data
metatrain_image, metatrain_label, metatest_image_training, metatest_label_training, metatest_image_testing, metatest_label_testing = LoadDataMeta(args.num_metatrain_classes, args.num_samples_metatrain, args.num_metatest_classes, args.num_samples_metatest_train, args.num_samples_metatest_test, args.seed)
# note: you should use metatrain_image, metatrain_label to meta-train, then use metatest_image_training, metatest_label_training to adapt, and finally evalute on metatest_image_testing, metatest_label_testing
# also note that, metatrain_label is [0,num_metatrain_classes), metatest_label_training/test is [num_metatrain_classes, num_metatrain_classes + num_metatest_classes) 

# metatrain model using metatrain_image and metatrain_label
for epoch in range(meta_train_epochs):
    model.train()
    optimizer.zero_grad()
    ### Your Code Here ###
    loss = None
    
    
    
    loss.backward()
    optimizer.step()    
    
# use metatest_image_training and metatest_label_training to adapt
### Your Code Here ###
for epoch in range(meta_test_epochs):
    model.train()
    optimizer.zero_grad()
    ### Your Code Here ###
    loss = None
    
    
    
    loss.backward()
    optimizer.step()    
    
# get predictions on metatest_image_testing
model.eval()
with torch.no_grad():
    ### Your Code Here ###
    pred = None
    
# evaluation
print("Final Test Accuracy:", np.mean(1.0 * (pred == metatest_label_testing)))
# note that you should not use metatest_label_testing elsewhere






