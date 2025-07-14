# Linear-scaling autoencoder
This code implements an algorithm that predicts blood glucose levels by analyzing the intensity of different wavelengths using Raman spectroscopy. 
It trains a linear-scaling autoencoder (LSE) model on a custom dataset and calculates various loss functions to optimize the model. 
The code also includes options for visualizing the latent space and predictions, as well as plotting the training loss over iterations.

## Requirement ##
We recommend to make new conda envrionment. 

`conda create --name lae --file requirements.txt` 

If you want to use package without making new environment, 

`conda install --file requirements.txt`

It's also a good approach to consider running codes in environments like Colab instead of setting up a local environment.

## Installation
`conda install lae`

## Usage ##

```python
import train;
train.run(data='data/ex', tolerance=3, plot_loss=True, vis_latent=True, vis_prediction=True)
python train.py --data data/ex --tolerance 3 --plot_loss True --vis_latent True --vis_prediction True1
```
### Input data structure

- The input format should be the path to the folder containing the files.(e.g., data=/data/ex)  
- Each file should be named in the format '[glucose concentration]-[order] _ 1' (e.g., 1ng-1_1, 100ng-4_1).  
- Each file contains 2 columns, where the first column represents the wavelength and the second column contains the corresponding values.  

### Parameters
- `lse` constructor:
    1. `data`: data location
    2. `batch size`: batch size (default: 32)
    3. `device`: device (default: 0)
    4. `lr`: learning rate (default: 1e-4)
    5. `wd`: weight decay (default: 1e-5)
    6. `epoch`: epoch (default: 200)
    7. `tolerance`: _What is tolerance_ (default: 0)
    8. `layers`: hidden layer structure (input, hidden layer, latent layer) (default: [10,10])
    8. `loss_coef`: coefficents for each losses (default: [1,1,10])
    9. `name`: name of saved model ('name'.pth)
    10. `plot_loss`: loss plot (default: False)
    11. `vis_latent`: visualize latent vector (default: Fasle)
    12. `vis_prediction`: visualize prediction (default: False)

## License ##
Distributed under the MIT License. See LICENSE.txt for more information.

## Contact ##
Sangyeon Lee - lsy5518@kaist.ac.kr
