from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Tambahkan CORS agar frontend Vue.js bisa mengakses API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model yang sudah di-download dari Colab
model = joblib.load("model_scam.pkl")

# Skema input data sesuai fitur transaksi
class TransactionData(BaseModel):
    sender_wallet_age_days: float
    receiver_wallet_age_days: float
    transaction_amount_usd: float
    gas_fee_usd: float
    num_prev_transactions_sender: int
    num_prev_transactions_receiver: int
    avg_txn_interval_sender_min: float
    failed_txn_ratio_sender: float
    velocity_score: float
    anomaly_score: float

@app.post("/predict")
def predict_scam(data: TransactionData):
    features = np.array([[
        data.sender_wallet_age_days, data.receiver_wallet_age_days,
        data.transaction_amount_usd, data.gas_fee_usd,
        data.num_prev_transactions_sender, data.num_prev_transactions_receiver,
        data.avg_txn_interval_sender_min, data.failed_txn_ratio_sender,
        data.velocity_score, data.anomaly_score
    ]])
    
    prediction = int(model.predict(features)[0])
    status = "Berisiko Scam / Penipuan" if prediction == 1 else "Transaksi Aman"
    
    return {"prediction": prediction, "status": status}