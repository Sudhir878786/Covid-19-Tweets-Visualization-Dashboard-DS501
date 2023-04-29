import streamlit as st
import plotly.graph_objects as go

import pandas as pd

TITLE = 'Daily Sentiment Analysis'
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

day_wise = pd.read_csv('day_wise.csv')


def positive(fig):
    fig.add_trace(go.Scatter(x=day_wise['Date'], y=day_wise['Positive'],
                             name='Positive Tweets',
                             mode='lines+markers',
                             line=dict(width=LINE_WIDTH, color=POS_LINE_COLOR)))

    fig.update_layout(hoverlabel=dict(
        bgcolor=POS_HOVER_TEXT_BACKG_COLOR,
    ))


def negative(fig):
    fig.add_trace(go.Scatter(x=day_wise['Date'], y=day_wise['Negative'],
                             name='Negative Tweets',
                             mode='lines+markers',
                             line=dict(width=LINE_WIDTH, color=NEG_LINE_COLOR)))

    fig.update_layout(hoverlabel=dict(
        bgcolor=NEG_HOVER_TEXT_BACKG_COLOR,
    ))


def neutral(fig):
    fig.add_trace(go.Scatter(x=day_wise['Date'], y=day_wise['Neutral'],
                             name='Neutral Tweets',
                             mode='lines+markers',
                             line=dict(width=LINE_WIDTH, color=NEU_LINE_COLOR)))

    fig.update_layout(hoverlabel=dict(
        bgcolor=NEU_HOVER_TEXT_BACKG_COLOR,
    ))


def main(theme='plotly_dark', height=650, width=850, sentiment_picker='All'):
    fig = go.Figure()

    global TEXT_COLOR, LEGEND_BACKG_COLOR, NEU_LINE_COLOR, POS_LINE_COLOR, NEG_LINE_COLOR, PLOT_BG_COLOR
    if theme == 'plotly':
        TEXT_COLOR = 'rgb(80,80,80)'
        LEGEND_BACKG_COLOR = 'rgb(200,210,220)'
        NEU_LINE_COLOR = 'rgb(97,97,97)'
        POS_LINE_COLOR = 'rgb(42,128,97)'
        NEG_LINE_COLOR = 'rgb(229,57,53)'
        PLOT_BG_COLOR = 'rgb(240,240,240)'
        theme = 'plotly'

    # For dark mode
    else:
        POS_LINE_COLOR = 'rgb(67,230,167)'
        NEG_LINE_COLOR = 'rgb(230,100,120)'
        NEU_LINE_COLOR = 'rgb(167,167,167)'
        TEXT_COLOR = 'rgb(200,200,200)'
        LEGEND_BACKG_COLOR = 'rgb(100,110,120)'
        PLOT_BG_COLOR = 'rgb(16,16,16)'
        theme = 'plotly_dark'

    # sentiment_picker = st.selectbox(label='Sentiment displayed',
    #                                options=('Positive', 'Negative', 'Neutral', 'All'),
    #                                index=0)
    # Adding a blank line after sentiment picker
    st.markdown('<br>', unsafe_allow_html=True)
    if sentiment_picker == 'Positive':
        positive(fig)

    elif sentiment_picker == 'Negative':
        negative(fig)

    elif sentiment_picker == 'Neutral':
        neutral(fig)

    else:
        positive(fig)
        negative(fig)
        neutral(fig)
        fig.update_layout(hoverlabel=dict(
            bgcolor=ALL_HOVER_TEXT_BACKG_COLOR,
        ))

    fig.update_layout(title=TITLE,
                      xaxis_title=X_AXIS_TEXT,
                      yaxis_title=Y_AXIS_TEXT,
                      xaxis=dict(showgrid=X_AXIS_GRID,),
                      yaxis=dict(showgrid=Y_AXIS_GRID),
                      xaxis_range=['2020-02-28', '2020-06-28'],
                      template=theme,
                      font=dict(
                          family="Courier New, monospace",
                          size=18,
                          color=TEXT_COLOR
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
                                  bgcolor=LEGEND_BACKG_COLOR,
                                  bordercolor="beige",
                                  borderwidth=1
                                  ),
                      height=height,
                      width=width,
                      plot_bgcolor=PLOT_BG_COLOR,
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
    # fig.update_xaxes(rangeslider_visible=True)

    fig.update_traces(hovertemplate='Tweets: %{y}')
    return st.plotly_chart(fig)
    # plot()


if __name__ == '__main__':
    main()
