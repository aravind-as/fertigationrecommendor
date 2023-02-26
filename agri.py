import streamlit as st

# define functions for each crop
def recommend_chilli(tds, temp, humidity, ph, ec, phase):
    optimum_ec = {'initial': 1.5,'middle': 2,'generative': 3}
    optimum_tds = {'min': 1260,'max': 1540}
    optimum_temperature = {'min': 20, 'max': 25}
    optimum_humidity = { 'min': 50,'max': 60,}
    optimum_ph = {'min': 5.5,'max': 6.8}

    if phase.lower() == "initial" and 1260 <= tds <= 1540 and 20 <= temp <= 25 and 50 <= humidity <= 60 and 5.5 <= ph <= 6.8 and ec==1.5 :
        st.write("Change in Fertigation is not required")
    if phase.lower() == "middle" and 1260 <= tds <= 1540 and 20 <= temp <= 25 and 50 <= humidity <= 60 and 5.5 <= ph <= 6.8 and ec==2 :
        st.write("Change in Fertigation is not required")
    if phase.lower() == "generative" and 1260 <= tds <= 1540 and 20 <= temp <= 25 and 50 <= humidity <= 60 and 5.5 <= ph <= 6.8 and ec==3 :
        st.write("Change in Fertigation is not required")
    else:
        st.write("")
        if tds < optimum_tds['min']:
            st.write(f"Add more fertilizer to increase TDS to at least {optimum_tds['min']} ppm.")
            st.write(f"Fertigation schedule for CHILLI")
            st.write(f"Recommended Dose of N, P, K is: 120:80:80 kg / ha")
            
        elif tds > optimum_tds['max']:
            st.write(f"Reduce fertilizer to decrease TDS to at most {optimum_tds['max']} ppm.")
        if temp < optimum_temperature['min']:
            st.write(f"Increase temperature to at least {optimum_temperature['min']} °C.")
        elif temp > optimum_temperature['max']:
            st.write(f"Reduce temperature to at most {optimum_temperature['max']} °C.")
        if humidity < optimum_humidity['min']:
            st.write(f"Increase humidity to at least {optimum_humidity['min']}%.")
        elif humidity > optimum_humidity['max']:
            st.write(f"Reduce humidity to at most {optimum_humidity['max']}%.")
        if ph < optimum_ph['min']:
            st.write(f"Adjust pH to at least {optimum_ph['min']} using lime or dolomite.")
        elif ph > optimum_ph['max']:
            st.write(f"Adjust pH to at most {optimum_ph['max']} using sulfur or acidifying fertilizers.")
        if phase.lower() == "initial" and  ec < optimum_ec['initial']:
            st.write(f"Increase EC level to {optimum_ec['initial']}")
        elif phase.lower() == "initial" and  ec > optimum_ec['initial']:
            st.write(f"Decrease EC level to {optimum_ec['initial']} by reducing fertilizers")
        elif phase.lower() == "middle" and  ec < optimum_ec['middle']:
            st.write(f"Increase EC level to {optimum_ec['middle']} by adding fertilizers")
        elif phase.lower() == "middle" and  ec > optimum_ec['middle']:
            st.write(f"Decrease EC level to {optimum_ec['middle']} by decreasing fertilizers")
        elif phase.lower() == "generative" and  ec < optimum_ec['middle']:
            st.write(f"Increse EC level to {optimum_ec['generative']} by adding fertilizers")
        elif phase.lower() == "generative" and  ec > optimum_ec['generative']:
            st.write(f"Decrese EC level to {optimum_ec['generative']} by reducing fertilizers")


