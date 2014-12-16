train = open('train.feat', 'r')
train_new = open('train_new.feat', 'w')
for line in train:
    if line[0] == '0' :
        line = '-' + line
    if line[0] == '1' :
        line = '+' + line
    line = list(line)
    line[1] = '1'
    line = "".join(line)
    train_new.write(line)
train.close()
train_new.close()
    
