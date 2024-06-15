import streamlit as st

# Function to calculate CAGR
def calculate_cagr(beginning_value, ending_value, years):
    if beginning_value == 0:
        return 0
    cagr = ((ending_value / beginning_value) ** (1 / years)) - 1
    return cagr

# Function to format numbers with commas
def format_number(number):
    return "{:,}".format(number)

# Streamlit app layout
def main():
    st.title("CAGR Calculator")

    st.write("""
    This app calculates the Compound Annual Growth Rate (CAGR).
    Use the text entry or sliders to set the initial and final values, and choose the time period.
    """)

    # Layout for initial value input
    col1, col2, col3 = st.columns([2, 3, 1])
    with col1:
        beginning_value_input = st.number_input("Initial Value:", min_value=0.0, step=1000.0, format="%0.0f")
    with col2:
        beginning_value = st.slider("", min_value=0, max_value=10000000, value=int(beginning_value_input), step=1000, format="%0.0f")
    with col3:
        st.write(f"Value: ₹{format_number(beginning_value)}")

    # Layout for final value input
    col4, col5, col6 = st.columns([2, 3, 1])
    with col4:
        ending_value_input = st.number_input("Final Value:", min_value=0.0, step=1000.0, format="%0.0f")
    with col5:
        ending_value = st.slider("", min_value=0, max_value=10000000000, value=int(ending_value_input), step=1000, format="%0.0f")
    with col6:
        st.write(f"Value: ₹{format_number(ending_value)}")

    # Time period selection
    col7, col8 = st.columns([1, 1])
    with col7:
        time_period_type = st.radio("Choose time period:", ("Years", "Months"), horizontal=True)

    if time_period_type == "Years":
        col9, col10, col11 = st.columns([2, 3, 1])
        with col9:
            years_input = st.number_input("Number of Years:", min_value=1, step=1)
        with col10:
            years = st.slider("", min_value=1, max_value=50, value=int(years_input), step=1)
        with col11:
            st.write(f"Years: {years}")
        cagr = calculate_cagr(beginning_value, ending_value, years)
    else:
        col12, col13, col14 = st.columns([2, 3, 1])
        with col12:
            months_input = st.number_input("Number of Months:", min_value=1, step=1)
        with col13:
            months = st.slider("", min_value=1, max_value=600, value=int(months_input), step=1)
        with col14:
            st.write(f"Months: {months}")
        years = months / 12
        cagr = calculate_cagr(beginning_value, ending_value, years)

    if st.button("Calculate CAGR"):
        st.write(f"Initial Value: ₹{format_number(beginning_value)}")
        st.write(f"Final Value: ₹{format_number(ending_value)}")
        st.success(f"The CAGR is {cagr*100:.2f}%")

if __name__ == "__main__":
    main()
