import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("supply_chain.csv", encoding= 'latin-1')

sns.set_theme(style="whitegrid")
fig1, axes = plt.subplots(2, 2, figsize=(20, 14))
fig1.suptitle('Supply Chain — Delivery & Shipping Analysis', fontsize=16, fontweight='bold')

# ── Chart 1: Delivery Status Breakdown ─────────────────────────────────────
delivery_counts = df['Delivery Status'].value_counts()
colors = ['#E24B4A', '#1D9E75', '#EF9F27', '#378ADD']
axes[0,0].pie(delivery_counts, labels=delivery_counts.index,
              autopct='%1.1f%%', colors=colors, startangle=90)
axes[0,0].set_title('Delivery Status Breakdown', fontweight='bold')

# ── Chart 2: Avg Shipping Delay by Shipping Mode ───────────────────────────
delay_by_mode = df.groupby('Shipping Mode')['Shipping Delay (days)'].mean().sort_values()
bar_colors = ['#1D9E75' if x <= 0 else '#E24B4A' for x in delay_by_mode]
axes[0,1].barh(delay_by_mode.index, delay_by_mode.values, color=bar_colors)
axes[0,1].axvline(0, color='black', linewidth=0.8, linestyle='--')
axes[0,1].set_title('Avg Shipping Delay by Shipping Mode', fontweight='bold')
axes[0,1].set_xlabel('Avg Delay (days)')
for i, v in enumerate(delay_by_mode.values):
    axes[0,1].text(v + 0.05, i, f'{v:.2f}d', va='center', fontsize=9)

# ── Chart 3: Late Delivery Risk % by Market ────────────────────────────────
late_by_market = df.groupby('Market')['Late_delivery_risk'].mean().sort_values(ascending=False) * 100
axes[1,0].bar(late_by_market.index, late_by_market.values, color='#378ADD')
axes[1,0].set_title('Late Delivery Risk % by Market', fontweight='bold')
axes[1,0].set_ylabel('Late Delivery Risk (%)')
axes[1,0].set_ylim(0, 110)
for i, v in enumerate(late_by_market.values):
    axes[1,0].text(i, v + 1.5, f'{v:.1f}%', ha='center', fontsize=9)

# ── Chart 4: Monthly Order Volume Trend ────────────────────────────────────
monthly_orders = df.groupby(['Order Year', 'Order Month'])['Order Id'].nunique().reset_index()
monthly_orders['Period'] = (monthly_orders['Order Year'].astype(str) + '-' +
                             monthly_orders['Order Month'].astype(str).str.zfill(2))
axes[1,1].plot(range(len(monthly_orders)), monthly_orders['Order Id'],
               color='#534AB7', linewidth=2, marker='o', markersize=3)
