import os, shutil, sys

def arrange(dir, function = shutil.copy):
    if not os.path.isdir(dir):
        return 1
    for root, dirs, files in os.walk(dir):
        print('dir: ', dirs)
        for file in files:
            name, ext = os.path.splitext(file)
            ext = ext[1:]
            if not os.path.exists(os.path.join("output", ext)):
                os.makedirs(os.path.join("output", ext))
            if os.path.exists(os.path.join("output", ext, file)):
                count = 1
                for newFile in os.listdir(os.path.join("output", ext, '')):
                    if name == "_".join(newFile.split('.')[0].split('_')[:-1]):
                        count += 1
                outfile = name+'_'+str(count)+'.'+ext
            else:
                outfile = file
            print('File:', os.path.join(root, file), '->', os.path.join("output", ext, outfile))
            function(os.path.join(root, file), os.path.join("output", ext, outfile))

if __name__ == "__main__":
    dir_name = ''
    if len(sys.argv) == 2:
        dir_name = sys.argv[1]
    else:
        print('error entering arguments')
    arrange(dir_name)
