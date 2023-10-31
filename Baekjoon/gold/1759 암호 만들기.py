L, C = map(int,input().split())
arr = list(input().split())
arr.sort()
# L개의 조합이 최소 한 갠의 모음과 최소 두 개의 자음으로 구성되어 있다
# == 전체 L의 조합 - {(모음이 없는 조합) U (자음이 1개거나 0개인 조합)}
def combination(a,r):
    result = []
    if r ==1:
        for i in a:
            result.append([i])
    else:
        for i in range(len(a)-r+1):
            for j in combination(a[i+1:],r-1):
                result.append([a[i]]+j)
    return result
Total_comb = combination(arr,L)
vowel = ['a','e','i','o','u']
vowel_num = 0
conson_num = 0
for i in range(len(Total_comb)):
    vowel_num = 0
    conson_num = 0
    for j in range(L):
        if Total_comb[i][j] in vowel:
            vowel_num += 1
        else:
            conson_num += 1

    if vowel_num > 0 and conson_num >1:
        print(f"{''.join(Total_comb[i])}")



#모음이 없는 조합
# vowel = ['a','e','i','o','u']
# vowel_num = 0
# conson_num = 0
# vowel_list = []
# conson_list = []
# for i in range(C):
#     if arr[i] in vowel:
#         vowel_num +=1
#         vowel_list.append(arr[i])
#     else:
#         conson_num +=1
#         conson_list.append(arr[i])
# #모음이 없는 조합
# if conson_num >= L:
#     conson_comb = combination(vowel_list,L)
# #자음이 1개인 조합
# if vowel_num >= L-1:
#     for i in conson_list:
#
#
# #자음이 0개인 조합
# if vowel_num >= L:



# print(int('z',36))
# print(int('Z',36))