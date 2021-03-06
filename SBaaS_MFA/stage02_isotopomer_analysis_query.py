#SBaaS
from .stage02_isotopomer_analysis_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage02_isotopomer_analysis_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for ...
        '''
        tables_supported = {'data_stage02_isotopomer_analysis':data_stage02_isotopomer_analysis,
                        };
        self.set_supportedTables(tables_supported); 
    ## Query from data_stage02_isotopomer_analysis
    # query simulation_id
    def get_simulationID_analysisID_dataStage02IsotopomerAnalysis(self,analysis_id_I):
        '''Querry simulations that are used for the anlaysis'''
        try:
            data = self.session.query(data_stage02_isotopomer_analysis.simulation_id).filter(
                    data_stage02_isotopomer_analysis.analysis_id.like(analysis_id_I),
                    data_stage02_isotopomer_analysis.used_.is_(True)).group_by(
                    data_stage02_isotopomer_analysis.simulation_id).order_by(
                    data_stage02_isotopomer_analysis.simulation_id.asc()).all();
            simulation_ids_O = [];
            if data: 
                for d in data:
                    simulation_ids_O.append(d.simulation_id);
            return simulation_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def add_data_stage02_isotopomer_analysis(self, data_I):
        '''add rows of data_stage02_isotopomer_analysis'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_analysis(d
                            #d['analysis_id'],d['simulation_id'],
                            #d['used_'],
                            #d['comment_']
                            );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_analysis(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_analysis'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_analysis).filter(
                            data_stage02_isotopomer_analysis.id.like(d['id'])
                            ).update(
                            {
                            'analysis_id':d['analysis_id'],
                            'simulation_id':d['simulation_id'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def initialize_datastage02_isotopomer_analysis(self):
        try:
            data_stage02_isotopomer_analysis.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_datastage02_isotopomer_analysis(self):
        try:
            data_stage02_isotopomer_analysis.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage02_isotopomer_analysis(self,analysis_id_I = None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage02_isotopomer_analysis).filter(data_stage02_isotopomer_analysis.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
