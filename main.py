import json
import os

input_dir = 'dicts'
target_dir = 'dist'
target_fmt = 'txt'


def handle_data_json_to_txt(input_file_path):
    file_base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    with open(input_file_path, 'r') as file:
        data = json.load(file)

    output_file_path = './' + target_dir + '/' + file_base_name + '.' + target_fmt
    with open(output_file_path, 'w') as output_file:
        for item in data:
            if 'name' in item:
                output_file.write(item['name'] + '\n')

    print("处理完成，结果已写入到", output_file_path)


def main():
    input_dir_path = './' + input_dir
    files = os.listdir(input_dir_path)
    for file_name in files:
        file_path = os.path.join(input_dir_path, file_name)
        handle_data_json_to_txt(file_path)


if __name__ == '__main__':
    main()
