import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Download BIDU stock data from 2020-01-01 to 2024-12-31
print("Downloading BIDU stock data from 2020-01-01 to 2024-12-31...")
bidu = yf.download("BIDU", start="2020-01-01", end="2024-12-31")

# Save the data to CSV
csv_filename = "BIDU_stock_data_2020_2024.csv"
bidu.to_csv(csv_filename)
print(f"Data saved to {csv_filename}")

# Display basic information about the data
print(f"\nData shape: {bidu.shape}")
print(f"Date range: {bidu.index.min()} to {bidu.index.max()}")

# Extract the closing price series properly
close_prices = bidu['Close'] if 'Close' in bidu.columns else bidu[('Close', 'BIDU')]

# Create the plot with higher quality settings
plt.figure(figsize=(14, 8))
plt.rcParams['svg.fonttype'] = 'none'  # Ensure text is stored as text, not paths

# Plot the closing price
plt.plot(bidu.index, close_prices, label='BIDU Closing Price', linewidth=2.5, color='#1f77b4')

# Add markers for the specified career dates
career_start = datetime(2020, 12, 23)
career_end = datetime(2023, 7, 12)

# Find the closest dates in the data
start_idx = bidu.index.get_indexer([career_start], method='nearest')[0]
end_idx = bidu.index.get_indexer([career_end], method='nearest')[0]

start_date = bidu.index[start_idx]
end_date = bidu.index[end_idx]

# Add markers for the career period
plt.axvline(x=start_date, color='green', linestyle='--', alpha=0.8, linewidth=2, 
            label=f'Career Start: {start_date.strftime("%Y-%m-%d")}')
plt.axvline(x=end_date, color='red', linestyle='--', alpha=0.8, linewidth=2, 
            label=f'Career End: {end_date.strftime("%Y-%m-%d")}')

# Highlight the career period
plt.axvspan(start_date, end_date, alpha=0.15, color='gold', label='Career Period')

# Customize the plot with better styling
plt.title('My Career Journey at Baidu (2020-2024)', fontsize=18, fontweight='bold', pad=20)
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
svg_filename = "BIDU_career_chart_2020_2024.svg"
plt.savefig(svg_filename, dpi=300, bbox_inches='tight', format='svg')
print(f"SVG plot saved to {svg_filename}")

# Also save as PNG for compatibility
png_filename = "BIDU_career_chart_2020_2024.png"
plt.savefig(png_filename, dpi=300, bbox_inches='tight')
print(f"PNG plot saved to {png_filename}")

# Show the plot
plt.show()

print(f"\nAnalysis complete!")
print(f"- Data saved to: {csv_filename}")
print(f"- SVG chart saved to: {svg_filename}")
print(f"- PNG chart saved to: {png_filename}")
print(f"- Career period: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")

# Display some statistics for the career period
career_data = bidu.loc[start_date:end_date]
career_close = career_data['Close'] if 'Close' in career_data.columns else career_data[('Close', 'BIDU')]

print(f"\nCareer Period Statistics:")
print(f"- Days in period: {len(career_data)}")
print(f"- Starting price: ${float(career_close.iloc[0]):.2f}")
print(f"- Ending price: ${float(career_close.iloc[-1]):.2f}")
price_change = float(career_close.iloc[-1]) - float(career_close.iloc[0])
percentage_change = ((float(career_close.iloc[-1]) / float(career_close.iloc[0])) - 1) * 100
print(f"- Price change: ${price_change:.2f}")
print(f"- Percentage change: {percentage_change:.2f}%")

# Additional overall statistics
print(f"\nOverall Period Statistics (2020-2024):")
print(f"- Total trading days: {len(bidu)}")
print(f"- Starting price (2020): ${float(close_prices.iloc[0]):.2f}")
print(f"- Ending price (2024): ${float(close_prices.iloc[-1]):.2f}")
overall_change = float(close_prices.iloc[-1]) - float(close_prices.iloc[0])
overall_percentage = ((float(close_prices.iloc[-1]) / float(close_prices.iloc[0])) - 1) * 100
print(f"- Overall price change: ${overall_change:.2f}")
print(f"- Overall percentage change: {overall_percentage:.2f}%")
