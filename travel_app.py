import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("✈️ Travel Budget Planner")

st.write("### Trip Details")

col1, col2 = st.columns(2)
destination = col1.text_input("Destination", value="Tokyo")
flight_cost = col1.number_input("Flight Cost ($)", min_value=0, value=1200)
hotel_per_night = col2.number_input("Hotel Cost per Night ($)", min_value=0, value=150)
num_days = col2.number_input("Number of Days", min_value=1, value=7)

st.write("### Budget")
daily_budget = st.number_input("Daily Spending Budget ($)", min_value=0, value=100)

total_hotel_cost = hotel_per_night * num_days
total_spending_budget = daily_budget * num_days
total_estimated_cost = flight_cost + total_hotel_cost + total_spending_budget

st.write("### Your Total Trip Budget")
total_budget = st.number_input("Total Budget ($)", min_value=0, value=3000)
budget_difference = total_budget - total_estimated_cost
budget_status = "Under Budget" if budget_difference >= 0 else "Over Budget"

st.write("### Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Total Estimated Cost", f"${total_estimated_cost:,.2f}")
col2.metric("Budget Difference", f"${budget_difference:,.2f}", delta_color="normal" if budget_difference >= 0 else "inverse")
col3.metric("Status", budget_status)

st.write("### Cost Breakdown")

cost_data = pd.DataFrame({
    "Category": ["Flights", "Hotel", "Spending"],
    "Cost": [flight_cost, total_hotel_cost, total_spending_budget]
})

# Dark-themed pie chart
fig, ax = plt.subplots(figsize=(3, 3), facecolor='none')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c'] 

wedges, texts, autotexts = ax.pie(
    cost_data["Cost"],
    labels=cost_data["Category"],
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'color': 'white'}
)

ax.axis('equal')  
fig.patch.set_alpha(0.0)  
for text in texts + autotexts:
    text.set_color('white') 

st.pyplot(fig)

st.write("### Cost Table")
st.dataframe(cost_data.set_index("Category"))

