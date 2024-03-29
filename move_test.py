import os
with open("normal/test_set.txt", 'r') as f:
    files = f.readlines()
for line in files:
    filename = line.rstrip()
    os.rename("normal/" + filename, "normal/test-set/" + filename)