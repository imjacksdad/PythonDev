##Loading CSV data from the filesystem

import pandas as pd
import numpy as np


##df = pd.read_csv(
##    "C:/Python39/DEVFiles/PythonDev/Support Files/GAVPOS.csv", 
##    # if your dataset doesn't have column names in the first row, you need to specify them like this
##    #header=0, names=["Rank", "NOC", "Gold", "Silver", "Bronze", "Total"]
##)
##
###print(df.info)
##
##print(df)
##
### after loading, we can explore the data in all different ways pandas support
###df = df.sort_values('PSNAME', ascending=False)




df_list = pd.read_html(
    "https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table", 
    match="2016 Summer Olympics medal table"
)

# Note - read_html() returns list of DataFrames!
df = df_list[0]

# Just for fun, let's create a simple visualization

import plotly.express as px

# Take first 35 countries and reverse (this way plotly will render the best country first)
plot_data = df.head(35)[::-1]

medals = px.bar(plot_data, x=["Gold", "Silver", "Bronze"], y="NOC")
medals.update_layout(
    title_text="2016 Olympics results",
    xaxis_title_text="Medals won",
    yaxis_title_text="Country",
    legend_title_text="",
    height=650
)
medals.update_layout()
medals.update_traces(marker_color="#FFD700", selector=0)
medals.update_traces(marker_color="#C0C0C0", selector=1)
medals.update_traces(marker_color="#CD7F32", selector=2)
medals.show()
