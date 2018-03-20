f= open('a.txt', 'r')
paragraph = 0
lines = f.readlines()
for idx, line in enumerate(lines):
    if not line == '\n':
        m = re.search(r'\w', line)
        str = m.group(0)
        try:
      paragraph +=1
    except:
      paragraph +=1

print paragraph
