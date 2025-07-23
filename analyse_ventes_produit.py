import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Les ventes par produit
df_ventes_produit = données.groupby('produit').agg(
    Qte_par_produit=('qte','sum')
).reset_index()

# Graphique
figure = px.pie(
    df_ventes_produit,
    values='Qte_par_produit',
    names='produit',
    title="Les ventes par produit"
)

figure.write_html('views/graph-ventes-produit.html')

print('graph-ventes-produit.html généré avec succès !')
