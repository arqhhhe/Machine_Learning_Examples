import data_plot as plot
import numpy as np
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    data = [1, 2, 1,  2, 2, 3, 3, 4, 4, 4, 4, 5, 2, 5]
    categories = ['A', 'B', 'C', 'D']
    values = [5, 7, 3, 8]
    # plot.line_plot(x, y)
    # plot.scattered_plot(x, y)
    # plot.bar_plot(x, y)
    # plot.customize_plot(x, y)
    # plot.histogram_plot(data)
    # x = [
    #     [1, 2, 3, 4],
    #     [2, 3, 4, 5],
    #     [3, 4, 5, 6]
    # ]
    # y = [10, 20, 30]
    # plot.multidimensional_plot(x, y)

    # x = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
    # y = np.array([[1, 4, 9, 16], [2, 3, 5, 7]])
    # plot.multi_multidimensional_plot(x, y)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
