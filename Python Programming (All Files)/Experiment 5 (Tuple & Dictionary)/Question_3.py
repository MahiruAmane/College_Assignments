# Write a Python Program To Input a List of Scores and Display the Score Of The Runner Up.

scores = []

n = int(input("Please Enter The Number Of Scores : "))
for i in range(n):
    score = float(input("Please Enter The {} Score : ".format(i + 1)))
    scores.append(score)

print("The Given Scores Are : ", scores)
unique_scores = set(scores)

if len(unique_scores) < 2:
    print("There Is No Runner Up Scores As All Scores Are The Same")
else:
    runner_up = sorted(unique_scores)[-2]
    print("The Runner Up Score Is : {:.2f}".format(runner_up))