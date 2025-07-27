# main.py

from visualizer import RiloVisualizer
from interpreter import Interpreter

if __name__ == '__main__':
    vis = RiloVisualizer()
    interp = Interpreter('example/prueba.rlo', visualizer=vis)
    interp.run()
    vis.close()
