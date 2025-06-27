import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

with open("random_forest_class_personality.pkl", 'rb') as file:
    model = pickle.load(file)
    
st.title("Personality Classification")
st.write("This app cliassifies Personality of a person based on answers provided using RandomForest Classifier")

st.subheader("Enter answers to the below questions.")

social_energy = st.number_input("Social Energy Level", min_value=0,max_value=10)
alone_time_preference  = st.number_input("Alone time preference", min_value=0,max_value=10) 
talkativeness = st.number_input("Talkativeness", min_value=0,max_value=10) 
deep_reflection  = st.number_input("Deep reflection", min_value=0,max_value=10) 
group_comfort  = st.number_input("Group comfort", min_value=0,max_value=10) 
party_liking  = st.number_input("Party likingl", min_value=0,max_value=10) 
listening_skill  = st.number_input("Listening skill", min_value=0,max_value=10) 
empathy  = st.number_input("Empathy", min_value=0,max_value=10) 
creativity  = st.number_input("Creativity", min_value=0,max_value=10) 
organization  = st.number_input("Organization", min_value=0,max_value=10) 
leadership  = st.number_input("Leadership Quality", min_value=0,max_value=10) 
risk_taking  = st.number_input("Risk taking", min_value=0,max_value=10) 
public_speaking_comfort  = st.number_input("Public speaking comfort", min_value=0,max_value=10) 
curiosity  = st.number_input("Curiosity", min_value=0,max_value=10) 
routine_preference  = st.number_input("Routine preference", min_value=0,max_value=10) 
excitement_seeking  = st.number_input("Excitement seeking", min_value=0,max_value=10) 
friendliness  = st.number_input("Friendliness", min_value=0,max_value=10) 
emotional_stability  = st.number_input("Emotional stability", min_value=0,max_value=10) 
planning  = st.number_input("Planning", min_value=0,max_value=10) 
spontaneity  = st.number_input("Spontaneity", min_value=0,max_value=10) 
adventurousness  = st.number_input("Adventurousness", min_value=0,max_value=10) 
reading_habit  = st.number_input("Reading habit", min_value=0,max_value=10) 
sports_interest  = st.number_input("Sports interest", min_value=0,max_value=10) 
online_social_usage  = st.number_input("Online social usage", min_value=0,max_value=10) 
travel_desire  = st.number_input("Travel desire", min_value=0,max_value=10) 
gadget_usage  = st.number_input("Gadget usage", min_value=0,max_value=10) 
work_style_collaborative  = st.number_input("Work style collaborative", min_value=0,max_value=10) 
decision_speed  = st.number_input("Decision speed", min_value=0,max_value=10) 
stress_handling  = st.number_input("Stress handling", min_value=0,max_value=10)

input_data = pd.DataFrame({
'social_energy': [social_energy],
'alone_time_preference': [alone_time_preference],
'talkativeness': [talkativeness],
'deep_reflection': [deep_reflection],
'group_comfort': [group_comfort],
'party_liking': [party_liking],
'listening_skill': [listening_skill],
'empathy': [empathy],
'creativity': [creativity],
'organization': [organization],
'leadership': [leadership],
'risk_taking': [risk_taking],
'public_speaking_comfort': [public_speaking_comfort],
'curiosity': [curiosity],
'routine_preference': [routine_preference],
'excitement_seeking': [excitement_seeking],
'friendliness': [friendliness],
'emotional_stability': [emotional_stability],
'planning': [planning],
'spontaneity': [spontaneity],
'adventurousness': [adventurousness],
'reading_habit': [reading_habit],
'sports_interest': [sports_interest],
'online_social_usage': [online_social_usage],
'travel_desire': [travel_desire],
'gadget_usage': [gadget_usage],
'work_style_collaborative': [work_style_collaborative],
'decision_speed': [decision_speed],
'stress_handling': [stress_handling]
})

print(input_data)

expected_order = [
    'social_energy', 'alone_time_preference', 'talkativeness', 'deep_reflection', 'group_comfort', 'party_liking',
    'listening_skill', 'empathy', 'creativity', 'organization', 'leadership', 'risk_taking', 'public_speaking_comfort',
    'curiosity', 'routine_preference', 'excitement_seeking', 'friendliness', 'emotional_stability', 'planning',
    'spontaneity', 'adventurousness', 'reading_habit', 'sports_interest', 'online_social_usage', 'travel_desire',
    'gadget_usage', 'work_style_collaborative', 'decision_speed', 'stress_handling' 
]

print(expected_order)

input_data = input_data.reindex(columns=expected_order)

print(input_data)
 
if st.button("Predict"):
    prediction = model.predict(input_data)
    result_mapping = {0: 'Ambivert', 1: 'Extrovert', 2: 'Introvert'}
    result = result_mapping[prediction[0]]
    st.write(f'The person is: **{result}**')
