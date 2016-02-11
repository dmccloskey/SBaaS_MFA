import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_1.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_base')
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_models')
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_MFA')
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_isotopomer')
sys.path.append(pg_settings.datadir_settings['drive']+'/genomeScale_MFA')
sys.path.append(pg_settings.datadir_settings['drive']+'/genomeScale_MFA_INCA')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/calculate_utilities')

###import MFA fluxmap from INCA

#simulation_ids that will be used for all analyses
simulation_ids = ["ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEcoli13CGlc_0",
    "ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo01EPEcoli13CGlc_11",
    "ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo02EPEcoli13CGlc_11",
    "ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo03EPEcoli13CGlc_11",
    "ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo04EPEcoli13CGlc_11",];
simulation_file = [
('ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEcoli13CGlc_0', 'C:/Users/dmccloskey-sbrg/Documents/MATLAB/INCAv1.3/workspace/ALEsKOs01/ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEcoli13CGlc_6.mat'),
('ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo01EPEcoli13CGlc_11', 'C:/Users/dmccloskey-sbrg/Documents/MATLAB/INCAv1.3/workspace/ALEsKOs01/ALEsKOs01_150526_iDM2015_OxicEvo04tpiAEvo01EPEcoli13CGlc_5.mat'),
('ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo02EPEcoli13CGlc_11', 'C:/Users/dmccloskey-sbrg/Documents/MATLAB/INCAv1.3/workspace/ALEsKOs01/ALEsKOs01_150526_iDM2015_OxicEvo04tpiAEvo02EPEcoli13CGlc_9.mat'),
('ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo03EPEcoli13CGlc_11', 'C:/Users/dmccloskey-sbrg/Documents/MATLAB/INCAv1.3/workspace/ALEsKOs01/ALEsKOs01_150526_iDM2015_OxicEvo04tpiAEvo03EPEcoli13CGlc_.mat'),
('ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo04EPEcoli13CGlc_11', 'C:/Users/dmccloskey-sbrg/Documents/MATLAB/INCAv1.3/workspace/ALEsKOs01/ALEsKOs01_150526_iDM2015_OxicEvo04tpiAEvo04EPEcoli13CGlc_.mat'),
    ];

#make the fittedData table
from SBaaS_MFA.stage02_isotopomer_fittedData_execute import stage02_isotopomer_fittedData_execute
exfittedData01 = stage02_isotopomer_fittedData_execute(session,engine,pg_settings.datadir_settings);
exfittedData01.drop_dataStage02_isotopomer_fittedData();
exfittedData01.initialize_dataStage02_isotopomer_fittedData();
for simulation_id in simulation_ids:
    exfittedData01.reset_dataStage02_isotopomer_fittedData(simulation_id);
#import .mat files containing the estimated fluxes
for s_f in simulation_file:
    exfittedData01.import_isotopomerSimulationResults_INCA(s_f[0],s_f[1]);
#calculate the statistics
for simulation_id in simulation_ids:
    # calculate the net flux statistics
    exfittedData01.execute_calculateFluxStatistics(simulation_id,flux_units_I = ['mmol*gDCW-1*hr-1'])
#export the fittedData to .csv
exfittedData01.export_data_stage02_isotopomer_fittedFluxStatistics_csv(analysis_ids,'ALEsKOs0_fittedFluxStatistics.csv');
exfittedData01.export_data_stage02_isotopomer_fittedNetFluxStatistics_csv(analysis_ids,'ALEsKOs0_fittedNetFluxStatistics.csv',flux_units_I = ['mmol*gDCW-1*hr-1']);
exfittedData01.export_data_stage02_isotopomer_fittedNetFluxStatistics_csv(analysis_ids,'ALEsKOs0_fittedNetFluxStatistics_coreFluxes.csv',flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized']);
exfittedData01.export_data_stage02_isotopomer_fittedNetFluxes_csv(analysis_ids,'ALEsKOs0_fittedNetFluxes.csv');
exfittedData01.export_data_stage02_isotopomer_fittedMeasuredFragments_csv(analysis_ids,'ALEsKOs0_fittedMeasuredFragments.csv');
exfittedData01.export_data_stage02_isotopomer_fittedData_csv(analysis_ids,'ALEsKOs0_fittedData.csv');

#make the fittedNetFluxes table
from SBaaS_MFA.stage02_isotopomer_fittedNetFluxes_execute import stage02_isotopomer_fittedNetFluxes_execute
exfittedNetFluxes01 = stage02_isotopomer_fittedNetFluxes_execute(session,engine,pg_settings.datadir_settings);
exfittedNetFluxes01.drop_dataStage02_isotopomer_fittedNetFluxes();
exfittedNetFluxes01.initialize_dataStage02_isotopomer_fittedNetFluxes();
for simulation_id in simulation_ids:
    exfittedNetFluxes01.reset_dataStage02_isotopomer_fittedNetFluxes(simulation_id);
    #convert fluxes to net fluxes
    #normalize to glucose uptake
    #break into individual reactions
    exfittedNetFluxes01.execute_makeNetFluxes(simulation_id,
        normalize_rxn_id_I="EX_glc_LPAREN_e_RPAREN_",
        convert_netRxn2IndividualRxns_I=True,
        calculate_fluxStdevFromLBAndUB_I=True,
        calculate_fluxAverageFromLBAndUB_I=False,
        substitute_zeroFluxForNone_I=False,
        lower_bound_I=0.0,upper_bound_I=1000.0
        );
    #convert fluxes to net fluxes
    exfittedNetFluxes01.execute_makeNetFluxes(simulation_id,
        normalize_rxn_id_I='mmol*gDCW-1*hr-1',
        convert_netRxn2IndividualRxns_I=False,
        calculate_fluxStdevFromLBAndUB_I=True,
        calculate_fluxAverageFromLBAndUB_I=False,
        substitute_zeroFluxForNone_I=False,
        lower_bound_I=0.0,upper_bound_I=1000.0
        );
    # calculate the net flux statistics
    exfittedNetFluxes01.execute_calculateNetFluxStatistics(analysis_id,flux_units_I = ['mmol*gDCW-1*hr-1'])
    exfittedNetFluxes01.execute_calculateNetFluxStatistics(simulation_id,
                                        flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized'],
                                        rxn_ids_I = ['ATPM','PGI','MDH','EDA','EDD','SUCOAS','PGL','PGM','PGK','ACONTa','ACONTb','GLCptspp','FUM','ENO','SUCDi','RPE','AKGDH','PDH','GAPD','MALS','CS','GND','PPC','TPI','RPI','PYK','ME1','ME2','TALA','ICDHyr','FBA','PFK','ICL','PPCK']
                                        )
#export the fittedNetFluxes to .csv
exfittedNetFluxes01.export_data_stage02_isotopomer_fittedNetFluxes_csv(
    simulation_ids,
    'ALEsKOs01_fittedNetFluxes.csv');
exfittedNetFluxes01.export_data_stage02_isotopomer_fittedNetFluxStatistics_csv(
    simulation_ids,
    'ALEsKOs01_fittedNetFluxStatistics.csv',
    flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized']);

#make the fittedExchangeFluxes table
#TODO: