import numpy as np

def sigmoid (z):
     return 1/(1+np.exp(-z))

def sigmoid_prime (z):
     return sigmoid(z)*(1-sigmoid(z))

def F_prop (W1, W2, X0):
    Y1 = np.dot (W1, X0
); 
    X1=np.append(sigmoid(Y1), np.ones((1, 4)), axis=0)
    Y2 = np.dot (W2, X1)
    X2 = sigmoid (Y2)
    return Y1,X1, Y2, X2

def F_star(W1, W2, X2,Y2, X1, Y1,y):
    X2_star=(1/4)* (X2-y); Y2_star = (X2_star) * sigmoid_prime (Y2)
    X1_star = np.dot (W2 [:, :N_1].T, Y2_star); Y1_star = (X1_star) *sigmoid_prime (Y1)
    return Y2_star, Y1_star

def predict (W1, W2, input):
    Y1,X1,Y2,X2 = F_prop (W1, W2, input)
    return np.where(X2>=0.5,1,0) 


X0=np.array([[0,0,1,1], [0,1,0,1], [1,1,1,1]]); y=np.array([[0,1,1,0]])
N_0= 2;N_1 = 2;N_2 = 1
np.random.seed(4)
W1= np.random.rand (N_1,N_0+1); W2 = np.random.rand (N_2,N_1+1)
eta = 0.5; k_max =5000
for k in range (k_max):
    Y1,X1, Y2, X2 = F_prop (W1, W2, X0)
    Y2_star, Y1_star=F_star (W1, W2, X2,Y2,X1,Y1,y)
    W1 = W1-eta*np.dot(Y1_star, X0.T)
    W2 = W2-eta*np.dot (Y2_star, X1.T)
    
print("W1=", np.round (W1, 1)); print ("W2=", np. round (W2, 1))
print("y_pred=",predict(W1, W2, X0))