axes[1,1].set_title('Monthly Order Volume Trend', fontweight='bold')
axes[1,1].set_ylabel('Number of Orders')
step = max(1, len(monthly_orders) // 10)
axes[1,1].set_xticks(range(0, len(monthly_orders), step))
axes[1,1].set_xticklabels(monthly_orders['Period'].iloc[::step], rotation=45, fontsize=8)

plt.tight_layout()
plt.savefig('eda_delivery_and_shipping_analysis.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Page 1 saved!")

fig2, axes = plt.subplots(2, 2, figsize=(20, 14))
fig2.suptitle('Supply Chain — Profit & Sales Analysis', fontsize=16, fontweight='bold')

# ── Chart 5: Top 10 Categories by Revenue ──────────────────────────────────
top_cats = df.groupby('Category Name')['Sales'].sum().sort_values(ascending=True).tail(10)
axes[0,0].barh(top_cats.index, top_cats.values, color='#534AB7')
axes[0,0].set_title('Top 10 Categories by Revenue', fontweight='bold')
axes[0,0].set_xlabel('Total Sales ($)')
axes[0,0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1e6:.1f}M'))
for i, v in enumerate(top_cats.values):
    axes[0,0].text(v + 1000, i, f'${v/1e6:.1f}M', va='center', fontsize=8)

# ── Chart 6: Avg Profit Ratio by Customer Segment ──────────────────────────
profit_segment = df.groupby('Customer Segment')['Order Item Profit Ratio'].mean() * 100
axes[0,1].bar(profit_segment.index, profit_segment.values, color='#1D9E75', width=0.5)
axes[0,1].set_title('Avg Profit Ratio by Customer Segment', fontweight='bold')
axes[0,1].set_ylabel('Profit Ratio (%)')
for i, v in enumerate(profit_segment.values):
    axes[0,1].text(i, v + 0.3, f'{v:.1f}%', ha='center', fontsize=10)

# ── Chart 7: Sales vs Profit by Department ─────────────────────────────────
dept_summary = df.groupby('Department Name').agg(
    Total_Sales=('Sales', 'sum'),
    Total_Profit=('Order Profit Per Order', 'sum')
).reset_index().sort_values('Total_Sales', ascending=True)
x = range(len(dept_summary))
bar_width = 0.4
axes[1,0].barh([i + bar_width/2 for i in x], dept_summary['Total_Sales'],
               height=bar_width, label='Total Sales', color='#534AB7', alpha=0.85)
axes[1,0].barh([i - bar_width/2 for i in x], dept_summary['Total_Profit'],
               height=bar_width, label='Total Profit', color='#1D9E75', alpha=0.85)
axes[1,0].set_yticks(list(x))
axes[1,0].set_yticklabels(dept_summary['Department Name'], fontsize=9)
axes[1,0].set_title('Sales vs Profit by Department', fontweight='bold')
axes[1,0].set_xlabel('Amount ($)')
axes[1,0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1e6:.1f}M'))
axes[1,0].legend(fontsize=9)

# ── Chart 8: Order Status Distribution ─────────────────────────────────────
status_counts = df['Order Status'].value_counts()
axes[1,1].bar(status_counts.index, status_counts.values, color='#EF9F27')
axes[1,1].set_title('Order Status Distribution', fontweight='bold')
axes[1,1].set_ylabel('Number of Orders')
axes[1,1].tick_params(axis='x', rotation=30)
for i, v in enumerate(status_counts.values):
    axes[1,1].text(i, v + 100, f'{v:,}', ha='center', fontsize=8)

plt.tight_layout()
plt.savefig('eda_profit_and_sales_analysis.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Page 2 saved!")


print("=" * 60)
print("📊 KEY OBSERVATIONS FROM EDA")
print("=" * 60)

late_pct = (df['Delivery Status'] == 'Late delivery').mean() * 100
print(f"\n1. DELIVERY: {late_pct:.1f}% of all orders are delivered late.")

best_mode = df.groupby('Shipping Mode')['Shipping Delay (days)'].mean().idxmin()
worst_mode = df.groupby('Shipping Mode')['Shipping Delay (days)'].mean().idxmax()
print(f"\n2. SHIPPING: '{best_mode}' has the lowest avg delay.")
print(f"   '{worst_mode}' has the highest avg delay.")

top_cat = df.groupby('Category Name')['Sales'].sum().idxmax()
print(f"\n3. REVENUE: '{top_cat}' is the highest revenue product category.")

top_market = df.groupby('Market')['Late_delivery_risk'].mean().idxmax()
print(f"\n4. RISK: '{top_market}' market has the highest late delivery risk.")

avg_margin = df['Profit Margin %'].replace(
    [float('inf'), -float('inf')], pd.NA).dropna().mean()
print(f"\n5. PROFIT: Avg profit margin across all orders is {avg_margin:.1f}%.")

print("\n" + "=" * 60)

# Save cleaned dataset
df.to_csv('supply_chain.csv', index=False)
print("✅ Cleaned dataset saved!")