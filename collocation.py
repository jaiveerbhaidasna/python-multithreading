import multiprocessing as mp    

class Collocation:
    dict = {}
    word = ""
    prev_word = ""

    def seq_collocate(self, num_pairs):
        with open('test.txt', mode='r') as f:
            contents = f.read()

        for i in range(len(contents)):
            if contents[i] == " ":
                if self.word in self.dict.keys():
                    if self.prev_word in self.dict[self.word].keys():
                        self.dict[self.word][self.prev_word] += 1
                    else:
                        self.dict[self.word][self.prev_word] = 1
                else:
                    self.dict[self.word] = {}
                self.prev_word = self.word
                self.word = ""
            else:
                self.word = self.word + contents[i]

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
            contents = f.read()
        
        p = mp.Pool(mp.cpu_count())
        

    def helper(self):

                    



def main():
    c = Collocation()
    seq_collocation = c.seq_collocate(5)

if __name__ == "__main__":
    main()
