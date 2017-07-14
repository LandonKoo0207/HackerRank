# Solution for Climbing The Leaderboard
# Problem description at https://www.hackerrank.com/challenges/climbing-the-leaderboard

n = int(input().strip())
scores = map(int, input().strip().split(' '))
m = int(input().strip())
alice = map(int, input().strip().split(' '))

# Remove the duplicates in the scores
# and arrange in ascending order
unique_scores = sorted(set(scores))

# Search through the existing scores to get the rank
# Search always starts from previously found position within the scores
#     ex) scores: [60, 60, 50, 40, 30, 20, 10]
#         scores(unique): [10, 20, 30, 40, 50, 60]
#         alice:  [1, 25, 40, 70]
#         if currently working out the rank for 40, then you only have to
#         search from the position of 30, as the previous score was 25.
#         You don't really have to search from position 0 to all the way to the end
prev_idx = 0
for score in alice:
    # if the alice's current score is the highest,
    # print 1 as in that case the rank will be 1
    if score >= unique_scores[-1]:
        print(1)
    # if any score is larger than alice's, the rank is
    #   the rank of that score + 1
    # or, if any score is the same as alice's the rank is
    #   the rank of that score on the leaderboard
    else:
        for i in range(prev_idx, len(unique_scores)):
            if score < unique_scores[i]:
                print(len(unique_scores)-i+1)
                prev_idx = i
                break
            elif score == unique_scores[i]:
                print(len(unique_scores)-i)
                prev_idx = i+1
                break
