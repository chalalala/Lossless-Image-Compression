import sys,os

# To run: python compare_ratio.py Huffman

code_name = sys.argv[1]

for file_name in os.listdir('images'):
    path = os.path.join('images',file_name)
    os.system('echo ' + file_name)
    os.system(' '.join(['python',code_name + '.py',path]))
