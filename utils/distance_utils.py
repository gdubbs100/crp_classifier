import numpy as np

class DistanceFunc:

    def __init__(self, func: callable, params_dict: dict):
        self.func = func
        self.params_dict = params_dict

    def __call__(self, x: np.array, y: np.array):
        return self.func(x, y, **self.params_dict)

euc_dist = lambda x, y, d: (
        (np.sum((x - y)**d, axis = len(y.shape) - 1))**(1/d)
    )

if __name__=="__main__":

    # euc_dist = lambda x, y, d: (
    #         (np.sum((x - y)**d, axis = len(y.shape) - 1))**(1/d)
    #     )
    
    x = np.array([1,1,1])
    y = np.array([0,0,0])

    for i in range(1, 10):
        EucDist = DistanceFunc(
            func = euc_dist,
            params_dict = {'d':i}
        )
        # print(euc_dist(x, y, **{'d':2}))
        print(i, EucDist(x, y))