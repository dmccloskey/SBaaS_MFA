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

###Import the measured data

#make the measuredData table
from SBaaS_MFA.stage02_isotopomer_measuredData_execute import stage02_isotopomer_measuredData_execute
exmeasuredData01 = stage02_isotopomer_measuredData_execute(session,engine,pg_settings.datadir_settings);
exmeasuredData01.drop_dataStage02_isotopomer_measuredData();
exmeasuredData01.initialize_dataStage02_isotopomer_measuredData();
exmeasuredData01.reset_dataStage02_isotopomer_measuredData('ALEsKOs01_evo04tpiA_11');
#define the model and sample conversions for import
ko_list = [];
flux_dict = {};
metID2RxnID = {'glc-D':{'model_id':'150526_iDM2015','rxn_id':'EX_glc_LPAREN_e_RPAREN_'},
                            'ac':{'model_id':'150526_iDM2015','rxn_id':'EX_ac_LPAREN_e_RPAREN_'},
                            'succ':{'model_id':'150526_iDM2015','rxn_id':'EX_succ_LPAREN_e_RPAREN_'},
                            'lac-D':{'model_id':'150526_iDM2015','rxn_id':'EX_lac_DASH_D_LPAREN_e_RPAREN_'},
                            'biomass':{'model_id':'150526_iDM2015','rxn_id':'Ec_biomass_iJO1366_WT_53p95M'}};
snaIsotopomer2snaPhysiology01 = {
        'OxicEvo04tpiAEcoli13CGlc':'OxicEvo04tpiAEcoliGlc',
        'OxicEvo04tpiAEvo01EPEcoli13CGlc':'OxicEvo04tpiAEvo01EPEcoliGlc',
        'OxicEvo04tpiAEvo02EPEcoli13CGlc':'OxicEvo04tpiAEvo02EPEcoliGlc',
        'OxicEvo04tpiAEvo03EPEcoli13CGlc':'OxicEvo04tpiAEvo03EPEcoliGlc',
        'OxicEvo04tpiAEvo04EPEcoli13CGlc':'OxicEvo04tpiAEvo04EPEcoliGlc',
                            }
sample_name_abbreviations01 = [
        #'OxicEvo04tpiAEcoli13CGlc',
        'OxicEvo04tpiAEvo01EPEcoli13CGlc',
        'OxicEvo04tpiAEvo02EPEcoli13CGlc',
        'OxicEvo04tpiAEvo03EPEcoli13CGlc',
        'OxicEvo04tpiAEvo04EPEcoli13CGlc',
                            ];
#import measured fluxes from data_stage01_physiology_averages
exmeasuredData01.reset_datastage02_isotopomer_measuredFluxes('ALEsKOs01')
exmeasuredData01.execute_makeMeasuredFluxes('ALEsKOs01',
                                metID2RxnID_I=metID2RxnID,
                                sample_name_abbreviations_I=sample_name_abbreviations01,
                                snaIsotopomer2snaPhysiology_I=snaIsotopomer2snaPhysiology01)
#import measured isotopomers from from data_stage01_isotopomer_averagesNormSum
exmeasuredData01.reset_datastage02_isotopomer_measuredFragments('ALEsKOs01')
exmeasuredData01.execute_makeMeasuredFragments('ALEsKOs01',
        sample_name_abbreviations_I=sample_name_abbreviations01
        );
#read in the data for OxicEvo04tpiAEcoli13CGlc from .csv
#'data/tests/analysis_isotopomer/150917_MFA_ALEsKOs01_OxicEvo04tpiAEcoli13CGlc_measuredFluxes.csv'
#'data/tests/analysis_isotopomer/150917_MFA_ALEsKOs01_OxicEvo04tpiAEcoli13CGlc_measuredFragments.csv'
#export the measuredData to .csv
exmeasuredData01.export_data_stage02_isotopomer_measuredFragments_csv(
    experiment_ids_I=['ALEsKOs01'],
    sample_name_abbreviations_I=sample_name_abbreviations01,
    filename_O='ALEsKOs01_measuredFragments.csv')
exmeasuredData01.export_data_stage02_isotopomer_measuredFluxes_csv(
    experiment_ids_I=['ALEsKOs01'],
    model_ids_I=['150526_iDM2015'],
    sample_name_abbreviations_I=sample_name_abbreviations01,
    filename_O='ALEsKOs01_measuredFluxes.csv')

#make the tracers table
from SBaaS_MFA.stage02_isotopomer_tracers_execute import stage02_isotopomer_tracers_execute
extracers01 = stage02_isotopomer_tracers_execute(session,engine,pg_settings.datadir_settings);
extracers01.drop_dataStage02_isotopomer_tracers();
extracers01.initialize_dataStage02_isotopomer_tracers();
extracers01.reset_dataStage02_isotopomer_tracers('ALEsKOs01_evo04tpiA_11');
extracers01.import_data_stage02_isotopomer_tracers_add('data/tests/analysis_isotopomer/150917_Isotopomer_ALEsKOs01_tracers01.csv');
