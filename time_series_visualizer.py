import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates= ['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    plt.plot(df.index, df['value'], color='red')  # Plot the data

    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')  # Set the title

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace = True)

    df_bar["Year"] = df_bar["date"].dt.year
    df_bar["Month"] = df_bar["date"].dt.month


    df_bar = df_bar.groupby(["Year", "Month"]).mean()
    df_bar.reset_index().pivot(index='Year', columns='Month', values='value').plot(kind='bar')
    plt.xlabel("Years")
    plt.ylabel('Average Page Views') 
    plt.title('Average Daily Page Views, Grouped by Month and Year')

    # Save image and return fig (don't change this part)
    fig = plt.gcf()
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months)

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(18,6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df_box['year'], y=df_box['value']).get_figure()
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df_box['month'], y=df_box['value']).get_figure()
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
     
