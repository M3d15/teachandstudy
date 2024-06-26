

import sys
sys.path.insert(0, 'tes/generators/generator')

# import generator

from generators import generator



# print(Gen.random_name())

def some_func():
    g = generator.Gen()
    print(g.name)