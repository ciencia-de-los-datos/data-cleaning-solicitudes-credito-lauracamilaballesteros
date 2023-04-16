"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col = 0)

    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['barrio'] = df['barrio'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['sexo'] = df['sexo'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.lower()

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: x.replace('$', '')).apply(lambda x: x.replace(',', '')).astype(float).astype(int)

    import datetime

    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst= True)
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='%Y/%m/%d', infer_datetime_format = False ).dt.date

    df['idea_negocio'] = df['idea_negocio'].str.replace('_',' ').str.replace('-',' ').str.strip()
    df['idea_negocio'] = df['idea_negocio'].apply(lambda x: x.replace(' ', '_'))

    df['barrio'] = df['barrio'].str.replace('_','-').str.replace('-',' ')
    df['línea_credito'] = df['línea_credito'].str.replace('_',' ').str.replace('-',' ').str.strip()

    df = df.drop_duplicates()
    df = df.dropna(subset=['tipo_de_emprendimiento'], axis=0)
    df = df.dropna(subset=['idea_negocio'], axis=0)
    df = df.dropna(subset=['barrio'], axis=0)


    return df
