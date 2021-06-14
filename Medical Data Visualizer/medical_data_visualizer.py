import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['bmi'] = df['weight']/((df['height']/100)**2)
df['overweight'] = 0
df.loc[df['bmi']>25,'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
def normalize(col:str):
    df[col] = df[col].map(lambda x: 0 if x==1 else 1)
    return

normalize("cholesterol")
normalize("gluc")

df = df.loc[:,[i for i in df.columns if i!="bmi"]]

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    melt_cols = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df, ['id', 'cardio'], melt_cols ,"variable","value")

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['variable','value', 'cardio']).count().reset_index().rename(columns={'id':'total'})

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot('variable', 'total','value', col='cardio',data=df_cat, kind='bar')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_lo']<=df['ap_hi']) &
                    (df['height'] >= df['height'].quantile(0.025)) &
                    (df['height'] < df['height'].quantile(0.975)) &
                    (df['weight'] >= df['weight'].quantile(0.025)) &
                    (df['weight'] < df['weight'].quantile(0.975))]


    # Calculate the correlation matrix
    corr =  df_heat.corr().round(1)

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots()
    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, annot=True, mask=mask, vmin=-0.08, vmax=0.24, center=0, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


df_heat = df.loc[(df['ap_lo']<=df['ap_hi']) &
                (df['height'] >= df['height'].quantile(0.025)) &
                (df['height'] <= df['height'].quantile(0.975)) &
                (df['weight'] >= df['weight'].quantile(0.025)) &
                (df['weight'] <= df['weight'].quantile(0.975))]

