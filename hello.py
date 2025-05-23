from preswald import text, plotly, connect, get_df, table, slider, checkbox, dropdown, radio, query
import pandas as pd
import plotly.express as px

text("# Welcome to Preswald!")
text("This is your first app. 🎉")

# Load the CSV dataset of student-scores
connect()
df = get_df('student-scores')
print(df.head())

# SQL: Query manipulation
sql = "SELECT * from student-scores where ABSENCE_DAYS > 5"
filtered_df = query(sql, "student-scores")
table(filtered_df, title="Students with more than 5 Absence Days")

# Building interactive UI
text(" # My Data Analysis App")
table(filtered_df, title="Filtered Data")

# Adding user controls
threshold = slider("Threshold", min_val = 0, max_val = 100, default = 50)
table(df[df["ABSENCE_DAYS"] > threshold], title = "Dynamic Data View")

# Creating Visualization 
fig = px.scatter(df, x="FIRST_NAME", y="ABSENCE_DAYS", color = "FIRST_NAME", title = "Absence by Students")
plotly(fig)

# Create a scatter plot
fig = px.scatter(df, x='FIRST_NAME', y='ABSENCE_DAYS', text='FIRST_NAME',
                 title='FIRST_NAME vs. ABSENCE_DAYS',
                 labels={'FIRST_NAME': 'FIRST_NAME', 'ABSENCE_DAYS': 'ABSENCE_DAYS'})

# Add labels for each point
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))

# Style the plot
fig.update_layout(template='plotly_white')

# Show the plot
plotly(fig)

# Show the data
table(df)