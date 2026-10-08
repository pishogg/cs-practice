def winner(names, scores):
    n = len(names)
    max_score = -10**10
    name_win = ''
    for i in range(n):
        if scores[i] > max_score:
            max_score = scores[i]
            name_win = names[i]
    return name_win

def average(scores):
    if len(scores) == 0: return 0.0
    return round(sum(scores)/len(scores), 2)

def ranking(names, scores):
    new_names = {}    
    n = len(names)
    for i in range(n):
        new_names[names[i]] = [scores[i]]
    new_names = dict(sorted(new_names.items(), key=lambda item: item[1], reverse=True))
    return list(new_names.keys())
    
def above_average(names, scores):
    new_names = []    
    n = len(names)
    aver = average(scores)
    for i in range(n):
        if scores[i] > aver:
            new_names += [names[i]]
    return new_names
