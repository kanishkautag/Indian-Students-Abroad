import pandas as pd
import folium
from folium.plugins import HeatMap
from shiny import App, ui, render

# Load the data
data = pd.read_csv(r"indian_students_final.csv")

app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.link(rel="stylesheet", href="/static/style.css")
    ),
    ui.div(
        ui.h2("Indian Students Heatmap"),
        class_="container"
    ),
    ui.output_ui("map"),
    ui.div(
        ui.p("This heatmap shows the distribution of Indian students across different locations. The size of the heatmap points is proportional to the number of students."),
        class_="footer"
    )
)

def server(input, output, session):
    @output
    @render.ui
    def map():
        # Create a Folium map centered on the mean latitude and longitude
        m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=2)
        
        # Add a heatmap layer
        heat_data = [[row['Latitude'], row['Longitude'], row['No of Indian Students']] for index, row in data.iterrows()]
        HeatMap(heat_data).add_to(m)
        
        # Ensure only one map is displayed by clearing any previous output
        return ui.HTML(m._repr_html_())

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
