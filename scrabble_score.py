def score(word):
    scores = {
        "score1" : ("AEIOULNRST", 1),
        "score2" : ("DG", 2),
        "score3" : ("BCMP", 3),
        "score4" : ("FHVWY", 4),
        "score5" : ("K", 5),
        "score8" : ("JX", 8),
        "score10" : ("QZ", 10),
    }
    
    totalscore = 0

    for letter in word:
        if letter.upper() in scores["score1"][0]:
            totalscore += scores["score1"][1]
        if letter.upper() in scores["score2"][0]:
            totalscore += scores["score2"][1]
        if letter.upper() in scores["score3"][0]:
            totalscore += scores["score3"][1]
        if letter.upper() in scores["score4"][0]:
            totalscore += scores["score4"][1]
        if letter.upper() in scores["score5"][0]:
            totalscore += scores["score5"][1]
        if letter.upper() in scores["score8"][0]:
            totalscore += scores["score8"][1]
        if letter.upper() in scores["score10"][0]:
            totalscore += scores["score10"][1]
    
    return totalscore

if __name__ == "__main__":
    print(score("cabbage"))