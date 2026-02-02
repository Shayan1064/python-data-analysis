# ---------- Reading from a file ----------
f = open("file.txt", "r")
data = f.read()
print("File content before append:")
print(data)
f.close()  # always close file if not using 'with'

# ---------- Appending to a file ----------
f = open("file.txt", "a")  # open in append mode
f.write("I will be there In Sha Allah\n")  # use write(), not append()
f.close()

# ---------- Reading again to see changes ----------
f = open("file.txt", "r")
data = f.read()
print("\nFile content after append:")
print(data)
f.close()
