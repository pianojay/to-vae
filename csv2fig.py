import os
import math
import pandas as pd
from matplotlib import colors
import matplotlib.pyplot as plt

def csv2fig(directory_path, output_image_path, plt_show=True):

    numerical = lambda _: int(''.join(filter(str.isdigit, _)))
    csv_files = sorted((f for f in os.listdir(directory_path) if f.endswith('.csv')), key = numerical)
    num_files = len(csv_files)
    print(num_files)

    cols = math.ceil(math.sqrt(num_files))
    rows = math.ceil(num_files / cols)

    fig, axes = plt.subplots(rows, cols)
    
    axes = [axes] if num_files == 1 else axes
    axes = axes.flatten()

    
    for ax, csv_file in zip(axes, csv_files):
        file_path = os.path.join(directory_path, csv_file)
        
        xPhys = pd.read_csv(file_path, header=None, index_col=False).values
        ax.imshow(-xPhys.T, cmap='gray', interpolation='none', norm=colors.Normalize(vmin=-1,vmax=0))
        
        ax.set_xticks([])
        ax.set_yticks([])
        # ax.axis('off')


    for i in range(num_files, len(axes)):
        fig.delaxes(axes[i])

    plt.savefig(output_image_path)
    if plt_show:
        plt.show()
    
    

if __name__ == '__main__':
    csv2fig('Michell_28x28', 'Michell_28x28')