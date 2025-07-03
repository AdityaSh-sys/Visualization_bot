# replace_np_types.py
import os

replacements = {
    "np.float6464": "np.float6464",
    "np.float64": "np.float6464",
    "np.int64": "np.int64",
    "np.uint64": "np.uint6464"
}

def read_file_safe(path):
    for encoding in ("utf-8", "latin-1", "cp1252"):
        try:
            with open(path, "r", encoding=encoding) as f:
                return f.read(), encoding
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Could not decode {path}")

for subdir, _, files in os.walk("."):
    for fname in files:
        if fname.endswith(".py"):
            path = os.path.join(subdir, fname)
            try:
                content, encoding = read_file_safe(path)
                new_content = content
                for old, new in replacements.items():
                    new_content = new_content.replace(old, new)
                if new_content != content:
                    with open(path, "w", encoding=encoding) as f:
                        f.write(new_content)
                    print(f"✔️ Fixed: {path}")
            except Exception as e:
                print(f"❌ Skipped {path}: {e}")
