import streamlit as st
import pandas as pd 
import numpy as np 
import pickle


st.set_page_config(page_title = 'Industrial Copper Modeling')

st.markdown(f'<h1 style="text-align: center; color: #B87333">Industrial Copper Modeling</h1>', unsafe_allow_html=True)    

price_tab, status_tab = st.tabs(['**PREDICT SELLING PRICE**', '**PREDICT LEAD STATUS**'])

status_options = ['', 'Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
status_values = {'Won':8, 'Lost':7, 'Not lost for AM':6, 'Revised':5, 'To be approved':4, 'Draft':3, 'Offered':2, 'Offerable':1, 'Wonderful':0}

item_type_options = ['', 'W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
item_type_values = {'SLAWR':0, 'IPL':1,  'WI':2, 'Others':3, 'PL':4, 'S':5, 'W':6}

product_ref_options = ['', 611728, 611733, 611993, 628112, 628117, 628377, 640400, 640405, 640665, 164141591, 164336407,
                       164337175, 929423819, 1282007633, 1332077137, 1665572032, 1665572374, 1665584320, 1665584642,
                       1665584662, 1668701376, 1668701698, 1668701718, 1668701725, 1670798778, 1671863738, 1671876026,
                       1690738206, 1690738219, 1693867550, 1693867563, 1721130331, 1722207579]

application_options = ['', 2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 19.0, 20.0, 22.0, 25.0, 26.0, 27.0, 28.0, 29.0, 38.0, 
                       39.0, 40.0, 41.0, 42.0, 56.0, 58.0, 59.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 79.0, 99.0]

country_options = ['', 25.0, 26.0, 27.0, 28.0, 30.0, 32.0, 38.0, 39.0, 40.0, 77.0, 78.0, 79.0, 80.0, 84.0, 89.0, 107.0, 113.0]

with price_tab:
    with st.form('Regression'):
        price1, price2, price3 = st.columns([0.5,0.3,0.5])
        with price1:
            quantity_tons = st.text_input("Quantity Tons Required", help='min_value = 0.00001 & max_value = 1000.00')
            customer = st.text_input("Customer Number", help= 'min_value= 12450 & max_value= 30400000')
            country = st.selectbox("Country Number", options = country_options)
            status = st.selectbox("Select Status", options = status_options)

        with price3:
            item_type = st.selectbox("Select Item Type", options = item_type_options)
            application = st.selectbox("Select Application Number", options = application_options)
            thickness = st.text_input(label = "Enter Thickness value", help='min_value = 0.1 & max_value = 100.00')
            product_reference = st.selectbox("Select Product Reference", options = product_ref_options)
        p1,p2,p3 = st.columns([0.3,0.3,0.3])
        with p2:
            st.write(' ')
            st.write(' ')               
            selling_price_result = st.form_submit_button("**Find the Selling Price**")

        if selling_price_result:
            with open(r'D:\ZEN\Copper_Modelling\Regression_model_selling_price.pkl', 'rb') as file:
                price = pickle.load(file)

            price_features = np.array([[float(quantity_tons), float(customer), float(country), status_values[status], item_type_values[item_type], float(application), float(thickness), float(product_reference)]])
            
            selling_price_value = price.predict(price_features)
            sp_value = np.exp(selling_price_value[0])

            st.markdown(f'<div style="text-align: center">'
                f'<h3 style= "color: #B87333">Predicted Selling Price would be <span style="color: green;">${sp_value}</span></h3>'
                '</div>', unsafe_allow_html=True)

with status_tab:
    with st.form('Classification'):
        status1, status2, status3 = st.columns([0.5,0.3,0.5])
        with status1:
            quantity_tons_c = st.text_input("Enter Quantity Tons Required", help='min_value = 0.00001 & max_value = 1000.00', key='c1')
            customer_c = st.text_input("Enter Customer Number", help= 'min_value= 12450 & max_value= 30400000', key='c2')
            country_c = st.selectbox("Select Country Number", options = country_options, key='c3')
            item_type_c = st.selectbox("Select the Item Type", options = item_type_options, key='c4')
            
        with status3:
            application_c = st.selectbox("Select the Application Number", options = application_options, key='c5')
            thickness_c = st.text_input("Enter Thickness value", help='min_value = 0.1 & max_value = 100.00', key='c6') 
            product_reference_c = st.selectbox("Select Product Reference", options = product_ref_options, key='c7')
            selling_price_c = st.number_input("Enter Selling Price Amount",help = 'price in $' , key='c8')
            spc = np.log(float(selling_price_c))
        s1,s2,s3 = st.columns([0.3,0.3,0.3])
        with s2:
            st.write(' ')
            st.write(' ')      
            staus_result = st.form_submit_button("**Find the Status Lead**")

        if staus_result:
            with open(r'D:\ZEN\Copper_Modelling\Classification_model_status.pkl', 'rb') as file:
                status = pickle.load(file)

                status_features = np.array([[float(quantity_tons_c), float(customer_c), float(country_c), item_type_values[item_type_c], float(application_c), float(thickness_c), float(product_reference_c), spc]])
                status_value = status.predict(status_features)

                if status_value[0] == 1:
                    s_value = 'Won' 
                else: 
                    s_value = 'Lost'
                
                st.markdown(f'<div style="text-align: center">'
                            f'<h3 style= "color: #B87333">Predicted Status lead as <span style="color: green;">{s_value}</span></h3>'
                            '</div>', unsafe_allow_html=True)
