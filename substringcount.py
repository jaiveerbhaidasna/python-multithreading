#finding the index of a substring

import multiprocessing as mp
import timeit

class Substring:

    def __init__(self, base):
        self.base = base
        self.search = ""
        self.count = mp.Manager().Value('i', 0)
    
    def sequential_sub(self, search):
        local_count = 0
        last_index = len(self.base) - len(search) + 1
        for i in range(0, last_index):
            sub_end = i + len(search)
            curr_sub = self.base[i:sub_end]
            if curr_sub == search:
                local_count += 1
        return local_count
    
    def parallel_sub(self, search):
        last_index = len(self.base) - len(search) + 1
        self.search = search
        start_inds = list(range(0, last_index))
        
        p = mp.Pool(mp.cpu_count())
        p.map_async(self.parallel_sub_helper, start_inds)  
        p.close()
        p.join()
        return self.count.value
        
    def parallel_sub_helper(self, i):
        sub_end = i + len(self.search)
        if self.base[i:sub_end] == self.search:
            self.count.value += 1

def main():

    file = open('test.txt', mode = 'r')
    base = file.read() 

    s = Substring(base)

    start = timeit.default_timer()
    p_index = s.parallel_sub("hysbsuna")
    end = timeit.default_timer()
    print("Parallel Substring count:", p_index)
    print("Parallel time:", end - start)

    start = timeit.default_timer()
    s_index = s.sequential_sub("hysbsuna")
    end = timeit.default_timer()
    print("Sequential Substring count:", s_index)
    print("Sequential time:", end - start)

    
if __name__ == "__main__":
    main()