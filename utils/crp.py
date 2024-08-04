"""
Class for Chinese Restaurant Process
"""
import numpy as np
from scipy.special import softmax

class CRP:

    def __init__(self, alpha):
        self.alpha = alpha
        # each index is a table, 
        # each entry is count of patrons
        self.tables = []


    def seat(self, i=None):
        if len(self.tables)==0:
            self.tables.append(1)
        else:
            assignment = self.assign_table()
            if assignment > len(self.tables)-1:
                self.tables.append(1)
            else:
                self.tables[assignment] += 1
        
    def calc_probs(self):
        C = (sum(self.tables) + self.alpha)
        ## calculate weighting by table
        table_probs = [i/C for i in self.tables]
        # probability of new table
        new_table_prob = self.alpha / C
        table_probs.append(new_table_prob)
        return table_probs
    
    def assign_table(self):
        probs = self.calc_probs()
        return (
            np.random.choice(
                [i for i in range(len(self.tables)+1)],
                p=probs
            )
        )

## any need to inherit?
class DCRP(CRP):

    def __init__(self, alpha, distance_func):
        self.alpha = alpha
        # each index is a table, 
        # each entry is a patron with data
        self.tables = []
        ## average of patrons
        self.table_centroids = [] ### NEED TO INITIALISE THIS ###
        # where patron i is seated
        self.assignments = []
        ## record all customers
        self.customer_list = []
        ## distance function
        self.distance_func = distance_func

    def seat(self, i):
        if len(self.customer_list) == 0:
            self.customer_list.append(i)
            self.assignments.append(0) ## first customer
        else:
            assignment = self.assign_customer(i)
            self.customer_list.append(i)
            self.assignments.append(assignment)

    
    def assign_customer(self, i):
        probs = self.calc_probs(i)
        # breakpoint()
        return (
            np.random.choice(
                [i for i in range(len(self.customer_list)+1)],
                p=probs
            )
        )
    
    def calc_probs(self, i):

        distances = [
            self.distance_func(i, customer)
            for customer in self.customer_list
        ]

        table_probs = softmax(
            [distances +[self.alpha]]
        )

        return table_probs.squeeze()
    

if __name__=="__main__":

    crp = CRP(0.1)

    # ## test tables
    # crp.tables = [1,9,7,10]
    # print(crp.tables)
    # print(crp.calc_probs())
    # print(crp.assign_table())

    # crp2 = CRP(0.5)
    # for i in range(10):
    #     crp2.seat(i)

    # print(crp2.tables)
