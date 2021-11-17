import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# write markdowns for the streamlit app

st.markdown('# Pakistan Covid-19 Analysis')

image = Image.open('covid19 image.jpg')

st.image(image)

st.markdown('''** A novel coronavirus (2019-nCoV) is a new coronavirus that has not been previously identified. Coronavirus disease
                (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus. Coronaviruses are a large family of viruses, some causing                 illness in people and others that circulate among animals, including camels, cats and bats. This outbreak started in the month of December 2019,  as an unknown cluster of respiratory illnesses first reported from Wuhan City, China.**''')

st.markdown('''**The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, 
            speak, sing or breathe. These particles range from larger respiratory droplets to smaller aerosols.
            You can be infected by breathing in the virus if you are near someone who has COVID-19, or by touching
            a contaminated surface and then your eyes, nose or mouth. The virus spreads more easily indoors and in 
            crowded settings.**''')

# Sidebars

st.sidebar.header('Exploratory Data Analysis')

st.sidebar.markdown('## Side Panel')

st.sidebar.markdown('Use this panel to explore the datasets')

# Covid-19 dataset

df = pd.read_csv('csse_covid19_daily_reports_cleaned.csv')

# Explore Dataset

# set the title

st.title('Explore the dataset')

st.sidebar.subheader('Pakistan Covid-19 Dataset')

# set the markdowns

st.markdown('Tick the check box on side panel to explore the dataset')

st.markdown('The dataset is taken from the Github repository of Center for Systems Science and Engineering (CSSE) at Johns Hopkins University.')

st.markdown('This dataset for pakistan is from 11-July-2020 to 05-August-2021 ')

if st.sidebar.checkbox('Get to know about the data'):
    
    #covid19 dataset first few rows
    
    if st.sidebar.checkbox('Covid-19 Dataset first few rows'):
        
        st.subheader('Displaying the first few rows of dataset')
        
        st.write(df.head())
        
    # Rows and columns of dataset
        
    if st.sidebar.checkbox('Rows and Columns of Dataset'):
        
        st.subheader('The Number of rows and columns are:')
        
        st.write('The number of rows are', df.shape[0], 'and the number of columns are', df.shape[1])
        
    # show columns    
   
    if st.sidebar.checkbox('Show Columns'):
        
        st.subheader('The Columns this dataset contains are')
        
        st.write(df.columns)
        
    # summary statistics
        
    if st.sidebar.checkbox('Summary statistics of dataset'):
        
        st.subheader('The summary statistics of numerical columns are')
        
        st.write(df.describe())
    
    # Province wise data
    
    if st.sidebar.checkbox('Province Wise Data'):
        
        st.subheader('The Province wise data which shows confirmed, deaths, recovered and active cases to the date of 05-Aug-2021 is')
        
        p_w = df.set_index('updated_dates').loc['2021-08-05'][['Province', 'confirmed', 'deaths', 'recovered', 'active']]
        
        st.write(p_w)
        
        fig,ax = plt.subplots()
        
        p_w.plot.bar('Province',['confirmed', 'deaths', 'recovered', 'active'], ax = ax)
        
        st.write(fig)

    # correlation and its plot        
        
    if st.sidebar.checkbox('Correlation of Variables'):
        
        st.subheader('Correlation of Confirmed, Deaths, Recovered, Active, Incident and Fatality variables are:')
        
        corr = df[['confirmed', 'deaths', 'recovered', 'active', 'incident', 'fatality']].corr()
        
        st.write(corr)
        
        fig,ax = plt.subplots()
        
        sns.heatmap(corr, annot = True, ax = ax)
        
        st.write(fig)
        
# Plots of correlated variables

st.sidebar.subheader('Visualize the Correlated Variables')

