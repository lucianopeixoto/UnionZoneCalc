# UnionZoneCalc

UnionZoneCalc is a simple Python CLI tool that calculates union work zones based on the distance from a City Hall or other landmark. The initial poof of concept version usese the Toronto City Hall and the distances from Local 30 Roofing map.

It uses the Google Geocoding API to convert addresses into coordinates and applies predefined distance rules to determine the correct zone.

---

## 📌 Features

- Convert address → coordinates using Google API
- Calculate distance from Toronto City Hall
- Automatically assign zone:
  - Zone 1: 0–20 km
  - Zone 3: 20–50 km
  - Zone 4: 50–80 km
  - Zone 5: 80–95 km
- Special case handling:
  - Toronto Islands (manual Zone 2 check)
  - Locations south of Lake Ontario → Room & Board
- CLI input or interactive prompt

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/unionzone.git
cd unionzone
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Create config file

Create a file named `config.cfg`:

```ini
[google]
api_key=YOUR_API_KEY_HERE
```

---

## ▶️ Usage

### Option 1: Pass address as argument

```bash
python zone_calculator.py "185 Conestoga Dr, Brampton"
```

### Option 2: Interactive mode

```bash
python zone_calculator.py
```

---

## 🧠 Special Rules

### Toronto Islands (Zone 2)
If the distance is between **2.2 km and 3.4 km**, verify manually if the address is on the Toronto Islands.

### South of Lake Ontario
If the location is south of the lake, it should be considered:
> **Room & Board**

---

## 📁 Project Structure

```
unionzone/
│
├── zone_calculator.py
├── config.cfg        # NOT committed (contains API key)
├── .gitignore
└── README.md
```

---

## 🔐 Security

Your API key is stored locally in `config.cfg` and is excluded from version control using `.gitignore`.

---

## 💻 Sample Output

```
C:\Repo\UnionZoneCalc> python.exe .\zone_calculator.py
Enter address: 185 Conestoga Drive, Brampton

--- RESULT ---
Address: 185 Conestoga Dr, Brampton, ON L6Z 2Z7, Canada
Coordinates: 43.7233218, -79.7906296
Distance from City Hall: 33.60 km
Zone: Zone 3
```

## 🚀 Future Improvements

- Web interface (Flask/FastAPI)
- Map visualization
- Batch processing (CSV input)
- More precise geographic rules (GIS polygons)

---

## 🧑‍💻 Author

Luciano Carvalho Peixoto
