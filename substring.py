import multiprocessing as mp

class Substring:
    base = ""
    search = ""

    def __init__(self, base):
        self.base = base
        self.ind = mp.Manager().Value('i', -1)
    
    def sequential_sub(self, search):
        last_index = len(self.base) - len(search) + 1
        for i in range(0, last_index):
            sub_end = i + len(search)
            curr_sub = self.base[i:sub_end]
            if curr_sub == search:
                return i
        return -1
    
    def parallel_sub(self, search):
        last_index = len(self.base) - len(search) + 1
        self.search = search
        start_inds = list(range(0, last_index))

        p = mp.Pool(mp.cpu_count())
        inds = p.map(self.parallel_sub_helper, start_inds)
        p.map(self.find_ind, inds)
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
    s = Substring("i am the test string test")
    s_index = s.sequential_sub("test")
    print("Sequential Substring index:", s_index)
    
    p_index = s.parallel_sub("test")
    print("Parallel Substring index:", p_index)

if __name__ == "__main__":
    main()