"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df.dropna()
    df = df.drop_duplicates()
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: x.replace('$', '')).apply(lambda x: x.replace(',', '')).astype(float).astype(int)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'])
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    df[['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']] =df[['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']].apply(lambda x: x.str.lower())
    df[['idea_negocio', 'línea_credito']] = df[['idea_negocio', 'línea_credito']].str.replace('_',' ').str.replace('-',' ').str.strip()
    
    df['barrio'] = df['barrio'].str.replace('_','-').str.replace('-',' ')
    
    df['idea_negocio'].apply(lambda x: x.replace(' ', '_'))
    
    df.drop(['Unnamed: 0'], axis=1)
    
    #
    # Inserte su código aquí
    #

    return df
