"""
Print a block of random characters to STDOUT, similar to the output from
ssh-keygen (when generating public/private key pairs). It's sort of a text-based
generative art, thing. Could use it to create a hacker background image
for your stackoverflow profile ;)
"""
import argparse
import string
import numpy as np

parser = argparse.ArgumentParser(
    prog='block_generator',
    description='Generate a block of random ascii characters.')
parser.add_argument('--to-file', action='store_true', help='Create file.')
parser.add_argument('--format',
                    action='store_true',
                    help='Print formatted version.')
parser.add_argument('--flow',
                    action='store_true',
                    help='Print sequence to screen.')


def generate_fname():
    name = list()
    ext = '.txt'
    for i in range(3):
        name.append(
            np.random.choice(list(string.ascii_uppercase + string.digits)))
    fname = str(''.join(name)) + ext
    return fname


def generate_rand_string():
    selectable_vals = (string.ascii_letters + string.digits +
                       string.punctuation)
    rand_string = list()
    for i in range(50):
        rand_string.append(str(np.random.choice(list(selectable_vals))))
    return '\t' + str(''.join(rand_string)) + '\n'


def inject_random_text_block():
    block = ''

    for i in range(30):
        block = block + generate_rand_string()

    return block


def generate_uniform_chunk():
    vals = string.ascii_uppercase + string.digits
    rand_string = list()
    for i in range(20):
        rand_string.append(str(np.random.choice(list(vals))))
    return str(''.join(rand_string))


def inject_formatted_block():
    main_chunk = generate_uniform_chunk()
    block = f'''
        {main_chunk}   {main_chunk}
        {main_chunk}   {main_chunk}

        {generate_uniform_chunk()}XXX{generate_uniform_chunk()} 
        {generate_uniform_chunk()}XXX{generate_uniform_chunk()} 
        {generate_uniform_chunk()}XXX{generate_uniform_chunk()}  

        {main_chunk}   {main_chunk}
        {main_chunk}   {main_chunk}
        {main_chunk}   {main_chunk}
    '''
    return block


def spacer():
    return '\n\n'


if __name__ == "__main__":

    args = parser.parse_args()

    if args.to_file:
        with open(generate_fname(), 'w') as f:
            f.write(spacer())
            f.write(inject_random_text_block())
            f.write(spacer())

    if args.format:
        print(spacer())
        print(inject_formatted_block())
        print(inject_formatted_block())
        print(spacer())

    if args.flow:
        for i in range(1, 100):
            print(inject_random_text_block)
            print(spacer())

    else:
        print(spacer())
        print(inject_random_text_block())
        print(spacer())
