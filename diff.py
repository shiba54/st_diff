from difflib import HtmlDiff

import streamlit as st


def main():
    st.set_page_config(
        page_title='Diff',
        page_icon='☕',
        layout='wide'
    )
    st.title('Diff')
    st.write('テキスト差分表示アプリ')

    with st.form(key='content'):
        col_from, col_to = st.columns(2)

        def text_area(key: str):
            initial_height = 300
            return st.text_area(
                label='_',
                height=initial_height,
                placeholder='テキストを入力してください',
                label_visibility='collapsed',
                key=key
            )

        with col_from:
            st.write(':material/Check: もとのテキスト')
            text_area(key='content_from')
        with col_to:
            st.write(':material/Check: くらべるテキスト')
            text_area(key='content_to')

        col1, col2, col3 = st.columns(3, vertical_alignment='bottom')
        with col1:
            st.write(':material/Check: テキスト差分の折り返しカラム幅')
            wrapcolumn = st.number_input(
                label='_',
                min_value=0,
                step=1,
                label_visibility='collapsed'
            )
        with col2:
            st.caption('0 で折り返しなし')
        with col3:
            st.write(':material/Check: 変更点前後のみ表示')
            is_context = st.toggle(
                label='_',
                label_visibility='collapsed'
            )

        st.form_submit_button(
            label='差分を表示',
            type='primary'
        )

    if st.session_state['content_from'] or st.session_state['content_to']:
        st.write(':sparkles: テキスト差分')

        diff = HtmlDiff(wrapcolumn=wrapcolumn)
        diff._styles += 'td {background-color: white; color: black;}' # type: ignore

        html_diff = diff.make_file(
            fromlines=st.session_state['content_from'].splitlines(),
            tolines=st.session_state['content_to'].splitlines(),
            context=is_context
        )

        st.html(body=html_diff)

    st.markdown("""
    * ブラウザ更新でリセットできます
    """)

if __name__ == '__main__':
    main()
