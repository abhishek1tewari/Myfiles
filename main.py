import streamlit as st
import pandas as pd
from rapidfuzz import fuzz
from io import BytesIO

st.set_page_config(page_title="COI Fuzzy Matching Tool", layout="wide")


def run_matching(vendor_df, employee_df, v_col, e_col, threshold):
    results = []

    for _, v_row in vendor_df.iterrows():
        for _, e_row in employee_df.iterrows():
            v_val = str(v_row[v_col])
            e_val = str(e_row[e_col])

            score = fuzz.token_set_ratio(v_val, e_val)

            if score >= threshold:
                row = {
                    "MATCH_TYPE": "EXACT" if score == 100 else "FUZZY",
                    "MATCH_FIELD": f"{v_col} vs {e_col}",
                    "MATCH_SCORE": score
                }

                for c in vendor_df.columns:
                    row[f"VENDOR_{c}"] = v_row[c]

                for c in employee_df.columns:
                    row[f"EMPLOYEE_{c}"] = e_row[c]

                results.append(row)

    return pd.DataFrame(results)


st.title("🔍 Conflict of Interest – Fuzzy Matching Tool")

vendor_file = st.file_uploader("Upload Vendor CSV", type="csv")
employee_file = st.file_uploader("Upload Employee CSV", type="csv")

if vendor_file and employee_file:
    vendor_df = pd.read_csv(vendor_file)
    employee_df = pd.read_csv(employee_file)

    vendor_df.columns = vendor_df.columns.str.upper().str.strip()
    employee_df.columns = employee_df.columns.str.upper().str.strip()

    col1, col2, col3 = st.columns(3)

    with col1:
        v_col = st.selectbox("Vendor Field", vendor_df.columns)

    with col2:
        e_col = st.selectbox("Employee Field", employee_df.columns)

    with col3:
        threshold = st.slider("Match Threshold (%)", 60, 100, 80)

    if st.button("Run Analysis"):
        result_df = run_matching(
            vendor_df,
            employee_df,
            v_col,
            e_col,
            threshold
        )

        if result_df.empty:
            st.success("No conflicts found.")
        else:
            st.warning(f"Conflicts Found: {len(result_df)}")
            st.dataframe(result_df, use_container_width=True)

            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                result_df.to_excel(writer, index=False, sheet_name="COI_RESULTS")
            buffer.seek(0)

            st.download_button(
                "Download Excel Report",
                buffer,
                "COI_Fuzzy_Match_Report.xlsx",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
else:
    st.info("Upload both CSV files to begin.")
