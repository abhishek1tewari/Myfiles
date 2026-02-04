import streamlit as st
import pandas as pd
from rapidfuzz import fuzz
from io import BytesIO

# -----------------------------
# APP CONFIG
# -----------------------------
st.set_page_config(
    page_title="COI Analyzer Pro",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #3B8ED0;
        color: white;
        height: 3em;
        font-weight: bold;
    }
    .stButton>button:hover {
        border-color: #3B8ED0;
        color: #3B8ED0;
    }
    div[data-testid="stMetric"] {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)


# -----------------------------
# LOGIC
# -----------------------------
def run_matching(vendor_df, employee_df, v_col, e_col, threshold):
    results = {}

    # 1. Determine columns to match
    match_pairs = []

    if v_col == "Auto-detect" and e_col == "Auto-detect":
        common = set(vendor_df.columns).intersection(employee_df.columns)
        for col in common:
            match_pairs.append((col, col))
    elif v_col != "Auto-detect" and e_col != "Auto-detect":
        match_pairs.append((v_col, e_col))
    else:
        return None, "Please select both fields or leave both as 'Auto-detect'."

    if not match_pairs:
        return None, "No common column names found for auto-detection."

    # 2. Run Match
    for vc, ec in match_pairs:
        # Check heuristics for fuzzy vs exact
        is_fuzzy_candidate = any(x in vc.upper() for x in ["NAME", "ADDRESS"]) or \
                             any(x in ec.upper() for x in ["NAME", "ADDRESS"])

        if is_fuzzy_candidate:
            # Fuzzy Match
            rows = []
            v_series = vendor_df[vc].dropna().astype(str)
            e_series = employee_df[ec].dropna().astype(str)

            # Optimisation: For larger datasets, this double loop is slow.
            # In a real heavy app, we'd use vectorization or recordlinkage library.
            # Keeping it simple for demo.
            for v_idx, v_val in v_series.items():
                for e_idx, e_val in e_series.items():
                    score = fuzz.token_set_ratio(v_val, e_val)
                    if score >= threshold:
                        row = {
                            "MATCH_TYPE": "FUZZY",
                            "MATCH_FIELD": f"{vc} vs {ec}",
                            "MATCH_SCORE": score
                        }
                        # Add all columns
                        for c in vendor_df.columns: row[f"VENDOR_{c}"] = vendor_df.at[v_idx, c]
                        for c in employee_df.columns: row[f"EMPLOYEE_{c}"] = employee_df.at[e_idx, c]
                        rows.append(row)

            if rows:
                results[f"{vc}_vs_{ec}"] = pd.DataFrame(rows)

        else:
            # Exact Match
            merged = vendor_df.merge(
                employee_df,
                left_on=vc,
                right_on=ec,
                how="inner",
                suffixes=("_VENDOR", "_EMPLOYEE")
            )

            if not merged.empty:
                merged.insert(0, "MATCH_SCORE", 100)
                merged.insert(0, "MATCH_FIELD", f"{vc} vs {ec}")
                merged.insert(0, "MATCH_TYPE", "EXACT")
                results[f"{vc}_vs_{ec}"] = merged

    return results, None


# -----------------------------
# UI LAYOUT
# -----------------------------

# Sidebar
with st.sidebar:
    st.header("Upload Data")

    vendor_file = st.file_uploader("Upload Vendor Master (CSV)", type="csv")
    employee_file = st.file_uploader("Upload Employee Master (CSV)", type="csv")

    st.divider()

    st.header("Configuration")

    # Placeholders for dropdowns
    v_cols = ["Auto-detect"]
    e_cols = ["Auto-detect"]

    if vendor_file:
        vendor_df = pd.read_csv(vendor_file)
        vendor_df.columns = vendor_df.columns.str.upper().str.strip()
        v_cols += list(vendor_df.columns)
    else:
        vendor_df = None

    if employee_file:
        employee_df = pd.read_csv(employee_file)
        employee_df.columns = employee_df.columns.str.upper().str.strip()
        e_cols += list(employee_df.columns)
    else:
        employee_df = None

    v_col = st.selectbox("Vendor Match Field", v_cols)
    e_col = st.selectbox("Employee Match Field", e_cols)

    st.write("")  # Spacer
    threshold = st.slider("Fuzzy Match Sensitivity (%)", 60, 100, 80)

# Main Area
st.title("COI Analyzer Pro")
st.caption("Conflict of Interest Detection Tool")

if vendor_df is None or employee_df is None:
    st.info("👋 Welcome! Please upload your **Vendor** and **Employee** CSV files in the sidebar to begin.")

    # Demo data generation (Optional helper)
    with st.expander("Need sample data?"):
        st.write("Copy-paste these into CSV files to test:")
        c1, c2 = st.columns(2)
        with c1:
            st.code(
                "ID,NAME,ADDRESS\nV1,Acme Corp,123 Main St\nV2,Global Tech,456 Market Rd\nV3,Smith Consulting,789 Oak Ave",
                language="csv")
            st.caption("vendor.csv")
        with c2:
            st.code(
                "EMP_ID,NAME,ADDRESS\nE1,John Smith,123 Main Street\nE2,Jane Doe,999 Elm St\nE3,Bob Wilson,789 Oak Avenue",
                language="csv")
            st.caption("employee.csv")

else:
    # Data Preview
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Vendor Data")
        st.dataframe(vendor_df.head(3), use_container_width=True, hide_index=True)
        st.caption(f"{len(vendor_df)} records")
    with c2:
        st.subheader("Employee Data")
        st.dataframe(employee_df.head(3), use_container_width=True, hide_index=True)
        st.caption(f"{len(employee_df)} records")

    st.divider()

    # Action
    if st.button("RUN ANALYSIS"):
        with st.spinner("Analyzing records for conflicts..."):
            results, error = run_matching(vendor_df, employee_df, v_col, e_col, threshold)

            if error:
                st.error(error)
            elif not results:
                st.success("✅ No conflicts found! No matches detected between datasets.")
            else:
                st.success(f"⚠️ Conflicts Found in {len(results)} categories!")

                # Create Excel buffer
                output = BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:

                    tabs = st.tabs(list(results.keys()))

                    for i, (sheet_name, df) in enumerate(results.items()):
                        # Excel Write
                        safe_sheet = sheet_name[:31].replace(":", "").replace("/", "")
                        df.to_excel(writer, sheet_name=safe_sheet, index=False)

                        # UI Display
                        with tabs[i]:
                            st.dataframe(df, use_container_width=True)
                            st.metric("Matches Found", len(df))

                output.seek(0)

                # Download Button
                st.download_button(
                    label="📥 Download COI Report (Excel)",
                    data=output,
                    file_name="COI_Analysis_Report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
