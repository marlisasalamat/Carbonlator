import streamlit as st
import pandas as pd

def app_checklist():

    st.subheader("Please select the following criteria within your apps:")

    st.write("**Usage and Relevance**")
    topic1_criteria1 = st.checkbox("Low Usage")
    topic1_criteria2 = st.checkbox("Redundancy")
    topic1_criteria3 = st.checkbox("Obsolete Functionality")
    topic1_criteria4 = st.checkbox("Compliance and Regulatory")

    st.write("**Environmental Impact**")
    topic2_criteria1 = st.checkbox("Resource Consumption")
    topic2_criteria2 = st.checkbox("Data Center Location")
    topic2_criteria3 = st.checkbox("Energy Efficiency Rating")

    st.write("**Cost and Business Impact**")
    topic3_criteria1 = st.checkbox("Maintenance Cost")
    topic3_criteria2 = st.checkbox("Business Value")
    topic3_criteria3 = st.checkbox("User Impact")

    # Convert selections into a dataframe with column name Criteria and Value
    data = {
        'Criteria': ['Low Usage', 'Redundancy', 'Obsolete Functionality', 'Compliance and Regulatory',
                     'Resource Consumption', 'Data Center Location', 'Energy Efficiency Rating',
                     'Maintenance Cost', 'Business Value', 'User Impact'],
        'Value': [int(topic1_criteria1), int(topic1_criteria2), int(topic1_criteria3), int(topic1_criteria4),
                  int(topic2_criteria1), int(topic2_criteria2), int(topic2_criteria3),
                  int(topic3_criteria1), int(topic3_criteria2), int(topic3_criteria3)]
    }

    df = pd.DataFrame(data)

    return df
