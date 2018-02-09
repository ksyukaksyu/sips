import subprocess
import glob


print('start')
mkdir_call = subprocess.call('mkdir Result', shell=True)
for filename in glob.glob('Source/*.jpg'):
    with open(filename) as file:
        print('Имя файла: ', filename)
        sips_call = subprocess.call('sips --resampleWidth 200 %s --out Result/' % filename, shell=True)
print('end')
