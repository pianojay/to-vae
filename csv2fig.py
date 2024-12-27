import os
import math
import pandas as pd
from matplotlib import colors
import matplotlib.pyplot as plt

def csv2fig(directory_path, output_image_path, plt_show=True, max_num = 30):

    numerical = lambda _: int(''.join(filter(str.isdigit, _)))
    csv_files = sorted((f for f in os.listdir(directory_path)[:max_num] if f.endswith('.csv')), key = numerical)
    num_files = len(csv_files)
    max_num = min(max_num, num_files)
    print(f"{max_num}/{num_files}")

    cols = math.ceil(math.sqrt(max_num))
    rows = math.ceil(max_num / cols)

    fig, axes = plt.subplots(rows, cols)
    
    axes = pd.array([axes]) if max_num == 1 else axes.flatten()

    
    for ax, csv_file in zip(axes, csv_files):
        file_path = os.path.join(directory_path, csv_file)
        
        xPhys = pd.read_csv(file_path, header=None, index_col=False).values
        ax.imshow(-xPhys.T, cmap='gray', interpolation='none', norm=colors.Normalize(vmin=-1,vmax=0))
        
        ax.set_xticks([])
        ax.set_yticks([])
        # ax.axis('off')


    for i in range(max_num, len(axes)):
        fig.delaxes(axes[i])

    plt.savefig(output_image_path)
    if plt_show:
        plt.show()
    
    

if __name__ == '__main__':
    csv2fig('Michell_28x28', 'Michell_28x28')