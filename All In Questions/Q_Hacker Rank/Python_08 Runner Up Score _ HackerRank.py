'''
if __name__ == '__main__':
    # n = int(input())  # number of scores
    arr = list(map(int, input().split()))  # convert input to a list of integers

    # Remove duplicates by converting to a set
    unique_scores = set(arr)

    # Find the highest score
    max_score = max(unique_scores)

    # Remove the highest score
    unique_scores.remove(max_score)

    # Runner-up is now the maximum of the remaining scores
    runner_up = max(unique_scores)

    print(runner_up)

'''
# Task/Question
# Given the participants' Scoresheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up(means second highest number).

# Input Format
# The first line contains n . The second line contains an array A[] of n  integers each separated by a space.

# Constraints
# 2 <= n <= 10
# -100 <= A[i] <= 100

# Output Format
# Print the runner-up score

# Sample Input
# 5
# 2 3 6 6 5

# Sample Output
# 5

# Explanation
# Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5.
# Hence, we print 5 as the runner-up score.


