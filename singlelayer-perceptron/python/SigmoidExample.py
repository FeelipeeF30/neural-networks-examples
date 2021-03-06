import numpy as np
from neural_networks.perceptron_sigmoid import perceptron_sigmoid
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    BATCH = True
    
    X=np.matrix \
    ([ \
    [-1,    -0.65080,    0.10970,    4.001],\
    [-1,    -1.44920,    0.88960,    4.401],\
    [-1,    2.08500,    0.68760,    12.071],\
    [-1,    0.26260,    1.14760,    7.799],\
    [-1,    0.64180,    1.02340,    7.043],\
    [-1,    0.25690,    0.67300,    8.327],\
    [-1,    1.11550,    0.60430,    7.445],\
    [-1,    0.09140,    0.33990,    7.068],\
    [-1,    0.01210,    0.52560,    4.632],\
    [-1,    -0.04290,    0.46600,    5.432],\
    [-1,    0.43400,    0.68700,    8.229],\
    [-1,    0.27350,    1.02870,    7.193],\
    [-1,    0.48390,    0.48510,    7.485],\
    [-1,    0.40890,    -0.12670,    5.502],\
    [-1,    1.43910,    0.16140,    8.584],\
    [-1,    -0.91150,    -0.19730,    2.196],\
    [-1,    0.36540,    1.04750,    7.486],\
    [-1,    0.21440,    0.75150,    7.170],\
    [-1,    0.20130,    1.00140,    6.549],\
    [-1,    0.64830,    0.21830,    5.899],\
    [-1,    -0.11470,    0.22420,    7.244],\
    [-1,    -0.79700,    0.87950,    3.876],\
    [-1,    -1.06250,    0.63660,    2.471],\
    [-1,    0.53070,    0.12850,   5.688],\
    [-1,    -1.22000,    0.77770,    1.725]\
    ])
    
    print('\nTraining data: samples x number of features')
    print(X)
    D=np.matrix \
    ([\
    [-1.0],\
    [-1.0],\
    [-1.0],\
    [1.0],\
    [1.0],\
    [-1.0],\
    [1.0],\
    [-1.0],\
    [1.0],\
    [1.0],\
    [-1.0],\
    [1.0],\
    [-1.0],\
    [-1.0],\
    [-1.0],\
    [-1.0],\
    [1.0],\
    [1.0],\
    [1.0],\
    [1.0],\
    [-1.0],\
    [1.0],\
    [1.0],\
    [1.0],\
    [1.0],\
    ])
    print('\nExpected output values')
    print(D)
    
    
    if BATCH:
        learning_rate=0.00001
        max_epochs=10000
        min_error = 0.0000001
        nn = perceptron_sigmoid(None,4,learning_rate,max_epochs)
        w,epoch,error_hist = nn.train_batch(X, D,min_error)
    else: #STOCHASTIC
        learning_rate=0.00001
        max_epochs=10000
        min_error = 0.0000001
        nn = perceptron_sigmoid(None,4,learning_rate,max_epochs)
        w,epoch,error_hist = nn.train_stochastic(X, D,min_error)
    
    
    epochs=[i for i in range(len(error_hist))]
    print('Final error: %f' %error_hist[-1])
    plt.plot(epochs,error_hist)
    plt.show()  

    print('\nFinal synaptic weights:')
    print(w)
    print('\nFinal number of epochs:')
    print(epoch)
    
    X=np.matrix\
    ([\
    [-1,-0.3565,0.0620,5.9891],\
    [-1,-0.7842,1.1267,5.5912],\
    [-1,0.3012,0.5611,5.8234],\
    [-1,0.7757,1.0648,8.0677],\
    [-1,0.1570,0.8028,6.3040],\
    [-1,-0.7014,1.0316,3.6005],\
    [-1,0.3748,0.1536,6.1537],\
    [-1,-0.6920,0.9404,4.4058],\
    [-1,-1.3970,0.7141,4.9263],\
    [-1,-1.8842,-0.2805,1.2548]\
    ])
    
    print('\nClassification:')
        
    for x in X:
        y=nn.classify(x,None)
        print(y)
    
    X=np.matrix\
    ([\
    [-1.0, 0.3957, 0.1076, 5.6623],\
    [-1.0, -0.1013, 0.5989, 7.1812],\
    [-1.0, 2.4482, 0.9455, 11.2095],\
    [-1.0, 2.0149, 0.6192, 10.9263],\
    [-1.0, 0.2012, 0.2611, 5.4631]\
    ])
         
    print('\nClassification:')
        
    for x in X:
        y=nn.classify(x,None)
        print(y)    