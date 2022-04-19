#k-differences string matching

import multiprocessing as mp
import timeit

class StringMatch:

    def __init__(self, text1, text2):
        self.word1 = text1
        self.word2 = text2
        self.l1 = len(text1) + 1
        self.l2 = len(text2) + 1
        self.C = [ [0]*self.l2 for i in range(self.l1)] 

    def setup(self):
        for i in range(0, self.l1):
            self.C[i][0] = i
        for j in range(0, self.l2):
            self.C[0][j] = j

    def dp_compute(self):
        for r in range(1, self.l1):
            for c in range(1, self.l2):
                x = self.C[r-1][c] + 1
                y = self.C[r][c-1] + 1
                if self.word1[r-1] == self.word2[c-1]:
                    z = self.C[r-1][c-1]
                else:
                    z = self.C[r-1][c-1] + 1
                self.C[r][c] = min(x, y, z)
        return self.C[self.l1 - 1][self.l2 - 1]
    

def main():
    s = StringMatch("abc", "de")
    start = timeit.default_timer()
    s.setup()
    k = s.dp_compute()
    end = timeit.default_timer()
    print("k-value:", k)
    print("DP time:", end - start)
    
    

if __name__ == "__main__":
    main()