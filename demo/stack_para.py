#! /usr/bin/env python

def judge(raws):
    stack = []
    match = {")": "(", "]": "[", "}": "{"}
    for s in raw_string:
        if s in ("(", "[", "{"):
            stack.append(s)
        elif s in (")", "]", "}"):
            try:
                if stack[-1] == match[s]:
                    stack.pop()
                else:
                    print("not match")
                    return
            except IndexError:
                print("not match")
                return
    print("match")

if __name__ == "__main__":
    raw_string = input("input your string:\n")
    judge(raw_string)
