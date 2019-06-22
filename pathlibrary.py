from pathlib import Path
import shutil
file_path = Path(r"D:\Programming\hamrosansar.html")
target = Path(r"C:\Users\SahilRaj\git\CodeHub\hamrosansar.html")
print(file_path.exists())


file_path.write_text("hello world!")
print(file_path.read_text())

shutil.copy(file_path, target)
