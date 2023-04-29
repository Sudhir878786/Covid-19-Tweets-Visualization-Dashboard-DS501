import streamlit as st
import plotly.graph_objects as go

import pandas as pd

TITLE = 'Sentiment Comparison'
X_AXIS_TEXT = 'Date'
Y_AXIS_TEXT = 'Tweet Count'
LINE_WIDTH = 3

X_AXIS_GRID = False
Y_AXIS_GRID = True

POS_LINE_COLOR = 'rgb(67,230,167)'
NEG_LINE_COLOR = 'rgb(230,100,120)'
NEU_LINE_COLOR = 'rgb(167,167,167)'
TEXT_COLOR = 'rgb(200,200,200)'
PLOT_BG_COLOR = 'rgb(240,240,240)'
LEGEND_BACKG_COLOR = 'rgb(100,110,120)'

POS_HOVER_TEXT_BACKG_COLOR = "teal"
NEG_HOVER_TEXT_BACKG_COLOR = "crimson"
NEU_HOVER_TEXT_BACKG_COLOR = "slategrey"
ALL_HOVER_TEXT_BACKG_COLOR = "silver"


def area_plot(theme, height=650, width=850):
    day_data = pd.read_csv('day_wise.csv')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=day_data['Date'], y=day_data['Positive'], fill='tozeroy', name='Positive'))
    fig.add_trace(go.Scatter(x=day_data['Date'], y=day_data['Negative'], fill='tozeroy', name='Negative'))
    fig.add_trace(go.Scatter(x=day_data['Date'], y=day_data['Neutral'], fill='tozeroy', name='Neutral'))
    fig.add_trace(
        go.Scatter(x=day_data['Date'], y=day_data['Somewhat Positive'], fill='tozeroy', name='Somewhat Positive'))
    fig.add_trace(
        go.Scatter(x=day_data['Date'], y=day_data['Somewhat Negative'], fill='tozeroy', name='Somewhat Negative'))
    # fig.add_trace(go.Scatter(x=date_data['Date'],y=date_data['Tweet Count'],fill='tozeroy'))
    fig.update_layout(template=theme, height=height, width=width)
    fig.update_layout(title=TITLE,
                      xaxis_title=X_AXIS_TEXT,
                      yaxis_title=Y_AXIS_TEXT,
                      xaxis=dict(showgrid=X_AXIS_GRID, ),
                      yaxis=dict(showgrid=Y_AXIS_GRID),
                      xaxis_range=['2020-02-28', '2022-06-28'],
                      template=theme,
                      font=dict(
                          family="Courier New, monospace",
                          size=18,
                          color=TEXT_COLOR if theme == 'plotly_dark' else 'black'
                      ),
                      showlegend=True,
                      legend_title_text='Sentiment',
                      legend=dict(x=0,
                                  y=1,
                                  traceorder="normal",
                                  font=dict(
                                      family="sans-serif",
                                      size=13,
                                      color="black"),
                                  bgcolor=LEGEND_BACKG_COLOR if theme == 'plotly_dark' else 'white',
                                  bordercolor="beige",
                                  borderwidth=1
                                  ),
                      height=height,
                      width=width,
                      plot_bgcolor=PLOT_BG_COLOR if theme == 'plotly' else 'rgb(25,25,25)',
                      margin=dict(
                          l=50,
                          r=50,
                          b=100,
                          t=100,
                          pad=4
                      ),
                      hovermode='x',
                      hoverlabel=dict(
                          font_size=16,
                      ),
                      )
    st.plotly_chart(fig)


def main(theme, height, width):
    area_plot(theme, height, width)


if __name__ == '__main__':
    main()
