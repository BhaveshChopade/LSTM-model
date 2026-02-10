# DoS Attack Detection Using LSTM (PyQt Desktop App)

This repository contains a desktop application for experimenting with **DoS (Denial-of-Service) traffic detection** using an LSTM-based workflow.

The project combines:
- A **PyQt5 GUI** for login, signup, model interaction, and result visualization.
- A **network traffic dataset** (`dataset_sdn.csv`) used for training and plotting.
- A simple **SQLite credential store** for local authentication.
- Serialized model/data artifacts used by the test pipeline.

> This is a research/demo-style codebase rather than a productionized ML system. Training, evaluation, and UI logic are tightly coupled in the current implementation.

---

## 1) Project Objectives

The app is designed to let a user:
1. Authenticate into the system.
2. Train an LSTM model on SDN-like traffic data.
3. Run per-record test predictions from a UI input.
4. Visualize aggregate traffic/attack behavior with charts.

The primary classification target is the `label` column in the dataset, where rows represent benign vs malicious traffic behavior.

---

## 2) Repository Layout

```text
LSTM-model/
├── README.md
└── Send_final/
    ├── login.py            # Login screen (entry point for normal usage)
    ├── signup.py           # User registration screen
    ├── MAIN_CODE.py        # Main app: Test / Train / Result actions
    ├── dataset_sdn.csv     # Input dataset
    ├── multiD.db           # SQLite database with userdetails table
    ├── LSTM.keras          # Serialized model artifact used by test flow
    ├── X.dat, y.dat        # Serialized feature/label artifacts for inference
    └── *.png, *.jpg        # UI background/skin assets
```

---

## 3) Runtime Flow

### 3.1 Authentication layer
- `login.py` renders the login page.
- On successful credential check against `multiD.db`, it opens the main dashboard (`Ui_MainWindow1` from `MAIN_CODE.py`).
- The same screen can open `signup.py` to create new users.

### 3.2 Main dashboard actions
Inside `MAIN_CODE.py`, three core actions are exposed:

- **TEST**
  - Reads a record index from the UI (`Data Number`).
  - Loads `LSTM.keras`, `X.dat`, and `y.dat`.
  - Runs a prediction for the selected record and prints whether it appears benign or DoS-like.

- **TRAIN**
  - Reads `dataset_sdn.csv`.
  - Drops some non-feature columns.
  - Performs one-hot encoding + standard scaling.
  - Builds a Keras LSTM network and trains it (current code uses full data for training/validation).

- **RESULT**
  - Generates EDA-like plots (request count by source IP, attack-only source counts, protocol distributions, and class pie chart).

---

## 4) Dataset Notes

The dataset includes network-flow related fields such as:
- addressing (`src`, `dst`),
- packet/byte counters,
- duration and throughput metrics,
- protocol metadata,
- and a final `label` column used as the target.

Example header:

```csv
dt,switch,src,dst,pktcount,bytecount,dur,dur_nsec,tot_dur,flows,packetins,pktperflow,byteperflow,pktrate,Pairflow,Protocol,port_no,tx_bytes,rx_bytes,tx_kbps,rx_kbps,tot_kbps,label
```

---

## 5) Local Setup

## 5.1 Python environment
Use Python 3.9+ (3.10 recommended).

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

Install dependencies (manual list, since requirements file is not yet included):

```bash
pip install pyqt5 opencv-python numpy pandas matplotlib seaborn scikit-learn tensorflow
```

## 5.2 Run the application
Run from the `Send_final` directory so relative asset paths resolve correctly:

```bash
cd Send_final
python login.py
```

---

## 6) Database Schema

The project uses a local SQLite DB (`multiD.db`) with a single table:

```sql
CREATE TABLE userdetails (
  username VARCHAR(100),
  email    VARCHAR(100),
  mob      VARCHAR(100),
  password VARCHAR(100)
);
```

---

## 7) Technical Caveats (Important)

1. **Model serialization path**
   - The test routine loads `LSTM.keras` using `pickle.load(...)`.
   - The training routine constructs a TensorFlow/Keras model, but does not clearly persist it in the same script.
   - If you extend the project, standardize save/load logic (`model.save(...)` + `tf.keras.models.load_model(...)`, or fully pickle-compatible objects).

2. **Security concerns in auth flow**
   - Login and signup currently build SQL queries via string concatenation.
   - Move to parameterized SQL statements to avoid injection risk.

3. **Tight coupling of concerns**
   - UI logic, preprocessing, model training, and plotting are all in button handlers.
   - For maintainability, split into modules: `ui/`, `data/`, `ml/`, `service/`.

4. **Reproducibility**
   - Training uses direct in-function configuration (epochs, batch size, feature shaping).
   - Introduce config files and versioned artifacts for repeatable experiments.
