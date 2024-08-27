import matplotlib.pyplot as plt

def line_plot(x, y):
    plt.plot(x, y, color='blue', linestyle='dashdot', marker='x')
    plt.title("Simple Line Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

def scattered_plot(x, y):
    plt.scatter(x, y)
    plt.title("Scatter Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

def bar_plot(categories, values):
    plt.bar(categories, values)
    plt.title("Simple Bar Plot")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.show()

def histogram_plot(data):
    plt.hist(data, bins=5)
    plt.title("Simple Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()

def customize_plot(x, y):
    plt.plot(x, y)
    plt.title("Customized Plot")
    plt.xlabel("X Axis Label")
    plt.ylabel("Y Axis Label")
    plt.xticks([1, 2, 3, 4, 5], ['One', 'Two', 'Three', 'Four', 'Five'])
    plt.yticks([0, 10, 20, 30])
    plt.show()

def multidimensional_plot(x, y):
    for i in range(len(x)):
        plt.plot(x[i], [y[i]] * len(x[i]), label=f'Line {i + 1}')  # Plot each x[i] against the corresponding y[i]

    plt.title("Multiple Arrays vs. Scalars")
    plt.xlabel("X Values")
    plt.ylabel("Y Value (Constant)")
    plt.legend()  # Optional: adds a legend to identify each line
    plt.show()

def multi_multidimensional_plot(x, y):
    for i in range(x.shape[0]):
        plt.plot(x[i], y[i], marker='o', label=f'Line {i + 1}')

    plt.title("Multiple Lines from 2D Arrays")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.legend()
    plt.show()