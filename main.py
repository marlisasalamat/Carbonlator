import streamlit as st
from co2_calculator import co2_calculator
from checklist import app_checklist

def main():
    st.title("Carbon Emission App Optimizer")

    tab_options = [['Introduction'], ['Carbon Emission Calculator'], ['App Checklist']]

    function = st.sidebar.radio(
        'Please select a function to proceed: ',
        options=[option[0] for option in tab_options],
        index=0
    )

    if function == 'Introduction':
        user_instructions()

    elif function == 'Carbon Emission Calculator':
        co2_calculator()

    elif function == 'App Checklist':
        app_checklist()


def user_instructions():
    st.write("Please enter the following information:")
    user_input = st.text_input("Enter the app name:")

    return user_input


if __name__ == '__main__':
    main()