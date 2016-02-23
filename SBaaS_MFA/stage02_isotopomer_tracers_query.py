#SBaaS
from .stage02_isotopomer_tracers_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage02_isotopomer_tracers_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for ...
        '''
        tables_supported = {'data_stage02_isotopomer_tracers':data_stage02_isotopomer_tracers,
                        };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage02_isotopomer_tracers
    # query rows from data_stage02_isotopomer_tracers
    def get_rows_experimentID_dataStage02IsotopomerTracers(self,experiment_id_I):
        '''Querry rows by experiment_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_tracers).filter(
                    data_stage02_isotopomer_tracers.experiment_id.like(experiment_id_I)).order_by(
                    data_stage02_isotopomer_tracers.met_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                                'sample_name_abbreviation':d.sample_name_abbreviation,
                                'met_id':d.met_id,
                                'met_name':d.met_name,
                                'isotopomer_formula':d.isotopomer_formula,
                                'met_elements':d.met_elements,
                                'met_atompositions':d.met_atompositions,
                                'ratio':d.ratio,
                                'supplier':d.supplier,
                                'supplier_reference':d.supplier_reference,
                                'purity':d.purity,
                                'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerTracers(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry rows by experiment_id and sample_name_abbreviation that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_tracers).filter(
                    data_stage02_isotopomer_tracers.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_tracers.sample_name_abbreviation.like(sample_name_abbreviation_I)).order_by(
                    data_stage02_isotopomer_tracers.met_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                                'sample_name_abbreviation':d.sample_name_abbreviation,
                                'met_id':d.met_id,
                                'met_name':d.met_name,
                                'isotopomer_formula':d.isotopomer_formula,
                                'met_elements':d.met_elements,
                                'met_atompositions':d.met_atompositions,
                                'ratio':d.ratio,
                                'supplier':d.supplier,
                                'supplier_reference':d.supplier_reference,
                                'purity':d.purity,
                                'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def add_data_stage02_isotopomer_tracers(self, data_I):
        '''add rows of data_stage02_isotopomer_tracers'''
        if data_I:
            for d in data_I:
                met_elements = None;
                if d['met_elements']:
                    met_elements = d['met_elements']
                    met_elements = met_elements.replace('{','')
                    met_elements = met_elements.replace('}','')
                    met_elements = met_elements.split(',')
                met_atompositions = None;
                if d['met_atompositions']:
                    met_atompositions = d['met_atompositions']
                    met_atompositions = met_atompositions.replace('{','')
                    met_atompositions = met_atompositions.replace('}','')
                    met_atompositions = met_atompositions.split(',')
                    met_atompositions = [int(x) for x in met_atompositions];
                isotopomer_formula = None;
                if d['isotopomer_formula']:
                    isotopomer_formula = d['isotopomer_formula']
                    isotopomer_formula = isotopomer_formula.replace('{','')
                    isotopomer_formula = isotopomer_formula.replace('}','')
                    isotopomer_formula = isotopomer_formula.split(',')
                try:
                    data_add = data_stage02_isotopomer_tracers(d['experiment_id'],
                            d['sample_name_abbreviation'],
                            d['met_id'],
                            d['met_name'],
                            isotopomer_formula,
                            met_elements,
                            met_atompositions,
                            d['ratio'],
                            d['supplier'],
                            d['supplier_reference'],
                            d['purity'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_tracers(self,data_I):
        #TODO:
        '''update rows of '''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(tracers).filter(
                            #tracers.sample_name.like(d['sample_name'])
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'model_id':d['model_id'],
                            'met_id':d['met_id'],
                            'met_name':d['met_name'],
                            'isotopomer_formula':d['isotopomer_formula'],
                            'met_elements':d['met_elements'],
                            'met_atompositions':d['met_atompositions'],
                            'ratio':d['ratio'],
                            'supplier':d['supplier'],
                            'supplier_reference':d['supplier_reference'],
                            'purity':d['purity'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def initialize_datastage02_isotopomer_tracers(self):
        try:
            data_stage02_isotopomer_tracers.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_datastage02_isotopomer_tracers(self):
        try:
            data_stage02_isotopomer_tracers.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
            
