import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

k1 = ['#NizamuddinMarkaz', '#LockdownWithoutPlan', '#Coronavirustruth', '#CoronaVillains', '#CoronaVirusUpdates',
      '#Coronafighters', '#socialdistancing', '#TablighiJamaat', '#CoronaStopKaroNa', '#workfromhome']
k2 = ['#EarthDay2020', '#QuarantineLife', '#SocialDistancing', '#COVID19Pandemic', '#lockdowneffect',
      '#IndiaUnitedAgainstCorona', '#business', '#BiharHealthDept', '#sundayvibes', '#life']
k3 = ['#MigrantLabourers', '#LiquorShops', '#MothersDay', '#CoronaUpdatesInIndia', '#NarendraModi', '#SocialDistancing',
      '#WaiveFeePromoteStudents', '#Karnataka', '#economy', '#atmanirbharbharat']
k4 = ['#EidMubarak', '#MigrantWorkers', '#rgpv_spreading_corona_virus', '#Coronavirus_Outbreak', '#CoronaRiskInJail',
      '#COVID19Pandemic', '#CycloneAmphan', '#PromoteStudentsSaveFuture', '#FeedTheNeedy', '#UmeedKiKiran']
k5 = ['#health', '#Unlock1', '#IndiaChinaFaceOff', '#Lockdown_Extension', '#business', '#IndianArmy', '#economy',
      '#StudentsLivesMatter', '#righttolearn', '#PatanjaliAyurved']
k6 = ['#StudentsLivesMatters', '#UGCGuidelines', '#Lockdown_Extension', '#ugc_cancel_exam', '#TN',
      '#SayNoToUGCGuidelines', '#cancelfinalyearexam', '#ICMR', '#Unlock2', '#cancelallexams']
v1 = [225, 219, 164, 163, 161, 160, 155, 152, 145, 109]
v2 = [300, 291, 151, 111, 96, 76, 75, 75, 74, 73]
v3 = [260, 182, 114, 108, 98, 96, 64, 63, 51, 51]
v4 = [82, 80, 80, 75, 66, 63, 62, 56, 55, 52]
v5 = [653, 394, 354, 298, 289, 276, 269, 205, 204, 203]
v6 = [601, 505, 487, 450, 441, 441, 424, 310, 278, 252]

data1 = pd.DataFrame(list(zip(k1, v1)), columns=['Keys', 'Values'])
data2 = pd.DataFrame(list(zip(k2, v2)), columns=['Keys', 'Values'])
data3 = pd.DataFrame(list(zip(k3, v3)), columns=['Keys', 'Values'])
data4 = pd.DataFrame(list(zip(k4, v4)), columns=['Keys', 'Values'])
data5 = pd.DataFrame(list(zip(k5, v5)), columns=['Keys', 'Values'])
data6 = pd.DataFrame(list(zip(k6, v6)), columns=['Keys', 'Values'])


def main(theme='plotly_dark'):
    st.subheader("Less Popular _Hash-Tags_ Analysis")
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
