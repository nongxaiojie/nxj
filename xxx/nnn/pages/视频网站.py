import streamlit as st
from streamlit.components.v1 import html
st.set_page_config(page_title='视频网站', page_icon='📽')
video_url = [{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/28/27/33323222728/33323222728-1-192.mp4?e=ig8euxZM2rNcNbNV7bdVhwdlhbdjhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=cosovbv&oi=771356656&deadline=1761302316&uipk=5&trid=0551cc84488847e79114ff0fe6422c2h&og=ali&platform=html5&mid=0&nbs=1&gen=playurlv3&upsig=97d39238df612c813f14489deae50423&uparams=e,os,oi,deadline,uipk,trid,og,platform,mid,nbs,gen&bvc=vod&nettype=0&bw=1661917&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
    'title':'📽《辉烬》瑶光角色PV「青冥问心」',
    'episode':'1',
    'introduction':'🐇《辉烬》瑶光 PV「青冥问心」中，浴火重生的 “天命之人” 持剑问心，叹剑能斩邪却难断情，白玉扇与故人是其红尘牵绊。',
    'poster':'https://wallpapers.com/images/hd/cartoon-pictures-cd152iia70gnzx2h.jpg'
    },{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/02/17/33265681702/33265681702-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&deadline=1761302577&os=cosovbv&og=hw&uipk=5&trid=995a605524fd41b5a344ea1097105f1h&platform=html5&oi=771356656&gen=playurlv3&nbs=1&upsig=c25004dbdaf454b5aacbc805996ff5ee&uparams=e,mid,deadline,os,og,uipk,trid,platform,oi,gen,nbs&bvc=vod&nettype=0&bw=657724&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
    'title':'📽天气之肘',
    'episode':'2',
    'introduction':'🐻由于洛杉矶长年不下雨，牢大准备离家出走去寻找传说中的雨姐，但是路途中发现自己处处碰壁，没想到遇见了一个奇怪的大姐姐，后面发现她就是一直要寻找的雨姐，然后影片中后期发生了一件事，完全不受他们的控制，导致了意想不到的结果。',
      'poster':'https://thewowstyle.com/wp-content/uploads/2015/04/wallpaper_cartoons-wallpaper-036-1920x1080-1024x576.jpeg'
    },{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/57/96/31365729657/31365729657-1-192.mp4?e=ig8euxZM2rNcNbNghbdVhwdlhbNghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&uipk=5&gen=playurlv3&os=cosovbv&mid=0&deadline=1761302822&oi=771356656&trid=b279792984914d518ab6f521a9a0cc0h&platform=html5&og=cos&upsig=251ad51db990fe68895047e5d0b83224&uparams=e,nbs,uipk,gen,os,mid,deadline,oi,trid,platform,og&bvc=vod&nettype=0&bw=1784809&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
    'title':'📽乱臣贼子',
    'episode':'3',
    'introduction':'📽“乱臣贼子” 是汉语成语，拼音 luàn chén zéi zǐ，出自《孟子・滕文公下》，原指不忠不孝者，后泛指背叛君主、危害国家与社会的奸邪之人，含贬义。',
    'poster':'https://wallpaperaccess.com/full/111158.jpg'
    }]
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
def play(arg):
      st.session_state['ind'] = int(arg)
current = video_url[st.session_state['ind']]
st.title(f"{current['title']} - 第 {current['episode']}集")
html(f"""<video width="100%" controls poster="{current['poster']}">
 <source src="{current['url']}" type="video/mp4">
</video>
""", height=400)
st.text(current["introduction"])
cols = st.columns(3)
for i in range(len(video_url)):
     with cols[i]:
          st.button(f"第{video_url[i]['episode']}集", use_container_width=True, on_click=play, args=(i,))
