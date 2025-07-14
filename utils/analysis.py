'''
Analysis of trained linear scaling autoencoder with test data
'''

import torch
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics
from matplotlib import cm
import utils.read_data as rd

def get_color(y):
    cmm = cm.get_cmap('inferno')
    ymin = min(y)
    ymax = max(y)
    colorlist= []
    for i in range(len(y)):
        if y[i] >= ymin and y[i] <= ymax:
            normalized = float(((y[i]-ymin)/(ymax-ymin)))
            colorlist.append(cmm(normalized))
        else:
            colorlist.append((0,0,0))
    return colorlist


def vis_latentspace(X, y):
    '''
    :param X: latent coordinate a, b
    :param y: external variables
    :return: scatter plot of latent space
    '''
    y_colors = np.array(get_color(y))
    X1 = np.array(X)[:,0]
    X2 = np.array(X)[:,1]
    for i in range(len(y)):
        plt.scatter(X1[i], X2[i], 80, color=y_colors[i], alpha=1, linewidths=1, edgecolors='black')

    plt.show()
    plt.clf()


def vis_prediction(X, y):
    '''
    Compare prediction values and external variables
    :param X: latent coordinate a, b (use a-axis only (X[:0])
    :param y: external variables
    :return: prediction plot, r2 score
    '''
    X1 = np.array(X)[:, 0]
    plt.scatter(X1, y, 80, alpha= 0.8, color='lightgrey', linewidths=1, edgecolors='black')
    plt.show()
    plt.clf()

    r2 = sklearn.metrics.r2_score(y, X1)
    print('r2 score: ', r2)
    return r2

def test_model(modelname, opt):
    '''
    Load trained model 
    ex) model = torch.load('PATH TO MODEL WEIGHT')
    '''
    model.to(opt.device)
    model.eval()
    x_tensor =[]
    X, y = rd.getData(opt.data, 'test')
    for i in range(len(X)):
        x_tensor.append(torch.from_numpy(np.array(X[i]).astype(np.float32)))
    xlatent = []
    for i in range(len(x_tensor)):
        latentspace = model.encoder(x_tensor[i].to(opt.device)).cpu().detach().numpy()
        xlatent.append(latentspace)

    if opt.vis_latent == True:
        vis_latentspace(xlatent, y)

    if opt.vis_prediction == True:
        r2 = vis_prediction(xlatent, y)
    return r2
