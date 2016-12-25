from itertools import combinations
def longest_palindromic(text):
    ans = ""
    for i,j in combinations(range(len(text) + 1), 2):
        if text[i:j] == text[i:j:][::-1] and len(ans) < j - i:
            ans = text[i:j]
    return ans
