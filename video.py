import streamlit as st
st.set_page_config(page_title='视频网站', page_icon='📽')
video_url = 'videodir/trailer.mp4'
st.video(video_url)
