import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('MY Menu',('home','fill form','downloads'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/Untitled_design__6_-removebg-preview-1-150x84.png')
st.title('onlei Technologies')
st.header('By abhinav srivastava')
st.text('this is a python tutorial on streamlit library')
if(mymenu=='home'):
    st.markdown('<centre><h1>WELCOME</h1></centre>',unsafe_allow_html=True)
    st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/kisspng-python-programming-language-computer-programming-language-5acfdc365292a6.6915108915235717663382.png')
    st.video('https://www.youtube.com/watch?v=0D0cgVPhxUw')
elif(mymenu=='fill form'):
     with st.form('My form'):
       name=st.text_input('enter name')
       dob=st.date_input('choose date of birth')
       marks=st.slider(' choose marks')
       k=st.form_submit_button("submit form")
       if k:
           st.write('name:',name,'dob:',dob,'marks:',marks)
elif(mymenu=='downloads'):
     st.header('downloads')
     st.download_button('download now','this is the downloaded data','onlei.txt')