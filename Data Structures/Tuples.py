tup = ('C', ' Java', 'Python')
empty_tup = ()
single_tup = ('Park',)

print(tup)
print(empty_tup)
print(single_tup)

# Concatenation: Joining two tuples
a = (1,2,3)
b = (4,5,6)
concat_result = a + b
print('a+b:', concat_result)


# Repetition: Repeating a list multiple times
c = ('Hi!',)
repet_result = c * 3
print('c*3', repet_result)

# Membership: Check if a value exists in a tuple
d = a + b + c
print('d:', d)
print('\'Hi!\' in d:', 'Hi!' in d)
print('7 in d:', 7 in d)

# Iteration
example = ('C', 'Java', 'Python', 'C#', 'JavaScript')

print('Tuple example items:')
for language in example:
    print(language)
print('--')

# Indexing
print('Index 1:', example[1])
print('Last Value:', example[-1])

# Slicing
print('Backwards:', example[::-1])
print('Every other:', example[::2])
print('From 1 to end:', example[1:])
print('From 1 to 3:', example[1:3])

example = ('C', 'Java', 'Python', 'C#', 'JavaScript')

print('Length:', len(example))
print('Minimum value:', min(example))
print('Maximum value:', max(example))
print('--')

word = 'Hello'
array = [1,2,3,4]
array_array = [[1],[2,3],[4]]

print('String to Tuple:', tuple(word))
print('List to Tuple:', tuple(array))
print('2D array to Tuple:', tuple(array_array))
print('--')

array_array[0][0] = 'p'
print(array_array)

#tuple comprehension
even_tup = tuple(i for i in range(1,101) if i % 2 == 0)

print(even_tup)

# Examine the following code

# Packing
var_1 = 2
var_2 = 3
var_3 = 5

prime = var_1, var_2, var_3

print('Packed prime values:', prime)

# Unpacking and Repacking
fib = (0, 1, 1, 2, 3, 5, 8)

fib_0, fib_1, fib_n = fib[0], fib[1], fib[2:]
print('fib_0:', fib_0)
print('fib_1:', fib_1)
print('fib_n:', fib_n)