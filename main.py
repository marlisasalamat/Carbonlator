import streamlit as st
from CarbonEmissionSimulatorCalculator import co2_calculator
from CarbonlatorPrediction import app_checklist
import pickle
link_url = "https://www.facebook.com/share/Z6B7v51vvof5kuMj/?mibextid=qi2Omg"
link_url1 = "https://www.enelgreenpower.com/learning-hub/energy-transition/carbon-footprint"
link_url2 = "https://www.britannica.com/science/carbon-footprint"             
def main():
    
    st.sidebar.title("Carbonlator App")
    tab_options = [['Introduction'], ['Carbon Emission Simulator Calculator'], ['App Checklist']]

    function = st.sidebar.radio(
        'Directory',
        options=[option[0] for option in tab_options],
        index=0
    )

    app_name = st.sidebar.text_input("Enter the app name:")

    if function == 'Introduction':
        introduction()

    elif function == 'Carbon Emission Simulator Calculator':

        # Title for the CO2 calculator section
        st.title("Carbon Emission Simulator Calculator")

        # Add your CO2 calculator logic here
        st.subheader("Let's see how much carbon footprint you have produced.")        

        if app_name:
            app_name = co2_calculator(app_name)
        else:
            st.warning('Please Enter Your App Name')

    elif function == 'App Checklist':

        # Title for the app checklist section
        st.title("App Checklist")

        # Add your app checklist logic here
        st.write("This is where the app checklist will be implemented.")        

        if app_name:
            df = app_checklist()
            pred = st.button("Predict")
            if pred:
                # Load the model and scaler from the pickle file
                with open('model.pkl', 'rb') as file:
                    loaded_knn = pickle.load(file)

                with open('scaler.pkl', 'rb') as file:
                    loaded_scaler = pickle.load(file)

                # Predict on new data using the loaded model and scaler
                predict_df = loaded_scaler.transform([df['Value'].values])
                prediction = loaded_knn.predict(predict_df)

                if prediction == 1:
                    st.write(f"The app **{app_name}** should be *continued*. ✅")
                else:
                    st.write(f"The app **{app_name}** should be *decommissioned*. ❌")

        else:
            st.warning('Please Enter Your App Name')


