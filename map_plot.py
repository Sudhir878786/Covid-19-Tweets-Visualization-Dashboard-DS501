import streamlit as st
import pandas as pd

import plotly.graph_objects as go

# read the state wise shapefile of India in a GeoDataFrame and preview it
import geopandas as gpd

map_data = gpd.read_file('Indian_States.shp')  # Please Change the Location of the Shape Files before Running this Code.
map_data.rename(columns={'st_nm': 'States/UT'}, inplace=True)

# correcting the names of states in the map dataframe

map_data['States/UT'] = map_data['States/UT'].str.replace('&', 'and')
map_data['States/UT'].replace('Arunanchal Pradesh', 'Arunachal Pradesh', inplace=True)
map_data['States/UT'].replace('Telangana', 'Telengana', inplace=True)
map_data['States/UT'].replace('NCT of Delhi', 'Delhi', inplace=True)

# read the City wise Number of Positive, Negative and Neutral Sentiments

tempdf = pd.read_csv('sentimentcount.csv')  # Please the File location before reading the Data from the csv file.
tempdf = pd.merge(map_data, tempdf, how='right', on='States/UT')
tempdf.drop(['Unnamed: 0'], axis=1, inplace=True)


# Enter your own mapbox Access Token.
def main(theme='plotly_dark', height=650, width=850):
    mapbox_access_token = 'pk.eyJ1IjoiYWFkaXR5YWthcG9vcjA2IiwiYSI6ImNrYzFxZDJpajB3MGUyd29lbWVpYTZiaTIifQ.ovRxBQm9ZxvBSrk5VGNngg'

    fig = go.Figure(go.Scattermapbox(
        lat=tempdf.lat,
        lon=tempdf.lng,
        customdata=tempdf.loc[:,
                   ['City', 'no_pos_sent', 'no_som_pos_sent', 'no_neg_sent', 'no_som_neg_sent', 'no_neut_sent']],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        # hoverinfo='text',
        # hovertext = merged_data[['no_pos_sent','no_neg_sent','no_neut_sent']],
        hovertemplate=
        "<b>%{customdata[0]} </b><br><br>" +
        "longitude: %{lon}<br>" +
        "latitude: %{lat}<br>" +
        "Pos Sentiment: %{customdata[1]}<br>" +
        "Some Pos Sentiment: %{customdata[2]}<br>" +
        "Neg Sentiment: %{customdata[3]}<br>" +
        "Some Neg Sentiment: %{customdata[4]}<br>" +
        "Neut Sentiment: %{customdata[5]}<br>",
        # showlegend=True
        # text=cty,
    ))

    if theme == 'plotly_dark':
        theme = 'dark'
    else:
        theme = 'light'
    fig.update_layout(
        autosize=False,
        margin={"r": 10, "t": 10, "l": 10, "b": 10},
        width=width,
        height=height,
        hovermode='closest',
        mapbox=dict(
            style=theme,
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=20.5937,
                lon=78.9629
            ),
            pitch=0,
            zoom=3.5
        ),
    )

    # Figure.plt(Figsize=(8,8))
    return st.plotly_chart(fig)


if __name__ == '__main__':
    main()