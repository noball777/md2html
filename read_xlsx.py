import sys

try:
    import pandas as pd
    file_path = "交付要望書5月17日.xlsx"
    xl = pd.ExcelFile(file_path)
    with open("read_xlsx_out.txt", "w", encoding="utf-8") as f:
        for sheet_name in xl.sheet_names:
            f.write(f"\n=== Sheet: {sheet_name} ===\n")
            df = xl.parse(sheet_name, header=None)
            df = df.fillna("")
            for row in df.itertuples(index=False, name=None):
                row_str = "\t".join([str(x).strip() for x in row if str(x).strip() != ""])
                if row_str:
                    f.write(row_str + "\n")
except Exception as e:
    with open("read_xlsx_out.txt", "w", encoding="utf-8") as f:
        f.write(f"Error: {e}")
