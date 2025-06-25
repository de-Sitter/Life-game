import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import copy

LIFE=[]
dim=int(input('the dimension is '))
frame_number=int(input('the frame number is '))

life=[random.choices([0,1], weights=[0.5,0.5], k=dim) for _ in range(dim)]
LIFE.append(life)



for k in range(1,frame_number+1):
    copied=copy.deepcopy(LIFE[k-1])
    print(np.array(LIFE[0]))
    copiedd=copy.deepcopy(life)
    for i in range(dim):
        for j in range(dim):
            sum=0
            for row in range(i-1,i+2):
                for col in range(j-1,j+2):
                    if row==i and col==j:
                        continue
                    if row==-1: row+=dim
                    if row==dim: row-=dim
                    if col==-1: col+=dim
                    if col==dim: col-=dim
                    sum+=copied[row][col]
            if sum<2 or sum>3:
                copiedd[i][j]=0
            elif sum==2:
                copiedd[i][j]=copied[i][j]
            elif sum==3:
                copiedd[i][j]=1
    news=copy.deepcopy(copiedd)
    LIFE.append(news)
        
Life=np.array(LIFE)

print(Life)

fig, ax=plt.subplots()
ax.set_title('Life program animation')
img=ax.imshow(Life[0], cmap='binary', interpolation='nearest', vmax=1, vmin=0)

def update(frame):
    img.set_data(Life[frame])
    return [img]

ani=FuncAnimation(fig, update, frame_number+1, interval=500, blit=True)
ani.save('life.gif')
plt.show()

