p='/home/ubuntu/create_311_project.py'
s=open(p).read()
s=s.replace("df = raw.rename(columns={", "for missing in ['due_date','open_data_channel_type']:\n    if missing not in raw.columns: raw[missing] = pd.NA\ndf = raw.rename(columns={")
s=s.replace("The extract contains **{len(df):,} service requests** created during Q1 2025.", "The extract contains **{len(df):,} real service requests** from a public NYC 311 sample.")
s=s.replace("The extract is a Q1 2025 slice", "The extract is a 100-row sample")
open(p,'w').write(s)
