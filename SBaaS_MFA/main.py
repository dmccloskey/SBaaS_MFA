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

#make the fittedData table
from SBaaS_MFA.stage02_isotopomer_fittedData_execute import stage02_isotopomer_fittedData_execute
exfittedData01 = stage02_isotopomer_fittedData_execute(session,engine,pg_settings.datadir_settings);

simulation_ids = [
     'ALEsKOs01_150526_iDM2015_full05_OxicEvo04pgiEvo03EPEcoli13CGlc_11',
    ]

## clear specific simulations
#for simulation_id in simulation_ids:
#    exfittedData01.reset_dataStage02_isotopomer_fittedData(simulation_id);

directory = 'F:/Users/dmccloskey-sbrg/Dropbox (UCSD SBRG)/MATLAB/INCA_workspace/ALEsKOs01';

simulation_file = [
 ('ALEsKOs01_150526_iDM2015_full05_OxicEvo04pgiEvo03EPEcoli13CGlc_11',
  directory + '/ALEsKOs01_150526_iDM2015_OxicEvo04pgiEvo03EPEcoli13CGlc_6.mat'), #testing different parameters?

    ];

## import .mat files containing the estimated fluxes
#for s_f in simulation_file:
#    exfittedData01.import_isotopomerSimulationResults_INCA(s_f[0],s_f[1]);

##make the fittedNetFluxes table
#from SBaaS_MFA.stage02_isotopomer_fittedNetFluxes_execute import stage02_isotopomer_fittedNetFluxes_execute
#exfittedNetFluxes01 = stage02_isotopomer_fittedNetFluxes_execute(session,engine,pg_settings.datadir_settings);
#for simulation_id in simulation_ids:
#    exfittedNetFluxes01.reset_dataStage02_isotopomer_fittedNetFluxes(simulation_id);
#    #convert fluxes to net fluxes
#    #normalize to glucose uptake
#    #break into individual reactions
#    exfittedNetFluxes01.execute_makeNetFluxes(simulation_id,
#        normalize_rxn_id_I="EX_glc_LPAREN_e_RPAREN_",
#        convert_netRxn2IndividualRxns_I=True,
#        calculate_fluxStdevFromLBAndUB_I=True,
#        calculate_fluxAverageFromLBAndUB_I=False,
#        substitute_zeroFluxForNone_I=False,
#        correct_fluxLBAndUBBounds_I=False, #maybe overly conservative
#                                        #can only use stdev and not lb/ub for further analyses
#        lower_bound_I=-1000.0,upper_bound_I=1000.0
#        );
#    #convert fluxes to net fluxes
#    #break into individual reactions
#    exfittedNetFluxes01.execute_makeNetFluxes(simulation_id,
#        normalize_rxn_id_I=None,
#        convert_netRxn2IndividualRxns_I=False,
#        calculate_fluxStdevFromLBAndUB_I=True,
#        calculate_fluxAverageFromLBAndUB_I=False,
#        substitute_zeroFluxForNone_I=False,
#        correct_fluxLBAndUBBounds_I=False, #maybe overly conservative
#                                        #can only use stdev and not lb/ub for further analyses
#        lower_bound_I=-1000.0,upper_bound_I=1000.0
#        );
#    # reset the net flux statistics
#    exfittedNetFluxes01.reset_dataStage02_isotopomer_fittedNetFluxStatistics(simulation_id);
#    # calculate the net flux statistics
#    exfittedNetFluxes01.execute_calculateNetFluxStatistics(simulation_id,flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized'])
#    #exfittedNetFluxes01.execute_calculateNetFluxStatistics(simulation_id,flux_units_I = ['mmol*gDCW-1*hr-1'])
#    #exfittedNetFluxes01.execute_calculateNetFluxStatistics(simulation_id,
#    #                                    flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized'],
#    #                                    rxn_ids_I = ['ATPM','PGI','MDH','EDA','EDD','SUCOAS','PGL','PGM','PGK','ACONTa','ACONTb','GLCptspp','FUM','ENO','SUCDi','RPE','AKGDH','PDH','GAPD','MALS','CS','GND','PPC','TPI','RPI','PYK','ME1','ME2','TALA','ICDHyr','FBA','PFK','ICL','PPCK']
#    #                                    )

#make the fittedExchangeFluxes table
from SBaaS_MFA.stage02_isotopomer_fittedExchangeFluxes_execute import stage02_isotopomer_fittedExchangeFluxes_execute
exfittedExchangeFluxes01 = stage02_isotopomer_fittedExchangeFluxes_execute(session,engine,pg_settings.datadir_settings);
for simulation_id in simulation_ids:
    # reset fitted exchange fluxes
    exfittedExchangeFluxes01.reset_dataStage02_isotopomer_fittedExchangeFluxes(simulation_id);
    # break apart lumped reactions into individual reactions
    # normalize the fluxes to glucose uptake
    # convert irreversible reactions to net reactions
    exfittedExchangeFluxes01.execute_makeExchangeFluxes(simulation_id,
        normalize_rxn_id_I="EX_glc_LPAREN_e_RPAREN_",
        convert_netRxn2IndividualRxns_I=True,
        calculate_fluxStdevFromLBAndUB_I=True,
        calculate_fluxAverageFromLBAndUB_I=False,
        substitute_zeroFluxForNone_I=False,
        lower_bound_I=-1000.0,upper_bound_I=1000.0);
    #make net reactions
    exfittedExchangeFluxes01.execute_makeExchangeFluxes(simulation_id,
        normalize_rxn_id_I=None,
        convert_netRxn2IndividualRxns_I=False,
        calculate_fluxStdevFromLBAndUB_I=True,
        calculate_fluxAverageFromLBAndUB_I=False,
        substitute_zeroFluxForNone_I=False,
        lower_bound_I=-1000.0,upper_bound_I=1000.0);
    # reset the net flux statistics
    exfittedExchangeFluxes01.reset_dataStage02_isotopomer_fittedExchangeFluxStatistics(simulation_id);
    # calculate the net flux statistics
    exfittedExchangeFluxes01.execute_calculateExchangeFluxStatistics(simulation_id,flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized'])
    #exfittedExchangeFluxes01.execute_calculateExchangeFluxStatistics(simulation_id,flux_units_I = ['mmol*gDCW-1*hr-1'])
    #exfittedExchangeFluxes01.execute_calculateExchangeFluxStatistics(simulation_id,
    #                                    flux_units_I = ['EX_glc_LPAREN_e_RPAREN__normalized'],
    #                                    rxn_ids_I = ['ATPM','PGI','MDH','EDA','EDD','SUCOAS','PGL','PGM','PGK','ACONTa','ACONTb','GLCptspp','FUM','ENO','SUCDi','RPE','AKGDH','PDH','GAPD','MALS','CS','GND','PPC','TPI','RPI','PYK','ME1','ME2','TALA','ICDHyr','FBA','PFK','ICL','PPCK']
    #                                    )