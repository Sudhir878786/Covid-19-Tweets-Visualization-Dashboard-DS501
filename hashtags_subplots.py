import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

k1 = ['#IndiaFightsCorona', '#21Days_Lockdown', '#Coronavirus_Outbreak', '#PMCARES', '#Lockdown_Extension',
      '#Quarantine', '#ChineseVirus', '#India', '#COVID19Pandemic', '#CoronaUpdate']
k2 = ['#IndiaFightsCorona', '#Lockdown_Extension', '#India', '#Coronavirus_Outbreak', '#Quarantine', '#Lockdown2',
      '#pandemic', '#CoronaWarriors', '#Lockdown3', '#india']
k3 = ['#StayHome_StaySafe', '#IndiaFightsCorona', '#Lockdown_Extension', '#India', '#pandemic', '#Lockdown4',
      '#Lockdown3', '#Quarantine', '#Mumbai', '#india']
k4 = ['#IndiaFightsCorona', '#India', '#pandemic', '#Lockdown_Extension', '#Lockdown4', '#CoronaWarriors', '#Quarantine',
      '#Lockdown5', '#Mumbai', '#Maharashtra']
k5 = ['#Coronavirus_Outbreak', '#Delhi', '#PMCARES', '#China', '#Coronil', '#Mumbai', '#Chennai', '#TamilNadu',
      '#Telangana', '#Maharashtra']
k6 = ['#AmitabhBachchan', '#Coronavirus_Outbreak', '#India', '#pandemic', '#TamilNadu', '#SpeakUpForStudents',
      '#BREAKING', '#CoronaVirusUpdates', '#COVID19Pandemic', '#Delhi']
v1 = [3034, 2781, 1685, 869, 790, 681, 603, 596, 530, 493]
v2 = [1564, 739, 552, 516, 444, 404, 360, 313, 302, 254]
v3 = [1703, 666, 445, 331, 282, 279, 193, 189, 186, 179]
v4 = [473, 305, 243, 205, 188, 172, 166, 153, 152, 143]
v5 = [1793, 1251, 1196, 925, 898, 834, 811, 792, 679, 675]
v6 = [1742, 1738, 1664, 1612, 1165, 1164, 983, 843, 816, 761]

data1 = pd.DataFrame(list(zip(k1, v1)), columns=['Keys', 'Values'])
data2 = pd.DataFrame(list(zip(k2, v2)), columns=['Keys', 'Values'])
data3 = pd.DataFrame(list(zip(k3, v3)), columns=['Keys', 'Values'])
data4 = pd.DataFrame(list(zip(k4, v4)), columns=['Keys', 'Values'])
data5 = pd.DataFrame(list(zip(k5, v5)), columns=['Keys', 'Values'])
data6 = pd.DataFrame(list(zip(k6, v6)), columns=['Keys', 'Values'])


def main(theme='plotly_dark'):
    # fig = go.Figure()
    st.subheader('Popular _Hash-Tags_ Analysis')
    fig = make_subplots(rows=3, cols=3, shared_yaxes=False,
                        subplot_titles=("Lockdown 1.0", "", "Lockdown 2.0", "Lockdown 3.0", "", "Lockdown 4.0",
                                        "Unlock 1.0", "", "Unlock 2.0"))
    fig.add_trace(go.Bar(x=data1.Values, y=data1.Keys, name='Lockdown 1.0', orientation='h'), 1, 1)

    fig.add_trace(go.Bar(x=data2.Values, y=data2.Keys, name='Lockdown 2.0', orientation='h'), 1, 3)

    fig.add_trace(go.Bar(x=data3.Values, y=data3.Keys, name='Lockdown 3.0', orientation='h'), 2, 1)

    fig.add_trace(go.Bar(x=data4.Values, y=data4.Keys, name='Lockdown 4.0', orientation='h'), 2, 3)

    fig.add_trace(go.Bar(x=data5.Values, y=data5.Keys, name='Unlock 1.0', orientation='h'), 3, 1)

    fig.add_trace(go.Bar(x=data6.Values, y=data6.Keys, name='Unlock 2.0', orientation='h'), 3, 3)

    fig.update_traces(marker_color=data1.Values, marker_line_width=1.5)

    fig.update_layout(height=1000, width=850,
                      title_text="")

    if theme == 'plotly_dark':
        fig.update_layout(template=theme,
                          font=dict(
                              family="Courier New, monospace",
                              size=13,
                              color='rgb(200,200,200)'
                          ), showlegend=False)
    else:
        fig.update_layout(template=theme,
                          font=dict(
                              family="Courier New, monospace",
                              size=13,
                              color='rgb(90,90,90)'
                          ), showlegend=False)

    st.plotly_chart(fig)


if __name__ == '__main__':
    main()
