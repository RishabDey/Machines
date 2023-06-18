import pandas as pd
import plotly.express as px
import streamlit as st


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





#SideBar


st.sidebar.header("Select Options Here:")

product = st.sidebar.multiselect(
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


left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Total Cost :")
    st.subheader(f" €{total_costRounded:}")



with middle_column:
    st.subheader("Total Weight :")
    st.subheader(f" {weightR} KiloGrams")


with right_column:
    st.subheader("Carbon Footprint of this Product :")
    st.subheader(f"{carbonFootprintR} Kg Co2-equivalent")




#insert a divider
st.markdown("---")


