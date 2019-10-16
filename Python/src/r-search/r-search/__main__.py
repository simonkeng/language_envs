import subprocess, os
import argparse

parser = argparse.ArgumentParser(
    description='''
        Recursively search through filesystem, 
        greping files for keywords in the input list file.
        '''
)
parser.add_argument(
    '--input_list_file', 
    '-i',
    help='Input .txt file with keywords, newline separated.'
)
parser.add_argument(
    '--top_level_directory', 
    '-t', 
    help='Top level directory to start at.'
)

def main(input_list_file, top_level_directory):
    '''
        Main for CLT
    '''
    
    with open(input_list_file, 'r') as fp:
        contents = fp.read()

    search_items = contents.split('\n')

    for i in search_items:

        with open('results.txt', 'a') as f:

            print(f'Searching for {i}')
            subprocess.call(
                ['grep', '-rnw', top_level_directory, '-e', i],
                stdout=f
            )

if __name__ == "__main__":

    args = parser.parse_args()

    main(args.input_list_file, args.top_level_directory)
