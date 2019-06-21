from pathlib import Path


path = Path(r"C:\Users\SahilRaj\git")
print(path.exists())

paths = [p for p in path.iterdir() if p.is_file()]
print(paths)

for x in paths:
    print(x)


py_files = [p for p in path.rglob("class.py")]
print(py_files)

for x in py_files:
    print(x)
