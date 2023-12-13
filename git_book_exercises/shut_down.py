def shut_down(s):

    if s == "YES":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"


print(shut_down("yes"))
print(shut_down("no"))
print(shut_down("I don't know"))
