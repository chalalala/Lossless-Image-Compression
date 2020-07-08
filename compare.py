import cv2, sys
import matplotlib.pyplot as plt

def compare(paths,titles):
    plt.figure('Comparison')
    
    for i in range(2):
        img = cv2.imread(paths[i])
        plt.subplot(1,2,i+1)
        plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        #plt.xticks([]),plt.yticks([])
        plt.axis("off")
        plt.title(titles[i])
    
    plt.tight_layout(pad=.5)
    plt.show()

paths = []
paths.append(sys.argv[1])
paths.append(sys.argv[2])

compare(paths, ['example', 'result'])