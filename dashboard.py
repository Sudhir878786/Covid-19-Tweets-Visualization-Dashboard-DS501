import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import pandas as pd

LABELS = ['Positive', 'Negative', 'Neutral']
POS_COLOR = 'rgb(42,128,97)'
NEG_COLOR = 'rgb(229,57,53)'
NEU_COLOR = 'rgb(97,97,97)'


def main():

    st.markdown('<h4>NOTE: Conventions used in the project:</h4>'
                '<h4>1. Shade of green to represent <i>Positive</i> sentiment</h4>'
                '<h4>2. Shade of red to represent <i>Negative</i> sentiment</h4>'
                '<h4>3. Shade of grey to represent <i>Neutral</i> sentiment</h4><br>', unsafe_allow_html=True)
    # st.write('')
    # st.markdown('<br>', unsafe_allow_html=True)
    # st.write('')
    # # st.markdown('<br>', unsafe_allow_html=True)
    # st.write('2. Shade of green to represent _Negative_ sentiment')
    # # st.markdown('<br>', unsafe_allow_html=True)
    # st.write('2. Shade of grey to represent _Neutral_ sentiment')


    st.subheader('Sentiment Analysis Dashboard')
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "xy"}, {"type": "xy"}],
               [{"type": "domain"}, {"type": "xy"}]],
        vertical_spacing=0.25,
        horizontal_spacing=0.2,
        subplot_titles=("Month-wise Analysis", "Day-wise Analysis", "Overall Analysis", "Phase-wise Analysis"),
    )
    # Month wise bar plot
    # Positive bars
    labels = ['March', 'April', 'May', 'June', 'July']
    fig.add_trace(go.Bar(y=[30805, 43042, 29736, 82452, 60975],
                         x=labels,
                         # xaxis='x',
                         marker_color='rgb(42,128,97)',
                         hovertemplate="%{label}: %{y} positive tweets"
                         # hovertext=['{y} Positive tweets', 'Tweet count April', '19% market share',
                         #            'Tweet count March', 'Tweet count March'],
                         ),
                  row=1, col=1)
    # Negative bars
    fig.add_trace(go.Bar(y=[19914, 24949, 17829, 56724, 40475],
                         x=labels,
                         marker_color='rgb(229,57,53)',
                         hovertemplate="%{label}: %{y} negative tweets"
                         # hovertext=['Tweet count March', 'Tweet count April', '19% market share',
                         #            'Tweet count March', 'Tweet count March'],
                         ),
                  row=1, col=1)
    # Neutral bars
    fig.add_trace(go.Bar(y=[17839, 22599, 15977, 51055, 59737],
                         x=labels,
                         marker_color='rgb(97,97,97)',
                         hovertemplate="%{label}: %{y} neutral tweets"
                         # hovertext=['Tweet count March', 'Tweet count April', '19% market share',
                         #            'Tweet count March', 'Tweet count March'],
                         ),
                  row=1, col=1)

    day_wise = pd.read_csv('day_wise.csv')
    fig.add_trace(go.Scatter(x=day_wise['Date'], y=day_wise['Positive'],
                             name='Positive Tweets',
                             mode='lines',
                             line=dict(width=2, color=POS_COLOR)),
                  row=1, col=2)

    fig.add_trace(go.Scatter(x=day_wise['Date'], y=day_wise['Negative'],
                             name='Negative Tweets',
                             mode='lines',
                             line=dict(width=2, color=NEG_COLOR)),
                  row=1, col=2)

    fig.add_trace(go.Scatter(x=day_wise['Date'], y=day_wise['Neutral'],
                             name='Neutral Tweets',
                             mode='lines',
                             line=dict(width=2, color=NEU_COLOR)),
                  row=1, col=2)

    fig.add_trace(
        go.Pie(values=[139113 + 79334, 78940 + 55421, 221300],
               hole=0.75,
               labels=LABELS,
               texttemplate="%{label}<br>(%{percent})",
               marker=dict(colors=[POS_COLOR, NEG_COLOR, NEU_COLOR])
               ),
        row=2, col=1
    )

    fig.add_trace(go.Bar(x=['Lockdown 1.0', 'Lockdown 2.0', 'Lockdown 3.0',
                            'Lockdown 4.0', 'Unlock 1.0', 'Unlock 2.0'],
                         y=[75879, 50023, 27873, 21894, 188978, 161187],
                         marker=dict(color='rgb(72,100,255)')),
                  row=2, col=2)

    fig.update_layout(height=650, width=850, showlegend=False)

    fig['layout']['xaxis']['title'] = 'Months'
    fig['layout']['xaxis2']['title'] = 'Days (March 01 to June 26)'
    fig['layout']['yaxis']['title'] = 'Number of Tweets'
    fig['layout']['yaxis2']['title'] = 'Number of Tweets'
    fig['layout']['xaxis3']['title'] = 'Phase'
    fig['layout']['yaxis3']['title'] = 'Number of Tweets'

    st.plotly_chart(fig)

    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("<h3 style='color:blue;font-weight:bold;font-size:25px;'><b>Navigate to the <i>Plots</i> page from "
                "the sidebar for "
                "more plots!</b><h3>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='color:green;font-weight:bold;font-size:25px;'><b>Visit the <i>About</i> page from the "
                "sidebar to read more about this project!</b><h3>",
                unsafe_allow_html=True)


if __name__ == '__main__':
    main()
