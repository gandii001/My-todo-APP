import streamlit as st
import functions

st.set_page_config(layout="wide")
todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title('My Todo app')

st.subheader('This is a subheading')
st.write('This app is to increase your <b>productivity</b>',
         unsafe_allow_html=True)  #unsafeallowhtml allows html to be used in the string



for todo in todos:
    st.checkbox(todo)
    #if checkbox:
     #   todos.pop(index)
      #  functions.write_todos(todos)
       # del st.session_state[todos]
        #st.rerun()


st.text_input(label='', placeholder='Add the new todo',
              on_change=add_todo,key='new_todo')






print('hello')