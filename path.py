from pathlib import Path

path = Path("git\Tutorial\path.py")
print(path)
print(path.exists())
print(path.is_file())
print(path.is_dir())

print(path)
print(path.exists())
print(path.absolute())
print(path.home())