if st.sidebar.checkbox('Visualize'):
    
    st.title('Visualize the correlated variables')
    
    if st.sidebar.checkbox('Confirmed Cases and Deaths'):
            
        fig, ax = plt.subplots()
        
        sns.lineplot(x = 'deaths', y = 'confirmed', data = df, hue =  'Province')
        plt.title('Confirmed cases and Deaths')
            
        st.write(fig)
        
    if st.sidebar.checkbox('Recovered and Confirmed Cases'):
        
        fig,ax = plt.subplots()
        
        sns.lineplot(x = 'recovered', y = 'confirmed', data = df, hue =  'Province')
        plt.title('Recovered and Confirmed cases')
        
        st.write(fig)
        
    if st.sidebar.checkbox('Confirmed and active cases Cases'):
        
        fig,ax = plt.subplots()
        
        sns.lineplot(x = 'confirmed', y = 'active', data = df, hue =  'Province')
        plt.title('Confirmed cases and Active Cases')
        
        st.write(fig)
        
        
    if st.sidebar.checkbox('Recovered and Deaths'):
        
        fig,ax = plt.subplots()
        
        sns.lineplot(x = 'deaths', y = 'recovered', data = df, hue =  'Province')
        plt.title('Recovered and Deaths')
        
        st.write(fig)
        
        
    if st.sidebar.checkbox('Recovered and active'):
        
        fig,ax = plt.subplots()
        
        sns.lineplot(x = 'recovered', y = 'active', data = df, hue =  'Province')
        plt.title('Recovered and active')
        
        st.write(fig)
    
    if st.sidebar.checkbox('Deaths and Active'):
        
        fig,ax = plt.subplots()
        
        sns.lineplot(x = 'deaths', y = 'active', data = df, hue =  'Province')
        plt.title('Deaths and Active')
        
        st.write(fig)

# Pakistan Economy dataset

pak_economy = pd.read_csv('Pakistan economic and unemployment data cleaned.csv')

st.title('Pakistan Economical Condition and Unemployment Dataset')

st.markdown('''These datasets are taken from World bank, World Development Indicators data bank. It contains the data of 
            consumer price index (CPI), Gross Domestic Product (GDP) and Unemployment of Pakistan from the year 1991 to 2020''')

st.sidebar.subheader('Pakistan Economic and Unemployment Dataset')

if st.sidebar.checkbox('Get to Know about the data'):
    
    # first few rows
    
    if st.sidebar.checkbox('View the First few rows of dataset'):
         
        st.write(pak_economy.head())
    
    # Check rows and columns
    
    if st.sidebar.checkbox('Check Rows and Columns'):
            
        st.write('There are', pak_economy.shape[0], 'rows and', pak_economy.shape[1], 'columns')
    
    # Check summary statistics
    
    if st.sidebar.checkbox('Summary statistics'):
        
        st.write(pak_economy.describe())
        
    if st.sidebar.checkbox('Correlation Matrix'):
        
        corr = pak_economy.corr()
        
        st.write(corr)
        
        fig,ax = plt.subplots()
        
        sns.heatmap(corr, annot = True, ax = ax)
        
        st.write(fig)
        
# Visualize the Trend

st.sidebar.subheader('Visualize the Trend')

if st.sidebar.checkbox('Visualize economy trend'):
    
    st.title('Visualize the Pakistan economy and unemployment trends')
    
    st.markdown('''According to investopedia definition of GDP, Economists traditionally use gross domestic product (GDP) to 
    measure economic progress. If GDP is rising, the economy is in solid shape, and the nation is moving forward. 
    On the other hand, if gross domestic product is falling, the economy might be in trouble, and the nation is losing ground.
    As we see the data trend from 1991 to 2020, the GDP starts to from 2019 when Covid19 pandemic arises, which highly 
    impact the economy of pakistan. Unemployment rate increasing with the passage of time, specially after the covid19 pandemic 
    it increased.''')
    
    # Consumer price index
    
    if st.sidebar.checkbox('Consumer Price Index (CPI)'):
        
        fig,ax = plt.subplots(figsize = (20,15))
        
        sns.set_style('darkgrid')
        
        sns.barplot(ax = ax, x = pak_economy['Year'], y = pak_economy['CPI Value'])
        
        plt.title('Inflation, consumer prices (annual %)')
        
        st.write(fig)
        
        # Gross domestic product
        
    if st.sidebar.checkbox('Gross Domestic Product (GDP)'):
        
        fig,ax = plt.subplots(figsize = (20,15))
        
        sns.set_style('darkgrid')
        
        sns.barplot(ax = ax, x = pak_economy['Year'], y = pak_economy['GDP value'])
        
        plt.title('GDP growth (annual %)')
        
        st.write(fig)
        
        # Unemployment rate
        
    if st.sidebar.checkbox('Unemployment Rate'):
        
        fig,ax = plt.subplots(figsize = (20,15))
        
        sns.set_style('darkgrid')
        
        sns.barplot(ax = ax, x = pak_economy['Year'], y = pak_economy['Unemployment rate'])
        
        plt.title('Unemployment, total (% of total labor force) (modeled ILO estimate)')
        
        st.write(fig)
        
        
# Data Sources

st.sidebar.subheader('Data Sources')

st.sidebar.info('[Covid-19 Dataset] (https://github.com/CSSEGISandData/COVID-19) | [Pakistan Economy Dataset](https://data.worldbank.org/)')
