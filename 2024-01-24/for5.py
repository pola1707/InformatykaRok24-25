import subprocess

for i in range(10):
command = "mspaint.exe"
process = subprocess.Popen(command, shell=True)