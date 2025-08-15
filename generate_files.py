import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

def generate_supply_chain_data():
    """Generate 63 realistic supply chain data points"""
    data = []
    
    for i in range(63):
        # Generate realistic supply chain metrics with correlations
        lead_time = np.random.randint(5, 26)  # 5-25 days
        inventory_levels = np.random.randint(1000, 6001)  # 1000-6000 units
        order_frequency = np.random.randint(2, 11)  # 2-10 orders/month
        
        # Delivery performance negatively correlated with lead time
        delivery_performance = max(65, min(98, 95 - (lead_time - 15) * 2 + np.random.normal(0, 5)))
        
        # Cost per unit correlated with lead time
        cost_per_unit = 50 + (lead_time * 1.5) + np.random.normal(0, 10)
        cost_per_unit = max(30, min(100, cost_per_unit))  # Cap between $30-$100
        
        data.append({
            'Transaction_ID': i + 1,
            'Supplier_Lead_Time': lead_time,
            'Inventory_Levels': inventory_levels,
            'Order_Frequency': order_frequency,
            'Delivery_Performance': round(delivery_performance, 1),
            'Cost_Per_Unit': round(cost_per_unit, 2)
        })
    
    return pd.DataFrame(data)

def calculate_correlation_matrix(df):
    """Calculate correlation matrix for supply chain variables"""
    variables = ['Supplier_Lead_Time', 'Inventory_Levels', 'Order_Frequency', 
                'Delivery_Performance', 'Cost_Per_Unit']
    
    correlation_matrix = df[variables].corr()
    return correlation_matrix

def create_excel_style_heatmap(corr_matrix, filename='heatmap.png', size=(400, 400)):
    """Create Excel-style heatmap with Red-White-Green color scheme"""
    
    # Create figure with specific size to ensure under 512x512
    fig, ax = plt.subplots(figsize=(4.8, 4.8), dpi=80)  # Adjusted for smaller output
    
    # Create custom colormap (Red-White-Green)
    import matplotlib.colors
    colors = ['#FF0000', '#FFFFFF', '#00FF00']  # Red, White, Green
    n_bins = 100
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list('excel', colors, N=n_bins)
    
    # Create heatmap
    im = ax.imshow(corr_matrix.values, cmap=cmap, vmin=-1, vmax=1, aspect='equal')
    
    # Set ticks and labels
    ax.set_xticks(range(len(corr_matrix.columns)))
    ax.set_yticks(range(len(corr_matrix.index)))
    ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right', fontsize=9)
    ax.set_yticklabels(corr_matrix.index, fontsize=9)
    
    # Add correlation values as text
    for i in range(len(corr_matrix.index)):
        for j in range(len(corr_matrix.columns)):
            value = corr_matrix.iloc[i, j]
            # Choose text color based on background
            text_color = 'white' if abs(value) > 0.5 else 'black'
            ax.text(j, i, f'{value:.3f}', ha='center', va='center', 
                   color=text_color, fontweight='bold', fontsize=8)
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Correlation Coefficient', rotation=270, labelpad=15)
    
    # Set title
    ax.set_title('Supply Chain Metrics Correlation Matrix\n(Excel Red-White-Green Style)', 
                fontsize=11, fontweight='bold', pad=15)
    
    # Adjust layout and save with controlled parameters
    plt.tight_layout()
    plt.savefig(filename, dpi=80, bbox_inches='tight', facecolor='white', pad_inches=0.1)
    plt.close()
    
    # Verify and resize if needed
    img = Image.open(filename)
    print(f"Initial heatmap dimensions: {img.size[0]}x{img.size[1]} pixels")
    
    # Ensure dimensions are under 512x512
    if img.size[0] > 512 or img.size[1] > 512:
        print("Resizing to meet requirements...")
        max_size = 500
        ratio = min(max_size/img.size[0], max_size/img.size[1])
        new_size = (int(img.size[0] * ratio), int(img.size[1] * ratio))
        img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
        img_resized.save(filename)
        print(f"Resized to: {img_resized.size[0]}x{img_resized.size[1]} pixels")
        return img_resized.size
    
    print(f"Heatmap saved as {filename} with dimensions: {img.size}")
    return img.size

def main():
    # Generate supply chain data
    print("Generating supply chain data...")
    df = generate_supply_chain_data()
    
    # Calculate correlation matrix
    print("Calculating correlation matrix...")
    corr_matrix = calculate_correlation_matrix(df)
    
    # Save correlation matrix as CSV (Excel format)
    print("Saving correlation matrix to correlation.csv...")
    corr_matrix.to_csv('correlation.csv')
    
    # Create Excel-style heatmap with size control
    print("Creating Excel-style heatmap...")
    dimensions = create_excel_style_heatmap(corr_matrix, 'heatmap.png')
    
    # Save sample data
    print("Saving sample data...")
    df.to_csv('sample_supply_chain_data.csv', index=False)
    
    # Final verification
    final_img = Image.open('heatmap.png')
    print(f"Final heatmap dimensions: {final_img.size[0]}x{final_img.size[1]} pixels")
    
    if final_img.size[0] <= 512 and final_img.size[1] <= 512:
        print("✅ Image size is within requirements!")
    else:
        print("❌ Image is still too large - manual resize needed")
    
    print(f"\nFiles generated successfully!")
    print(f"- correlation.csv: {corr_matrix.shape[0]}x{corr_matrix.shape[1]} correlation matrix")
    print(f"- heatmap.png: {dimensions[0]}x{dimensions[1]} pixels")
    print(f"- sample_supply_chain_data.csv: {len(df)} data points")
    
    # Display correlation matrix
    print("\nCorrelation Matrix:")
    print(corr_matrix.round(3))

if __name__ == "__main__":
    main()
