# LAE
This agoritm ~ descpriton

## Requirement ##

	torch==1.11.0+cu113
	numpy==1.21.6
	sklearn==1.0.2
	matplotlib
  ```

## Installation
`pip install node2vec`

## Usage ##

```python
import train;
train.run(data='data/ftir.csv', tolerance=3, plot_loss=True, vis_latent=True, vis_prediction=True)
python train.py --data data/ftir.csv --tolerance 3 --plot_loss True --vis_latent True --vis_prediction True1

### Parameters
- `lae` constructor:
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
