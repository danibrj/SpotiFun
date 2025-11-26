def xxx():
    x = 0
    for i in range(3):
        for j in range(5):
            if j != 4:
                x +=1
            else:
                print("yyy")
                return

xxx()