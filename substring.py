#finding the index of a substring

import multiprocessing as mp
import timeit

class Substring:

    def __init__(self, base):
        self.base = base
        self.search = ""
        self.ind = mp.Manager().Value('i', -1)
    
    def sequential_sub2(self, search):
        last_index = len(self.base) - len(search) + 1
        for i in range(0, last_index):
            sub_end = i + len(search)
            curr_sub = self.base[i:sub_end]
            if curr_sub == search:
                return i
        return -1
    
    def sequential_sub(self, search):
        return self.base.index(search)
    
    def parallel_sub(self, search, num_threads):
        last_index = len(self.base) - len(search) + 1
        self.search = search
        start_inds = list(range(0, last_index))
        
        p = mp.Pool(num_threads)
        inds = p.map_async(self.parallel_sub_helper, start_inds)  
        p.map_async(self.find_ind, inds.get())
        p.close()
        p.join()
        return self.ind.value
        
    def parallel_sub_helper(self, i):
        sub_end = i + len(self.search)
        if self.base[i:sub_end] == self.search:
            return i
        return -1
    
    def find_ind(self, i):
        if i >= 0 and (self.ind.value == -1 or i < self.ind.value):
            self.ind.value = i



def main():

    file = open('test1.txt', mode = 'r')
    base = file.read() 

    s = Substring(base)

    start = timeit.default_timer()
    s_index = s.sequential_sub2("advanced addition absolute received")
    end = timeit.default_timer()
    print("Sequential Substring index:", s_index)
    print("Sequential time:", end - start)

    start = timeit.default_timer()
    p_index = s.parallel_sub("advanced addition absolute received", 2)
    end = timeit.default_timer()
    print("Parallel Substring index:", p_index)
    print("Parallel time:", end - start)


if __name__ == "__main__":
    main()