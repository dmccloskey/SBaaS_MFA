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

###Make the simulations

#make the simulation table
simulation_ids = ["ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEcoli13CGlc_0",
    "ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo01EPEcoli13CGlc_11",
    "ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo02EPEcoli13CGlc_11",
    "ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo03EPEcoli13CGlc_11",
    "ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo04EPEcoli13CGlc_11",];
from SBaaS_MFA.stage02_isotopomer_simulation_execute import stage02_isotopomer_simulation_execute
exsimulation01 = stage02_isotopomer_simulation_execute(session,engine,pg_settings.datadir_settings);
exsimulation01.drop_dataStage02_isotopomer_simulation();
exsimulation01.initialize_dataStage02_isotopomer_simulation();
#import the simulations
for simulation_id in simulation_ids:
    exsimulation01.reset_dataStage02_isotopomer_simulation(simulation_id);
exsimulation01.import_dataStage02IsotopomerAnalysis_add('data/tests/analysis_isotopomer/150917_MFA_ALEsKOs01_simulation01.csv');
#export the simulations for INCA
#define extra flux constraints (initial KO)
ko_list = [];
flux_dict = {};
flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
flux_dict['EX_etoh_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_for_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_fum_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_lac_DASH_D_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_pyr_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_acald_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_glyclt_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_glyc_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_succ_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0}; 
#check that the model converges to a solution
sol = exsimulation01.simulate_model('150526_iDM2015',ko_list=ko_list,flux_dict=flux_dict);
print(sol.solution.f)
#export the model, flux data, tracer data, and MS data
exsimulation01.execute_makeIsotopomerSimulation_INCA(simulation_ids[0],stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);
#define extra flux constraints (initial KO)
ko_list = [];
flux_dict = {};
flux_dict['EX_o2_LPAREN_e_RPAREN__reverse'] = {'lb':0,'ub':16};
flux_dict['EX_etoh_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_for_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_fum_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
#flux_dict['EX_lac_DASH_D_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0}; end-points produce lactate
flux_dict['EX_pyr_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_acald_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_glyclt_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_glyc_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0};
flux_dict['EX_succ_LPAREN_e_RPAREN_']={'lb':0.0,'ub':0.0}; 
#check that the model converges to a solution
sol = exsimulation01.simulate_model('150526_iDM2015',ko_list=ko_list,flux_dict=flux_dict);
print(sol.solution.f)
for simulation_id in simulation_ids[1:]:
    exsimulation01.execute_makeIsotopomerSimulation_INCA(simulation_id,stationary_I=True,ko_list_I=ko_list,flux_dict_I=flux_dict,description_I=None);
