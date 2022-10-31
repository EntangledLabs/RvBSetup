import time, os
from mailbee import mail_bees

cwd = os.getcwd()

injects = os.listdir(path="{}/injects/".format(cwd))
injects.sort()

with open('{}/schedule.txt'.format(cwd)) as f:
    times = f.readlines()
    for i in range(0,len(times)):
        times[i] = int(times[i])*60

for i in range(0,len(injects)):
    injects[i] = (injects[i], times[i])

print(injects)

mark = time.time()

while len(injects) > 0:
    print("Mark inject")
    try:
        if (time.time() - mark) > injects[0][1]:
            mail_bees('{}/injects/{}'.format(cwd, injects[0][0]))
            injects.pop(0)
    except:
        break