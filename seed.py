# Adapted from reference converter
# https://esolangs.org/wiki/Seed#Running_programs

import random
import sys

if len(sys.argv) != 3:
  print(f"usage: {sys.argv[0]} <length> <seed>")
  exit(2)

length=int(sys.argv[1])
seed=sys.argv[2]

if len(seed) > sys.get_int_max_str_digits():
  sys.set_int_max_str_digits(len(seed))

random.seed(int(seed))
chars = "".join(map(chr, range(32, 127))) + '\n'
prog = "".join([chars[int(random.random() * 96)] for _ in range(length)])

print(prog, end="")
