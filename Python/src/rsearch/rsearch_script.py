import subprocess, os, sys
import click

@click.command()
@click.option('--input_list_file', '-i', help='.txt file, new line separated list')
@click.option('--top_level_directory', '-t', help='location to begin search')
def cli(input_list_file, top_level_directory):
    '''
        Recursively search through filesystem,
        greping files for keywords in the input file.
    '''

    if (sys.version_info < (3, 0)):
        print('Please use a Python version 3.6 or greater.')
        sys.exit()

    try: 
        sys.argv[1]
    except IndexError as err:
        print('No arguments provided\n')
        print('Try: rsr --help\n')
        sys.exit()


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
