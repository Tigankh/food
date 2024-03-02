
with open('notnormalformatfood.txt', 'r') as file:
    lines = file.readline().split('. ')
lst = []
for i in range(len(lines)):
    lst.append(lines[i][:-3].replace(',', ''))
