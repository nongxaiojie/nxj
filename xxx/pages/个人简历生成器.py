import streamlit as st
from datetime import datetime, timedelta
from datetime import datetime, time
st.set_page_config(page_title='个人简历', page_icon='📋')
st.set_page_config(layout='wide')
st.header('🎉个人简历生成器')
st.text('使用Streamlit创建您的个人简历')
c1, c2 = st.columns([1,2])
with c1:
    st.subheader('个人信息表单') 
    st.markdown('<hr style="border:3px solid gold;">', unsafe_allow_html = True)  
    name = st.text_input('姓名')
    position = st.text_input('职位')
    telephone = st.text_input('电话')
    email = st.text_input('邮箱')
    date = st.date_input('日期', value=None)
    st.write('性别')
    gender = st.radio(
       label='请选择性别',
       options=['男','女','其他'],
       horizontal=True,
       label_visibility='hidden')
    graduate = st.text_input('毕业院校')
    major = st.text_input('所学专业')
    st.write('学历')
    educational_background = st.selectbox('选择你的学历',
                                      ['高中', '专科', '本科', '硕士', '博士'],
                                      label_visibility='collapsed')
    st.write('语言能力')
    language_ability = st.multiselect('选择你的语言',
                                      options=['中文', '英语', '日语', '法语', '德语', '西班牙语'],
                                      label_visibility='collapsed')
    st.write('技能(可多选)')
    skills = st.multiselect(
                           label='选择你的技能',
                           options=['Java', 'Python', '数据分析', '数据可视化', 'HTML/CSS', 'JavaScript', 'SQL'],
                           label_visibility='collapsed' )
    st.write('证书(可多选)')
    certificates= st.multiselect(
                           label='选择你的证书',
                           options=['计算机二级', '数据分析师认证(CAD)', '谷歌数据分析证书', '注册信息安全工程师', '网络安全工程师'],
                           label_visibility='collapsed' )
    st.write('工作经验(年)')
    age = st.slider(label='选择你的工作经验',
                    min_value=0,
                    max_value=30,
                    value=0,
                    label_visibility='collapsed')
    st.write('期望薪资范围(元)')
    salary_options  = list(range(5000,50001,5000))
    start_salary, end_salary = st.select_slider(label='选择你期望的薪资',
                                              options=salary_options,
                                              value=(10000,30000),
                                              label_visibility='collapsed')
    personal_intro = st.text_area(label='个人简介', placeholder='请简要介绍您的专业背景、职业目标和个人特点……')
    personal_intro = st.text_area(label='工作经历', placeholder='请简要介绍您的工作经历……')
    st.write('每日最佳联系时间段')
    time_options = []
    for hour in range(24):
        for minute in [0,15,30,45]:
            time_options.append(f'{hour:02d}:{minute:02d}')
    best_contact_time = st.selectbox(label='选择时间段',
                                     options=time_options,
                                     index=time_options.index('01:15'),
                                     label_visibility='collapsed')
    st.write('上传个人照片')
    photo = st.file_uploader(label='上传照片',
                             type=['jpg', 'jpeg', 'png'],
                             accept_multiple_files=False,
                             label_visibility='collapsed')
    
with c2:
    st.subheader('简历实时预览')
    st.markdown('<hr style="border:3px solid gold;">', unsafe_allow_html = True)
    st.title(f'{name}')
    if photo:
        st.image(photo, width=150)
    else:
        st.image('https://via.placeholder.com/150', width=150)
    a1, a2, a3 = st.columns(3)
    with a1:
        st.text(f'职位:{position}')
        st.text(f'电话:{telephone}')
        st.text(f'邮箱:{email}')
        st.text(f'出生日期:{date}')
    with a2:
        st.text(f'性别:{gender}')
        st.text(f'毕业院校:{graduate}')
        st.text(f'所学专业:{major}')
        st.text(f'学历:{educational_background}')
       
    with a3:
        st.text(f'工作经验:{age}年')
        st.text(f'期望薪资:{start_salary}-{end_salary}元')
        st.text(f'最佳联系时间:{best_contact_time}')
        st.text(f'语言能力:{",".join(language_ability)}')
    st.markdown('<hr style="border:1px solid silver;">', unsafe_allow_html = True)
    st.subheader('个人简介👩')
    st.write(personal_intro if personal_intro else'这个人很神秘，没有留下任何介绍……')
    st.subheader('工作经历🌐')
    st.write(personal_intro if personal_intro else'简述您的工作经历……')
    st.subheader('专业技能👩‍🔧')
    if skills:
        for skill in skills:
            st.write(skill)
    st.subheader('所获证书📚')
    if certificates:
        for certificate in certificates:
            st.write(certificate)
   
 
