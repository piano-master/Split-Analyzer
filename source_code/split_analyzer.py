import math

class Split:
    def __init__(self,name,pb,gold,number):
        self.name = name
        self.pb = pb
        self.gold = gold
        self.number = number
        self.timesave = pb-gold
    
    def __lt__(self,other):
        # I'm using gt symbol so that most timesave is at beginning of list
        return self.timesave > other.timesave
        

def min_to_ms(time_min):
    # parsing string to get min,sec,ms    
    time_ms = 0
    unit = 0
    min_num = 0
    sec_num = 0
    ms_num = 0
    min_str = ""
    sec_str = ""
    cs_str = ""
    for i in range(0, len(time_min)):
        if time_min[i] == ':':
            unit = 1
            continue
        elif time_min[i] == '.':
            unit = 2
            continue
        
        if unit == 0:
            min_str += time_min[i]
        elif unit == 1:
            sec_str += time_min[i]
        elif unit == 2:
            cs_str += time_min[i]
            
    min_num = int(min_str)
    sec_num = int(sec_str)
    ms_num = int(cs_str)*10
    
    time_ms = min_num*60000+sec_num*1000+ms_num
    
    return time_ms

def ms_to_min(time_ms):    
    min_num = math.floor(time_ms / 60000)
    time_ms -= min_num*60000
    sec_num = math.floor(time_ms / 1000)
    time_ms -= sec_num*1000
    cs_num = int(time_ms / 10)
    
    min_str = str(min_num) + ':'
    if min_str == "0:":
        min_str = ""
    
    sec_str = ""
    if (min_str != "") & (sec_num < 10):
        sec_str = "0"
    sec_str += str(sec_num)
    
    cs_str = ""
    if cs_num < 10:
        cs_str = "0"
    cs_str += str(cs_num)
    
    time_min = min_str + sec_str + '.' + cs_str
    return time_min

# read splits.txt file
def read_splits(file):
    # each line is a split
    # save each split as an object containing name, pb, gold, number
    # convert times to ms
    number = 1
    split_table = []
    for line in file:
        tab = 0
        pb = 0
        gold = 0
        name = ""
        pb_str = ""
        gold_str = ""
        for i in range(0, len(line)):
            if line[i] == '\t':
                tab += 1
                continue
            if tab == 0:
                name += line[i]
            elif tab == 2:
                pb_str += line[i]
            elif tab == 3:
                gold_str += line[i]
        pb = min_to_ms(pb_str)
        gold = min_to_ms(gold_str)
        split = Split(name,pb,gold,number)
        split_table.append(split)
        # print("Processed Split " + str(number))
        number += 1
    return split_table

# sort splits based on timesave
def sort_splits(split_table):
    split_table = sorted(split_table)
    return split_table

# output splits to output.txt in order of most to least timesave
# just show name and timesave for each split
def print_file(split_table,filename):
    file_out = open(filename, 'w')
    for split in split_table:
        timesave_str = ms_to_min(split.timesave)
        file_out.write('{:>4s}{:<30s}{:>10s}'.format(str(split.number) + '. ',split.name,timesave_str))
        file_out.write('\n')
    return


if __name__ == "__main__":
    print("Filename:  ")
    filename = input()
    split_file = open(filename, 'r')
    
    splits = read_splits(split_file)
    splits_sorted = sort_splits(splits)
    
    split_file.close()
    
    print_file(splits,"splits_output.txt")
    print_file(splits_sorted,"splits_sorted_output.txt")
    print("Finished processing splits!")