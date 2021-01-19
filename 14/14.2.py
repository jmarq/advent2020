import re




class Solver():

    def __init__(self):
        self.mask = "0"*36
        self.data = {}
        

    def get_mem_index(self, command):
        index_regex = re.compile(r"mem\[(\d+)\]")
        match = index_regex.match(command)
        index = int(match.groups()[0])
        return index

    def set_data(self, index, value):
        indexes = self.get_masked_indexes(index)
        for index in indexes:
            self.data[index] = int(value)
    
    def get_masked_indexes(self, index):
        masked_index = self.apply_mask(index)
        print("masked index:")
        print(masked_index)
        # masked index is something like "000111001001XXX00XXX"
        indexes = self.get_floating_bit_indexes(masked_index)
        return indexes

    def get_floating_bit_indexes(self, index):
        if "X" not in index:
            return [index]
        
        first_floating_index = index.index("X")

        prefix = index[0:first_floating_index]
        prefixes = [prefix+"1", prefix+"0"]
        if first_floating_index+1 < len(index):
            indexes_for_remainder = self.get_floating_bit_indexes(index[first_floating_index+1:])
        else:
            indexes_for_remainder = [""]
        
        results = []
        for idx in indexes_for_remainder:
            results.append(prefixes[0] + idx)
            results.append(prefixes[1] + idx)
        return results


    def apply_mask(self, value):
        bin_string = bin(value)[2:]
        bin_list = list(bin_string.zfill(36))
        mask_list = list(self.mask)
        for i in range(0,len(mask_list)):
            if mask_list[i] != "0":
                bin_list[i] = mask_list[i]
            # else:
            #     bin_list[i] = "X"
        result = "".join(bin_list)
        return result

    def process_line(self, line):
        command,value = line.split(" = ")
        if command == "mask":
            self.mask = value
        elif "mem" in command:
            index = self.get_mem_index(command)
            self.set_data(index,int(value))

    def get_result(self):
        values = self.data.values()
        return sum(values)


if __name__ == "__main__":
    infile = open("input.txt", 'r')
    lines = infile.read().strip().split("\n")

    solver = Solver()
    for line in lines:
        solver.process_line(line)

    print(solver.data)
    print(solver.get_result())

    
