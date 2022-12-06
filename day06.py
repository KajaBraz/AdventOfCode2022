from read_data import get_data_00


def get_min_chrs_num_including_marker(data: str, marker_len: int) -> int:
    for i in range(len(data) - marker_len):
        if len(set(data[i:i + marker_len])) == marker_len:
            return i + marker_len
    return -1


if __name__ == '__main__':
    input_data = get_data_00('input06.txt')

    # part 1
    r1 = get_min_chrs_num_including_marker(input_data, 4)

    # part 2
    r2 = get_min_chrs_num_including_marker(input_data, 14)

    print(r1)
    print(r2)
