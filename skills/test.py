from fastapi import FastAPI
import openpyxl
import requests

app = FastAPI()

@app.get("/scrape")
async def scrape():
    # 下載 Excel 檔案
    url = "https://docs.google.com/spreadsheets/d/1xT20il2JtGCHwjnB4Azbsfk5Xbi3_7fTrJKkNcI2Bko/edit?usp=sharing"
    response = requests.get(url)
    response.raise_for_status()

    # 讀取 Excel 檔案
    wb = openpyxl.load_workbook(filename=response.content)
    ws = wb.active

    # 解析 Excel 檔案
    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        name, age, address = row
        data.append({"name": name, "age": age, "address": address})

    return {"data": data}
