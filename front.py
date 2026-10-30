import requests
import streamlit as st

st.title('Распознавание дорожных знаков')

file = st.file_uploader('Загрузите фото знака', type=['jpg', 'jpeg', 'png'])

if file:
    st.image(file, caption='Загруженное фото', width=300)

    if st.button('Определить знак'):
        response = requests.post(
            'http://127.0.0.1:8000/pdd/analyze',
            files={'file': (file.name, file.getvalue(), file.type)}
        )

        if response.status_code == 200:
            data = response.json()
            st.success('Знак определён')
            st.write('Номер класса:', data['class_id'])
            st.write('Название:', data['class_name'])
            st.write('Категория:', data['category'])
            st.write('Описание:', data['description'])
        else:
            st.error('Ошибка: ' + response.text)