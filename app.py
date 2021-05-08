import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

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
                    title='2020 Arrests by Race and Gender')
mvs_fig = px.bar(df_keene_mvs2020,
                 x='Gender', y='Total Warnings and Citations', color='Race',
                 title='2020 Motor Vehicle Citations and Warnings')
stops_fig = px.bar(df_keene_stops2020,
                   x='Gender', y='Number of Stops', color='Race',
                   title='2020 Subject Stops')
keene_pop_fig = px.bar(df_keene_census,
                   x='Year', y='Population', color='Race',
                   title='Keene, NH Demographic Data')
cheshire_pop_fig = px.bar(df_cheshire_census,
                   x='Year', y='Population', color='Race',
                   title='Cheshire County Demographic Data')
nh_pop_fig = px.bar(df_nh_census,
                   x='Year', y='Population', color='Race',
                   title='New Hampshire Demographic Data')

# Render app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='2020 Keene, NH Policing Data'),

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
        )
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)
