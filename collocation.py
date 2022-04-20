import multiprocessing as mp
import timeit    

class Collocation:

    def __init__(self):
        self.dict = {}
        self.word = ""
        self.prev_word = ""
        self.contents = []

        self.dict_pairs = mp.Manager().dict()
        self.max = mp.Manager().Value('i', -1)
        self.max_pair = mp.Manager().Value('c', "")

    def seq_collocate(self, num_pairs):
        with open('test.txt', mode='r') as f:
            contents = f.read().split()

        self.prev_word = contents[0]
        for i in range(1, len(contents)):
            self.word = contents[i]
            if self.word in self.dict.keys():
                if self.prev_word in self.dict[self.word].keys():
                    self.dict[self.word][self.prev_word] = self.dict[self.word][self.prev_word] + 1
                else:
                    self.dict[self.word][self.prev_word] = 1
            else:
                self.dict[self.word] = {}
                self.dict[self.word][self.prev_word] = 1
            self.prev_word = self.word

        result = []
        for x in range(num_pairs):
            temp = {}
            max = 0
            max_key1 = ""
            max_key2 = ""
            for i in self.dict:
                for j in self.dict[i]:
                    if max < self.dict[i][j]:
                        max = self.dict[i][j]
                        max_key1 = i
                        max_key2 = j
            temp[max_key2] = max_key1
            result.append(temp)
            self.dict[max_key1][max_key2] = -1
        
        return result

    def par_collocation(self, num_pairs):
        with open('test.txt', mode='r') as f:
            self.contents = f.read().split()
        
        start_inds = list(range(1, len(self.contents)))
        p = mp.Pool(mp.cpu_count())
        pair_list = p.map(self.helper1, start_inds)
        p.map(self.helper2, pair_list)
        
        most_common = []

        for i in range(num_pairs):
             p.map(self.helper3, self.dict_pairs)
             most_common.append(self.max_pair.value)
             self.max.value = -1
             self.dict_pairs[self.max_pair.value] = -1

        #p.close()
        #p.join()
        
        
        return most_common
        
    def helper1(self, index):
        temp = {}
        temp[self.contents[index]] = self.contents[index-1]
        return temp

    def helper2(self, dpair):
        big_key = list(dpair.keys())[0]
        small_key = list(dpair.values())[0]
        new_key = big_key + "," + small_key

        if new_key in self.dict_pairs.keys():
            self.dict_pairs[new_key] = self.dict_pairs[new_key] + 1
        else:
            self.dict_pairs[new_key] = 1

    def helper3(self, pair):
        if self.dict_pairs[pair] > self.max.value:
            self.max.value = self.dict_pairs[pair]
            self.max_pair.value = pair


def main():
    c = Collocation()

    start = timeit.default_timer()
    seq_collocation = c.seq_collocate(5)
    end = timeit.default_timer()
    print(seq_collocation)
    print("seq:", end - start)

    start = timeit.default_timer()
    par_collocation = c.par_collocation(5)
    end = timeit.default_timer()
    print(par_collocation)
    print("par:", end - start)

if __name__ == "__main__":
    main()
