import os
import subprocess
import tempfile

print("Welcome to C++ Terminal (created by Chase Stirling)!")
print("Type 'exit' to quit.")
print("Type 'run' to compile and execute your code.")
print("©2025 Bjarne Stroustrup, Chase Stirling")
print("---------------------------------------------")

code_lines = []

while True:
    line = input("C++> ")
    if line.strip().lower() == "exit":
        break
    elif line.strip().lower() == "run":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".cpp") as tmp_cpp:
            tmp_cpp.write("\n".join(code_lines).encode("utf-8"))
            tmp_cpp_path = tmp_cpp.name
        exe_path = tmp_cpp_path.replace(".cpp", ".exe")

        try:
            compile_proc = subprocess.run(["g++", tmp_cpp_path, "-o", exe_path], capture_output=True, text=True)
            if compile_proc.returncode == 0:
                print("✅ Compilation successful!\nRunning program...\n-------------------------")
                subprocess.run([exe_path])
            else:
                print("❌ Compilation failed:\n")
                print(compile_proc.stderr)
        except FileNotFoundError:
            print("⚠️  g++ not found! Make sure MinGW (with g++) is installed and in PATH.")
        finally:
            os.remove(tmp_cpp_path)
            if os.path.exists(exe_path):
                os.remove(exe_path)
        code_lines = []
    else:
        code_lines.append(line)
