import pandas as pd
import matplotlib.pyplot as plt

# Create dataframe from your data
data = {
    "Supplier_Lead_Time": [16.5, 9.4, 17.8, 20, 15.4, 7.9, 19.1, 11.2],
    "Inventory_Levels": [361, 245, 479, 314, 127, 232, 163, 451],
    "Order_Frequency": [6.1, 9.2, 6.2, 5.5, 5.1, 10.3, 4, 7.2],
    "Delivery_Performance": [81.7, 89.6, 75.7, 72.9, 77.7, 90.5, 76.9, 84.4],
    "Cost_Per_Unit": [30.97, 24.76, 31.88, 35.26, 29.82, 20.8, 32.5, 27.07]
}

df = pd.DataFrame(data)

# Generate correlation matrix
corr_matrix = df.corr()

# Save correlation matrix as CSV
corr_matrix.to_csv("correlation.csv", index=True)

# Plot heatmap
plt.figure(figsize=(5, 5))  # Square image between 400-512px
plt.imshow(corr_matrix, cmap="RdYlGn", vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.tight_layout()
plt.savefig("heatmap.png", dpi=100)
plt.close()
