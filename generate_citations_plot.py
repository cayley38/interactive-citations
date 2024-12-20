import pandas as pd
import plotly.graph_objects as go


Year = [2013 , 2014 , 2015 , 2016 , 2017 , 2018 , 2019 , 2020 , 2021 , 2022 , 2023 , 2024 ]
Citations_SCOPUS = [  4 , 4 , 11 , 13 , 25 , 21 , 32 , 47 , 46 , 68 , 57 , 111 ]
Citations_ADS = [  4 ,4 , 10 , 14 , 25 , 24 , 59 , 51 , 52 , 73 , 76 , 147 ]
Citations_Google_scholar = [  6 ,4 , 15 , 13 , 28 , 18 , 45 , 55 , 58 , 82 , 108 , 161 ]



# Create the interactive plot with filtered data
fig_filtered = go.Figure()


# Add Google Scholar data to the plot
fig_filtered.add_trace(go.Bar(
    x=Year,
    y=Citations_SCOPUS,
    name='SCOPUS',
    marker=dict(color='red')
))

# Add ADS data to the plot
fig_filtered.add_trace(go.Bar(
    x=Year,
    y=Citations_ADS,
    name='ADS',
    marker=dict(color='blue')
))

# Add Google Scholar data to the plot
fig_filtered.add_trace(go.Bar(
    x=Year,
    y=Citations_Google_scholar,
    name='Google scholar',
    marker=dict(color='green')
))


# Customize layout without a legend title and borders
fig_filtered.update_layout(
    xaxis_title="Year",
    yaxis_title="Citations per year",
    barmode='group',
    legend=dict(
        x=0.02,  # Horizontal position (close to the left edge)
        y=0.95,  # Vertical position (top of the plot)
        bgcolor="rgba(255,255,255,0.5)"  # Semi-transparent background, no border
    ),
    template="simple_white"
)

# Save the updated plot as an interactive HTML file
fig_filtered.write_html("citations-plot-file.html")
print("Interactive plot saved as 'citations_plot.html'")
