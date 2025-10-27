import streamlit as st
import importlib. util 
import os
st.image('https://2.bp.blogspot.com/-NvgNKrfZKms/UQ_WUzKbzzI/AAAAAAAAS3A/hl0QLyDoNxo/s1600/Tom+and+Jerry+Funny+Pics+(1).jpg', width=200)
st.title("我的应用") 
file_names =[
     "图片",
     "简历", 
     "美食", 
     "视频", 
     "档案",
     "music"] 
tabs = st. tabs (file_names) 
for i, tab in enumerate(tabs): 
  with tab: 
     file_name = file_names [i] 
     file_path = os.path.join('pagess', f'{file_name}.py')
     spec =importlib.util.spec_from_file_location(file_name, file_path) 
     module = importlib.util.module_from_spec(spec) 
     spec.loader.exec_module(module)
