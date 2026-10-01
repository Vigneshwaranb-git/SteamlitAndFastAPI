import streamlit as st

st.title("Hello, Book Lovers!")
st.write("This is a simple Streamlit app integrated with FastAPI to check book availability.")

book_name = st.text_input("Enter a book name:")
st.write("You entered:", book_name)

chapter_Number = st.number_input("Enter a chapter number:", min_value=1, step=1)
st.write("You entered chapter number:", chapter_Number)

genre = st.radio("Choose your favorite genre:", ("Fiction", "Non-Fiction", "Science Fiction", "Fantasy"))
st.write("You selected:", genre)

is_available = "Not Available"
if book_name == "Test" and chapter_Number == 1:
    is_available = "Available"

if st.button("Check Availability"):
    if is_available == "Available":
        st.write(f"You submitted book '{book_name}' and chapter number {chapter_Number}.")
        st.success(f"The book '{book_name}' is {is_available}.")
    else:
        st.write(f"You submitted book '{book_name}' and chapter number {chapter_Number}.")
        st.error(f"The book '{book_name}' is {is_available}. Please check the book name and chapter number.")

st.checkbox("I agree to the terms and conditions.")
st.write("Thank you for using the Streamlit app! You can now proceed to interact with the FastAPI endpoints.")