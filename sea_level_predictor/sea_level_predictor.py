import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import data
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10, label='Original Data')

    # 3. Create first line of best fit (using all data)
    # Get slope and intercept
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create an array of years from 1880 to 2050 for the prediction
    years_extended = pd.Series([i for i in range(1880, 2051)])
    # Formula: y = mx + b
    line1 = res.slope * years_extended + res.intercept
    plt.plot(years_extended, line1, 'r', label='Best Fit Line 1 (1880-2050)')

    # 4. Create second line of best fit (data from year 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create an array of years from 2000 to 2050
    years_recent = pd.Series([i for i in range(2000, 2051)])
    line2 = res_recent.slope * years_recent + res_recent.intercept
    plt.plot(years_recent, line2, 'green', label='Best Fit Line 2 (2000-2050)')

    # 5. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save image and return fig (for testing)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
