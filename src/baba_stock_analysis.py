import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Download BABA stock data from 2020-01-01 to 2021-12-31
print("Downloading BABA stock data from 2020-01-01 to 2021-12-31...")
baba = yf.download("BABA", start="2020-01-01", end="2021-12-31")

# Save the data to CSV
csv_filename = "BABA_stock_data_2020_2021.csv"
baba.to_csv(csv_filename)
print(f"Data saved to {csv_filename}")

# Display basic information about the data
print(f"\nData shape: {baba.shape}")
print(f"Date range: {baba.index.min()} to {baba.index.max()}")
print("\nFirst 5 rows:")
print(baba.head())

# Create the plot
plt.figure(figsize=(12, 8))

# Plot the closing price
plt.plot(baba.index, baba['Close'], label='BABA Closing Price', linewidth=2)

# Add markers for the specified dates
highlight_start = datetime(2020, 7, 2)
highlight_end = datetime(2020, 12, 21)

# Find the closest dates in the data
start_idx = baba.index.get_indexer([highlight_start], method='nearest')[0]
end_idx = baba.index.get_indexer([highlight_end], method='nearest')[0]

start_date = baba.index[start_idx]
end_date = baba.index[end_idx]

# Add markers for the specified period
plt.axvline(x=start_date, color='green', linestyle='--', alpha=0.7, label=f'Start: {start_date.strftime("%Y-%m-%d")}')
plt.axvline(x=end_date, color='red', linestyle='--', alpha=0.7, label=f'End: {end_date.strftime("%Y-%m-%d")}')

# Highlight the period between the two dates
plt.axvspan(start_date, end_date, alpha=0.2, color='yellow', label='Highlighted Period')

# Customize the plot
plt.title('BABA Stock Price (2020-2021)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot
plot_filename = "BABA_stock_chart_2020_2021.png"
plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
print(f"Plot saved to {plot_filename}")

# Show the plot
plt.show()

print(f"\nAnalysis complete!")
print(f"- Data saved to: {csv_filename}")
print(f"- Chart saved to: {plot_filename}")
print(f"- Highlighted period: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")