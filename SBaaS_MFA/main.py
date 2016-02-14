import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
#filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_1.ini';
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_metabolomics.ini';
#filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_metabolomics_151001.ini';
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
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_physiology')
sys.path.append(pg_settings.datadir_settings['github']+'/genomeScale_MFA')
sys.path.append(pg_settings.datadir_settings['github']+'/genomeScale_MFA_INCA')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_visualization')
sys.path.append(pg_settings.datadir_settings['github']+'/SBaaS_statistics')
# SBaaS dependencies paths:
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/python_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/r_statistics')
sys.path.append(pg_settings.datadir_settings['github']+'/listDict')
sys.path.append(pg_settings.datadir_settings['github']+'/ddt_python')
sys.path.append(pg_settings.datadir_settings['github']+'/molmass')

#simulation_ids = [
#     'ALEWt01_140407_iDM2014_OxicEcoli13CGlc_0',
#     'ALEWt01_140407_iDM2014_OxicEvo03Ecoli13CGlc_0',
#     'ALEWt01_140407_iDM2014_OxicEvo04Ecoli13CGlc_0',
#     'ALEWt01_140407_iDM2014_OxicEvo05Ecoli13CGlc_0',
#     'ALEWt01_140407_iDM2014_OxicEvo08Ecoli13CGlc_0',
#     'ALEWt01_140407_iDM2014_OxicEvo09Ecoli13CGlc_0',
#     'ALEWt01_140407_iDM2014_OxicEvo10Ecoli13CGlc_0',
#                 ]

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