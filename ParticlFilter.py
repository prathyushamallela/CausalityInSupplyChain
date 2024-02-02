import numpy as np
#inputs: e, (dbn->) prior, transitionmodel, sensormodel, N
def initialise(e ,trans_probs,next_state,curr_state ,N):
    Samples=[]
    for i in range(300):
        val = np.random.uniform(0, 1)
        if val > trans_probs:
            obs = np.choose(np.random.choice([0, 1]), e)
            Samples.append((next_state, obs))
        else:
            obs = np.choose(np.random.choice([0, 1]), e)
            Samples.append((curr_state, obs))
    return Samples

def propagate():
    update = []
    return update

def weight():
    weight = []
    return weight

def Resample():
    resample = []
    return resample #resample and send values to next timestep

def updateDBNtables():
    transitionmodelupdate = []
    sensormodelupdate = []
    priorsupdate = []
    return transitionmodelupdate, sensormodelupdate, priorsupdate

def validatePF():
    return 0