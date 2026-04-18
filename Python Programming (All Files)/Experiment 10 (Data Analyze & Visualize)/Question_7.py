# Write a Python Program To Demonstrate Different Visual Forms Using Matplotlib.

import matplotlib.pyplot as plt
import numpy as np

def main():

    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Matplotlib Visual Forms Demonstration', fontsize=18, fontweight='bold')
    plt.subplots_adjust(hspace=0.4, wspace=0.3)

    x_line = np.array([1, 2, 3, 4, 5, 6])
    y_line = np.array([2, 5, 4, 8, 7, 12])
    axs[0, 0].plot(x_line, y_line, color='blue', marker='o', linestyle='-', linewidth=2)
    axs[0, 0].set_title('1. Line Chart')
    axs[0, 0].set_xlabel('Time')
    axs[0, 0].set_ylabel('Growth')
    axs[0, 0].grid(True, linestyle='--', alpha=0.6)

    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 12, 56, 32]
    axs[0, 1].bar(categories, values, color=['red', 'green', 'blue', 'orange', 'purple'])
    axs[0, 1].set_title('2. Bar Chart')
    axs[0, 1].set_xlabel('Categories')
    axs[0, 1].set_ylabel('Values')

    np.random.seed(42)
    x_scatter = np.random.rand(50) * 10
    y_scatter = x_scatter + np.random.randn(50) * 2
    axs[0, 2].scatter(x_scatter, y_scatter, color='darkred', alpha=0.7)
    axs[0, 2].set_title('3. Scatter Plot')
    axs[0, 2].set_xlabel('Variable X')
    axs[0, 2].set_ylabel('Variable Y')

    data_hist = np.random.randn(1000)
    axs[1, 0].hist(data_hist, bins=20, color='teal', edgecolor='black')
    axs[1, 0].set_title('4. Histogram')
    axs[1, 0].set_xlabel('Data Range')
    axs[1, 0].set_ylabel('Frequency')
    
    labels = ['Python', 'Java', 'C++', 'JavaScript']
    sizes = [40, 25, 15, 20]
    explode = (0.1, 0, 0, 0)
    color_used=['gold', 'lightblue', 'lightcoral', 'lightgreen']
    axs[1, 1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=color_used)
    axs[1, 1].set_title('5. Pie Chart')

    group_1 = np.random.normal(100, 10, 200)
    group_2 = np.random.normal(90, 20, 200)
    group_3 = np.random.normal(80, 30, 200)
    data_to_plot = [group_1, group_2, group_3]
    
    bplot = axs[1, 2].boxplot(data_to_plot, patch_artist=True, notch=True, tick_labels=['G1', 'G2', 'G3'])
    colors = ['lightblue', 'lightgreen', 'pink']
    
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
    for median in bplot['medians']:
        median.set(color='red', linewidth=2)
    for flier in bplot['fliers']:
        flier.set(marker='o', color='purple', alpha=0.5)

    axs[1, 2].set_title('6. Box Plot')
    axs[1, 2].set_xlabel('Groups')
    axs[1, 2].set_ylabel('Values')
    axs[1, 2].yaxis.grid(True, linestyle='--', alpha=0.7)

    plt.show()

if __name__ == "__main__":
    main()