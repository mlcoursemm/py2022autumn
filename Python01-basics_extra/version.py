from platform import python_version

with open('version.txt', 'w') as f:
    f.write(python_version())