import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
pd.set_option('display.max_columns', None)
sns.set_theme(style="whitegrid")

# print("Libraries loaded successfully!")

# # Load the dataset (update path if needed)
df = pd.read_csv('raw data/DataCoSupplyChainDataset.csv', encoding='latin-1')

# # First look
# print("Shape:", df.shape)
# print("\nColumn names:\n", df.columns.tolist())
# print("\nFirst 5 rows:")
# print(df.head())

# print("=== DATA TYPES ===")
# print(df.dtypes)

# print("\n=== MISSING VALUES ===")
# missing = df.isnull().sum()
# missing_pct = (missing / len(df) * 100).round(2)
# missing_df = pd.DataFrame({'Missing Count': missing, 'Missing %': missing_pct})
# print(missing_df[missing_df['Missing Count'] > 0])

# print("\n=== BASIC STATS ===")
# print(df.describe())

######### --data cleaning
# Drop useless / PII columns 
cols_to_drop = [
    'Product Description',   # 100% missing
    'Order Zipcode',         # 86% missing
    'Customer Email',        # PII
    'Customer Password',     # PII
    'Customer Street',       # PII
    'Product Image',         # URL, not useful
    'Customer Fname',        # PII (we have Customer Id)
    'Customer Lname'         # PII
]
df.drop(columns=cols_to_drop, inplace=True)
print(f"Dropped {len(cols_to_drop)} columns. New shape: {df.shape}")

#  Fix remaining missing values ────────────────────────────────────────
df['Customer Zipcode'].fillna(df['Customer Zipcode'].median(), inplace=True)

#  Convert date columns to datetime ────────────────────────────────────
df['order date (DateOrders)']    = pd.to_datetime(df['order date (DateOrders)'])
df['shipping date (DateOrders)'] = pd.to_datetime(df['shipping date (DateOrders)'])

# Create useful derived columns ───────────────────────────────────────
# Actual shipping delay (positive = late, negative = early)
df['Shipping Delay (days)'] = (
    df['Days for shipping (real)'] - df['Days for shipment (scheduled)']
)

# Order year and month for trend analysis
df['Order Year']  = df['order date (DateOrders)'].dt.year
df['Order Month'] = df['order date (DateOrders)'].dt.month

# Profit margin % per order item
df['Profit Margin %'] = (
    df['Order Profit Per Order'] / df['Sales'] * 100
).round(2)

# Rename messy columns for convenience ────────────────────────────────
df.rename(columns={
    'order date (DateOrders)'    : 'Order Date',
    'shipping date (DateOrders)' : 'Shipping Date',
    'Days for shipping (real)'   : 'Days Shipped (actual)',
    'Days for shipment (scheduled)': 'Days Shipped (scheduled)',
}, inplace=True)

# Final check ─────────────────────────────────────────────────────────
print("\n✅ Cleaned shape:", df.shape)
print("\nRemaining missing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print("\nNew columns added:", ['Shipping Delay (days)', 'Order Year', 'Order Month', 'Profit Margin %'])

df.to_csv('supply_chain.csv', index=False)
print("✅ Cleaned dataset saved!")