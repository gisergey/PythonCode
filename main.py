import numpy as np
from matplotlib import pyplot as plt

def mistake(x : np.array,y : np.array,func= lambda x,y: np.abs(x-y)):
    if np.shape(x) != np.shape(y):
        raise Exception("arrays not the same shape")
    return sum(func(x, y))

def main():
    x = np.linspace(0, 10, 50) 
    δ = np.random.rand(*np.shape(x))
    y = x + δ
    plt.plot(x, y, 'o')
    X = np.ones((50,2))
    X[:,1] = x
    w=np.linalg.inv(X.T@X)@X.T@y
    plt.plot(x,X@w)
    plt.show()

if __name__ == '__main__':
    main()