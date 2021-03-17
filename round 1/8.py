def find_ranking(scores, myScore):
    ranking, highScore, count = {}, 0, 1
    scores.sort(reverse=True)
    highScore = max(scores)
    ranking[highScore] = 1

    for i in range(1, len(scores)):
        count += 1
        if(scores[i] != scores[i-1]):
            ranking[scores[i]] = count

    return ranking.get(myScore)


if __name__ == '__main__':
    N = int(input())
    myScore = int(input())
    scores = []

    for i in range(N):
        score = int(input())
        scores.append(score)

    print(find_ranking(scores, myScore))
