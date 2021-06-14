import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data
df = df.loc[(df['value']>=df['value'].quantile(0.025)) &
            (df['value']<=df['value'].quantile(0.975))]

df['date'] = pd.to_datetime(df['date'])

def draw_line_plot():
    fig, ax = plt.subplots()
    ax.plot(df['date'],df['value'], c='red')
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = pd.DatetimeIndex(df['date']).month
    df_bar['year'] = pd.DatetimeIndex(df['date']).year

    df_bar = pd.DataFrame(df_bar.groupby(['year','month'])['value'].mean()).reset_index()
    month_list = ['January', 'February','March','April','May','June','July','August','September','October','November','December']
    num_list = [i for i in range(1,13)]
    month_dict = dict(zip(num_list,month_list))

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8,6))
    sns.barplot(df_bar['year'], df_bar['value'], df_bar['month'], ax=ax, palette='tab10')
    ax.legend(plt.gca().get_legend_handles_labels()[0], month_dict.values(), loc='upper left', title='Months')
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_numeric'] = [int(d.strftime('%m')) for d in df_box.date]
    df_box = df_box.sort_values(by='month_numeric')

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14,6))
    sns.boxplot(x='year',y='value',data=df_box, ax=ax[0])
    sns.boxplot(x='month',y='value',data=df_box, ax=ax[1])
    for x in [0,1]:
        ax[x].set_ylim((0,200000))
        ax[x].set_yticks([i for i in range(0,220000, 20000)])
        ax[x].set_ylabel("Page Views")
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[0].set_xlabel("Year")
    ax[1].set_xlabel("Month")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
