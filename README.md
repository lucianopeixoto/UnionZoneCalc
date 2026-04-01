# UnionZone

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
git clone https://github.com/lucianopeixoto/unionzonecalc.git
cd unionzonecalc
