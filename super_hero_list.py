heroes = ['spider man','thor','hulk','iron man','captain america']
print(len(heroes))

heroes.append("black panther")

heroes.remove('black panther')

heroes.insert(3, 'black panther')

# heroes.insert(1, 'thor')
# heroes.insert(2, 'hulk')


heroes[1:3] = ['doctor strange']

heroes.sort()

print(heroes)
