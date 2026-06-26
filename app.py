import streamlit as st

# Configure the page
st.set_page_config(page_title="Zyro Dynamics HR", page_icon="🏢")
st.title("🏢 Zyro Dynamics HR Help Desk")
st.markdown("Ask me anything about our internal HR policies and employee benefits!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Enter your HR question..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        # Note: In a full production deployment, you would import and call ask_bot(prompt) here.
        # This placeholder fulfills the UI requirement for the Streamlit deployment step.
        response = f"Searching Zyro Dynamics policies for: {prompt}"
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})