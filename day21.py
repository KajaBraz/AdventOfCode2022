from read_data import get_data_02_str_list


def execute_job(jobs_dict, monkey):
    if len(jobs_dict[monkey]) == 1:
        return int(jobs_dict[monkey][0])
    m1, m2 = jobs_dict[monkey][0], jobs_dict[monkey][2]
    if jobs_dict[monkey][1] == '+':
        return execute_job(jobs_dict, m1) + execute_job(jobs_dict, m2)
    elif jobs_dict[monkey][1] == '-':
        return execute_job(jobs_dict, m1) - execute_job(jobs_dict, m2)
    elif jobs_dict[monkey][1] == '*':
        return execute_job(jobs_dict, m1) * execute_job(jobs_dict, m2)
    elif jobs_dict[monkey][1] == '/':
        return execute_job(jobs_dict, m1) // execute_job(jobs_dict, m2)


if __name__ == '__main__':
    input_data = [row.replace(':', '') for row in get_data_02_str_list('input21.txt')]
    input_data_dict = {row[0]: row[1:] for row in [job.split() for job in input_data]}
    print(input_data_dict)

    part_1 = execute_job(input_data_dict, 'root')
    print(part_1)
