#SBaaS
from .stage02_isotopomer_fittedNetFluxDifferences_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage02_isotopomer_fittedNetFluxDifferences_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for ...
        '''
        tables_supported = {'data_stage02_isotopomer_fittedNetFluxDifferences':data_stage02_isotopomer_fittedNetFluxDifferences,
                        };
        self.set_supportedTables(tables_supported); 
    ## Query from data_stage02_isotopomer_fittedNetFluxDifferences
    # query rows from data_stage02_isotopomer_fittedNetFluxDifferencess   
    def get_rows_analysisID_dataStage02IsotopomerFittedNetFluxDifferences(self,analysis_id_I):
        '''Query rows by analysis_id that are used from the fittedNetFluxDifferences'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedNetFluxDifferences).filter(
                    data_stage02_isotopomer_fittedNetFluxDifferences.analysis_id.like(analysis_id_I),
                    data_stage02_isotopomer_fittedNetFluxDifferences.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = {'id':d.id,
                    'analysis_id':d.analysis_id,
                    'simulation_id_1':d.simulation_id_1,
                    'simulation_dateAndTime_1':d.simulation_dateAndTime_1,
                    'simulation_id_2':d.simulation_id_2,
                    'simulation_dateAndTime_2':d.simulation_dateAndTime_2,
                    'rxn_id':d.rxn_id,
                    'flux_difference':d.flux_difference,
                    'flux_distance':d.flux_distance,
                    'significant':d.significant,
                    'significant_criteria':d.significant_criteria,
                    'flux_units':d.flux_units,
                    'fold_change_geo':d.fold_change_geo,
                    'used_':d.used_,
                    'comment_':d.comment_};
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);  

    def add_data_stage02_isotopomer_fittedNetFluxDifferences(self, data_I):
        '''add rows of data_stage02_isotopomer_fittedNetFluxDifferences'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_fittedNetFluxDifferences(
                        d
                            #d['analysis_id'],
                            #d['simulation_id_1'],
                            #d['simulation_dateAndTime_1'],
                            #d['simulation_id_2'],
                            #d['simulation_dateAndTime_2'],
                            #d['rxn_id'],
                            #d['flux_difference'],
                            #d['flux_distance'],
                            #d['significant'],
                            #d['significant_criteria'],
                            #d['flux_units'],
                            #d['fold_change_geo'],
                            #d['used_'],
                            #d['comment_']
                            );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_data_stage02_isotopomer_fittedNetFluxDifferences(self,data_I):
        '''update rows of data_stage01_resequencing_lineage'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_fittedNetFluxDifferences).filter(
                           data_stage02_isotopomer_fittedNetFluxDifferences.id==d['id']).update(
                            {'analysis_id':d['analysis_id'],
                            'simulation_id_1':d['simulation_id_1'],
                            'simulation_dateAndTime_1':d['simulation_dateAndTime_1'],
                            'simulation_id_2':d['simulation_id_2'],
                            'simulation_dateAndTime_2':d['simulation_dateAndTime_2'],
                            'rxn_id':d['rxn_id'],
                            'flux_difference':d['flux_difference'],
                            'flux_distance':d['flux_distance'],
                            'significant':d['significant'],
                            'significant_criteria':d['significant_criteria'],
                            'flux_units':d['flux_units'],
                            'fold_change_geo':d['fold_change_geo'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def initialize_datastage02_isotopomer_fittedNetFluxDifferences(self):
        try:
            data_stage02_isotopomer_fittedNetFluxDifferences.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_datastage02_isotopomer_fittedNetFluxDifferences(self):
        try:
            data_stage02_isotopomer_fittedNetFluxDifferences.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage02_isotopomer_fittedNetFluxDifferences(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_isotopomer_fittedNetFluxDifferences).filter(data_stage02_isotopomer_fittedNetFluxDifferences.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
