def question1():
    d = sys.stdin.read()
    sys.stdout.write(d)
    sys.stderr.write("No error")

def question2():
    if __name__ == "__main__":
    d = sys.stdin.read()
    sys.stdout.write(d)
    a = 0

    for i in str(d):
        try:
            if i == "\n":
                break
            a += int(i)
        except:
            sys.stderr.write("Addition Error")
            break
    print("Sum = ", a)
