import subprocess

with open('new3.py', 'w') as f:
    a = subprocess.Popen('python new1.py', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    f.write(a.communicate()[0].decode('ascii'))