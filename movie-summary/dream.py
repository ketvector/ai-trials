from transformers import pipeline

classifier = pipeline("summarization")
contents = ""
with open('/home/neeraj/Code/movie-summary/scripts/As-Good-As-It-Ge.txt') as f:
    contents = f.read()
    n = 1024
split_content = [contents[i:i+n] for i in range(0, len(contents), n)]
result = []
for part in split_content:
    summary = classifier(part)
    print(summary)
    result = result + summary