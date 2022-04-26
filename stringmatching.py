#k-differences string matching

import multiprocessing as mp
import timeit

class StringMatch:

    def __init__(self, text1, text2):
        self.word1 = text1
        self.word2 = text2
        self.help_text1 = ""
        self.help_text2 = ""
        self.l1 = len(text1) + 1
        self.l2 = len(text2) + 1
        self.C = [[0]*self.l2 for i in range(self.l1)]
        self.diff_count = mp.Manager().Value('i', 0) 

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
    
    def par_compute(self, num_processes):
        start_inds1 = list(range(0, len(self.word1)))
        #start_inds2 = list(range(1, len(self.word2) + 1))
        p = mp.Pool(num_processes)
        p.map(self.compare_strings, start_inds1)
        return self.diff_count.value

    def compare_strings(self, i):
        if self.word1[i] != self.word2[i]:
            self.diff_count.value += 1


def main():
    s = StringMatch("abd", "dbb")
    start = timeit.default_timer()
    s.setup()
    k = s.dp_compute()
    end = timeit.default_timer()
    print("Sequential k-value:", k)
    print("DP time:", end - start)
    
    start = timeit.default_timer()
    k = s.par_compute(2)
    end = timeit.default_timer()
    print("\nParallel k-value:", k)
    print("Parallel time:", end - start)
    
    
if __name__ == "__main__":
    main()