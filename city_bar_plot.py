import streamlit as st
import plotly.graph_objects as go

TITLE = 'City Wise Sentiment Analysis'
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

c1 = ['Mumbai', 'Delhi', 'New Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Kolkata', 'Bhubaneswar',
      'Ahmedabad', 'Dispur', 'Chandigarh', 'Jaipur', 'Lucknow', 'Jammu', 'Patna', 'Surat', 'Indore', 'Panaji', 'Bhopal']
c2 = ['Mumbai', 'Delhi', 'New Delhi', 'Bangalore', 'Hyderabad', 'Kolkata', 'Chennai', 'Pune', 'Bhubaneswar',
      'Ahmedabad', 'Lucknow', 'Chandigarh', 'Dispur', 'Jaipur', 'Jammu', 'Patna', 'Panaji', 'Indore', 'Bhopal', 'Surat']
c3 = ['Mumbai', 'Delhi', 'New Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Kolkata', 'Ahmedabad',
      'Bhubaneswar', 'Lucknow', 'Dispur', 'Chandigarh', 'Jaipur', 'Patna', 'Jammu', 'Surat', 'Indore', 'Bhopal',
      'Panaji']

pos = [29411, 17642, 15852, 13828, 10454, 7344, 7260, 6276, 3768, 3437, 2924, 2731, 2560, 2376, 1531, 1524, 1290, 1149,
       1126, 876]
neg = [16915, 10710, 9363, 8226, 5885, 4270, 3986, 3466, 1807, 1679, 1412, 1338, 1301, 1234, 1009, 925, 719, 580, 537,
       527]
neut = [43155, 32314, 23952, 21298, 15943, 15868, 10344, 9552, 5307, 4841, 4633, 4197, 4099, 4034, 2850, 2401, 1922,
        1884, 1798, 1647]

fig = go.Figure()


def positive(fig):
    fig.add_trace(go.Bar(
        x=c1,
        y=pos,
        name='Positive Sentiment',
        marker_color=POS_LINE_COLOR
    ))
    fig.update_layout(hoverlabel=dict(
        bgcolor=POS_HOVER_TEXT_BACKG_COLOR,
    ))


# def some_positive(fig):
#    fig.add_trace(go.Bar(
#        x=cities,
#        y=num_som_pos_sent,
#        name='Somewhat Positive Sentiment',
#        marker_color=SOM_POS_LINE_COLOR
#    ))

def negative(fig):
    fig.add_trace(go.Bar(
        x=c2,
        y=neg,
        name='Negative Sentiment',
        marker_color=NEG_LINE_COLOR
    ))
    fig.update_layout(hoverlabel=dict(
        bgcolor=NEG_HOVER_TEXT_BACKG_COLOR,
    ))


# def some_negative(fig):
#    fig.add_trace(go.Bar(
#        x=cities,
#        y=num_som_neg_sent,
#        name='Somewhat Negative Sentiment',
#        marker_color=SOM_NEG_LINE_COLOR
#    ))

def neutral(fig):
    fig.add_trace(go.Bar(
        x=c3,
        y=neut,
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
    # st.title('IBM Hack Challenge 2020')
    fig = go.Figure()

    global TEXT_COLOR, LEGEND_BACKG_COLOR, NEU_LINE_COLOR, POS_LINE_COLOR, NEG_LINE_COLOR, SOM_POS_LINE_COLOR, SOM_NEG_LINE_COLOR, PLOT_BG_COLOR
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

    if sentiment_picker == 'Positive':
        positive(fig)

    # elif sentiment_picker == 'Somewhat Positive':
    #     some_positive(fig)
    elif sentiment_picker == 'Negative':
        negative(fig)

    # elif sentiment_picker == 'Somewhat Negative':
    #     some_negative(fig)

    elif sentiment_picker == 'Neutral':
        neutral(fig)

    else:
        positive(fig)
        # some_positive(fig)
        negative(fig)
        # some_negative(fig)
        neutral(fig)
        fig.update_layout(hoverlabel=dict(
            bgcolor=ALL_HOVER_TEXT_BACKG_COLOR,
        ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.

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
                      legend=dict(x=0.77,
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
