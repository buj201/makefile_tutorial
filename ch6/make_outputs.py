outputs = ['output/output{}.txt'.format(i) for i in range(1,4)]

i = 1
for output in outputs:
    with open(output, 'w') as f:
        f.write(str(i))
        i += 1
