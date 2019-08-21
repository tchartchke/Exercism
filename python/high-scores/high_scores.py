def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)
    

def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]