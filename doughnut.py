import streamlit as st
import plotly.graph_objects as go

# import pandas as pd

TITLE = 'Overall Sentiment Distribution'
LABELS = ['Positive', 'Negative', 'Neutral', 'Somewhat Positive', 'Somewhat Negative']
FONT_SIZE = 15
HOLE_FRACTION = 0.75

pie_dark_colors = ['rgb(67,230,167)', 'rgb(229,57,53)', 'rgb(167,167,167)', 'lightskyblue', 'palevioletred']
pie_light_colors = ['rgb(42,128,97)', 'rgb(229,57,53)', 'rgb(97,97,97)', 'lightgreen', 'orange']

TEXT_COLOR = 'rgb(80,80,80)'
TEXT_COLOR_DARK = 'rgb(200,200,200)'

# TODO Currently not working Line 53
PLOT_BG_COLOR = 'rgb(240,240,240)'

LEGEND_BACKG_COLOR_DARK = 'rgb(100,110,120)'
LEGEND_BACKG_COLOR = 'rgb(200,210,220)'


def plot(theme='plotly', height=650, width=850):
    # scores = [i for i in data['Sentiment']]
    # # Positive sentiments
    # pos = len([x for x in scores if x > 0.5])
    # # Negative sentiments
    # neg = len([x for x in scores if x < -0.5])
    # # Somewhat positive sentiments
    # some_pos = len([x for x in scores if 0.5 > x > 0.25])
    # # Somewhat negative sentiments
    # some_neg = len([x for x in scores if -0.25 > x > -0.5])
    # neutral = len(data) - (pos + neg + some_pos + some_neg)
    # sentiments = [pos, neg, neutral, some_pos, some_neg]
    sentiments = [139113, 78940, 221300, 79334, 55421]

    # if theme == 'plotly':
    fig = go.Figure(go.Pie(values=sentiments,
                           labels=LABELS,
                           texttemplate="%{label}<br>(%{percent})",
                           hole=HOLE_FRACTION,
                           ))
    fig.update_traces(textfont_size=FONT_SIZE,
                      marker=dict(colors=pie_light_colors if theme == 'plotly' else pie_dark_colors,
                                  line=dict(color='aliceblue', width=2))
                      )
    fig.update_layout(template=theme,
                      title=dict(text=TITLE,
                                 font=dict(size=25),),
                      width=width,
                      height=height,
                      plot_bgcolor=PLOT_BG_COLOR,
                      showlegend=True,
                      font=dict(
                          family="Courier New, monospace",
                          size=18,
                          color=TEXT_COLOR if theme == 'plotly' else TEXT_COLOR_DARK
                      ),
                      legend=dict(traceorder="normal",
                                  font=dict(
                                      family="sans-serif",
                                      size=13,
                                      color="black"),
                                  bgcolor=LEGEND_BACKG_COLOR if theme == 'plotly' else LEGEND_BACKG_COLOR_DARK,
                                  bordercolor="beige",
                                  borderwidth=1.0
                                  ),
                      )

    # Dark
    # else:
    #     fig = go.Figure(go.Pie(values=sentiments,
    #                            labels=LABELS,
    #                            texttemplate="%{label} <br>(%{percent})",
    #                            # textposition="outside",
    #                            hole=0.75,
    #                            ))
    #     fig.update_traces(textfont_size=FONT_SIZE,
    #                       marker=dict(colors=pie_dark_colors,
    #                                   line=dict(color='aliceblue', width=2))
    #                       )
    #     fig.update_layout(template=theme,
    #                       title=dict(text=TITLE,
    #                                  font=dict(size=25)),
    #                       width=width,
    #                       height=height,
    #                       showlegend=True,
    #                       font=dict(
    #                           family="Courier New, monospace",
    #                           size=18,
    #                           color=TEXT_COLOR_DARK
    #                       ),
    #                       legend=dict(traceorder="normal",
    #                                   font=dict(
    #                                       family="sans-serif",
    #                                       size=13,
    #                                       color="white"),
    #                                   bgcolor=LEGEND_BACKG_COLOR_DARK,
    #                                   bordercolor="beige",
    #                                   borderwidth=1.0
    #                                   ),
    #                       )
    fig.update_layout(legend_title_text='Sentiments', font_size=20,
                      )

    st.plotly_chart(fig)


def main(theme, height=700, width=900):
    # data = pd.read_csv('plot.csv')
    plot(theme=theme, height=height, width=width)


if __name__ == '__main__':
    main()
