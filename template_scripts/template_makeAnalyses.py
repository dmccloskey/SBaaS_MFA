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

###MFA analysis using INCA

analysis_ids = [
    'ALEsKOs01_0_11_evo04tpiA',
    'ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEcoli13CGlc_0',
    'ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo01EPEcoli13CGlc_11',
    'ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo02EPEcoli13CGlc_11',
    'ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo03EPEcoli13CGlc_11',
    'ALEsKOs01_150526_iDM2015_full05_OxicEvo04tpiAEvo04EPEcoli13CGlc_11',
    #...
    ]

#make the analysis table
from SBaaS_MFA.stage02_isotopomer_analysis_execute import stage02_isotopomer_analysis_execute
exanalysis01 = stage02_isotopomer_analysis_execute(session,engine,pg_settings.datadir_settings);
exanalysis01.drop_dataStage02_isotopomer_analysis();
exanalysis01.initialize_dataStage02_isotopomer_analysis();
#reset previous analyses
for analysis_id in analysis_ids:
    exanalysis01.reset_dataStage02_isotopomer_analysis(analysis_id);
#import new analysis
exanalysis01.import_data_stage02_isotopomer_analysis_add('data/tests/analysis_isotopomer/150917_MFA_ALEsKOs01_analysis01.csv');
