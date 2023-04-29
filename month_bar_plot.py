import streamlit as st
import plotly.graph_objects as go

import pandas as pd

TITLE = 'Monthly Sentiment Analysis'
X_AXIS = 'Month'
Y_AXIS = 'Tweet Count'
LINE_WIDTH = 3

POS_LINE_COLOR = 'rgb(67,230,167)'
NEG_LINE_COLOR = 'rgb(230,100,120)'
NEU_LINE_COLOR = 'rgb(167,167,167)'
SOM_POS_LINE_COLOR = 'lightskyblue'
SOM_NEG_LINE_COLOR = 'palevioletred'
TEXT_COLOR = 'rgb(200,200,200)'
LEGEND_BACKG_COLOR = 'rgb(100,110,120)'

POS_HOVER_TEXT_BACKG_COLOR = "teal"
NEG_HOVER_TEXT_BACKG_COLOR = "crimson"
NEU_HOVER_TEXT_BACKG_COLOR = "slategrey"
ALL_HOVER_TEXT_BACKG_COLOR = "silver"

# List of number of positive,negative and neutral sentiments
num_pos_tweets_mons=[17320,24901,17282,45726,33884]
num_som_pos_tweets_mons=[9984,13384,9185,26946,19835]
num_neg_tweets_mons=[9628,12315,9050,28333,19614]
num_som_neg_tweets_mons=[7160,8715,6092,19372,14082]
num_neut_tweets_mons=[24466,31275,21933,69854,73772]


# This Grpah is to show Month-wise number of Positive, Negative and Neutral Sentiments

months = ['Mar','Apr', 'May', 'Jun','Jul']   # List of Months

fig = go.Figure()   # Calling Figure Class

# Adding Traces

# Adding trace for Positive Sentiment
def positive(fig):
    fig.add_trace(go.Bar(
        x=months,
        y=num_pos_tweets_mons,
        name='Positive Sentiment',
        marker_color=POS_LINE_COLOR
    ))
    fig.update_layout(hoverlabel=dict(
        bgcolor=POS_HOVER_TEXT_BACKG_COLOR,
    ))

# Adding trace for Somewhat Positive Sentiment
def some_positive(fig):
    fig.add_trace(go.Bar(
        x=months,
        y=num_som_pos_tweets_mons,
        name='Somewhat Positive Sentiment',
        marker_color=SOM_POS_LINE_COLOR
    ))

# Adding trace for Negative Sentiment
def negative(fig):
    fig.add_trace(go.Bar(
        x=months,
        y=num_neg_tweets_mons,
        name='Negative Sentiment',
        marker_color=NEG_LINE_COLOR
    ))
    fig.update_layout(hoverlabel=dict(
        bgcolor=NEG_HOVER_TEXT_BACKG_COLOR,
    ))

# Adding trace for Somewhat Negative Sentiment
def some_negative(fig):    
    fig.add_trace(go.Bar(
        x=months,
        y=num_som_neg_tweets_mons,
        name='Somewhat Negative Sentiment',
        marker_color=SOM_NEG_LINE_COLOR
    ))

# Adding traces for Neutral Sentiment
def neutral(fig):
    fig.add_trace(go.Bar(
        x=months,
        y=num_neut_tweets_mons,
        name='Neutral Sentiment',
        marker_color=NEU_LINE_COLOR
    ))
    fig.update_layout(hoverlabel=dict(
        bgcolor=NEU_HOVER_TEXT_BACKG_COLOR,
    ))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
# Changed the background plot color of the graph as well as the paper to Black.
# Changed the font style , size and color. 

def plot(theme='plotly_dark'):
    pass


def main(theme='plotly_dark', height=650, width=850, sentiment_picker='All'):
    #st.title('IBM Hack Challenge 2020')
    fig = go.Figure()

    global TEXT_COLOR, LEGEND_BACKG_COLOR, NEU_LINE_COLOR, POS_LINE_COLOR, NEG_LINE_COLOR, SOM_POS_LINE_COLOR, SOM_NEG_LINE_COLOR,PLOT_BG_COLOR
    if theme == 'plotly':
        # global TEXT_COLOR, LEGEND_BACKG_COLOR, NEU_LINE_COLOR, POS_LINE_COLOR, NEG_LINE_COLOR
        TEXT_COLOR = 'rgb(100,100,100)'
        LEGEND_BACKG_COLOR = 'rgb(200,210,220)'
        NEU_LINE_COLOR = 'rgb(97,97,97)'
        POS_LINE_COLOR = 'rgb(42,128,97)'
        NEG_LINE_COLOR = 'rgb(229,57,53)'
        SOM_POS_LINE_COLOR = 'lightgreen' 
        SOM_NEG_LINE_COLOR = 'orange'
        PLOT_BG_COLOR = 'rgb(240,240,240)'
        theme = 'plotly'
        # st.write(LEGEND_BACKG_COLOR)
    else:
        POS_LINE_COLOR = 'rgb(67,230,167)'
        NEG_LINE_COLOR = 'rgb(230,100,120)'
        NEU_LINE_COLOR = 'rgb(167,167,167)'
        SOM_POS_LINE_COLOR = 'lightskyblue'
        SOM_NEG_LINE_COLOR = 'palevioletred'
        TEXT_COLOR = 'rgb(200,200,200)'
        LEGEND_BACKG_COLOR = 'rgb(100,110,120)'
        PLOT_BG_COLOR = 'rgb(16,16,16)'

        theme = 'plotly_dark'

    #sentiment_picker = st.selectbox(label='Pick sentiment for analysis data',
     #                               options=('Positive', 'Somewhat Positive', 'Negative', 'Somewhat Negative', 'Neutral', 'All'),
     #                               index=0)
    
    if sentiment_picker == 'Positive':
        positive(fig)

    elif sentiment_picker == 'Somewhat Positive':
        some_positive(fig)
    
    elif sentiment_picker == 'Negative':
        negative(fig)

    elif sentiment_picker == 'Somewhat Negative':
        some_negative(fig)

    elif sentiment_picker == 'Neutral':
        neutral(fig)

    else:
        positive(fig)
        some_positive(fig)
        negative(fig)
        some_negative(fig)
        neutral(fig)
        fig.update_layout(hoverlabel=dict(
            bgcolor=ALL_HOVER_TEXT_BACKG_COLOR,
        ))

    fig.update_layout(title=TITLE,
                      xaxis_title=X_AXIS,
                      yaxis_title=Y_AXIS,
                      barmode='group', xaxis_tickangle=-45,
                      # showgrid=False,
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
                                      size=12,
                                      color="black"),
                                  bgcolor=LEGEND_BACKG_COLOR,
                                  bordercolor="beige",
                                  borderwidth=1
                                  ),
                      height=height,
                      width=width,
                      margin=dict(
                          l=50,
                          r=50,
                          b=100,
                          t=100,
                          pad=4
                      ),
                      hovermode='x',
                      hoverlabel=dict(
                          font_size=16
        ))
    return st.plotly_chart(fig)
    # plot()


if __name__ == '__main__':
    main()