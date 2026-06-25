import os


# os.mkdir("data")
    
for i in range(0, 10):
    os.rename(f"data/{i+1}temp.png", f"data/{i+1}.png")    