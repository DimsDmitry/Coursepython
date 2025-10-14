sizes = '11M 14M 13M 430k 429k Varies_with_device'.split()
print(sizes)
for size in sizes:
    if size[-1] == 'M':
        print(float(size[:-1]))
    elif size[-1] == 'k':
        print(float(size[:-1])/1024)
    else:
        print(-1)

installs = "50,000,000+"

def set_installs(installs):




text = 'привет мир!'
text = text.replace('и', '-')
print(text)
