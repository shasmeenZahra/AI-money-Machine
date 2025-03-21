import streamlit as st
import random

def generate_business_idea():
    ideas = [
        "Start a dropshipping business",
        "Create an affiliate marketing website",
        "Develop a subscription-based service",
        "Invest in cryptocurrency and NFTs",
        "Sell digital products like e-books or courses",
        "Start a YouTube channel and monetize content",
        "Create and sell AI-generated artwork",
        "Build a mobile app with in-app purchases"
    ]
    return random.choice(ideas)

def calculate_savings(income, expenses, percentage):
    savings = (income - expenses) * (percentage / 100)
    return max(savings, 0)

def main():
    st.title("💰 AI-Powered Money Making Machine 💰")
    
    st.header("📈 Business & Passive Income Ideas")
    if st.button("Generate Money-Making Idea"):
        st.success(generate_business_idea())
    
    st.header("💵 Savings & Investment Calculator")
    income = st.number_input("Enter your monthly income ($):", min_value=0)
    expenses = st.number_input("Enter your monthly expenses ($):", min_value=0)
    percentage = st.slider("Select savings percentage:", 0, 100, 20)
    
    if st.button("Calculate Savings"):
        savings = calculate_savings(income, expenses, percentage)
        st.success(f"You should save ${savings:.2f} per month!")
    
    st.header("🛠 More Features Coming Soon!")
    st.write("✅ AI-powered job & freelancing suggestions")
    st.write("✅ Automated stock & crypto market analysis")
    st.write("✅ AI-driven financial planning & tracking")
    
if __name__ == "__main__":
    main()
