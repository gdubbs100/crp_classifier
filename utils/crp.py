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

## any need to inherit?
class DCRP(CRP):

    def __init__(self, alpha):
        self.alpha = alpha
        # each index is a table, 
        # each entry is a patron with data
        self.tables = []
        ## average of patrons
        self.table_centroids = [] ### NEED TO INITIALISE THIS ###
        # where patron i is seated
        self.assignments = []

    def seat(self, i):
        if len(self.tables)==0:
            self.tables.append(i)
            self.assignments.append(0) ## is this the right index?
        else:
            assignment = self.assign_table(i)
            if assignment > len(self.tables)-1:
                self.tables.append(i)
                self.assignments.append(assignment)
            else:
                # self.tables[assignment] += 1
                self.tables[assignment] = (
                    np.vstack(
                        [
                            self.tables[assignment],
                            i
                        ]
                    )
                )
        # recalculate centroid for each table
        self.update_table_centroids()
    
    def update_table_centroids(self):
        
        return [np.mean(table, axis=0) for table in self.tables]

    def calc_probs(self, i):
        ## whats the distance metric? start with euclidean
        euc_dist = lambda x, y: np.sqrt(np.sum((x - y)**2, axis = len(y.shape) - 1))
        
        # measure distance against table centroid
        distances = [euc_dist(i, centroid) for centroid in self.table_centroids]
        C = (np.sum(distances) + self.alpha)
        table_probs = [distance / C for distance in distances]
        new_table_prob = self.alpha / C
        table_probs.append(new_table_prob)
        breakpoint()
        return table_probs
    
    def assign_table(self, i):
        probs = self.calc_probs(i)
        breakpoint()
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
