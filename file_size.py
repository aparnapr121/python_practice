import os
path="/Users/aparnaprajan/Documents/python_practice"
def get_size(path):
    total_size=0
    for dirpath, dirname, filenames in os.walk(path):
        for f in filenames:
            fp=os.path.join(dirpath,f)
            if os.path.exists(fp):
                total_size+=os.path.getsize(fp)
        return total_size




