import streamlit as st

st.title("SupplyGuard AI 🚀")

# Inputs
source = st.text_input("Source")
destination = st.text_input("Destination")
delay = st.slider("Delay (days)", 0, 10)
congestion = st.slider("Port Congestion (%)", 0, 100)
weather = st.selectbox("Weather", ["Normal", "Rain", "Storm"])

# Prediction logic
def predict_risk(delay, congestion, weather):
    score = 0
    
    if delay > 3:
        score += 2
    if congestion > 50:
        score += 2
    if weather != "Normal":
        score += 2

    if score >= 5:
        return "HIGH", "Weather + Congestion + Delay"
    elif score >= 3:
        return "MEDIUM", "Some disruption signals"
    else:
        return "LOW", "Stable conditions"

def recommend_action(risk):
    if risk == "HIGH":
        return "Use alternate route or supplier"
    elif risk == "MEDIUM":
        return "Monitor and prepare backup plan"
    else:
        return "Proceed as planned"

# Button
if st.button("Predict Risk"):
    risk, reason = predict_risk(delay, congestion, weather)
    action = recommend_action(risk)

    st.subheader(f"Risk Level: {risk}")
    st.write(f"Reason: {reason}")
    st.write(f"Recommended Action: {action}")
