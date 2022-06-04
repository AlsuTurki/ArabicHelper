import streamlit as st
import pyarabic.araby as ar
import pyarabic.number as an
import pyarabic.trans as tr
from pyarabic.unshape import unshaping_word



st.set_page_config(
    page_title="Your Arabic Helper",
    page_icon="🎈")



# Title of the main page
st.title("Your Arabic Helper")


def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    # st.image("logo.png", width=400)
    st.title("")
    st.header("")


with st.expander("ℹ️  - About this app", expanded=True):

    st.write(
        """     
The app is an easy-to-use interface built in Streamlit to help you with:

 - Arabic letters classification
 - Text tokenization into words or sentences
 - Strip Harakat ( all, except Shadda, tatweel, last_haraka)
 - Sperate and join Letters and Harakat
 - Reduce tashkeel
 - Mesure tashkeel similarity ( Harakats, fully or partially vocalized, similarity with a template)
 - Letters normalization ( Ligatures and Hamza)
 - Numbers to words
 - Extract numerical phrases
 - Pre-vocalization of numerical phrases
 - Unshiping texts

 #### Contribute
 
 This an open source project and you are very welcome to **contribute** your awesome comments, questions, resources and apps as [issues](https://github.com/AlsuTurki/ArabicHelper/issues) of or
 [pull requests](https://github.com/AlsuTurki/ArabicHelper/pulls) to the [source code](https://github.com/AlsuTurki/ArabicHelper). 
 
 This app is maintained by **Alsu Turki**.
	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## **📌 Paste document **")
with st.form(key="my_form"):


    ce, c1, ce, c2, c3 = st.columns([0.07, 2, 0.07, 5, 0.07])
    with c1:

        ModelType = st.selectbox(
            "Select Your Method",
            ["strip tashkeel",
            "strip harakat",
            "strip lastharaka",
            "strip tatweel",
            "normalize hamza",
            "tokenize",
            "sentence tokenize",
            "tokenize with location"
            "number to words",
            "number to ordinal words",
            "arabic text into number",
            "Extract number words in a text",
            "Extract number words in a text with context",
            "Normalize digits",
            "Unshape a word",
            ]
         )
        if ModelType == 'strip tashkeel':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return ar.strip_tashkeel(text)
        if ModelType == 'strip harakat':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return ar.strip_harakat(text)            
        if ModelType == 'strip lastharaka':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return ar.strip_lastharaka(text)
        if ModelType == 'strip tatweel':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return ar.strip_tatweel(text)
        if ModelType == 'normalize hamza':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return ar.normalize_hamza(text)
        if ModelType == 'tokenize':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return ar.tokenize(text)
        if ModelType == 'sentence tokenize':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return ar.sentence_tokenize(text)
        if ModelType == 'tokenize with location':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return ar.tokenize_with_location(text)
        if ModelType == 'number to words':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return an.ArNumbers.int2str(text)
        if ModelType == 'number to ordinal words':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return an.number2ordinal(text)       
        if ModelType == 'arabic text into number':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return an.text2number(text)
        if ModelType == 'Extract number words in a text':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return an.extract_number_phrases(text)        
        if ModelType == 'Extract number words in a text with context':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return an.extract_number_context(text)
        if ModelType == 'Normalize digits':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return tr.normalize_digits(text, source='all', out='west')
        if ModelType == 'Unshape a word':
            @st.cache(allow_output_mutation=True)
            def load_model(text):
                return unshaping_word(text)
    with c2:
        doc = st.text_area(
            "Paste your text below (max 1000 words)",
            height=300,
        )

        MAX_WORDS = 1000
        import re
        res = len(re.findall(r"\w+", doc))
        if res > MAX_WORDS:
            st.warning(
                "⚠️ Your text contains "
                + str(res)
                + " words."
                + " Only the first 1000 words will be reviewed. Stay tuned as increased allowance is coming! 😊"
            )

            doc = doc[:MAX_WORDS]
        

        output = load_model(doc)

        submit_button = st.form_submit_button(label="✨ Get me the data!")

        if  submit_button:
            st.markdown("## **🎈 Check results **")

            st.text_area(label ="",value=output, height =300)


if not submit_button:
    st.stop()

