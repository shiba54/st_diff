from difflib import HtmlDiff

import streamlit as st


def main():
    st.set_page_config(
        page_title='Diff',
        page_icon='☕',
        layout='wide'
    )
    st.title('Diff')
    st.markdown('テキスト差分表示アプリ')

    with st.form(key='content'):
        col_from, col_to = st.columns(2)

        def text_area(label: str, key: str):
            initial_height = 300
            return st.text_area(
                label=label,
                height=initial_height,
                placeholder='テキストを入力してください',
                key=key
            )

        with col_from:
            text_area(
                label=':material/Check: もとのテキスト',
                key='content_from'
            )
        with col_to:
            text_area(
                label=':material/Check: くらべるテキスト',
                key='content_to'
            )

        wrapcolumn = st.number_input(
            label=':material/Check: テキスト差分の折り返しカラム幅',
            min_value=0,
            step=1,
            help='0 で折り返しなし'
        )
        is_context = st.toggle(label='変更点前後のみ表示')

        st.form_submit_button(
            label='差分を表示'
        )

    if st.session_state['content_from'] or st.session_state['content_to']:
        with st.container(border=True):
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
