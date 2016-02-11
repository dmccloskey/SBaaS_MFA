import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_1.ini';
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_metabolomics.ini';
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

###Structural analysis

from SBaaS_LIMS.lims_msMethod_query import lims_msMethod_query
msmethodquery = lims_msMethod_query(session,engine,pg_settings.datadir_settings);
from genomeScale_MFA.MFA_utilities import MFA_utilities
from io_utilities.base_exportData import base_exportData

def export_allMetaboliteFragmentMappings_csv(filename_I='ms_method_fragments.csv',mode_I='-',msmethodtype_I='tuning'):
    '''export all metabolite fragment mappings to .csv
    INPUT:
    filename_I = string, filename
    mode_I = string, MS mode (default=-)
    msmethodtype_I = string, ms_methodtype (default=tuning)
    '''
    
    mfautil = MFA_utilities();
    #Query met_ids
    met_ids = [];
    met_ids = msmethodquery.get_metIDs_msModeAndMsMethodType('-','tuning');
    data_O = [];
    for met in met_ids:
        # fragments
        fragment_formulas = [];
        parent,product=[],[];
        parent,product= msmethodquery.get_precursorAndProductFormulas_metID(met,'-','tuning');
        parent = list(set(parent));
        fragment_formulas.extend(parent);
        fragment_formulas.extend(product);
        # fragment carbon mappings
        frag_cmap = {};
        frag_cmap = msmethodquery.get_precursorFormulaAndProductFormulaAndCMapsAndPositions_metID(met,'-','tuning');
        for frag in fragment_formulas:
            if frag_cmap[frag]['fragment'] is None: continue;
            # combine into a structure
            positions,elements = [],[];
            positions,elements = mfautil.convert_fragmentAndElements2PositionAndElements(frag_cmap[frag]['fragment'],frag_cmap[frag]['fragment_elements']);
            if positions:
                tmp = {'met_id':met,'positions':positions,'elements':elements,'formula':frag};
                data_O.append(tmp);
    # export the data
    if data_O:
        export = base_exportData(data_O)
        export.write_dict2csv(filename_I);