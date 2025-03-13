import streamlit as st
import time
import random

# Function to show animated effects
def show_animation():
    animations = ["🎈", "✨", "🎊", "🔥", "💥"]
    for _ in range(5):
        st.write("".join(random.choices(animations, k=10)))
        time.sleep(0.2)

# Configure page layout
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="wide")

# Sidebar for navigation
with st.sidebar:
    st.title("🌟 Navigation")
    st.write("Use this sidebar to navigate!")
    st.markdown("---")
    st.write("🔹 **Enter your details below**")
    
# Main UI
st.title('💪 Advanced BMI Calculator')
st.subheader("Welcome to the enhanced BMI Calculator app! 🎉")
st.markdown("Use this tool to calculate your Body Mass Index (BMI) with a modern and interactive UI.")
st.markdown("---")

# Input fields with styled layout
col1, col2 = st.columns(2)
with col1:
    height = st.number_input("📏 Enter your height in meters:", min_value=0.1, format="%.2f", step=0.01)
with col2:
    weight = st.number_input("⚖️ Enter your weight in kilograms:", min_value=0.1, format="%.2f", step=0.1)

# Button to calculate BMI
if st.button("🚀 Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        show_animation()
        st.success(f"✅ Your BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("🏃‍♂️ You're underweight. Consider a balanced diet! 🍎")
        elif 18.5 <= bmi < 24.9:
            st.success("🎯 You have a normal weight. Keep it up! 💪")
        elif 25 <= bmi < 29.9:
            st.info("⚡ You're overweight. Try to stay active! 🏋️‍♂️")
        else:
            st.error("⚠️ You are obese. Consult a healthcare professional. 🏥")
    else:
        st.error("❌ Please enter valid height and weight values!")

# Footer
st.markdown("---")
st.write("💡 **Tip:** Regular exercise and a balanced diet help maintain a healthy BMI!")