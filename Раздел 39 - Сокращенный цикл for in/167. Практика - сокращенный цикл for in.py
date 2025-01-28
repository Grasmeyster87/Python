my_scores = {
    'a': 10,
    'b': 7,
    'm': 14,
}
my_scores_list = [10, 7, 4]

# scores = {}

# for key, value in my_scores.items():
#     scores[key] = value * 10

# scores = {k: v * 10 for k, v in my_scores.items()} # Dictionary Comprehension
# scores = {v * 10 for k, v in my_scores.items()}
scores = [v * 10 for k, v in my_scores.items()]
scores_list = {k: v * 2 for k, v in enumerate(my_scores_list)}

print('scores: ', scores)
print('type(scores): ', type(scores))
print('my_scores: ', my_scores)

print('scores_list: ', scores_list)
