cur = lng = s[0]
for c in s[1:]:
    cur = '' if c < cur[-1] else cur
    lng, cur = max(lng, cur + c, key=len), cur + c
print('Longest substring in alphabetical order is:', lng)
