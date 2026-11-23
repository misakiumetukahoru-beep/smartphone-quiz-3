
import streamlit as st

st.set_page_config(page_title="スマホ操作クイズ第3弾", page_icon="📱")

st.title("📱 スマホ操作クイズ 第3弾")
st.write("スマホを安全・便利に使うためのクイズです！")
st.write("全5問・3択です。満点を目指しましょう！")

questions = [
    {
        "question": "スマホに更新のお知らせが来たら？",
        "choices": [
            "どんな通知でもすぐ押す",
            "設定や公式アプリから更新を確認する",
            "すべての更新を無視する"
        ],
        "answer": 1,
        "explanation": "更新は安全性を高めます。偽の通知には注意しましょう。"
    },
    {
        "question": "アプリが位置情報の利用を求めたら？",
        "choices": [
            "必要性を確認して許可を選ぶ",
            "すべてのアプリに常に許可する",
            "必ずスマホの電源を切る"
        ],
        "answer": 0,
        "explanation": "位置情報は必要なアプリだけに許可しましょう。"
    },
    {
        "question": "スマホの文字が小さくて読みにくいときは？",
        "choices": [
            "画面を強く押す",
            "スマホを振る",
            "設定から文字サイズを変更する"
        ],
        "answer": 2,
        "explanation": "設定の画面表示などから文字を大きくできます。"
    },
    {
        "question": "写真を間違って削除したときは？",
        "choices": [
            "すぐにスマホを初期化する",
            "写真アプリのゴミ箱などを確認する",
            "必ず復元できないので諦める"
        ],
        "answer": 1,
        "explanation": "写真アプリによっては一定期間、削除した写真が残ります。"
    },
    {
        "question": "公共Wi-Fiを利用するときの注意は？",
        "choices": [
            "接続先を確認し、重要な操作は慎重に行う",
            "名前が似ていれば必ず安全",
            "Wi-Fiならどこでも安全"
        ],
        "answer": 0,
        "explanation": "偽のWi-Fiに注意し、接続先を確認しましょう。"
    }
]

answers = []

with st.form("quiz_form"):
    for i, q in enumerate(questions):
        st.subheader(f"第{i + 1}問")
        st.write(q["question"])

        choice = st.radio(
            "答えを選んでください",
            q["choices"],
            index=None,
            key=f"question_{i}"
        )
        answers.append(choice)

    submitted = st.form_submit_button("📝 採点する")

if submitted:
    if any(answer is None for answer in answers):
        st.warning("まだ答えていない問題があります。")
    else:
        score = 0

        for i, q in enumerate(questions):
            st.write(f"**第{i + 1}問**")

            selected = q["choices"].index(answers[i])

            if selected == q["answer"]:
                st.success("⭕ 正解！")
                score += 20
            else:
                st.error("❌ 残念！")

            st.write(
                "正解：" + q["choices"][q["answer"]]
            )
            st.info(q["explanation"])

        st.header(f"🎯 あなたの得点：{score}点 / 100点")

        if score == 100:
            st.balloons()
            st.success("🎉 全問正解！おめでとうございます！")
        else:
            st.write("また挑戦してみましょう！")
