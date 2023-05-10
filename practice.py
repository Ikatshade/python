# l = [[1, 2, 5], [7, 4, 3], [9, 8, 6]]

# out = [x for i in l for x in i]
# sorted_o = sorted(out)

# new = []
# k = 0
# for idx in range(3):
#         sub = []
#         for jdx in range(3):
#             sub.append(sorted_o[k])
#             k += 1
#         new.append(sub)
# print(sorted_o, new)

c = 123
s = str(c)
tot = 0
for i in s:
    tot += int(i)
print(tot)