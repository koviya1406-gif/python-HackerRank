if __name__ == "__main__": 
    n, x = map(int, input().split())
    subjects_marks = []
    for _ in range(x):
        subjects_marks.append(map(float, input().split()))
    for student_scores in zip(*subjects_marks):
        avg = sum(student_scores) / x
        print(f"{avg:.1f}")
