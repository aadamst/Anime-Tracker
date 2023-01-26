from time import sleep

count = 15
isCounting = True

while isCounting:
    print(count)
    count -= 1
    sleep(1)

    if count <= 0:
        isCounting = False