def introduction():
    # Title of the app
    st.title("Introduction")

    # Long text content about carbon emissions
    long_text = """
    ### Understanding Carbon Emissions

    Carbon emissions are a significant contributor to climate change. They primarily come from burning fossil fuels, deforestation, and industrial processes. Understanding the sources and impacts of carbon emissions is crucial for developing strategies to mitigate climate change.
    """

    # Display the long text
    st.markdown(long_text)

    # Expander with additional content about carbon emissions
    with st.expander("Read More about Carbon Emissions"):
        st.markdown("#### Sources of Carbon Emissions")
        st.markdown("""
        1. **Transportation**: Cars, trucks, airplanes, and ships burn fossil fuels, releasing CO2 into the atmosphere.
        2. **Electricity Generation**: Power plants that burn coal, oil, or natural gas are major sources of carbon emissions.
        3. **Industrial Processes**: Manufacturing and construction activities often involve processes that emit greenhouse gases.
        4. **Gadget usage**: From the usage from your smartphone and applications can actually emit carbon from the electricity usage and having a cloud storage can actually leave carbon footprint.
        """)

        st.markdown("#### Impacts of Carbon Emissions")
        st.markdown("""
        High levels of carbon emissions lead to global warming, which can cause severe weather patterns, rising sea levels, and disruptions to ecosystems. Reducing carbon emissions is essential for protecting the environment and ensuring a sustainable future.
        """)

        st.markdown("#### Strategies for Reduction")
        st.markdown("""
        - **Energy Efficiency**: Improving energy efficiency in buildings and transportation can significantly reduce emissions.
        - **Renewable Energy**: Transitioning to solar, wind, and other renewable energy sources can help decrease reliance on fossil fuels.
        - **Carbon Offsetting**: Investing in projects that absorb CO2, such as reforestation, can help offset emissions.
        - **Smart usage**: Delete unnecesarry application in your phone that have similiar function and try to use application that support Zero Net Carbon Emission.
        """)

        st.markdown("""
        Understanding and addressing carbon emissions is vital for combating climate change and protecting our planet for future generations.
        """)

    # Additional expander for introducing Carbonlator
    with st.expander("Read More about Carbonlator"):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
         st.image('./Media/logo medium.png', width=300, )
        st.markdown("""### Introducing Carbonlator""")
        st.markdown("""            
        Carbonlator is an innovative application designed to help individuals and organizations assess their carbon footprint effectively. By providing users with a straightforward interface, Carbonlator enables users to input their activities and receive immediate feedback on their carbon emissions. 

        The app utilizes advanced algorithms to calculate emissions based on various factors, including energy consumption, transportation habits, and waste generation. Whether you are a small business looking to understand your environmental impact or an individual aiming to reduce your carbon footprint, Carbonlator offers tailored insights and recommendations.

        Key features of Carbonlator include:

        - **User-Friendly Interface**: Easily navigate through the app to input data and view results.
        - **Real-Time Calculations**: Get instant feedback on your carbon emissions based on your inputs.
        - **Calculation Simulator**: You can get a gist of how much carbon emission you had produced by checking our Simulator feature and can start using your smartphone attentively now!

        By leveraging Carbonlator, users can take meaningful steps towards reducing their carbon emissions and contributing to a more sustainable future. Join us in the fight against climate change by understanding your impact and making informed decisions.

        """)

    with st.expander("How does it work?"):
        st.markdown("#### Simulator Calculator")
        col1, col2, col3 = st.columns([1, 6, 5])
        with col2:
         st.image('./Media/formula.png', width=500, )
         st.markdown("""**Calculation formula** """)
         st.markdown("""

            This is the general formula that had been used to calculate the carbon emission. This had been sourced from: """) 
         st.markdown(f"[1. Enel Green]({link_url})", unsafe_allow_html=True)
         st.markdown(f"[2. Britannica]({link_url})", unsafe_allow_html=True)
        
                    
        st.markdown("#### Machine Learning Feature")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
         st.image('./Media/KNN.png',)
        st.markdown("""**K-Nearest Neighbour**""")
        st.markdown(""" K-Nearest Neighbor (KNN) is a simple and effective machine learning algorithm used for classification and regression tasks. It works by finding the K closest data points (neighbors) to a given input and making a prediction based on the majority class (for classification) or the average value (for regression) of those neighbors. Here's a simple explanation of how KNN works:""")
        
        st.markdown("""
        1. **Choose a value for K,** which represents the number of nearest neighbors to consider.
        2. **Calculate the distance** between the input data point and all other data points in the dataset. The most common distance metric used is Euclidean distance.
        3. **Sort the distances**  in ascending order and select the K data points with the smallest distances.
        4. **For classification,** the algorithm assigns the input data point to the class that has the most representatives among the K nearest neighbors. For regression, it predicts the average value of the K nearest neighbors.
        5. **The algorithm returns,** the predicted class (for classification) or the predicted value (for regression).
        """)

        st.markdown("#### Checklist Concept")

        st.markdown("""Hence the checklist concept is used by adopting K-Nearest Neighbour concept where every checkbox represent a data point and it functions to find which classification it will be (Commission/decommission)""")


    with st.expander("About us"):
        st.markdown("""
        ### Background Story : Senjaya Innovators

        The Senjaya Innovators is an enthusiastic group of students from SK Sentosa Jaya, a primary school located in Kinabatangan, Sabah, who are passionate about learning STEM and coding. Under the guidance of their dedicated teacher, Mr. Danial, the Senjaya Innovators are constantly seeking new opportunities to expand their knowledge and skills in these fields.


        The team, composed of bright and curious students, is driven by a strong desire to explore the world of technology and innovation. They spend their free time tinkering with robotics kits, experimenting with coding languages, and participating in various STEM-related activities organized by the school.

        As the Senjaya Innovators continue to grow and learn, they are excited about the future. They dream of creating innovative solutions to real-world problems and inspiring others to pursue their passions in STEM and coding. With the support of their school, teacher, and community, the Senjaya Innovators are well on their way to becoming the next generation of leaders in technology and innovation.

        
        """)

        st.markdown(f"[Click here to go to know more about SK Sentosa Jaya]({link_url})", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
