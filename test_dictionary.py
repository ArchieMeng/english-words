import statprof
from dictionary import CrosswordSolver

from time import time
from random import choice, seed
import statprof
import pickle

try:
    with open("cross_word_solver.dmp", 'rb') as fp:
        solver = pickle.load(fp)
except:
    with open("words.txt") as fp:
        words = set(line[:-1].lower() for line in fp)
        solver = CrosswordSolver()
        solver.updateWords(words)

characters = [chr(_) for _ in range(ord('a'), ord('z') + 1)]

# test = [
#     ['m', 'e', 'r'],
#     ['a', 'p', 'i'],
#     ['y', 'e', 'p']
# ]
smin, smax = 400, 401
statprof.start()
for size in range(smin, smax):
    seed(time())
    test = [[choice(characters) for _ in range(size)] for _ in range(size)]

    for row in test:
        print(row)

    ans = solver.solve(test)
statprof.stop()
statprof.display()

with open("cross_word_solver.dmp", 'wb') as fp:
    pickle.dump(solver, fp)
