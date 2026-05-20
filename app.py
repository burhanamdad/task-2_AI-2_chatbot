import streamlit as st

from rag import retrieve
from llm import ask_llm

st.title(
    "TEYZIX CORE Internal Chatbot"
)

if "messages" not in st.session_state:
    st.session_state.messages=[]


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


query=st.chat_input(
    "Ask your question..."
)

if query:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":query
        }
    )

    with st.chat_message(
        "user"
    ):

        st.write(query)


    docs,metadata=retrieve(
        query
    )

    context="\n".join(docs)


    answer=ask_llm(
        query,
        context
    )


    if metadata and len(metadata) > 0:
       source = metadata[0].get("source", "Unknown")
else:
    source = "No source found"
    with st.chat_message(
        "assistant"
    ):

        st.write(answer)

        st.caption(
            f"Source: {source}"
        )


    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
