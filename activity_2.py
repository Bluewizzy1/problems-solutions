

num = 5  # the number whose multiples we want to find
limit = 20  # the maximum value we want to consider

multiples = []
for i in range(1, limit+1):
    if i % num == 0:
        multiples.append(i)

print(multiples)






num = 3
limit = 100

num_multiples = [i for i in range(1, limit+1) if i % num == 0]

print(num_multiples)
