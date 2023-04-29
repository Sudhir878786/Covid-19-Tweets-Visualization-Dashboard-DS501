import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def main(choice):
    if choice == 'INFORMATION RETIEVAL DS501':
        st.markdown("<h3 style='color:blue;font-weight:bold;'><u>INFORMATION RETIEVAL DS501</h3>", unsafe_allow_html=True)
     

       
        st.markdown('<br>', unsafe_allow_html=True)
        st.markdown("<h3 style='color:red;font-weight:bold;'><u>Our problem statement</h3>", unsafe_allow_html=True)
        st.subheader('Analysis of COVID-19 Tweets Visualization Dashboard')

        st.write('''The sentiment analysis of Indians after the extension of lockdown announcements to be analyzed with the relevant #tags on twitter and build a predictive analytics model to understand the behavior of people if the lockdown is further extended.
                    Also develop a dashboard with visualization of people reaction to the govt announcements on lockdown extension ''')

    else:
        st.markdown("<h3 style='color:blue;font-weight:bold;'><u>About Sentiment Analysis</h3>", unsafe_allow_html=True)
        st.subheader('Sentiment Analysis (a.k.a Opinion Mining)')
        st.write('Sentiment Analysis is a technique widely used in Data analysis. Twitter Sentiment Analysis, '
                 'therefore means, using data analysis techniques to analyze the sentiment of the tweets, thus '
                 'classifying tweets into the categories of positive, negative and neutral.')
        st.markdown('<br>', unsafe_allow_html=True)
        st.write('In this project, we have used the VADER Sentiment Analysis tool for classifying tweets into '
                 'positive, negative or neutral polarity. Below, is a text field in which you can enter any sentence '
                 'to find out its polarity to see sentiment classification in action!!')
        st.markdown('<br>', unsafe_allow_html=True)
        text = st.text_input(label='Enter text below',
                             value='I am super excited today!!')

        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(text)
        score = vs['compound']
        st.write('Sentiment output = {}  \n'
                 '{} text predicted'.format(score, 'Negative' if score < 0.1 else 'Positive' if score > 0.1 else 'Neutral'))
        st.markdown('<br>', unsafe_allow_html=True)
        st.write('A positive value above means the entered text is classified as a _positive_ text. '
                 'Similarly, a negative value means the text entered is _negative_ and a value close to 0 '
                 'means that the text is _neutral_.')


if __name__ == '__main__':
    main()
