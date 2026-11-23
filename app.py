import streamlit as st

# =====================================================
# PAGE SETUP
# =====================================================

st.set_page_config(
    page_title="PileTrack",
    page_icon="🚧",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title("🚧 PileTrack - Marine Construction Cost & Delay Engine")

st.markdown(
    "Future Project Planning | Delay Impact | Cost Exposure | Productivity Loss"
)

# =====================================================
# TABS
# =====================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Project Setup",
        "Resource Costs",
        "Delay Event",
        "Results"
    ]
)

# =====================================================
# PROJECT SETUP
# =====================================================

with tab1:

    st.subheader("Project Information")

    contract_value = st.number_input(
        "Contract Value (USD)",
        value=1670000.0
    )

    project_cost = st.number_input(
        "Project Cost (USD)",
        value=1477040.0
    )

    duration_days = st.number_input(
        "Project Duration (Days)",
        value=90
    )

    total_piles = st.number_input(
        "Total Piles",
        value=2000
    )

    working_hours = st.number_input(
        "Working Hours Per Day",
        value=8
    )

    daily_productivity = st.number_input(
        "Daily Productivity (Piles / Day)",
        value=23.0
    )

# =====================================================
# RESOURCE COSTS
# =====================================================

with tab2:

    st.subheader("Equipment Fleet")

    pile_rig_qty = st.number_input(
        "Pile Rig Quantity",
        value=3
    )

    pile_rig_rate = st.number_input(
        "Pile Rig Cost / Day",
        value=1500.0
    )

    excavator_qty = st.number_input(
        "Excavator Quantity",
        value=2
    )

    excavator_rate = st.number_input(
        "Excavator Cost / Day",
        value=1000.0
    )

    barge_qty = st.number_input(
        "Barge Quantity",
        value=1
    )

    barge_rate = st.number_input(
        "Barge Cost / Day",
        value=700.0
    )

    st.divider()

    labour_daily_cost = st.number_input(
        "Labour Cost / Day",
        value=547.0
    )

    fuel_daily_cost = st.number_input(
        "Fuel Cost / Day",
        value=500.0
    )

    overhead_daily_cost = st.number_input(
        "Overhead Cost / Day",
        value=139.0
    )

    ld_per_day = st.number_input(
        "LD Exposure / Day",
        value=1000.0
    )

# =====================================================
# DELAY EVENT
# =====================================================

with tab3:

    st.subheader("Delay Details")

    delay_type = st.selectbox(
        "Delay Type",
        [
            "Weather",
            "Equipment Breakdown",
            "Client Delay",
            "Material Shortage",
            "Labour Issue"
        ]
    )

    delay_hours = st.number_input(
        "Delay Hours",
        value=4.0
    )

    repair_cost = st.number_input(
        "Repair Cost",
        value=0.0
    )

    responsible_party = st.selectbox(
        "Responsible Party",
        [
            "Contractor",
            "Client",
            "Weather",
            "Third Party"
        ]
    )

# =====================================================
# CALCULATIONS
# =====================================================

# Equipment Totals

pile_rig_total = pile_rig_qty * pile_rig_rate

excavator_total = excavator_qty * excavator_rate

barge_total = barge_qty * barge_rate

equipment_daily_cost = (
    pile_rig_total
    + excavator_total
    + barge_total
)

# Hourly costs

daily_project_cost = project_cost / duration_days

hourly_project_cost = daily_project_cost / working_hours

equipment_hourly = equipment_daily_cost / working_hours

labour_hourly = labour_daily_cost / working_hours

fuel_hourly = fuel_daily_cost / working_hours

overhead_hourly = overhead_daily_cost / working_hours

# Productivity

productivity_per_hour = (
    daily_productivity / working_hours
)

lost_piles = (
    productivity_per_hour * delay_hours
)

# Cost impacts

equipment_loss = (
    equipment_hourly * delay_hours
)

labour_loss = (
    labour_hourly * delay_hours
)

fuel_loss = (
    fuel_hourly * delay_hours
)

overhead_loss = (
    overhead_hourly * delay_hours
)

# Weather consumes less fuel

if delay_type == "Weather":
    fuel_loss = fuel_loss * 0.2

actual_delay_cost = (
    equipment_loss
    + labour_loss
    + fuel_loss
    + overhead_loss
    + repair_cost
)

additional_days = (
    delay_hours / working_hours
)

cost_per_pile = (
    project_cost / total_piles
)

claimable_cost = 0

if responsible_party == "Client":
    claimable_cost = actual_delay_cost

# =====================================================
# RESULTS
# =====================================================

with tab4:

    st.subheader("Delay Impact Assessment")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Actual Delay Cost",
            f"${actual_delay_cost:,.2f}"
        )

    with c2:
        st.metric(
            "Lost Piles",
            f"{lost_piles:.2f}"
        )

    with c3:
        st.metric(
            "Additional Days",
            f"{additional_days:.2f}"
        )

    with c4:
        st.metric(
            "Claimable Cost",
            f"${claimable_cost:,.2f}"
        )

    st.divider()

    st.subheader("Equipment Fleet Breakdown")

    st.write(
        f"Pile Rigs ({pile_rig_qty}) = ${pile_rig_total:,.2f}"
    )

    st.write(
        f"Excavators ({excavator_qty}) = ${excavator_total:,.2f}"
    )

    st.write(
        f"Barges ({barge_qty}) = ${barge_total:,.2f}"
    )

    st.write(
        f"Total Equipment Cost = ${equipment_daily_cost:,.2f}"
    )

    st.divider()

    st.subheader("Cost Breakdown")

    st.write(
        f"Equipment Standby = ${equipment_loss:,.2f}"
    )

    st.write(
        f"Labour Standby = ${labour_loss:,.2f}"
    )

    st.write(
        f"Fuel Impact = ${fuel_loss:,.2f}"
    )

    st.write(
        f"Overhead Impact = ${overhead_loss:,.2f}"
    )

    st.write(
        f"Repair Cost = ${repair_cost:,.2f}"
    )

    st.divider()

    st.subheader("Project Summary")

    st.write(f"Delay Type : {delay_type}")
    st.write(f"Responsible Party : {responsible_party}")
    st.write(f"Project Cost : ${project_cost:,.2f}")
    st.write(f"Cost Per Pile : ${cost_per_pile:,.2f}")
    st.write(f"Potential Hourly Exposure : ${hourly_project_cost:,.2f}/hr")