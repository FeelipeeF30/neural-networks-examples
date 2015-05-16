TrainingData=[
    0.1701
    0.1023
    0.4405
    0.3609
    0.7192
    0.2258
    0.3175
    0.0127
    0.4290
    0.0544
    0.8000
    0.0450
    0.4268
    0.0112
    0.3218
    0.2185
    0.7240
    0.3516
    0.4420
    0.0984
    0.1747
    0.3964
    0.5114
    0.6183
    0.3330
    0.2398
    0.0508
    0.4497
    0.2178
    0.7762
    0.1078
    0.3773
    0.0001
    0.3877
    0.0821
    0.7836
    0.1887
    0.4483
    0.0424
    0.2539
    0.3164
    0.6386
    0.4862
    0.4068
    0.1611
    0.1101
    0.4372
    0.3795
    0.7092
    0.2400
    0.3087
    0.0159
    0.4330
    0.0733
    0.7995
    0.0262
    0.4223
    0.0085
    0.3303
    0.2037
    0.7332
    0.3328
    0.4445
    0.0909
    0.1838
    0.3888
    0.5277
    0.6042
    0.3435
    0.2304
    0.0568
    0.4500
    0.2371
    0.7705
    0.1246
    0.3701
    0.0006
    0.3943
    0.0646
    0.7878
    0.1694
    0.4468
    0.0372
    0.2632
    0.3048
    0.6516
    0.4690
    0.4132
    0.1523
    0.1182
    0.4334
    0.3978
    0.6987
    0.2538
    0.2998
    0.0195
    0.4366
    0.0924
    0.7984
    0.0077
];

//np=5, np=10, np=15
//n1=10, n1=15, n1=25
np=10;
n1=15;

[r,c]=size(TrainingData);

//Preparing training data
x=[];
d=[];
nd=1;
for t=np+1:1:r
    for i=1:np
        x(i,t-np)=TrainingData(t-i);
    end
    d(1,t-np)=TrainingData(t);
    nd=nd+1;
end
disp(x);
disp(d);

//Initializing ANN
NeuralNetwork = [np n1 1];
W = ann_FF_init(NeuralNetwork);

//===============Training===========
//Taxa de aprendizagem e limiar do erro
lp = [0.01, 1e-4];

//Maximo numero de épocas
epochs = 3000;

//treinando
W = ann_FF_Std_batch(x,d,NeuralNetwork,W,lp,epochs);
disp(W);

save('ANN.sod','W','np','n1');