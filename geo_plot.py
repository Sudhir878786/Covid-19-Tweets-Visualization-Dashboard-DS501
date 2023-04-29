import streamlit as st
import pydeck as pdk

import pandas as pd


def main(theme):
    df = pd.read_csv('sentimentcount.csv')

    view = pdk.data_utils.compute_view(df[["lng", "lat"]])
    view.pitch = 40
    view.bearing = 60

    column_layer = pdk.Layer(
        "ColumnLayer",
        data=df,
        get_position=["lng", "lat"],
        get_elevation="no_neut_sent",
        elevation_scale=15,
        radius=20000,
        get_fill_color=[255, 140, 0] if theme == 'plotly' else [100, 100, 200] if theme == 'plotly_dark' else [70, 102,
                                                                                                               255],
        pickable=True,
        auto_highlight=True,
    )

    tooltip = {
        "html": "<b>{City}</b>  {States/UT}<br>"
                "<b>{no_pos_sent}</b> Positive tweets<br>"
                "<b>{no_neg_sent}</b> Negative tweets<br>"
                "<b>{no_neut_sent}</b> Neutral tweets<br>",
        "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
    }

    view_state = pdk.ViewState(
        longitude=85.9629,
        latitude=20.5937,
        zoom=3.9,
        min_zoom=3.5,
        max_zoom=6.5,
        pitch=50,
        bearing=-10)

    r = pdk.Deck(
        column_layer, initial_view_state=view_state, tooltip=tooltip,
        map_style="mapbox://styles/mapbox/light-v9" if theme == 'plotly' else "mapbox://styles/mapbox/dark-v9"
        if theme == 'plotly_dark' else "mapbox://styles/mapbox/satellite-v9",
    )
    st.pydeck_chart(r)


if __name__ == '__main__':
    main()
