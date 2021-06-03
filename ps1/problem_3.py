longest = ''
for i in range(len(s)):
    i_long = s[i]
    for j in range(i + 1, len(s)):
        if s[j] < i_long[-1]:
            break
        i_long = s[i:j + 1]
    if len(i_long) > len(longest):
        longest = i_long
print('Longest substring in alphabetical order is:', longest)
