import joblib
import pandas as pd

# Chargement du modèle et du scaler
model = joblib.load("modele_effortC1.pkl")
scaler = joblib.load("scaler_effort_C1.pkl")  # ✅ ne pas recréer un scaler vierge

# # Test avec différentes valeurs de TON_CYL_TS1
# for valeur in range(0, 1100, 100):
#     nouveau_produit = pd.DataFrame([{
#         "CEPAI_EN_MOD": 2.2,
#         "TON_CYL_TS1": valeur,
#         "TON_CYL_TI1": valeur,
#         "DURETE": 65,
#         "LARGEUR": 1004
#     }])

#     nouveau_scaled = scaler.transform(nouveau_produit)
#     prediction = model.predict(nouveau_scaled)[0]
#     print(f"TS1 = {valeur} → Prédiction effort : {prediction:.2f}")

nouveau_produit = pd.DataFrame([{
    "CEPAI_EN_MOD": 2.4,
    "TON_CYL_TS1": 1300,
    "TON_CYL_TI1": 1300,
    "DURETE": 60.2,
    "LARGEUR": 847
}])

nouveau_scaled = scaler.transform(nouveau_produit)
prediction = model.predict(nouveau_scaled)[0]
print(f" Prédiction effort : {prediction:.2f}")
