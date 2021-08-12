if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
#finding the percentage in python - Hacker Rank Solution 
output = list(student_marks[query_name])    
per = sum(output)/len(output);
print("%.2f" % per);
