# lambda function: different type of funciton which doesn't have a name and is only use to return values

#  they are exclusively use to operate on inputs and return outputs

# lambda keyword + parameters: + return value
# print((lambda x,y: x+y)(2,23)) <- not very common



def doubled(x):
    return x * 2

sequence = [2,4,6,8]

# res = [doubled(x) for x in sequence]
res = [(lambda a: a*3)(x) for x in sequence ]
res2 = list(map(lambda e: e*3, sequence))
print(res)
print(res2)