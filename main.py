from Samples import py1, py2, py3, py4
import random

if __name__ == "__main__":
    m = random.choice([py1, py2, py3, py4])
    s = m.madlib()
    print(s)