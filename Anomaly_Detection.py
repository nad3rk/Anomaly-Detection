from __future__ import division
from anom_detect import anom_detect
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# %matplotlib inline (only used for if Jupyter is used)

# Load Text file as DataFrame (Acceleration Sensor Data)
df = pd.read_csv(r"D:\Users\Nader\OneDrive\Dokumente\HSRW\System_Simulation\AnomalyDetection\AnomalyDetection\AnomalyDetection\Data\AccData.csv", delimiter =',')

# Print the Head of the data (5 rows)
df.head()

# Column names
list(df)

# Have a look at the size of the DataSet (Rows x Columns)
df.shape

# General statistic (mean, std etc.)
df.describe()

# Check if all numeric and non-null
df.info()

# Filter and print only two variables (standard data) for plotting (see plot_data() function)
dfs = df[["Time (s)", "Total Acceleration (g)"]]
dfs.head()

# Filter Dataset and change column names
df = df[["Time (s)", "Total Acceleration (g)"]]
df.columns = ['time', 'Acceleration']
df.head()

# Set the column "time" as index of the dataframe
df = df.set_index('time')
df.head()

# Class with Parameters method, window, max_ouliers, alpha, mode, 
an = anom_detect(alpha=0.3)

df = dfse
df.head()

an.evaluate(df)
#an.esd_test(df)

results = an.results
results.head()

anoma_points = an.anoma_points
#anoma_points.head()

plot_anomalies()

def edit_plot_data():
    dfse = dfs[6500:9100]
    dfse.info()
    dfse.describe()
    dfse.columns = ['time','Acceleration']
    dfse = dfse.set_index('time')
    dfse.info()
    dfse.head()
    print(dfse)


plot_data('Edited Dataset',df['Time (s)'], df['Total Acceleration (g)'])

def plot_data(Title, x_axis, y_axis):
    x = x_axis
    y = y_axis

    plt.title(Title)
    plt.xlabel('Time')
    plt.ylabel('Total Acceleration (g)')
    plt.xlim(left=13,right=18.74)
    plt.ylim(bottom=-17,top=5)
    plt.plot(x,y,label='Acceleration (g)')
    plt.legend();
    plt.show()

list(df)
df_anoms_pos = df[df['residual'] > df['pos_std_2']]
df_anoms_neg = df[df['residual'] < df['neg_std_2']]
print(df)
print(df_anoms_pos)
print(df_anoms_neg)

def plot_anomalies():
    plt.plot()
    plt.plot(list(df.index),df.iloc[:,0],'b.',label="Acceleration")
    plt.plot(list(df.index),df.mean_count,'r',label='Moving Average',linewidth=1.0)
    plt.fill_between(df.index,df.pos_std,df.neg_std,color='red',alpha=0.3,label='1Sigma')
    plt.fill_between(df.index,df.pos_std_2,df.neg_std_2,color='red',alpha=0.1,label='2Sigma')
    plt.plot(list(anoma_points.index),anoma_points.iloc[:,0],'g*',label='Anomalous Points')
    #plt.plot(list(df_anoms_pos.index),df_anoms_pos.iloc[:,0],'b+',label="Anoms")
    plt.xlabel('Time')
    plt.ylabel(data_label)
    plt.title('Data with Anomalies starred')
    #plt.xlim(left=6500,right=9100)
    #plt.ylim(bottom=-17,top=3)
    plt.legend();
    plt.show()


#an.normality()
def normality():
    if results is not None:
        df_results = results
        x = df.residual.values
        plt.hist(df.residual,bins=100);
        plt.title('Distribution of Residuals');
        plt.show()