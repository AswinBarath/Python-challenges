st1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

ans = list(map((lambda string: string.count('A') + string.count('a')), st1))

print(ans)