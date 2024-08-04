import streamlit as st

def co2_calculator():
    st.header("Carbon Emission Calculator")

    st.subheader("Device Usage")
    device_power = st.number_input("Device Power Rating:", min_value=0.0, value=50.0)
    usage_duration = st.number_input("Usage Duration (hours):", min_value=0.1, value=24.0)

    st.subheader("Data Transmission")
    data_transmitted = st.number_input("Data Transmitted (MB):", min_value=0.0, value=100.0)
    data_emission_factor = st.number_input("Data Emission Factor (kg CO2e/MB):", min_value=0.0, value=0.2)

    st.subheader("Server Operation")
    server_power = st.number_input("Server Power Rating:", min_value=0.0, value=500.0)
    utilization_rate = st.number_input(" Server Utilization Rate (%):", min_value=0.0, value=50.0)
    total_time = st.number_input("Total Time (hours):", min_value=0.1, value=24.0)

    st.subheader("Electricity Emission Factor")
    emission_factor = st.number_input("Electricity Emission Factor (kg CO2e/kWh):", min_value=0.0, value=0.5)

    st.subheader("User Engagement")
    number_of_users = st.number_input("Number of Active Users:", min_value=0, value=1)

    if st.button("Calculate Emission"):
        E_device = (device_power * usage_duration/1000) * emission_factor
        E_data = data_transmitted * data_emission_factor
        E_server = (server_power * utilization_rate/100 * total_time/1000) * emission_factor
        E_total = (E_device + E_data + E_server) * number_of_users

        st.write(f"Carbon Emission from Device: {E_device} kg CO2e")
        st.write(f"Carbon Emission from Data Transmission: {E_data} kg CO2e")
        st.write(f"Carbon Emission from Server Operation: {E_server} kg CO2e")
        st.write(f"Total Carbon Emission: {E_total} kg CO2e")
