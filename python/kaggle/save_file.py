import os

audioFile = "/kaggle/input/datasets/abdulzoha786/regret/abc.m4a"
filePath = audioFile.split("/")[-1]
fileName,_ = filePath.split(".")
modelName = "large-v2"
fileName = f"{fileName}-{modelName}.srt"

# output file
for file in os.listdir():
    if file == filePath:
        os.rename(file, fileName)

if os.path.exists(fileName):
    print(fileName)