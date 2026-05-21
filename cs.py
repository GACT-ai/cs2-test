import streamlit as st

# =============================
# 页面设置
# =============================

st.set_page_config(
    page_title="CS2 命运测试",
    page_icon="🎮",
    layout="centered"
)

# =============================
# CSS样式
# =============================

st.markdown("""
<style>

.stApp {
    background-color: #0d0d0d;
    color: white;
}

h1,h2,h3,p,label {
    color: white !important;
}

.block-container {
    padding-top: 2rem;
}

div[data-baseweb="radio"] label {
    background-color: #1f1f1f;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    transition: 0.3s;
}

div[data-baseweb="radio"] label:hover {
    background-color: #ff7b00;
    color: black !important;
}

.stButton>button {
    background-color: #ff7b00;
    color: black;
    height: 50px;
    width: 100%;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}

.result-box {
    background-color: #1a1a1a;
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #ff7b00;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =============================
# 标题
# =============================

st.title("🎮 CS2 命运测试")
st.subheader("测测你在平行宇宙中会成为怎样的玩家")

st.markdown("---")

# =============================
# 第一题
# =============================

q1 = st.radio(
    "🏜️ 当你穿越到荒漠迷城，CT已经下包。现在地上只剩4件武器，你会捡起：",
    [
        "AK47",
        "AWP",
        "蝴蝶刀",
        "爪子刀"
    ]
)

# =============================
# AK路线
# =============================

if q1 == "AK47":

    q2 = st.radio(
        "🔥 你更希望这把AK是什么风格？",
        [
            "红黑暴力美学",
            "科技未来感",
            "奢华收藏感",
            "野兽压迫感"
        ]
    )

    if q2 == "红黑暴力美学":

        q3 = st.radio(
            "⚡ 下面你只能留一个：",
            [
                "火神",
                "血腥运动",
                "红线",
                "暴怒野兽"
            ]
        )

        result = "你是【极限突破型收藏家】"
        desc = "你偏爱具有压迫感与竞技美学的武器设计。"

    elif q2 == "科技未来感":

        q3 = st.radio(
            "🌌 下面你只能留一个：",
            [
                "霓虹骑士",
                "可燃冰",
                "霓虹革命",
                "抽象派"
            ]
        )

        result = "你是【未来科技型玩家】"
        desc = "你喜欢具有视觉冲击力和未来感的设计。"

    elif q2 == "奢华收藏感":

        q3 = st.radio(
            "💰 下面你只能留一个：",
            [
                "黄金藤蔓",
                "传承",
                "翔鹤",
                "燃料喷射器"
            ]
        )

        result = "你是【收藏家型玩家】"
        desc = "你更偏向稀有感与身份象征。"

    else:

        q3 = st.radio(
            "🐉 下面你只能留一个：",
            [
                "火蛇",
                "暴怒野兽",
                "美洲猛虎",
                "野荷"
            ]
        )

        result = "你是【野性压制型玩家】"
        desc = "你追求最纯粹的压迫感与力量感。"

# =============================
# AWP路线
# =============================

elif q1 == "AWP":

    q2 = st.radio(
        "🎯 作为狙击手，你更喜欢：",
        [
            "一枪震慑全场",
            "冷酷科技感",
            "经典职业风",
            "张扬视觉冲击"
        ]
    )

    if q2 == "一枪震慑全场":

        q3 = st.radio(
            "🐲 下面你只能留一个：",
            [
                "龙狙",
                "美杜莎",
                "九头金蛇",
                "永恒"
            ]
        )

        result = "你是【传奇狙击艺术家】"
        desc = "你喜欢全场聚焦于你开枪的一瞬间。"

    elif q2 == "冷酷科技感":

        q3 = st.radio(
            "🧊 下面你只能留一个：",
            [
                "渐变之色",
                "印花集",
                "克拉考",
                "死神"
            ]
        )

        result = "你是【冷静掌控型狙击手】"
        desc = "你追求精准、冷静与高级感。"

    elif q2 == "经典职业风":

        q3 = st.radio(
            "🏆 下面你只能留一个：",
            [
                "雷击",
                "红线",
                "二西莫夫",
                "野火"
            ]
        )

        result = "你是【职业赛场型玩家】"
        desc = "你偏爱真正属于竞技场的经典设计。"

    else:

        q3 = st.radio(
            "🔥 下面你只能留一个：",
            [
                "鬼退治",
                "暴怒野兽",
                "嘣",
                "蠕虫之神"
            ]
        )

        result = "你是【高调统治型狙击手】"
        desc = "你享受全场目光聚焦于你的感觉。"

# =============================
# 蝴蝶刀路线
# =============================

elif q1 == "蝴蝶刀":

    q2 = st.radio(
        "🦋 你玩刀最在意：",
        [
            "转刀手感",
            "开刀动作",
            "稀有度",
            "纯帅"
        ]
    )

    q3 = st.radio(
        "⚔️ 如果只能选一种刀风格：",
        [
            "渐变系",
            "多普勒系",
            "传说系",
            "原皮竞技风"
        ]
    )

    result = "你是【操作观赏型玩家】"
    desc = "你追求手感、动作与观赏性的极致统一。"

# =============================
# 爪子刀路线
# =============================

else:

    q2 = st.radio(
        "🐺 你觉得爪子刀最吸引你的是：",
        [
            "野性压迫感",
            "暗杀者气质",
            "稀有感",
            "切枪动作"
        ]
    )

    q3 = st.radio(
        "🌑 如果只能选一种风格：",
        [
            "黑红风",
            "紫色系",
            "深海系",
            "低调竞技风"
        ]
    )

    result = "你是【暗影猎杀型玩家】"
    desc = "你更喜欢危险、冷酷与压迫感。"

# =============================
# 结果按钮
# =============================

if st.button("🔥 查看最终命运"):

    st.markdown("---")

    st.markdown(f"""
    <div class="result-box">
        <h1>{result}</h1>
        <p style="font-size:20px;">
        {desc}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🎁 你的本命武器")

    st.success(f"你最终选择了：{q3}")

    st.markdown("---")

    st.info("平行宇宙中的你，已经成为传奇。")
