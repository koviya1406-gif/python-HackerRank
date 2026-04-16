from collections import Counter

if __name__ == '__main__':
    s = input()
    chars = Counter(sorted(s))
    for char, count in chars.most_common(3):
        print(f"{char} {count}")
