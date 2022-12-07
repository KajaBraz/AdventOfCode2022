from read_data import get_data_02_str_list


def sum_under_100000_dirs(dir_sizes):
    return sum(v for k, v in dir_sizes.items() if v <= 100000)


def get_min_remove_dir_size(dir_sizes, disk_space, min_disk_space):
    free_space = disk_space - dir_sizes['/']
    remove_dir_size = [k for k, v in sorted(dir_sizes.items(), reverse=True, key=lambda x: x[1])
                       if free_space + v >= min_disk_space][-1]
    return sizes[remove_dir_size]


def find_dir(data):
    filesystem = {}
    cur_dir = []
    i = 0
    while i < len(data):
        if '$ cd ..' == data[i]:
            cur_dir = cur_dir[:-1]
            i += 1
        elif '$ cd' == data[i][:4]:
            directoty = data[i].split()[-1]
            if '-'.join(cur_dir) not in filesystem:
                filesystem['-'.join(cur_dir)] = []
            cur_dir += [directoty]
            i += 1
        if '$ ls' == data[i][:4]:
            i += 1
            while i < len(data) and '$' not in data[i]:
                if 'dir' in data[i][:3]:
                    filesystem['-'.join(cur_dir + [data[i].split()[-1]])] = []
                    if '-'.join(cur_dir) in filesystem:
                        filesystem['-'.join(cur_dir)].append('-'.join(cur_dir + [data[i].split()[-1]]))
                    else:
                        filesystem['-'.join(cur_dir)] = ['-'.join(cur_dir + [data[i].split()[-1]])]
                else:
                    if '-'.join(cur_dir) in filesystem:
                        filesystem['-'.join(cur_dir)].append(data[i])
                    else:
                        filesystem['-'.join(cur_dir)] = [data[i]]
                i += 1
    return filesystem


def get_dir_size(directory, dirs):
    inner_dirs = [item for item in dirs[directory] if len(item.split()) == 1]
    files_size = sum([int(item.split()[0]) for item in dirs[directory] if len(item.split()) == 2])
    inner_dir_size = 0
    for inner in inner_dirs:
        inner_dir_size += get_dir_size(inner, dirs)
    return inner_dir_size + files_size


def get_sizes(dirs):
    dir_sizes = {}
    for k, v in dirs.items():
        dir_sizes[k] = get_dir_size(k, dirs)
    return dir_sizes


if __name__ == '__main__':
    input_data = get_data_02_str_list('input07.txt')
    files_structure = find_dir(input_data)
    sizes = get_sizes(files_structure)

    # part 1
    r1 = sum_under_100000_dirs(sizes)
    print(r1)

    # part 2
    r2 = get_min_remove_dir_size(sizes, 70000000, 30000000)
    print(r2)
