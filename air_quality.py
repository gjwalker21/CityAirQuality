import pandas as pd
from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px



connect()  # Initialize connection to preswald.toml data sources
df = get_df("AQ")  # Load data

sql = "SELECT * FROM AQ ORDER BY Date ASC, CO ASC"
filtered_df = query(sql, "AQ")
text("# Air Quality per City")
table(filtered_df, title="Filtered Data")
text("# Carbon Monoxide Levels per city")
fig = px.scatter(filtered_df, x="Date",y="CO",color="City")
plotly(fig)
