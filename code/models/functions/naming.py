def rename_columns(df):
    df['date'] = df['Unnamed: 0']
    df['pko_fob_malaysia'] = df['Palmkernel oil(FOB Malaysia)']
    df['pko_cif_rotterdam'] = df['Palmkernel oil (CIF Rotterdam)']
    df['coconut_cif_rotterdam'] = df['Coconut oil (CIF Rotterdam)']
    df['palm_oil_cif_nwe'] = df['Palm oil, crude (CIF NWE)']
    df['palm_olein_fob_malaysia'] = df['Palm olein (FOB Malaysia)']
    df['palm_stearin_cif_rotterdam'] = df['Palm stearin (CIF Rotterdam)']
    df['tallow_fob_us_gulf'] = df['Tallow, edible (FOB US Gulf)']
    df['soybean_oil_zlz2'] = df['Soybean Oil, edible (ZLZ2)']
    df['bio_ethanol'] = df['(Bio)-Ethanol']
    df['fatty_alcohol_c12_14_fob_asia'] = df['Fatty Alcohol C12-14 FOB Asia (USD/ton)']
    df['fatty_alcohol_c16_18_fob_asia'] = df['Fatty Alcohol C16-18 FOB Asia (USD/ton)']
    df['fatty_alcohol_c12_14_fd_nwe'] = df['Fatty Alcohol C12-14 FD NWE (EUR/ton)']
    df['rspo'] = df['RSPO (EUR/ton)']
    df['jet_fuel_europe'] = df['Jet Fuel Europe (US$/ton)']
    df['jet_fuel_us'] = df['Jet Fuel US ($c/gallon)']
    df['jet_fuel_us_usd_mt'] = df['Jet Fuel US US$/MT']
    df['ukraine_war'] = df['Ukraine War']
    df['malaysia_harvest'] = df['Malaysia-Harvest']
    df['malaysia_disaster'] = df['Malaysia_Disaster']
    df['indonesia_disaster'] = df['Indonesia_Disaster']
    df['indonesia_harvest'] = df['Indonesia-Harvest']
    df['myr_usd_rate'] = df['MYR_USD_rate']
    df['idr_usd_rate'] = df['IDR_USD_rate']
    df['palm_oil_harvest_area_indonesia'] = df['Palm Oil Harvest Area (M.Ha) - Indonesia']
    df['palm_oil_production_indonesia'] = df['Palm Oil Production  (M.Tons) - Indonesia']
    df['pko_production_indonesia'] = df['PKO Production - Indonesia']
    df['palm_oil_harvest_area_malaysia'] = df['Palm Oil Harvest Area (M.Ha) - Malaysia']
    df['palm_oil_production_malaysia'] = df['Palm Oil Production  (M.Tons) - Malaysia']
    df['pko_production_malaysia'] = df['PKO Production - Malaysia']
    df['pko_monthly_stocks_indonesia'] = df['PKO Monthly Stocks (M.Tons) - Indonesia']
    df['pko_monthly_stocks_malaysia'] = df['PKO Monthly Stocks (M.Tons) - Malaysia']
    df['pko_domestic_consumption_indonesia'] = df['PKO Domestic Consumption (M.Tons) - Indonesia']
    df['pko_domestic_consumption_malaysia'] = df['PKO Domestic Consumption (M.Tons) - Malaysia']
    df['pko_exports_indonesia'] = df['PKO Exports (M.Tons) - Indonesia']
    df['pko_exports_malaysia'] = df['PKO Exports (M.Tons) - Malaysia']
    df['pko_total_supply_indonesia'] = df['PKO Total Supply (M.Tons) - Indonesia']
    df['pko_total_supply_malaysia'] = df['PKO Total Supply (M.Tons) - Malaysia']
    df['pmi_indonesia'] = df['Indonesia PMI']
    df['pmi_malaysia'] = df['Malaysia PMI']
    df['export_tarrifs_indonesia'] = df['Export_Tarrifs_Indonesia']
    df['cpopc_mal_ind_2015'] = df['CPOPC_Mal/Ind_2015']
    df['mspo_certification'] = df['MSPO Certification']
    df['ispo_certification'] = df['ISPO Certification']

    #delete old columns
    df = df.drop(columns=['Unnamed: 0', 'Palmkernel oil(FOB Malaysia)', 'Palmkernel oil (CIF Rotterdam)', 'Coconut oil (CIF Rotterdam)',
                           'Palm oil, crude (CIF NWE)', 'Palm olein (FOB Malaysia)',
                           'Palm stearin (CIF Rotterdam)', 'Tallow, edible (FOB US Gulf)', 'Soybean Oil, edible (ZLZ2)', '(Bio)-Ethanol',
                           'Fatty Alcohol C12-14 FOB Asia (USD/ton)', 'Fatty Alcohol C16-18 FOB Asia (USD/ton)', 'Fatty Alcohol C12-14 FD NWE (EUR/ton)',
                           'RSPO (EUR/ton)', 'Jet Fuel Europe (US$/ton)',
                           'Jet Fuel US ($c/gallon)', 'Jet Fuel US US$/MT', 'Ukraine War', 'Malaysia-Harvest',
                           'Malaysia_Disaster', 'Indonesia_Disaster', 'Indonesia-Harvest',
                           'MYR_USD_rate', 'IDR_USD_rate', 
                           'Palm Oil Harvest Area (M.Ha) - Indonesia',
                           'Palm Oil Production  (M.Tons) - Indonesia',
                           'PKO Production - Indonesia', 'Palm Oil Harvest Area (M.Ha) - Malaysia',
                           'Palm Oil Production  (M.Tons) - Malaysia', 'PKO Production - Malaysia',
                           'PKO Monthly Stocks (M.Tons) - Indonesia',
                           'PKO Monthly Stocks (M.Tons) - Malaysia',
                           'PKO Domestic Consumption (M.Tons) - Indonesia',
                           'PKO Domestic Consumption (M.Tons) - Malaysia',
                           'PKO Exports (M.Tons) - Indonesia', 'PKO Exports (M.Tons) - Malaysia',
                           'PKO Total Supply (M.Tons) - Indonesia',
                           'PKO Total Supply (M.Tons) - Malaysia','Indonesia PMI', 'Malaysia PMI',
                           'Export_Tarrifs_Indonesia', 'CPOPC_Mal/Ind_2015', 'MSPO Certification','ISPO Certification'])
    
    return df