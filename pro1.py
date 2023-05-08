import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Aplikasi Perhitungan Stoikiometri Dasar', page_icon=':computer:')

#sidebar
with st.sidebar :
    selected = option_menu('Aplikasi Perhitungan Stoikiometri Dasar',
                         ['Tentang Aplikasi','Stoikiometri','Perhitungan Stoikiometri Dasar','Kelompok 2'],
                           default_index= 0)
#pengenalan aplikasi
if selected==('Tentang Aplikasi'):
    st.subheader('Project Webapps Kelompok 2 :computer:')
    st.title('Selamat Datang :wave:')
    st.header('Aplikasi Perhitungan Stoikiometri Dasar')
    st.write('Aplikasi ini diperuntukkan untuk mempermudah dalam perhitungan stoikiometri yang sering ditemukan dalam perhitungan kimia dengan data yang banyak dan harus dihitung dalam waktu yang singkat. Dengan adanya perkembangan teknologi aplikasi perhitungan,maka akan sangat mempermudah pengolahan data perhitungan dilaboratorium. Dengan memanfaatkan aplikasi perhitungan maka Laboran akan lebih mudah untuk mengolah data perhitungan.   ')
    
    st.image('https://i.pinimg.com/originals/28/18/73/281873087a6561e51a9186f7430deffc.png')


    
    
#halaman stoikiometri
if selected=='Stoikiometri':
    st.title('Stoikiometri')
    st.write('Stoikiometri berasal dari kata “stoicheion” dalam bahasa Yunani yang berarti mengukur. Dalam ilmu kimia, stoikiometri adalah ilmu yang mempelajari kuantitas suatu zat dalam reaksi kimia. Zat-zat tersebut meliputi massa, jumlah mol, volume, dan jumlah partikel dan molaritas.')

    st.image('https://i.pinimg.com/originals/98/d1/53/98d153f5111d9b79dd565f822c53be55.jpg',caption= 'Rumus Dasar Perhitungan Stoikiometri')

    st.write('Stoikiometri bersandar pada hukum-hukum dasar ilmu kimia salah satunya yaitu Hukum Kekekalan Massa & Hukum Perbandingan Tetap')
    col1,col2 = st.columns(2)
    col1.write('''Hukum Kekekalan Massa
    
    "massa zat-zat sebelum dan sesudah
    sebuah reaksi adalah tetap”
    ''')
    col2.write('''Hukum Perbandingan Tetap
    
    "perbandingan massa unsur-unsur 
    dalam tiap-tiap senyawa adalah tetap"''')


    
#tab 2
if selected=='Perhitungan Stoikiometri Dasar':
    st.title ('Perhitungan Stoikiometri Dasar')
    option=st.selectbox(
    'Silahkan pilih satuan konsentrasi yang ingin dicari ',
    ('Molekul (n)','Molaritas (M)','Volume (v)','Partikel'))
        
    if option=='Molekul (n)':
        massa=st.number_input('Masukkan massa zat')
        mr=st.number_input('Masukkan mr larutan')
        if st.button('Hitung'):
            Molekul=massa/mr
            st.success(f'Molekul larutan sebesar {Molekul} mol')
    elif option=='Molaritas (M)':
        mol=st.number_input('Masukkan mol zat')
        v=st.number_input('Masukkan volume pelarut')
        if st.button('Hitung'):
            Molaritas=mol/v
            st.success(f'Molaritas larutan sebesar {Molaritas} M')
    elif option=='Volume (v)':
        mol=st.number_input('Masukkan molekul zat')
        if st.button('Hitung'):
            Volume=mol*22.4
            st.success(f'Volume larutan sebesar {Volume}')
    elif option=='Partikel':
        mol=st.number_input('Masukkan molekul zat')
        if st.button('Hitung'):
            Partikel=mol*6.02*10**23
            st.success(f'Partikel larutan sebesar {Partikel}')
            
            
#kelommpok 2
if (selected=='Kelompok 2'):
    st.title('Kelompok 2')
    st.image('https://i.pinimg.com/originals/88/43/cb/8843cbaf3b70af10e483f22d6a84c53c.jpg')
    st.write('Oleh Kelompok 2 :')
    st.write('Abdul Nazhmi Makarim (2219023)')
    st.write('Muhammad Ihsan Aula Hikam (2219115)')
    st.write('Chandrika Raysa Mulya (2219053)')
    st.write('R Amelia Nurbani Sumarya (2219146)')
   
    