import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon='🔐')

st.title('🔐 Password Strength Checker')
st.markdown('''
## Welcome to the Ultimate Password Strength Checker! 🔐  
Use this simple tool to check the strength of your password and get tips on how to make it much stronger.  
We’ll help you create a **strong password** with actionable advice.
''')

password = st.text_input('Enter your password', type='password')
feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append('Password should be at least 8 characters long.')

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append('Password should contain both uppercase and lowercase letters.')

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append('Password should contain at least one digit.')

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append('Password should contain at least one special character (!@#$%^&* etc).')

    # Final evaluation
    if score == 4:
        st.success('✅ Your password is strong!')
    elif score == 3:
        st.warning('⚠️ Your password is medium strength. Consider improving it.')
    else:
        st.error('❌ Your password is weak. Please strengthen it.')

    if feedback:
        st.markdown('## 🔧 Improvement Suggestions:')
        for tip in feedback:
            st.write(f"- {tip}")
else:
    st.info('Please enter your password to get started.')
