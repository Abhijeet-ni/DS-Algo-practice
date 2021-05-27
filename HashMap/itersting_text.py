import re
import timeit

f = open("poem.txt", "r")
# res = f.read().replace('.','')
# res = res.replace("\n"," ")
# print(f)
pat = " |\n|;|:|,|!|.$"
result = re.split(pat,f.read())

dist={}
count = 0
result_set = set(result)
for i in result_set:
    for j in result:
        if i == j:
            count += 1
    dist[i] = count
    count = 0

print(dist)
print('diverged :', dist['diverged'])
print('in :', dist['in'])
print('I :', dist['I'])
print(timeit.timeit())

# word_count = {}
# with open("poem.txt","r") as f:
#     for line in f:
#         tokens = line.split(' ')
#         for token in tokens:
#             token=token.replace('\n','')
#             if token in word_count:
#                 word_count[token]+=1
#             else:
#                 word_count[token]=1
#
# print(word_count)
# print('diverged :', word_count['diverged'])
# print('in :', word_count['in'])
# print('I :', word_count['I'])
# print(timeit.timeit())