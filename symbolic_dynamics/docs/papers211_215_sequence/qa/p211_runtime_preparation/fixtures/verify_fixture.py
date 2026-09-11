"""Pure runtime fixture. No mathematical map, theorem or P211 implementation."""
import itertools
import json
import math
import sys


def main():
    if len(sys.argv) != 3 or sys.argv[1] != '--parameters':
        raise RuntimeError('fixture requires explicit parameters')
    with open(sys.argv[2], encoding='utf-8') as stream:
        parameters = json.load(stream)
    if parameters != {'fixture_only': True, 'value': 17}:
        raise RuntimeError('wrong pure fixture parameters')
    print(json.dumps({'fixture_only': True, 'value': parameters['value']},
                     sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
