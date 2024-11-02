import streamlit as st
from datetime import datetime
from openai import OpenAI
import random

# OpenAI API Key
openai_api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_api_key)


# チャット関数の定義
def chat(message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        response_format={
            "type": "text"
        }
    )
    return response.choices[0].message.content


# アプリのレイアウト
st.title("🎉 誕生日お祝いアプリ 🎉")
st.write("あなたの誕生日から今日までの日数を計算し、お祝いメッセージを送ります。")

# 誕生日の入力
birthday_input = st.text_input("誕生日をYYYY-MM-DD形式で入力してください:")

# 日数計算とお祝いメッセージ生成
if birthday_input:
    try:
        birthday_date = datetime.strptime(birthday_input, "%Y-%m-%d")
        today = datetime.now()
        days_since_birth = (today - birthday_date).days

        # メッセージスタイルと引用の選択
        styles = {
            "1": "丁寧なアナウンサー",
            "2": "大阪のおばちゃん",
            "3": "体育会系熱血先生",
            "4": "プロレスアナウンサー",
            "5": "田舎のおばあちゃん"
        }

        quotes = {
            "1": "聖書",
            "2": "日本のことわざ、慣用句",
            "3": "中国の古典",
            "4": "古今東西の名言",
            "5": "歌詞の一フレーズ"
        }
        style_choice = styles[str(random.randint(1, 5))]
        quote_choice = quotes[str(random.randint(1, 5))]

        # お祝いメッセージの生成
        message = f"今日は、私が生まれてから{days_since_birth}日目です。{quote_choice}を引用して、{style_choice}の口調でお祝いしてください！"
        celebration_message = chat(message)

        # 出力
        st.write(f"**誕生日から今日までの日数:** {days_since_birth}日")
        st.write("🎉 お祝いメッセージ 🎉")
        st.write(celebration_message)

    except ValueError:
        st.error("日付の形式が正しくありません。YYYY-MM-DD形式で入力してください。")
