l = [34,1,23,4,3,3,12,4,3,1]
l.sort()
mean = sum(l) / len(l)
std = (sum([(x - mean) ** 2 for x in l]) / len(l)) ** 0.5
kurtosis = sum([(x - mean) ** 4 for x in l]) / len(l) / std ** 4
skewness = sum([(x - mean) ** 3 for x in l]) / len(l) / std ** 3
print(kurtosis, skewness)