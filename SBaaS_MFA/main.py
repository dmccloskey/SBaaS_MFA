import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Documents/GitHub/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_settings/settings_metabolomics.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
# SBaaS paths:
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_base')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_models')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_MFA')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_isotopomer')
sys.path.append(pg_settings.datadir_settings['github']+'/genomeScale_MFA')
sys.path.append(pg_settings.datadir_settings['github']+'/genomeScale_MFA_INCA')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_visualization')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_physiology')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')

###manuscript 2
###------------------

simulation_ids=[
    #'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_0', # incorrect glyc_c and 25
    #'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_1', # incorrect 25
    #'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_3', # correct
    #'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_3_noCofactorsMS', # no cofactor measurements
    #'WTEColi_113C80_U13C20_01_140407_iDM2014_full04_OxicWtGlc_0', # different data set
    #'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_0_extra', # added glucose importer and gluthione oxidase/reductase
    #'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_0_pfl', # removed pfl
    'WTEColi_113C80_U13C20_02_140407_iDM2014_full04_OxicWtGlc_0_no13C', # no 13C measurements
    ]

#make the fittedNetFluxes table
from SBaaS_MFA.stage02_isotopomer_fittedNetFluxes_execute import stage02_isotopomer_fittedNetFluxes_execute
exfittedNetFluxes01 = stage02_isotopomer_fittedNetFluxes_execute(session,engine,pg_settings.datadir_settings);
for simulation_id in simulation_ids:
    exfittedNetFluxes01.reset_dataStage02_isotopomer_fittedNetFluxes(simulation_id);
    # break apart lumped reactions into individual reactions
    # normalize the fluxes to glucose uptake
    # convert irreversible reactions to net reactions
    exfittedNetFluxes01.execute_makeNetFluxes(simulation_id,
        normalize_rxn_id_I="EX_glc_LPAREN_e_RPAREN_",
        convert_netRxn2IndividualRxns_I=True,
        calculate_fluxStdevFromLBAndUB_I=True,
        calculate_fluxAverageFromLBAndUB_I=False,
        substitute_zeroFluxForNone_I=False,
        correct_fluxLBAndUBBounds_I=True,
        lower_bound_I=-1000.0,upper_bound_I=1000.0);
    #make net reactions
    exfittedNetFluxes01.execute_makeNetFluxes(simulation_id,
        normalize_rxn_id_I=None,
        convert_netRxn2IndividualRxns_I=False,
        calculate_fluxStdevFromLBAndUB_I=True,
        calculate_fluxAverageFromLBAndUB_I=False,
        substitute_zeroFluxForNone_I=False,
        correct_fluxLBAndUBBounds_I=True,
        lower_bound_I=-1000.0,upper_bound_I=1000.0);
    # reset the net flux statistics
    exfittedNetFluxes01.reset_dataStage02_isotopomer_fittedNetFluxStatistics(simulation_id);
    # calculate the net flux statistics
    exfittedNetFluxes01.execute_calculateNetFluxStatistics(simulation_id,flux_units_I = ['mmol*gDCW-1*hr-1'])
    exfittedNetFluxes01.execute_calculateNetFluxStatistics(simulation_id,
                                        flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized'],
                                        rxn_ids_I = ['ATPM','PGI','MDH','EDA','EDD','SUCOAS','PGL','PGM','PGK','ACONTa','ACONTb','GLCptspp','FUM','ENO','SUCDi','RPE','AKGDH','PDH','GAPD','MALS','CS','GND','PPC','TPI','RPI','PYK','ME1','ME2','TALA','ICDHyr','FBA','PFK','ICL','PPCK']
                                        )

##make the fittedExchangeFluxes table
#from SBaaS_MFA.stage02_isotopomer_fittedExchangeFluxes_execute import stage02_isotopomer_fittedExchangeFluxes_execute
#exfittedExchangeFluxes01 = stage02_isotopomer_fittedExchangeFluxes_execute(session,engine,pg_settings.datadir_settings);
#for simulation_id in simulation_ids:
#    # reset fitted exchange fluxes
#    exfittedExchangeFluxes01.reset_dataStage02_isotopomer_fittedExchangeFluxes(simulation_id);
#    # break apart lumped reactions into individual reactions
#    # normalize the fluxes to glucose uptake
#    # convert irreversible reactions to net reactions
#    exfittedExchangeFluxes01.execute_makeExchangeFluxes(simulation_id,
#        normalize_rxn_id_I="EX_glc_LPAREN_e_RPAREN_",
#        convert_netRxn2IndividualRxns_I=True,
#        calculate_fluxStdevFromLBAndUB_I=True,
#        calculate_fluxAverageFromLBAndUB_I=False,
#        substitute_zeroFluxForNone_I=False,
#        lower_bound_I=-1000.0,upper_bound_I=1000.0);
#    #make net reactions
#    exfittedExchangeFluxes01.execute_makeExchangeFluxes(simulation_id,
#        normalize_rxn_id_I=None,
#        convert_netRxn2IndividualRxns_I=False,
#        calculate_fluxStdevFromLBAndUB_I=True,
#        calculate_fluxAverageFromLBAndUB_I=False,
#        substitute_zeroFluxForNone_I=False,
#        lower_bound_I=-1000.0,upper_bound_I=1000.0);
#    # reset the net flux statistics
#    exfittedExchangeFluxes01.reset_dataStage02_isotopomer_fittedExchangeFluxStatistics(simulation_id);
#    # calculate the net flux statistics
#    exfittedExchangeFluxes01.execute_calculateExchangeFluxStatistics(simulation_id,flux_units_I = ['mmol*gDCW-1*hr-1'])
#    exfittedExchangeFluxes01.execute_calculateExchangeFluxStatistics(simulation_id,
#                                        flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized'],
#                                        rxn_ids_I = ['ATPM','PGI','MDH','EDA','EDD','SUCOAS','PGL','PGM','PGK','ACONTa','ACONTb','GLCptspp','FUM','ENO','SUCDi','RPE','AKGDH','PDH','GAPD','MALS','CS','GND','PPC','TPI','RPI','PYK','ME1','ME2','TALA','ICDHyr','FBA','PFK','ICL','PPCK']
#                                        )