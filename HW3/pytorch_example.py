# import libraries
import argparse
import numpy as np
import torch
from torch import nn
import torch.optim as optim
import torch.utils.data as Data
from utils import *
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using {} device".format(device))
# define settings
parser = argparse.ArgumentParser()
parser.add_argument('--num_classes', type=int, default=50, 
                    help='number of classes used')
parser.add_argument('--num_samples_train', type=int, default=15, 
                    help='number of samples per class used for training')
parser.add_argument('--num_samples_test', type=int, default=5, 
                    help='number of samples per class used for testing')
parser.add_argument('--seed', type=int, default=1, 
                    help='random seed')
args = parser.parse_args()

# define you model, loss functions, hyperparameters, and optimizers
### Your Code Here ###
epochs = 64
batch_size = 32
in_features = 28*28
out_features = 50
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(in_features, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512,out_features)
        )
    def forward(self, x):
        logits = self.linear_relu_stack(x)
        return logits
model = NeuralNetwork().to(device)
print(model)

# load data
train_image, train_label, test_image, test_label = LoadData(args.num_classes, args.num_samples_train, args.num_samples_test, args.seed)
x_train = torch.from_numpy(train_image).cuda()
y_train = torch.from_numpy(train_label).cuda()
x_test = torch.from_numpy(test_image).cuda()
y_test = torch.from_numpy(test_label).cuda()
train_dataset = Data.TensorDataset(x_train,y_train)
train_loader = Data.DataLoader(dataset=train_dataset,batch_size=batch_size,shuffle=False)
test_dataset = Data.TensorDataset(x_test,y_test)
test_loader = Data.DataLoader(dataset=test_dataset,batch_size=batch_size)

print(train_image.shape,train_label.shape)
# note: you should use train_image, train_label for training, apply the model to test_image to get predictions and use test_label to evaluate the predictions 
learning_rate = 0.01
momentum = 0.9
optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=momentum)
#criterion = nn.MSELoss()
criterion = nn.CrossEntropyLoss()
# train model using train_image and train_label
for epoch in range(epochs):
    model.train()
    size = len(train_loader.dataset)
    for batch,(x,y) in enumerate(train_loader):
        #optimizer.zero_grad()
    ### Your Code Here ###
        x = x.float()# the parameter is float or otherwise it will error
        #y = y.float()
        pred = model(x)
        loss = criterion(pred, y)
        #print(pred,y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if batch % 30 == 0:
            loss, current = loss.item(), batch*len(x)
            print(f'loss: {loss:>7f} [{current:>5d}/{size:>5d}]')

# get predictions on test_image
    '''
    model.eval()
    size = len(test_loader.dataset)
    test_loss, correct = 0,0
    with torch.no_grad():
    ### Your Code Here ###
        for x,y in test_loader:
            x = x.float()
            pred = model(x)
            test_loss += criterion(pred,y).item()
            correct += (pred.argmax(1) ==y).type(torch.float).sum().item()
    test_loss /= size
    correct /= size
    print(f'Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss:{test_loss:>8f} \n')
    '''
# evaluation
model.eval()
with torch.no_grad():
    x_test = x_test.float()
    pred = model(x_test)
    pred = np.argmax(pred.cpu().numpy(),axis=1)
print("Test Accuracy:", np.mean(1.0 * (pred == test_label)))
# note that you should not use test_label elsewhere





