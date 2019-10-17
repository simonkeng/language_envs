import subprocess, os
import click

@click.command()
@click.option('--input_list_file', '-i', help='.txt file, new line separated list')
@click.option('--top_level_directory', '-t', help='location to begin search')
def cli(input_list_file, top_level_directory):
    '''
        Recursively search through filesystem, 
        greping files for keywords in the input file.
    '''
    
    with open(input_list_file, 'r') as fp:
        contents = fp.read()

    items = contents.split('\n')
    search_items = list(filter(None, items))

    for i in search_items:

        with open('results.txt', 'a') as f:

            print(f'Searching for {i}')
            subprocess.call(
                ['grep', '-rnw', top_level_directory, '-e', i],
                stdout=f
            )
