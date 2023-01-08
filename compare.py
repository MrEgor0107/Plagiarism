import argparse
parser = argparse.ArgumentParser()
parser.add_argument('input', type=str)
parser.add_argument('scores',type=str)
args = parser.parse_args()

def lev_distance(i, j, s1, s2, matrix):
    if i == 0 and j == 0:
        return 0
    elif j == 0 and i > 0:
        return i
    elif i == 0 and j > 0:
        return j
    else:
        m = 0 if s1[i-1] == s2[j-1] else 1
        return min(matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1]+m)

def calculate_levenshtein_distance(s1, s2):
    n = len(s1)
    m = len(s2)
    matrix = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            matrix[i][j] = lev_distance(i, j, s1, s2, matrix)
    return matrix[n][m]

file = open(args.input, encoding='utf-8') 
s = file.readlines()
for i in range(len(s)):
    st = s[i]
    probel = st.find(' ')
    f1 = st[:probel]
    f2 = st[probel + 1:len(st[i]) - 2]
    file1 = open(f1, encoding='utf-8')
    file2 = open(f2, encoding='utf-8')
    s1 = file1.read()
    s2 = file2.read()
    file1.close()
    file2.close()
    result = 1 - calculate_levenshtein_distance(s1, s2) / len(s2)
    scores_file = open(args.scores, 'a', encoding='utf-8') 
    scores_file.write(str(result))
    scores_file.write('\n')
    scores_file.close()
file.close()
