import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Chiffre d'affaires par produit
données['CA'] = données['prix'] * données['qte']

df_ca_produit = données.groupby('produit').agg(
    CA_par_produit=('CA','sum')
).reset_index()

# Graphique
figure = px.pie(
    df_ca_produit,
    values='CA_par_produit',
    names='produit',
    title="Chiffre d'affaires par produit (€)"
)

figure.write_html('views/graph-CA-produit.html')

print('graph-CA-produit.html généré avec succès !')
