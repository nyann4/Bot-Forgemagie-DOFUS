from pathlib import Path
import time
root_path = Path("..").resolve()
print(root_path)
tmp_dir = root_path / "screen modifier"
try:
    tmp_dir.mkdir(parents=True)
except:
    pass
