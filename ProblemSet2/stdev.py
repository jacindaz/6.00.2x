import math

def calcMean(L):
    sum = 0
    for l in L:
        sum += len(l)
    mean = float(sum) / len(L)
    return mean

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    else:
        mean = calcMean(L)
        print "\nMean inside function: ", mean
        variance = 0
        for list_item in L:
            print 'Variance: ', variance
            variance += (len(list_item) - mean) ** 2

        variance = variance / len(L)
        print "\nNew Variance: ", variance
        std_dev = math.sqrt(variance)
        return std_dev


# 1.8708
L = ['apples', 'oranges', 'kiwis', 'pineapples']

# 1.699673171197595
J = ['pqmt', 'hdvnids', 'rws']

# 4.498888751680798
K = ['rweneh', 'yqdkvodqycz', 'u', 'zmzoqnvyryix', 'efiahgfbxiusx']

# 2.2271057451320084
Y = ['bjfqgsxqtcompt', 'laijvqws', 'lzyzyakcssdo', 'cqdnalgrzwier', 'nbgpvnruggefid']


def print_things(list):
    print "Mean is ", calcMean(list)
    print "\nStandard Deviation: ", stdDevOfLengths(list)
    print "\n"

print_things(Y)
