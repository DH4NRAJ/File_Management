import os, sys, shutil

def disarrange(main, dirs):
    for root, subdir, files in os.walk(dirs):
        print("Root:", root)
        print("Sub Dir:", subdir)
        print("Files:", files)
        for file in files:
            path = os.path.join(root, file)
            shutil.copy(path, main)

if __name__ == "__main__":
    path = os.getcwd()
    if len(sys.argv) == 3:
        dirs = path+ '/' + sys.argv[1]      #dir which has all the files
        main = path+ '/' + sys.argv[2]      # dir where all the files are being copyed
    else:
        print("error entering arguments")

    disarrange(main, dirs)
