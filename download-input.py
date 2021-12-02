import sys
import os
import requests

if len(sys.argv) < 2:
    print('day number required in argument 1')
    exit(0)

day = sys.argv[1];

input = requests.get(
    'https://adventofcode.com/2021/day/{}/input'.format(day),
    cookies={'session': open('.secret').read()}
).text

if not os.path.exists('day-{}'.format(day)):
    os.mkdir('day-{}'.format(day))
open('day-{}/input.txt'.format(day), 'w+').write(input)