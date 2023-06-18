import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
#pip install streamlit-aggrid
from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder


st.set_page_config(page_title= "Machines Dashboard",
                   page_icon= ":bar_chart:",
                   layout= "wide")





df = pd.read_excel(
    io = 'FakeDataCoffeeMachineExcel.xlsx',
    engine = 'openpyxl',
    sheet_name= 'FakeDataCoffeeMachine',
    skiprows=0,
    usecols= 'A:T',
    nrows=6

    
)


#st.dataframe(df)

#SideBar


st.sidebar.header("Available Products:")

product = st.sidebar.selectbox(
    "Select the Product:", 
    options=df['Product'].unique(),
    #default= df['Product'].unique()
)

#year = st.sidebar.multiselect(
#    "Select the Year:", 
#    options=df['ManufacturingYear'].unique(),
#    default= df['ManufacturingYear'].unique()
#)




#material = st.sidebar.multiselect(
#    "Select the Material:", 
#    options=df['Material'].unique(),
#    default= df['Material'].unique()

#)


df_selection = df.query(
    "Product == @product"
)


st.session_state['df'] = df_selection

#st.dataframe(df_selection)



#KPIs in Main Page

st.title(":bar_chart: Machines Dashboard")
st.markdown("##")


total_cost = df_selection['Cost'].sum()
total_costRounded = round(total_cost,2)

weight = df_selection['Weight'].sum()
weightR = round(weight,2)

carbonFootprint = df_selection['CarbonFootprint'].sum()
carbonFootprintR = round(carbonFootprint,2)

#=============================================================================
with st.container():
    st.write("---")
    left_column, middle_column, right_column = st.columns(3)

    with left_column:
        st.subheader(f"Cost : € {total_costRounded}")
    #st.subheader(f" €{total_costRounded:}")

    with middle_column:
        st.subheader(f" Weight : {weightR} Kilograms")
    #st.subheader(f" {weightR} KiloGrams")

    with right_column:
        st.subheader("Carbon Footprint of this Product :")
        st.subheader(f"{carbonFootprintR} Kg Co2-equivalent")


#=============================================================================  

Product_ID = df_selection['ProductID'].mean()
ModelNumber = df_selection['ModelNumber'].sum()



with st.container():
    st.write('---')
    l_column, m_column, r_column = st.columns(3)
    
    with l_column:
        st.subheader(":blue[Product ID]")    
        st.subheader(Product_ID)
    
    with m_column:
        st.subheader(':blue[ModelNumber]')
        st.subheader(f":orange[{ModelNumber}]")

    with r_column:
        st.subheader(":blue[Product Image]")
        for index, row in df_selection.iterrows():
            image_path = row['MyUrl']
            image = Image.open(image_path)
            resized_image = image.resize((200,200))
            st.image(resized_image, use_column_width= True)




#st.map(df)

   
    #filtered_df = df_selection
    #st.image(filtered_df['MyUrl'].values[0], width= 1000)





#selected_product = st.sidebar.selectbox('Select product' , df['Product'])


#for index, row in df_selection.iterrows():
#    image_path = row['MyUrl']
#    image = Image.open(image_path)
#    resized_image = image.resize((300,300))
#    st.image(resized_image, use_column_width= True)






#insert a divider
st.markdown("---")




