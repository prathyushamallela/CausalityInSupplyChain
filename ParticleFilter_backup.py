import numpy as np
import numpy as np
import scipy as scipy
from numpy.random import uniform
import scipy.stats

#show particles as part of graph

def create_uniform_particles(x_range, y_range, N):
    particles = np.empty((N, 2))
    particles[:, 0] = uniform(x_range[0], x_range[1], size=N)
    particles[:, 1] = uniform(y_range[0], y_range[1], size=N)
    return particles


def predict(particles, u, std, dt=1.):
    N = len(particles)
    dist = (u[1] * dt) + (np.random.randn(N) * std[1])
    particles[:, 0] += np.cos(u[0]) * dist
    particles[:, 1] += np.sin(u[0]) * dist


def update(particles, weights, z, R, landmarks):
    weights.fill(1.)
    for i, landmark in enumerate(landmarks):
        distance = np.power((particles[:, 0] - landmark[0]) ** 2 + (particles[:, 1] - landmark[1]) ** 2, 0.5)
        weights *= scipy.stats.norm(distance, R).pdf(z[i])

    weights += 1.e-300  # avoid round-off to zero
    weights /= sum(weights)


def neff(weights):
    return 1. / np.sum(np.square(weights))


def systematic_resample(weights):
    N = len(weights)
    positions = (np.arange(N) + np.random.random()) / N

    indexes = np.zeros(N, 'i')
    cumulative_sum = np.cumsum(weights)
    i, j = 0, 0
    while i < N and j < N:
        if positions[i] < cumulative_sum[j]:
            indexes[i] = j
            i += 1
        else:
            j += 1
    return indexes


def estimate(particles, weights):
    pos = particles[:, 0:1]
    mean = np.average(pos, weights=weights, axis=0)
    var = np.average((pos - mean) ** 2, weights=weights, axis=0)
    return mean, var


def resample_from_index(particles, weights, indexes):
    particles[:] = particles[indexes]
    weights[:] = weights[indexes]
    weights /= np.sum(weights)