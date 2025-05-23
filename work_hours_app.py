
import streamlit as st
from datetime import datetime, timedelta

st.title("Weekly Work Hours Calculator")

required_daily = timedelta(hours=7, minutes=36)

days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
work_times = {}

st.markdown("### Enter Start and End Times")

for day in days:
    col1, col2 = st.columns(2)
    with col1:
        start = st.text_input(f"{day} Start", "7:00", key=f"{day}_start")
    with col2:
        end = st.text_input(f"{day} End", "14:36", key=f"{day}_end")
    work_times[day] = (start, end)

def compute_duration(start, end):
    try:
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
        return end_time - start_time
    except:
        return timedelta()

total_worked = timedelta()
daily_durations = {}

for day, (start, end) in work_times.items():
    duration = compute_duration(start, end)
    daily_durations[day] = duration
    total_worked += duration

total_required = required_daily * len(days)
time_diff_minutes = int((total_worked - total_required).total_seconds() / 60)
diff_sign = "+" if time_diff_minutes > 0 else ""

st.markdown("### Weekly Totals")
st.write(f"**Total Worked:** {total_worked.total_seconds() / 3600:.2f} hours")
st.write("**Required:** 38.00 hours")
st.write(f"**Difference:** {diff_sign}{time_diff_minutes} minutes")

st.markdown("### Daily Work Summary")
for day in days:
    st.write(f"{day}: Worked {daily_durations[day]}")
