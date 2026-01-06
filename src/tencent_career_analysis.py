import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Download Tencent stock data from 2023-01-01 to 2025-12-31
print("Downloading Tencent stock data from 2023-01-01 to 2025-12-31...")
tencent = yf.download("0700.HK", start="2023-01-01", end="2025-12-31")

# Save the data to CSV
csv_filename = "Tencent_stock_data_2023_2025.csv"
tencent.to_csv(csv_filename)
print(f"Data saved to {csv_filename}")

# Display basic information about the data
print(f"\nData shape: {tencent.shape}")
print(f"Date range: {tencent.index.min()} to {tencent.index.max()}")

# Extract the closing price series properly
close_prices = tencent['Close'] if 'Close' in tencent.columns else tencent[('Close', '0700.HK')]

# Create the plot with higher quality settings
plt.figure(figsize=(14, 8))
plt.rcParams['svg.fonttype'] = 'none'  # Ensure text is stored as text, not paths

# Plot the closing price
plt.plot(tencent.index, close_prices, label='Tencent Closing Price', linewidth=2.5, color='#1f77b4')

# Add marker for career start date (no end date specified)
career_start = datetime(2023, 7, 13)

# Find the closest date in the data
start_idx = tencent.index.get_indexer([career_start], method='nearest')[0]
start_date = tencent.index[start_idx]

# Add marker for career start
plt.axvline(x=start_date, color='green', linestyle='--', alpha=0.8, linewidth=2, 
            label=f'Career Start: {start_date.strftime("%Y-%m-%d")}')

# Highlight the period from career start to end of data (ongoing career)
plt.axvspan(start_date, tencent.index[-1], alpha=0.15, color='gold', label='Career Period (Ongoing)')

# Customize the plot with better styling
plt.title('My Career Journey at Tencent (2023-2025)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Price (HKD)', fontsize=14)
plt.legend(fontsize=12, framealpha=0.9)
plt.grid(True, alpha=0.2)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the plot as SVG for high quality
svg_filename = "Tencent_career_chart_2023_2025.svg"
plt.savefig(svg_filename, dpi=300, bbox_inches='tight', format='svg')
print(f"SVG plot saved to {svg_filename}")

# Also save as PNG for compatibility
png_filename = "Tencent_career_chart_2023_2025.png"
plt.savefig(png_filename, dpi=300, bbox_inches='tight')
print(f"PNG plot saved to {png_filename}")

# Show the plot
plt.show()

print(f"\nAnalysis complete!")
print(f"- Data saved to: {csv_filename}")
print(f"- SVG chart saved to: {svg_filename}")
print(f"- PNG chart saved to: {png_filename}")
print(f"- Career start: {start_date.strftime('%Y-%m-%d')} (ongoing)")

# Display some statistics for the career period
career_data = tencent.loc[start_date:]
career_close = career_data['Close'] if 'Close' in career_data.columns else career_data[('Close', '0700.HK')]

print(f"\nCareer Period Statistics (Ongoing):")
print(f"- Days in period: {len(career_data)}")
print(f"- Starting price: ${float(career_close.iloc[0]):.2f}")
print(f"- Current price: ${float(career_close.iloc[-1]):.2f}")
price_change = float(career_close.iloc[-1]) - float(career_close.iloc[0])
percentage_change = ((float(career_close.iloc[-1]) / float(career_close.iloc[0])) - 1) * 100
print(f"- Price change: ${price_change:.2f}")
print(f"- Percentage change: {percentage_change:.2f}%")

# Additional overall statistics
print(f"\nOverall Period Statistics (2023-2025):")
print(f"- Total trading days: {len(tencent)}")
print(f"- Starting price (2023): ${float(close_prices.iloc[0]):.2f}")
print(f"- Ending price (2025): ${float(close_prices.iloc[-1]):.2f}")
overall_change = float(close_prices.iloc[-1]) - float(close_prices.iloc[0])
overall_percentage = ((float(close_prices.iloc[-1]) / float(close_prices.iloc[0])) - 1) * 100
print(f"- Overall price change: ${overall_change:.2f}")
print(f"- Overall percentage change: {overall_percentage:.2f}%")

# Performance comparison: career period vs overall period
if overall_percentage != 0:
    relative_performance = (percentage_change - overall_percentage) / abs(overall_percentage) * 100
    print(f"\nPerformance Comparison:")
    print(f"- Career period performance relative to overall: {relative_performance:.1f}% better/worse")