def recommend_rice(tds, humidity, ph, ec, temp, phase):
    
    optimum_ec = {'min': 0.65, 'max': 12.50}
    optimum_tds = {'min': 450, 'max': 2000}
    optimum_humidity = {'min': 60, 'max': 80}
    optimum_ph = {'min': 5.5, 'max': 6.5}
    optimum_temp = {'initial': {'min': 26.5, 'max': 29.5}, 'middle': 10, 'generative': {'min': 20, 'max': 21}}
    
    if phase.lower() == "initial" and 450 <= tds <= 2000 and 60 <= humidity <= 80 and 5.5 <= ph <= 6.5 and 0.65 <= ec <= 12.50 and 26.5 <= temp <= 29.5:
        st.write("Change in Fertigation is not required")
    if phase.lower() == "middle" and 450 <= tds <= 2000 and 60 <= humidity <= 80 and 5.5 <= ph <= 6.5 and 0.65 <= ec <= 12.50 and temp == 10:
        st.write("Change in Fertigation is not required")
    if phase.lower() == "generative" and 450 <= tds <= 2000 and 60 <= humidity <= 80 and 5.5 <= ph <= 6.5 and 0.65 <= ec <= 12.50 and 20 <= temp <= 21:
        st.write("Change in Fertigation is not required")
    
    else:
        st.write("")
        if tds < optimum_tds['min']:
            st.write(f"Add more fertilizer to increase TDS to at least {optimum_tds['min']} ppm.")
            st.write("Fertigation schedule for rice")
            st.write("Recommended Dose of N, P, K is: 60:30:30 kg/ha")
        elif tds > optimum_tds['max']:
            st.write(f"Reduce fertilizer to decrease TDS to at most {optimum_tds['max']} ppm.")
        if humidity < optimum_humidity['min']:
            st.write(f"Increase humidity to at least {optimum_humidity['min']}%.")
        elif humidity > optimum_humidity['max']:
            st.write(f"Reduce humidity to at most {optimum_humidity['max']}%.")
        if ph < optimum_ph['min']:
            st.write(f"Adjust pH to at least {optimum_ph['min']}.")
        elif ph > optimum_ph['max']:
            st.write(f"Adjust pH to at most {optimum_ph['max']} using sulfur or acidifying fertilizers.")
        if ec < optimum_ec['min']:
            st.write(f"Increase ec level to at least {optimum_ec['min']}.")
        elif ec > optimum_ec['max']:
            st.write(f"Decrease ec level to at most {optimum_ec['max']} .")


        if phase.lower() == "initial" and temp < optimum_temp['initial']['min']:
            st.write(f"Increase temp level to at least {optimum_temp['initial']['min']}.")
        elif phase.lower() == "initial" and temp > optimum_temp['initial']['max']:
            st.write(f"Decrease temp level to at most {optimum_temp['initial']['max']} by reducing fertilizers.")
        if phase.lower() == "middle" and temp < optimum_temp['middle']:
            st.write(f"Increase temp level to at least {optimum_temp['middle']}.")
        elif phase.lower() == "middle" and temp > optimum_temp['middle']:
            st.write(f"Decrease temp level to at most {optimum_temp['middle']} .")
        if phase.lower() == "generative" and temp < optimum_temp['generative']['min']:
            st.write(f"Increase temp level to at least {optimum_temp['generative']['min']}.")
        elif phase.lower() == "generative" and temp > optimum_temp['generative']['max']:
            st.write(f"Decrease temp level to at most {optimum_temp['generative']['max']} .")
                        

if __name__ == '__main__':
    st.set_page_config(page_title='Fertigation Recommender')
    st.title('Fertigation Recommender')
    crop = st.selectbox("Select the crop name", ["select", "chilli", "rice"])

    
    num_days = st.selectbox("Select the number of days after planting:",["select", "1 to 20 days", "21 to 75 days", "76 to 120 days"])
    
    if num_days == "1 to 20 days":
        phase = "initial"
        st.write("The growth phase is:", phase)
    elif num_days =="21 to 75 days":
        phase = "middle"
        st.write("The growth phase is:", phase)
    elif num_days =="76 to 120 days":
        phase = "generative"
        st.write("The growth phase is:", phase)
    else:
        if num_days == "select":
            st.write("Please select Number of days.")
        else:
            st.write("Invalid selection")
    
    #phase = st.selectbox("Enter the growth phase", ["initial", "middle", "generative"])
    tds = st.number_input("Enter the TDS value")
    temp = st.number_input("Enter the temperature (in Celsius)")
    humidity = st.number_input("Enter the humidity (in percentage)")
    ph = st.number_input("Enter the pH value")
    ec = st.number_input("Enter the current EC value the plant")

    if (tds==0 and temp==0) or (humidity==0 or ph==0 or ec ==0 ):
        st.write("Please fill all the values")
    else:
        if crop == "chilli":
            recommend_chilli(tds, temp, humidity, ph, ec, phase)
        elif crop == "rice":
            recommend_rice(tds, temp, humidity, ph, ec, phase)

        else:
            if crop == "select":
                st.write("Please select crop.")
            else:
                st.write("We are sorry. Data is unavailable for the plant you have entered.")

