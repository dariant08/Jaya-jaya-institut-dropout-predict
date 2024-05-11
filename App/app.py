#import library
import pickle
import streamlit as st

#read model
model_predict = pickle.load(open('Student.sav', 'rb'))

#create web title
st.title('Student Status Predict')

st.markdown ('Keterangan nilai')
st.markdown ('Gender (0 = Perempuan, 1 = Laki-laki)')
st.markdown ('Class (0 = Regular, 1 = Internasional)')
st.markdown ('Scholarship_holder  (0 = Mandiri, 1 = Beasiswa)')
st.markdown ('Debtor (0 = bayar, 1 = Lunas)')

#create input column
col1, col2 = st.columns(2)
with col1 :
    Age_at_enrollment = int(st.number_input(label='Age_at_enrollment', min_value=17, max_value=35, value=20, step=1))
with col2 :
    Gender = str(st.selectbox(label='Gender', options=[ 0, 1], index=0))

col1, col2 = st.columns(2)
with col1 :
    Class = int(st.selectbox(label='Class', options=[ 0, 1], index=0))
with col2 :
    Evening_class = int(st.selectbox(label='Evening_class', options=[ 0, 1], index=0))

col1, col2 = st.columns(2)
with col1 :
    Scholarship_holder = str(st.selectbox(label='Scholarship_holder', options=[ 0, 1], index=0))
with col2 :
    Debtor = str(st.selectbox(label='Debtor', options=[ 0, 1], index=0))
    
col1, col2 = st.columns(2)
with col1 :
    Smt_1_passed = int(st.number_input(label='Smt_1_passed', min_value=0, max_value=26, value=0, step=1)) 
with col2 :
    Smt_2_passed = int(st.number_input(label='Smt_2_passed', min_value=0, max_value=26, value=0, step=1))
    
col1, col2 = st.columns(2)
with col1 :
    Fathers_occupation = int(st.select_slider(label='Fathers_occupation', options=range(0, 21), value=0))
with col2 :
    Mothers_occupation = int(st.select_slider(label='Mothers_occupation', options=range(0, 21), value=0))

#prediction code
Status_predict=''

#create prediction button
if st.button('Student status test'):
    Status_predict = model_predict.predict([[Evening_class, Mothers_occupation, Fathers_occupation, Debtor,
                                                   Gender, Scholarship_holder, Age_at_enrollment, Class,
                                                    Smt_1_passed, Smt_2_passed]])
    
    if(Status_predict[0] == 0):
        Status_predict = 'Siswa sudah lulus'
    elif(Status_predict[0] == 1):
        Status_predict = 'Siswa sudah dropout'        
    else :
        Status_predict = 'Siswa masih sekolah'
    st.success(Status_predict)