from precise.skatertools.syntheticdata.factor import create_band_dataset, create_factor_dataset
import numpy as np

DEFAULT_COV_NOISE = 0.2

# Generate random covariance matrices

def random_factor_cov(n=500, n_dim=100):
    xs = create_factor_dataset(n=n, n_dim=n_dim)
    return np.cov(xs,rowvar=False)


def random_band_cov(n=250, n_dim=20, n_bands=5):
    xs = create_band_dataset(n=250, n_dim=20, n_bands=5)
    return np.cov(xs, rowvar=False)


def random_known_cov(cov, n_samples=60):
    n_dim = np.shape(cov)[0]
    xs = np.random.multivariate_normal(mean=np.zeros(n_dim), cov=cov, size=n_samples)
    return np.cov(xs,rowvar=False)


def jiggle_cov(cov, noise=DEFAULT_COV_NOISE):
    n_assets = np.shape(cov)[0]
    x_rand = np.atleast_2d(np.random.randn(n_assets) * np.sqrt(np.diag(cov) + 0.000001))
    cov_jiggle = np.dot(np.transpose(x_rand), x_rand)
    jiggled_cov = cov + noise * cov_jiggle
    return jiggled_cov
