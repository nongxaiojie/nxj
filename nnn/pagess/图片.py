import streamlit as st
st.set_page_config(page_title='动物园', page_icon='🐑')
images = [
    {
        'url': 'https://anzen-dogfood.com/wp-content/uploads/2019/02/dog-3635504_960_720-1.jpg',
        'parm': '狗'
     },
    {
        'url': 'https://wallup.net/wp-content/uploads/2016/01/195009-animals-cat.jpg',
        'parm':'猫'
    },
    {
        'url':'https://birdwatchinghq.com/wp-content/uploads/2021/10/bluebird-featured-image-scaled.jpg',
        'parm': '鸟'
    }
]
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)
def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)
st.image(images[st.session_state['ind']]['url'], caption=images[st.session_state['ind']]['parm'])
c1, c2 = st.columns(2)
with c1:
    st.button('上一张', on_click=prevImg, use_container_width=True)
with c2:
    st.button('下一张', on_click=nextImg, use_container_width=True)


