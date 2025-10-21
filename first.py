import pandas as pd
import streamlit as st
st.title("🐈小猫 核桃-数字档案")
st.header("🧭基础信息")
st.image("https://img95.699pic.com/photo/60067/3115.jpg_wh860.jpg", width=100)
st.text("主人ID:NEO-2025-D11")
st.markdown("**注册时间: :green[2025-10-20 11:11:10] |精神状态:✅正常**")
st.markdown("**当前所在宠物店: :green[小宠当家] |安全等级:✨:green[绝密]**")
st.markdown("**品种: :green[英短银渐层]**")
st.header("📊技能矩阵")
c1, c2, c3 = st.columns(3)
c1.metric(label="踩奶",help="技能", value="98%", delta="3%")
c2.metric(label="接逗猫棒",help="技能", value="85%", delta="-2%")
c3.metric(label="躲猫猫",help="技能", value="72%", delta="-5%")
st.header("💰任务日志")
data = {
    '任务':["消灭沙发上的羽毛",  "监督主人倒猫粮",  "霸占键盘阻止工作"],
    '状态':["完成",  "进行中",  "未完成"],
    '难度':["⭐⭐",  "⭐⭐⭐",  "⭐⭐⭐⭐"],
}
index = pd.Series(["2025-10-18", "2025-10-19", "2025-10-20"], name="日期")
df = pd.DataFrame(data, index=index)

st.subheader("静态表")
st.table(df)
st.header("🔐最新代码成果")
st.subheader("日常作妖")
python_code = '''def 日常作妖(主人在工作，键盘空闲):
                                   print("已跳上键盘，开始踩按键~")
'''
st.code(python_code, language=None)
st.code(python_code)
st.code(python_code, line_numbers=True)
st.write(":green[>>SYSTEM HESSAGE:] 下一个任务目标已解锁……")
st.write(":green[>>TARGET:]  打翻主人水杯")
st.write(":green[>>COUNTDOWN:] 2025-10-21  09:30:20")
st.write("系统状态:  在线  |  连接状态:  已加密")
