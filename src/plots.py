import matplotlib.pyplot as plt

# Plot NPV to Initial Investment Ratio
def plot_npv_ratio(df_fin_profit_ilr):
    plt.figure(figsize=(10,6))
    plt.plot(df_fin_profit_ilr['ILR_value'], df_fin_profit_ilr['npv/I'], color='k', linewidth=2)
    plt.title('Ratio Net Present Value - Initial Investment (NPV/I)')
    plt.grid(axis='both', which='both', linestyle='--')
    plt.ylabel("NPV/I")
    plt.xlabel('Inverter Loading Ratio (ILR)')
    plt.show()

# Plot NPV (M€)
def plot_npv(df_fin_profit_ilr):
    plt.figure(figsize=(10,6))
    plt.plot(df_fin_profit_ilr['ILR_value'], df_fin_profit_ilr['NPV']/1000000, color='k', linewidth=2)
    plt.title('Net Present Value (M€)')
    plt.grid(axis='both', which='both', linestyle='--')
    plt.ylabel("NPV (M€)")
    plt.xlabel('Inverter Loading Ratio (ILR)')
    plt.show()

# Plot IRR (%)
def plot_irr(df_fin_profit_ilr):
    plt.figure(figsize=(10,6))
    plt.plot(df_fin_profit_ilr['ILR_value'], df_fin_profit_ilr['IRR']*100, color='k', linewidth=2)
    plt.title('Internal Rate of Return (%)')
    plt.grid(axis='both', which='both', linestyle='--')
    plt.ylabel("IRR (%)")
    plt.xlabel('Inverter Loading Ratio (ILR)')
    plt.show()

# Plot Clipping
def plot_clipping(clippingdf_group):
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_axes([0,0,1,1])
    ax.tick_params(axis='x', labelrotation=90)
    
    ax.bar(clippingdf_group['ILR'], clippingdf_group['energy_increase_percentage'], color='g', width=0.25)
    ax.bar(clippingdf_group['ILR'], clippingdf_group['energy_loss_to_inverter'], color='r', width=0.25)
    
    plt.ylim([-100, 100])
    plt.title('Inverter Clipping per ILR value')
    plt.legend(['Energy increase over ILR 1.0', 'Energy loss to inverter clipping'], loc=2)
    plt.grid(axis='y', which='both', linestyle='--')
    plt.ylabel("%")
    plt.xlabel('Inverter Loading Ratio (ILR)')
    plt.show()
