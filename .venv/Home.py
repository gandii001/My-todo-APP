import streamlit as st
import myfunctions
from streamlit import checkbox

todos = myfunctions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    myfunctions.write_todos(todos)



st.title('My Todo app')
st.subheader('This is ')
st.write('This app is to increase your productivity')

for index,todo in enumerate(todos):
     checkbox = st.checkbox(todo, key=todo)
     if checkbox:
        todos.pop(index)
        myfunctions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()




st.text_input(label='Enter a todo: ', placeholder='Enter todo',
              on_change=add_todo,key='new_todo')




print('hello')