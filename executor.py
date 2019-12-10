import argparse

import program_modes as p_m
import functions as func

parser = argparse.ArgumentParser(prog='linearcode', usage='%(prog)s mode param',
                                 description='Linear error-correcting code.')

subparsers = parser.add_subparsers(title='mode', description='valid modes', help='additional help')

parser_gencode = subparsers.add_parser('gencode', help='generate code and decode vector')
parser_gencode.add_argument('r', type=int, help='number of check bits')
parser_gencode.add_argument('n', type=int, help='length of code')
parser_gencode.add_argument('t', type=int, help='number of correct errors')
parser_gencode.add_argument('--out-file', dest='out', type=str, default='code_information.pickle',
                            help='file to write information for coder/decoder (default: code_information.pickle)')
parser_gencode.set_defaults(func=p_m.gencode)

parser_coder = subparsers.add_parser('coder', help='code message in blocks length k and add error')
parser_coder.add_argument('inputfile', type=str, help='information file for coder in pickle format')
parser_coder.add_argument('m', type=str, help='message')
parser_coder.add_argument('-e', dest='e', type=str, help='error', default=None)
parser_coder.set_defaults(func=p_m.coder)

parser_decoder = subparsers.add_parser('decoder', help='decode message and subtract error vector')
parser_decoder.add_argument('inputfile', type=str, help='file whith information for decoder in pickle format')
parser_decoder.add_argument('y', type=str, help='message with error')
parser_decoder.set_defaults(func=p_m.decoder)


@func.timeout(seconds=20)
def run(parser_):
    args = parser_.parse_args()
    args.func(args)

if __name__ == '__main__':
    exceptions = (ValueError, TimeoutError)
    try:
        run(parser)
    except exceptions as err:
        print("\n There is an error:\n")
        print(err, '\n')
