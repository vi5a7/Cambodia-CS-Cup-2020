def workout(Times):
    for i in range(T):
        if(Times[i][0]==16):
            if(Times[i][1]>=2):
                Times[i][1]%=2
                if (Times[i][1]==0):
                    if (Times[i][2] >= 15):
                        print("She is working out")
                    else:
                        print("She is resting")
                elif(Times[i][1]==1):
                    if (Times[i][2] >= 15):
                        print("She is resting")
                    else:
                        print("She is working out")
            else:
                if(Times[i][2]>=15):
                    if(Times[i][1]==0):
                        print("She is working out")
                    else:
                        print("She is resting")
                else:
                    print("She is working out")
        else:
            print("No information")

if __name__ == '__main__':    
    T = int(input())
    Times = []
    for i in range(T):
        time = list(map(int, input().split()))
        Times.append(time)

    workout(Times)