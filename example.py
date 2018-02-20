from NumProb.random import Random as randy

# functional instantiation with assigned dict
_randy = randy({2: 0.50, 3: 0.20, 4: 0.05, 5: 0.05, 0: 0.05, 11: 0.05, 31: 0.05, 99: 0.05})

# how a coder might see the result
_randy.gen()

# how you would replay values
amount = 1
#amount = int(input("Amount of past values to show?: "))

for each in _randy.play()[0:amount]:
    print(each.replace("\n", ""))