import numpy as np
from sklearn.linear_model import Lasso
from argparse import ArgumentParser

# Parse arguments
parser = ArgumentParser()
parser.add_argument('seed', type=int, help='Seed for rng')
args = parser.parse_args()
seed = args.seed


rng = np.random.RandomState(seed)
# Hyper parameters with random search
log_alpha_range = (-4, 4)
log_alpha = rng.uniform(*log_alpha_range)

# Data (with no structure)
X = np.random.randn(100, 10)
y = np.random.randn(100)


# Fit the model using hyperparameters
model = Lasso(alpha=np.exp(log_alpha))
model.fit(X, y)
# Run some analysis with or on the model, save things...
np.savez('{}.npz'.format(seed), coef=model.coef_)
