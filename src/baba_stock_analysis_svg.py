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

# Create the plot with higher quality settings
plt.figure(figsize=(14, 8))
plt.rcParams['svg.fonttype'] = 'none'  # Ensure text is stored as text, not paths

# Extract the closing price series properly
close_prices = baba['Close'] if 'Close' in baba.columns else baba[('Close', 'BABA')]

# Plot the closing price
plt.plot(baba.index, close_prices, label='BABA Closing Price', linewidth=2.5, color='#1f77b4')

# Add markers for the specified dates
highlight_start = datetime(2020, 7, 2)
highlight_end = datetime(2020, 12, 21)

# Find the closest dates in the data
start_idx = baba.index.get_indexer([highlight_start], method='nearest')[0]
end_idx = baba.index.get_indexer([highlight_end], method='nearest')[0]

start_date = baba.index[start_idx]
end_date = baba.index[end_idx]

# Add markers for the specified period
plt.axvline(x=start_date, color='green', linestyle='--', alpha=0.8, linewidth=2, 
            label=f'Start: {start_date.strftime("%Y-%m-%d")}')
plt.axvline(x=end_date, color='red', linestyle='--', alpha=0.8, linewidth=2, 
            label=f'End: {end_date.strftime("%Y-%m-%d")}')

# Highlight the period between the two dates
plt.axvspan(start_date, end_date, alpha=0.15, color='gold', label='Highlighted Period')

# Customize the plot with better styling
plt.title('My Career Journey at Alibaba Group (2020-2021)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Price (USD)', fontsize=14)
plt.legend(fontsize=12, framealpha=0.9)
plt.grid(True, alpha=0.2)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot as SVG for high quality
svg_filename = "BABA_stock_chart_2020_2021.svg"
plt.savefig(svg_filename, dpi=300, bbox_inches='tight', format='svg')
print(f"SVG plot saved to {svg_filename}")

# Also save as PNG for compatibility
png_filename = "BABA_stock_chart_2020_2021.png"
plt.savefig(png_filename, dpi=300, bbox_inches='tight')
print(f"PNG plot saved to {png_filename}")

# Show the plot
plt.show()

print(f"\nAnalysis complete!")
print(f"- Data saved to: {csv_filename}")
print(f"- SVG chart saved to: {svg_filename}")
print(f"- PNG chart saved to: {png_filename}")
print(f"- Highlighted period: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")

# Display some statistics for the highlighted period
highlighted_data = baba.loc[start_date:end_date]
highlighted_close = highlighted_data['Close'] if 'Close' in highlighted_data.columns else highlighted_data[('Close', 'BABA')]

print(f"\nHighlighted Period Statistics:")
print(f"- Days in period: {len(highlighted_data)}")
print(f"- Starting price: ${float(highlighted_close.iloc[0]):.2f}")
print(f"- Ending price: ${float(highlighted_close.iloc[-1]):.2f}")
price_change = float(highlighted_close.iloc[-1]) - float(highlighted_close.iloc[0])
percentage_change = ((float(highlighted_close.iloc[-1]) / float(highlighted_close.iloc[0])) - 1) * 100
print(f"- Price change: ${price_change:.2f}")
print(f"- Percentage change: {percentage_change:.2f}%")