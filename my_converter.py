import subprocess
import os


def get_and_make_dirs():

    source = 'Source'
    result = 'Result'

    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_directory = os.path.join(current_dir, source)
    output_directory = os.path.join(current_dir, result)
    source_files = os.listdir(input_directory)
    os.mkdir(output_directory)

    return input_directory, output_directory, source_files


def convert_pictures(input_directory, output_directory, source_files):

    i = 0
    for file in source_files:
        result_files = os.path.join(input_directory, file)
        output_file = 'output_{}.jpg'.format(i)
        output_files = os.path.join(output_directory, output_file)

        cmd = 'convert {} -resize 200 {}'.format(result_files, output_files)

        subprocess.Popen(cmd)

        i += 1


def main():

    my_input_directory, my_output_directory, my_source_files = get_and_make_dirs()
    print('---Start program')
    convert_pictures(my_input_directory, my_output_directory, my_source_files)
    print('---End program')


main()
