# graph :
# e1<-x1->x2->e2
import numpy as np
#basic particle filter
# P(xt = x) = no.of particles at x / total no. of particles
# P(xt = x | xt-1 = x') = P(xt = x, xt-1 = x') / P(xt-1 = x')
#forward model: P(xt = x | xt-1 = x')
def forward(trans_probs, curr_state, next_state):
    #x1 -> x2 : prob = 0.5
    #draw from uniform distribution
    # for each particle in curr_state, draw a sample from uniform distribution
    samples = []
    for i in range(300):
        val = np.random.uniform(0, 1)
        if val > trans_probs:
            obs = np.choose(np.random.choice([0,1]),['e1','e2'])
            samples.append((next_state,obs))
        else:
            obs = np.choose(np.random.choice([0,1]),['e1','e2'])
            samples.append((curr_state,obs))
    return samples

def observe(samples):
    # evidence in x1 = e1 P(x1, e1) = 0.8, p(x1, e2) = 0.2
    # evidence in x2 = e2 P(x2, e2) = 0.9, p(x2, e1) = 0.1
    # w = p(xi) * p(ei | xi)
    # prior belief = p(xi) = 0.5
    weights = []
    for sample in samples:
        sample_ = sample[0]
        obs  = sample[1]
        if sample_ == 'x1' and obs == 'e1':
            weights.append(0.8*0.5)
        elif sample_ == 'x1' and obs == 'e2':
            weights.append(0.2*0.5)
        elif sample_ == 'x2' and obs == 'e2':
            weights.append(0.9*0.5)
        elif sample_ == 'x2' and obs == 'e1':
            weights.append(0.1*0.5)

    # normalize p(xi, ei) = p(X,ei)/ sum(p(X,ei))
    weights = weights/np.sum(weights)
    # predicted_state = np.random.choice(samples, p=weights)
    #or maximum weighted state
    predicted_state_index = np.argmax(weights)
    print(samples[predicted_state_index])
    return weights

def resample(samples, weights):
    # resample from samples with probability = weights
    # resample 100 particles
    # pick 100 samples from samples with probability = weights
    # return resampled samples
    resampled_samples = []
    samples = np.array(samples)
    samples = samples[:,0]
    for i in range(100):
        resampled_samples.append(np.random.choice(samples, p=weights))
    return resampled_samples

if __name__ == '__main__':
    print("running forward")
    samples = forward(0.5, 'x1', 'x2')
    print("running observe")
    weights = observe(samples)
    print("resample with new belief")
    resampled_samples = resample(samples, weights)
    #continue this loop for some iterations