import streamlit as st

# Growth mindset messages
growth_messages = [
    "Every mistake is a step toward success! 🚀",
    "Progress, not perfection! Keep going. 💪",
    "Challenges help us grow. Stay strong! 🌱",
    "Small steps lead to big achievements! 🔥",
    "You're improving every day! Keep learning. 📚"
]

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 Growth Mindset To-Do List")

# Input for new task
new_task = st.text_input("Enter a task:", key="new_task")

# Add task button
if st.button("➕ Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success("Task added successfully! ✅")
    else:
        st.warning("Please enter a task before adding.")

# Show tasks
st.subheader("Your Tasks:")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        col1.write(f"✅ {task}")
        if col2.button("❌ Remove", key=f"del_{i}"):
            del st.session_state.tasks[i]
            st.experimental_rerun()

# Show a random growth mindset message
if st.session_state.tasks:
    st.write("💡 **Growth Mindset Tip:**")
    st.info(random.choice(growth_messages))
