def all_variants(text):
  abc_ = len(text)
  for i in range(1, abc_ + 1):
      for j in range(abc_ - i + 1):
          yield text[j:j + i]

a = all_variants("abc")
for i in a:
  print(i)