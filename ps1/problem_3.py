print('Longest substring in alphabetical order is:', end=' ')
print(max((''.join([a + ' ' if a > b else a for a, b in zip(s, s[1:] + s)])).split(), key=len))
