import re




class Solver():

    def __init__(self):
        self.mask = "0"*36
        self.data = {}
        

    def get_mem_index(self, command):
        index_regex = re.compile("mem\[(\d+)\]")
        match = index_regex.match(command)
        index = int(match.groups()[0])
        return index

    def set_data(self, index, value):
        self.data[index] = self.apply_mask(value)

    def apply_mask(self, value):
        bin_string = bin(value)[2:]
        bin_list = list(bin_string.zfill(36))
        mask_list = list(self.mask)
        for i in range(0,len(mask_list)):
            if mask_list[i] != "X":
                bin_list[i] = mask_list[i]
        result = "".join(bin_list)
        result = int(result,2)
        
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

    print(solver.get_result())

    
