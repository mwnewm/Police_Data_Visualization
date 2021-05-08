import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Set variables
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
githublink = 'https://github.com/mwnewm/Police_Data_Visualization'
datasourcelink = 'https://ci.keene.nh.us/police/news-public-information-faqs'
tabtitle = 'Keene Policing Data'
pagetitle = '2020 Keene, NH Policing Data'

# Import data to pandas dataframe
df_keene_arrests2020 = pd.read_csv('data/KeeneDataCSV_arrests.csv', skiprows=None)
df_keene_mvs2020 = pd.read_csv('data/KeeneDataCSV_MVS.csv', skiprows=None)
df_keene_stops2020 = pd.read_csv('data/KeeneDataCSV_subjectstops.csv', skiprows=None)
df_keene_census = pd.read_csv('data/KeeneCensusData.csv', usecols=['Race', 'Year', 'Population', 'share'], skiprows=None)
df_cheshire_census = pd.read_csv('data/CheshireCensusData.csv', usecols=['Race', 'Year', 'Population'], skiprows=None)
df_nh_census = pd.read_csv('data/NewHampshireCensusData.csv', usecols=['Race', 'Year', 'Population'], skiprows=None)

# Construct figures with plotly
arrest_fig = px.bar(df_keene_arrests2020,
                    x='Gender', y='Number of Arrests', color='Race',
                    title='2020 Arrests by Race and Gender', custom_data=['Race'])
mvs_fig = px.bar(df_keene_mvs2020,
                 x='Gender', y='Total Warnings and Citations', color='Race',
                 title='2020 Motor Vehicle Citations and Warnings', custom_data=['Race'])
stops_fig = px.bar(df_keene_stops2020,
                   x='Gender', y='Number of Stops', color='Race',
                   title='2020 Subject Stops', custom_data=['Race'])
keene_pop_fig = px.bar(df_keene_census,
                   x='Year', y='Population', color='Race',
                   title='Keene, NH Demographic Data', custom_data=['Race'])
cheshire_pop_fig = px.bar(df_cheshire_census,
                   x='Year', y='Population', color='Race',
                   title='Cheshire County Demographic Data', custom_data=['Race'])
nh_pop_fig = px.bar(df_nh_census,
                   x='Year', y='Population', color='Race',
                   title='New Hampshire Demographic Data', custom_data=['Race'])

# Update hover tools
for fig in [arrest_fig, mvs_fig, stops_fig]:
    fig.update_traces(
        hovertemplate="<br>".join([
            "Number of Arrests: %{y}",
            "Race: %{customdata[0]}"
        ])
    )

for fig in [keene_pop_fig, cheshire_pop_fig, nh_pop_fig]:
    fig.update_traces(
        hovertemplate="<br>".join([
            "Population: %{y}",
            "Race: %{customdata[0]}"
        ])
    )

# Render app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

app.layout = html.Div(children=[
    html.H1(children=pagetitle),

    html.Div(children=[
        html.Div(children=[
            dcc.Graph(
                id='keene-arrest-graph',
                figure=arrest_fig
            ),
            dcc.Graph(
                id='keene-census',
                figure=keene_pop_fig
            )],
        style={'columnCount': 2}),

        html.Div(children=[
            dcc.Graph(
                id='keene-mvs-graph2',
                figure=mvs_fig
            ),
            dcc.Graph(
                id='cheshire-census',
                figure=cheshire_pop_fig
            )],
            style={'columnCount': 2}
        ),
        html.Div(children=[
            dcc.Graph(
                id='keene-stops-graph',
                figure=stops_fig
            ),
            dcc.Graph(
                id='nh-census',
                figure=nh_pop_fig
            )],
            style={'columnCount': 2}
        ),

        html.Div(children=[
            html.H4(children=
                    html.A('Code on Github', href=githublink)
                    ),
            html.H4(children=
                    html.A('Data Source', href=datasourcelink)
                    )
        ]),
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)
