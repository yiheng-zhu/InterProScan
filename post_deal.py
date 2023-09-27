import os.path
import sys
from configure import run_interproscan_file, all_entry_list_file
def read_result_file(result_file):  # read result.file

    f = open(result_file, "r")
    text = f.read()
    f.close()

    result_dict = dict()

    for line in text.splitlines():
        values = line.split("	")
        name = values[0]
        entry = values[11]

        if(name not in result_dict):
            result_dict[name] = []

        result_dict[name].append(entry)

    for name in result_dict.keys():

        temp_list = sorted(list(set(result_dict[name])))
        if("-" in temp_list):
            temp_list.remove("-")

        result_dict[name] = temp_list

    return result_dict

def read_all_entry_list(entry_list_file):  # read all entry list

    f = open(entry_list_file, "r")
    text = f.read()
    f.close()

    all_entry_list = []
    line_set = text.splitlines()
    line_set = line_set[1:]

    for line in line_set:
        all_entry_list.append(line.split("	")[0])

    return all_entry_list

def create_entry_index(current_entry_list, all_entry_list): # create entry index

    entry_index = []
    for entry in current_entry_list:
        entry_index.append(all_entry_list.index(entry))

    return sorted(entry_index)

def write_file(array_list, save_file):

    f = open(save_file, "w")
    for array in array_list:
        f.write(str(array) + "\n")
    f.close()

def single_process(result_file, output_dir1, output_dir2):

    if(os.path.exists(output_dir1)==False):
        os.makedirs(output_dir1)

    if (os.path.exists(output_dir2) == False):
        os.makedirs(output_dir2)

    result_dict = read_result_file(result_file)
    all_entry_list = read_all_entry_list(all_entry_list_file)

    for name in result_dict.keys():

        entry_name_file = os.path.join(output_dir1, name)
        entry_index_file = os.path.join(output_dir2, name)

        entry_name_list = result_dict[name]
        entry_index_list = create_entry_index(entry_name_list, all_entry_list)

        write_file(entry_name_list, entry_name_file)
        write_file(entry_index_list, entry_index_file)


if __name__ == '__main__':

    single_process(sys.argv[1], sys.argv[2], sys.argv[3])








