import streamlit as st
import random
st.set_page_config(page_title='音乐播放器', page_icon='🎙')
images = [
    {
        'title': '玫瑰窃贼🎧',
        'url': 'https://music.163.com/song/media/outer/url?id=2750516473.mp3',
        'parm': '专辑封面',
        'photo': 'https://p2.music.126.net/zjNghQlICtm9hrqUUUzQJw==/109951171674408769.jpg?param=200y200',
        'author': '云浠',
        'time': '3:15🕐'
    },
    {
        'title': '我记得🎧',
        'url': 'https://music.163.com/song/media/outer/url?id=1974443814.mp3',
        'parm': '专辑封面',
        'photo': 'https://p2.music.126.net/9bVOooAY6U6EJLzpv1Fikw==/109951169682871673.jpg?param=200y200',
        'author': '赵雷',
        'time': '5:29🕐'
     },
    {
        'title': '黑夜问白天🎧',
        'url': 'https://music.163.com/song/media/outer/url?id=2751381348.mp3',
        'parm': '专辑封面',
        'photo': 'https://p2.music.126.net/lEpbaWjrZnJcLn1bLiZJ9A==/109951172085778809.jpg?param=200y200',
        'author': '林俊杰/胡彦斌',
        'time': '4:31🕐'
    },
    {
        'title': '演员🎧',
        'url': 'https://music.163.com/song/media/outer/url?id=1357774367.mp3',
        'parm': '专辑封面',
        'photo': 'https://p2.music.126.net/qmhlhk-Sa5If1iD485n1dA==/109951163133349763.jpg?param=200y200',
        'author': '赵英俊/薛之谦',
        'time': '4:19🕐'
    },
   {
        'title': '夏夜晚风🎧',
        'url': 'https://music.163.com/song/media/outer/url?id=34200650.mp3',
        'parm': '专辑封面',
        'photo': 'https://p1.music.126.net/cpoUinrExafBHL5Nv5iDHQ==/109951166361218466.jpg?param=200y200',
        'author': '田馥甄',
        'time': '2:51🕐'
    }
]
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
if 'shuffle' not in st.session_state:
    st.session_state['shuffle'] = False
def nextImg():
      if st.session_state['shuffle']:
           current_ind = st.session_state['ind']
           candidate_inds = [i for i in range(len(images)) if i != current_ind]
           st.session_state['ind'] = random.choice(candiadate_inds)
      else:
           st.session_state['ind'] = (st.session_state['ind'] + 1) % len(images)
def prevImg():
           st.session_state['ind'] = (st.session_state['ind'] - 1) % len(images)
st.title('🎶简易音乐播放器')
st.subheader('   👏  使用Streamlit 制作的简单音乐播放器，支持切歌和基本播放控制')
st.session_state['shuffle'] = st.checkbox('🔀开启随机播放', value=st.session_state['shuffle'])
col_covel, col_info = st.columns([1,2], gap='medium')
with col_covel:
      current = images[st.session_state['ind']]
      st.image(current['photo'], width=200)
      st.caption(current['parm'])
with col_info:
      st.header(current['title'])
      st.text(f"歌手: {current['author']}")
      st.text(f"时长: {current['time']}")
      c1, c2 = st.columns(2)
      with c1:
          st.button('⏮上一首', on_click=prevImg, use_container_width=True)
      with c2:
          st.button('⏭下一首', on_click=nextImg, use_container_width=True)
st.audio(current['url'])





     
