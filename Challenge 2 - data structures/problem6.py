sampleDict = {
	"name": "Kelly",
	"age": 25,
	"salary": 8000,
	"city": "New York"
}

new_key = "location"
old_key = "city"
sampleDict[new_key] = sampleDict.pop(old_key)

print(sampleDict)