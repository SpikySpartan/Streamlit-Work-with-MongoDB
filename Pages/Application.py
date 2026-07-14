import base64
import os
import streamlit as st


st.set_page_config(page_title="Math Playground", page_icon="🧠", layout="centered")
#..........Background Image and Styling..........

def get_base64_image(image_path: str) -> str:
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""


def render_source_code(code_snippet: str, use_expander: bool = True) -> None:
    if use_expander:
        with st.expander("Source Code", expanded=True):
            st.code(code_snippet)
    else:
        st.markdown("### Source Code")
        st.code(code_snippet)


bg_base64 = get_base64_image("images/Color2.png")
if bg_base64:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(180deg, rgba(12, 28, 56, 0.94), rgba(4, 12, 32, 0.96)),
                        url("data:image/jpg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        div[data-testid="stContainer"] {{
            background-color: rgba(5, 12, 28, 0.88) !important;
            backdrop-filter: blur(12px);
            border: 1px solid rgba(56, 189, 248, 0.24) !important;
            border-radius: 24px;
            padding: 30px 32px 32px 32px;
        }}

        .main-title {{
            color: #7dd3fc !important;
            font-size: 3.2rem !important;
            font-weight: 800 !important;
            text-align: center !important;
            margin-bottom: 0.2rem !important;
        }}

        .subtitle {{
            color: #cbd5e1 !important;
            font-size: 1rem !important;
            text-align: center !important;
            margin-bottom: 1.2rem !important;
            line-height: 1.6 !important;
        }}

        .section-heading {{
            color: #38bdf8 !important;
            font-size: 1.5rem !important;
            margin-top: 1.4rem !important;
            margin-bottom: 0.8rem !important;
            border-bottom: 1px solid rgba(56, 189, 248, 0.28);
            padding-bottom: 0.35rem !important;
        }}

        .tool-card {{
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(96, 165, 250, 0.18);
            border-radius: 18px;
            padding: 18px 20px;
            margin-bottom: 20px;
        }}

        .tool-card p {{
            color: #e2e8f0 !important;
            margin: 0.35rem 0 0.8rem 0;
        }}

        .stButton>button {{
            background: linear-gradient(90deg, #0ea5e9, #38bdf8) !important;
            color: #020617 !important;
            font-weight: 700 !important;
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.14) !important;
            box-shadow: 0 10px 24px rgba(56, 189, 248, 0.18) !important;
        }}

        .stButton>button:hover {{
            transform: scale(1.01);
        }}

        pre, code {{
            white-space: pre-wrap !important;
            word-break: break-word !important;
            overflow-x: hidden !important;
            overflow-y: visible !important;
            max-height: none !important;
        }}

        .stCodeBlock, .stMarkdown pre {{
            overflow-x: hidden !important;
            overflow-y: visible !important;
            max-height: none !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

#.............button styling.........

st.html("""
    <style>
    .st-key-B1{
        background-color: transparent !important;
        color: #e2e8f0 !important;
        border-radius: 10px !important; 
        border: 2px solid rgba(56, 189, 248, 0.45) !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 10px 24px !important;
        transition: 0.3s;
    }
    
    /* Hover effect */
    .st-key-B1 button:hover {
        background-color: rgba(56, 189, 248, 0.16) !important;
        transform: scale(1.05);
    }
    </style>
""")
#.............check if user is logged in........

if st.session_state.get("username", False):
    st.success(f"Welcome :{st.session_state['username']}")
else:
    st.error("⚠️ System Alert: You must be logged in to access this page.")
    st.stop()
col1, col2 = st.columns([2,1])
with col2:
    if st.button("Settings ⚙️", key="B1"):
        st.switch_page("pages/profile.py")
with col1:
    st.markdown("# <span class='main-title'>Math Playground</span>", unsafe_allow_html=True)

#.............Main Application Logic........

st.markdown("<div class='section-heading'>Select a section</div>", unsafe_allow_html=True)
selected_tab = st.radio("Choose a tool area", ["Number Tools", "String Tools", "Calculator","Notes", "Quiz"], horizontal=True,key="R1")

#.............Number Tools Section........
#..factorial, table, greatest, prime/even/odd, palindrome/armstrong/reverse....

if selected_tab == "Number Tools":
    st.markdown("<div class='section-heading'>Number Tools</div>", unsafe_allow_html=True)
    number_tool = st.selectbox(
        "Choose a number tool",
        ["Factorial", "Table", "Greatest", "Prime & Even/Odd", "Palindrome / Armstrong"],
        key="number_tool_selector",
    )

    if number_tool == "Factorial":
        st.markdown("<div class='section-heading'>Factorial Calculator</div>", unsafe_allow_html=True)
        st.markdown("<div class='tool-card'><p>Factorials values up to 50.</p></div>", unsafe_allow_html=True)
        fact_n = st.number_input("Choose a number", min_value=0, max_value=50, value=6, step=1, key="fact_n")
        calc_col, source_col = st.columns([3, 4])
        with calc_col:
            if st.button("Calculate Factorial", key="fact_button"):
                factorial = 1
                for i in range(1, fact_n + 1):
                    factorial *= i
                st.success(f"{fact_n}! = {factorial}")
        with source_col:#..source code display...
            with st.expander("Source Code"):
                st.code('''fact_n = st.number_input("Choose a number", min_value=0, max_value=50, value=6, step=1, key="fact_n")
if st.button("Calculate Factorial", key="fact_button"):
    factorial = 1
    for i in range(1, fact_n + 1):
        factorial *= i
    st.success(f"{fact_n}! = {factorial}")''',
            )

    elif number_tool == "Table":
        st.markdown("<div class='section-heading'>Generate Multiplication Table</div>", unsafe_allow_html=True)
        st.markdown("<div class='tool-card'><p>Multiplication table for any integer.</p></div>", unsafe_allow_html=True)
        table_num = st.number_input("Number for table", min_value=0, max_value=100, value=7, step=1, key="table_num")
        table_len = st.slider("Table length", 1, 20, 12, key="table_len")
        calc_col, source_col = st.columns([3, 4])
        with calc_col:
            if st.button("Generate Table", key="table_button"):
                st.write(f"**Multiplication table for {table_num}:**")
                for i in range(1, table_len + 1):
                    st.write(f"{table_num} × {i} = {table_num * i}")
        with source_col:#...source code display...
            with st.expander("Source Code"):
                st.code('''table_num = st.number_input("Number for table", min_value=0, max_value=100, value=7, step=1, key="table_num")
table_len = st.slider("Table length", 1, 20, 12, key="table_len")
if st.button("Generate Table", key="table_button"):
    st.write(f"**Multiplication table for {table_num}:**")
    for i in range(1, table_len + 1):
        st.write(f"{table_num} × {i} = {table_num * i}")''',
            )

    elif number_tool == "Greatest":
        st.markdown("<div class='section-heading'>Greatest Between Numbers</div>", unsafe_allow_html=True)
        st.markdown("<div class='tool-card'><p>Compare two, three, or four numbers to find the greatest value.</p></div>", unsafe_allow_html=True)
        count = st.selectbox("How many numbers?", [2, 3, 4], index=1, key="greatest_count")
        values = [st.number_input(f"Number {idx + 1}", value=0, step=1, key=f"greatest_{idx}") for idx in range(count)]
        calc_col, source_col = st.columns([3, 4])
        with calc_col:
            if st.button("Find Greatest", key="greatest_button"):
                greatest = max(values)
                st.success(f"Greatest among {values} is {greatest}.")
        with source_col:#...source code display...
            with st.expander("Source Code"):
                st.code('''count = st.selectbox("How many numbers?", [2, 3, 4], index=1, key="greatest_count")
values = [st.number_input(f"Number {idx + 1}", value=0, step=1, key=f"greatest_{idx}") for idx in range(count)]
if st.button("Find Greatest", key="greatest_button"):
    greatest = max(values)
    st.success(f"Greatest among {values} is {greatest}.")''',
            )

    elif number_tool == "Prime & Even/Odd":
        st.markdown("<div class='section-heading'>Prime and Even/Odd Checker</div>", unsafe_allow_html=True)
        st.markdown("<div class='tool-card'><p>Check whether a number is prime and whether it is even or odd.</p></div>", unsafe_allow_html=True)
        num_check = st.number_input("Enter a number", min_value=0, max_value=1000, value=29, step=1, key="num_check")
        calc_col, source_col = st.columns([3, 4])
        with calc_col:
            if st.button("Analyze Number", key="prime_even_button"):
                if num_check < 2:
                    prime_text = "not prime"
                else:
                    prime_text = "prime" if all(num_check % i for i in range(2, int(num_check ** 0.5) + 1)) else "not prime"
                parity = "even" if num_check % 2 == 0 else "odd"
                st.info(f"{num_check} is {parity} and {prime_text}.")
        with source_col:  # ...source code display...
            with st.expander("Source Code"):
                st.code('''num_check = st.number_input("Enter a number", min_value=0, max_value=1000, value=29, step=1, key="num_check")
if st.button("Analyze Number", key="prime_even_button"):
    if num_check < 2:
        prime_text = "not prime"
    else:
        prime_text = "prime" if all(num_check % i for i in range(2, int(num_check ** 0.5) + 1)) else "not prime"
    parity = "even" if num_check % 2 == 0 else "odd"
    st.info(f"{num_check} is {parity} and {prime_text}.")''',
            )

    else:
        st.markdown("<div class='section-heading'>Palindrome, Armstrong, and Reverse Number</div>", unsafe_allow_html=True)
        st.markdown("<div class='tool-card'><p>Test a number for palindrome and Armstrong properties, then show its reverse.</p></div>", unsafe_allow_html=True)
        num_tool = st.number_input("Enter a number", min_value=0, max_value=99999, value=121, step=1, key="num_tool")
        calc_col, source_col = st.columns([3, 4])
        with calc_col:
            if st.button("Check Number", key="number_tool_button"):
                text_value = str(num_tool)
                reversed_value = text_value[::-1]
                palindrome = text_value == reversed_value
                armstrong = sum(int(d) ** len(text_value) for d in text_value) == num_tool
                st.write(f"**Reversed value:** {reversed_value}")
                st.write(f"**Palindrome:** {'Yes' if palindrome else 'No'}")
                st.write(f"**Armstrong number:** {'Yes' if armstrong else 'No'}")
        with source_col:#...source code display...
            render_source_code(
                '''num_tool = st.number_input("Enter a number", min_value=0, max_value=99999, value=121, step=1, key="num_tool")
if st.button("Check Number", key="number_tool_button"):
    text_value = str(num_tool)
    reversed_value = text_value[::-1]
    palindrome = text_value == reversed_value
    armstrong = sum(int(d) ** len(text_value) for d in text_value) == num_tool
    st.write(f"**Reversed value:** {reversed_value}")
    st.write(f"**Palindrome:** {'Yes' if palindrome else 'No'}")
    st.write(f"**Armstrong number:** {'Yes' if armstrong else 'No'}")''',
                use_expander=False,
            )

#.............String Tools Section........

elif selected_tab == "String Tools":
    st.markdown("<div class='section-heading'>String Tools</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-heading'>Reverse Text and Palindrome Check</div>", unsafe_allow_html=True)
    st.markdown("<div class='tool-card'><p>Reverse any phrase or word and verify whether it reads the same backwards.</p></div>", unsafe_allow_html=True)
    text_value = st.text_input("Enter text", value="Enter your Word or sentence", key="text_value")
    calc_col, source_col = st.columns([3, 4])
    with calc_col:
        if st.button("Analyze Text", key="text_button"):
            normalized = text_value.replace(" ", "").lower()
            reversed_text = text_value[::-1]
            palindrome_text = normalized == normalized[::-1]
            st.write(f"**Reversed text:** {reversed_text}")
            st.write(f"**Palindrome text:** {'Yes' if palindrome_text else 'No'}")
    with source_col:#...source code display...
        render_source_code(
            '''text_value = st.text_input("Enter text", value="Enter your Word or sentence", key="text_value")
if st.button("Analyze Text", key="text_button"):
    normalized = text_value.replace(" ", "").lower()
    reversed_text = text_value[::-1]
    palindrome_text = normalized == normalized[::-1]
    st.write(f"**Reversed text:** {reversed_text}")
    st.write(f"**Palindrome text:** {'Yes' if palindrome_text else 'No'}")''',
            use_expander=False,
        )

#.............Calculator Section........

elif selected_tab == "Calculator":
    st.markdown("<div class='section-heading'>Calculator</div>", unsafe_allow_html=True)
    st.markdown("<div class='tool-card'><p>Perform addition, subtraction, multiplication, and division with ease.</p></div>", unsafe_allow_html=True)
    num1 = st.number_input("Enter the first number:", key="cal1")
    num2 = st.number_input("Enter the second number:", key="cal2")
    operation = st.selectbox("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"], key="calc_operation")
    calc_col,source_col=st.columns([3,4])
    with calc_col:
     if st.button("Calculate", key="calculator_button"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."
        st.write(f"The result of {operation.lower()} is: {result}")
    with source_col:#...source code display...
        with st.expander("Source code", expanded=True):
            st.code('''num1 = st.number_input("Enter the first number:", key="cal1")
    num2 = st.number_input("Enter the second number:", key="cal2")
    operation = st.selectbox("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"], key="calc_operation")
     if st.button("Calculate", key="calculator_button"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            result = num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."
        st.write(f"The result of {operation.lower()} is: {result}")''')

#.............Notes Section........

elif selected_tab == "Notes":

    st.markdown("<div class='section-heading'>Notes</div>", unsafe_allow_html=True)
    st.markdown("<div class='tool-card'><p>Write and save your math notes, formulas, reminders, or examples here.</p></div>", unsafe_allow_html=True)
    notes = st.text_area(
        "Your notes",
        value=st.session_state.get("hello_notes", "Example:\n- 7 × 8 = 56\n- 153 is an Armstrong number\n- 121 is a palindrome number."),
        height=220,
        key="hello_notes_area",
    )
    if st.button("Save Notes", key="save_notes_button"):
        st.session_state["hello_notes"] = notes
        st.success("Notes saved successfully.")
    st.markdown("### Saved notes preview")
    st.write(st.session_state.get("hello_notes", notes))

#.............Quiz Section........

else:
    st.markdown("<div class='section-heading'>Quiz</div>", unsafe_allow_html=True)
    st.markdown("<div class='tool-card'><p>Test your understanding of factorials, primes, palindromes, and more.</p></div>", unsafe_allow_html=True)
    questions = [
        {
            "question": "What is 5! (factorial of 5)?",
            "options": ["24", "60", "120", "720"],
            "answer": "120",
        },
        {
            "question": "Which number is prime?",
            "options": ["21", "29", "51", "95"],
            "answer": "29",
        },
        {
            "question": "Is 1221 a palindrome?",
            "options": ["Yes", "No"],
            "answer": "Yes",
        },
        {
            "question": "What is the reverse of 407?",
            "options": ["704", "047", "407", "740"],
            "answer": "704",
        },
        {
            "question": "Which number is an Armstrong number?",
            "options": ["153", "154", "370", "4070"],
            "answer": "153",
        },
    ]
    with st.form("hello_quiz_form"):
        answer_pairs = []
        for idx, item in enumerate(questions, start=1):
            selected = st.radio(f"{idx}. {item['question']}", item["options"], index=0, key=f"hello_quiz_{idx}")
            answer_pairs.append((selected, item["answer"]))
        submit = st.form_submit_button("Submit Quiz")

    if submit:
        score = sum(1 for selected, answer in answer_pairs if selected == answer)
        st.success(f"Your score: {score} / {len(questions)}")
        if score == len(questions):
            st.balloons()
        for index, (selected, answer) in enumerate(answer_pairs, start=1):
            if selected == answer:
                st.write(f":white_check_mark: Question {index} correct")
            else:
                st.write(f":x: Question {index} incorrect — correct answer: {answer}")


