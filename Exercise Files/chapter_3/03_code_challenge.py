import matplotlib.pyplot as plt

def create_annotated_bar_chart(data):
    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Create the bar chart
    bars = ax.bar(data['Category'], data['Sales'])
    
    # Add title and y-axis label
    ax.set_title("Annual Sales by Category", fontsize=16)
    ax.set_ylabel("Sales ($)", fontsize=12)
    
    # Add text annotations above each bar
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'${bar.get_height():,}', ha='center', va='bottom')
    
    # Find the highest bar and add "Best Seller!" label
    max_sales = max(data['Sales'])
    max_index = data['Sales'].index(max_sales)
    
    ax.text(max_index, max_sales, "Best Seller!", ha='left', va='bottom')
    
    # Adjust layout and return the figure
    plt.tight_layout()
    return fig