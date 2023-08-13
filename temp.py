import numpy as np
import pickle
import streamlit as st

pickle_in = open(r"C:\Users\91999\Downloads\LassoRegressionModel.pkl", "rb")
lass_regression = pickle.load(pickle_in)

def predict_car_price(input_data):
    numpy_arr = np.asarray(input_data, dtype=float)  # Convert input to float
    reshaped_arr = numpy_arr.reshape(1, -1)
    prediction = lass_regression.predict(reshaped_arr)
    return prediction[0]

def main():
    st.title("Car Price Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Car Price Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    year = st.text_input("Year", "")
    present_price = st.text_input("Present Price", "")
    kms_driven = st.text_input("Kms Driven", "")
    fuel_type = st.text_input("Fuel Type", "")
    seller_type = st.text_input("Seller Type", "")
    transmission = st.text_input("Transmission", "")
    owner = st.text_input("Owner", "")
    
    result = ""
    if st.button("Predict"):
        input_data = [year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]
        result = predict_car_price(input_data)
        st.success('The predicted car price is: {}'.format(result))
        
    if st.button("About"):
        st.text("Built with Streamlit")
        
if __name__ == '__main__':
    main()

    
    
    