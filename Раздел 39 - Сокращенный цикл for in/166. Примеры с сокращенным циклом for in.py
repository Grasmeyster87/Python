# my_set = {1, 10, 15}
# new_set = set()
# for val in my_set:
#     new_set.add(val * val)

# new_set = {val * val for val in my_set} # сокращенный цикл for in

# print(new_set)

# print(my_set)

my_scores = {
    'a': 10,
    'b': 7,
    'm': 14,
}

# scores = {}

# for key, value in my_scores.items(): 
#     scores[key] = value * 10

scores = {k: v * 10 for k, v in my_scores.items()} # Dictionary Comprehension 
print(scores)
print(my_scores)