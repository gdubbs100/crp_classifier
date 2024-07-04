"""
Class for Chinese Restaurant Process
"""
import numpy as np

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

if __name__=="__main__":

    crp = CRP(0.1)

    ## test tables
    crp.tables = [1,9,7,10]
    print(crp.tables)
    print(crp.calc_probs())
    print(crp.assign_table())

    crp2 = CRP(0.5)
    for i in range(10):
        crp2.seat(i)

    print(crp2.tables)
