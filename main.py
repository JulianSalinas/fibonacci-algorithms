# -----------------------------------------------------------------------------

from timeit import *
CALCULATED_VALUES = [0, 1, 1, 2, 3, 5, 8, 13]
CALCULATED_SPACES = len(CALCULATED_VALUES)


# -----------------------------------------------------------------------------

# Init the array with the first values of the serie
# We have 8 calculated values the rest of spaces are -1
def init(n, calculated):
    while len(calculated) <= n:
        calculated.append(-1)
    return calculated


# -----------------------------------------------------------------------------

# Classic dynamic_fib
def classic_fib(n):
    return n if n <= 1 else classic_fib(n-1) + classic_fib(n-2)


# -----------------------------------------------------------------------------

# Dynamic programming versión (fastest)
def dynamic_fib(n):

    # We have it without any calculus
    if 0 <= n < CALCULATED_SPACES:
        return CALCULATED_VALUES[n]

    values = init(n, CALCULATED_VALUES[:])

    if values[n - 1] == -1:
        values[n - 1] = dynamic_fib(n - 1)

    if values[n - 2] == -1:
        values[n - 2] = dynamic_fib(n - 2)

    values[n] = values[n - 2] + values[n - 1]
    return values[n]


# -----------------------------------------------------------------------------

# Classic dynamic_fib
def iterative_fib(n):

    values = CALCULATED_VALUES[:]

    # We have it without any calculus
    if 0 <= n < CALCULATED_SPACES:
        return CALCULATED_VALUES[n]

    steps = n - CALCULATED_SPACES

    while steps >= 0:
        index = CALCULATED_SPACES - 1
        values.append(values[index] + values[index - 1])
        values.pop(0)
        steps -= 1

    return values[CALCULATED_SPACES - 1]


# -----------------------------------------------------------------------------

# List of available versions
ALGORITHMS = {
    "classic": classic_fib,
    "dynamic": dynamic_fib,
    "iterative": iterative_fib
}


# -----------------------------------------------------------------------------
# Wrapper para todos los algoritmos
@timeit
def fib(n, variant):
    if ALGORITHMS.__contains__(variant):
        algorithm = ALGORITHMS[variant]
        return algorithm(n)
    raise Exception("Not available variant")


# -----------------------------------------------------------------------------

# Time: 0.418885469436645508
print(fib(30, "classic"))

# Time: 0.114739418029785156
print(fib(30, "dynamic"))

# Time: 0.000000000000000000
# Iterative version is the fastest and fixed memory consumer
print(fib(300, "iterative"))
print(222232244629420445529739893461909967206666939096499764990979600)

# -----------------------------------------------------------------------------
