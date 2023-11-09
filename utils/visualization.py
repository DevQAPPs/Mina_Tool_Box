import matplotlib.pyplot as plt

def generate_performance_plot(data, title='Validator Performance'):
    """Generates a simple line plot for given data."""
    plt.figure(figsize=(10, 6))
    plt.plot(data['x'], data['y'], marker='o')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Performance Metric')
    plt.grid(True)
    plt.savefig('performance_plot.png')
    # TODO option to return the plot object or bytes data
