#LIMS
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
#SBaaS
from .stage02_isotopomer_measuredData_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base

class stage02_isotopomer_measuredData_query(sbaas_base):
    ## Query from data_stage02_isotopomer_measuredFragments
    # query sample_name_abbreviations from data_stage02_isotopomer_measuredFragments
    def get_sampleNameAbbreviations_experimentID_dataStage02IsotopomerMeasuredFragments(self,experiment_id_I):
        '''Querry sample_name_abbreviations that are used from
        the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_measuredFragments.sample_name_abbreviation).filter(
                    data_stage02_isotopomer_measuredFragments.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_measuredFragments.used_.is_(True)).group_by(
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation).order_by(
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            if data: 
                for d in data:
                    sample_name_abbreviations_O.append(d.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    # query timePoint from data_stage02_isotopomer_measuredFragments
    def get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFragments(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry rows for the sample_name_abbreviation that are used from the experiment'''
        try:
            data = self.session.query(
                    data_stage02_isotopomer_measuredFragments.time_point).filter(
                    data_stage02_isotopomer_measuredFragments.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage02_isotopomer_measuredFragments.used_.is_(True)).group_by(
                    data_stage02_isotopomer_measuredFragments.time_point).order_by(
                    data_stage02_isotopomer_measuredFragments.time_point.asc()).all();
            time_points_O = [];
            if data: 
                for d in data:
                    time_points_O.append(d.time_point);
            return time_points_O;
        except SQLAlchemyError as e:
            print(e);
    # query row from data_stage02_isotopomer_measuredFragments
    def get_row_experimentID_dataStage02IsotopomerMeasuredFragments(self,experiment_id_I):
        '''Querry rows by experiment_id that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_measuredFragments.experiment_id,
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation,
                    data_stage02_isotopomer_measuredFragments.time_point,
                    data_stage02_isotopomer_measuredFragments.met_id,
                    data_stage02_isotopomer_measuredFragments.fragment_id,
                    data_stage02_isotopomer_measuredFragments.fragment_formula,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_average,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_cv,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_stdev,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_units,
                    data_stage02_isotopomer_measuredFragments.scan_type,
                    data_stage02_isotopomer_measuredFragments.met_elements,
                    data_stage02_isotopomer_measuredFragments.met_atompositions).filter(
                    data_stage02_isotopomer_measuredFragments.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_measuredFragments.used_.is_(True)).group_by(
                    data_stage02_isotopomer_measuredFragments.experiment_id,
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation,
                    data_stage02_isotopomer_measuredFragments.time_point,
                    data_stage02_isotopomer_measuredFragments.met_id,
                    data_stage02_isotopomer_measuredFragments.fragment_id,
                    data_stage02_isotopomer_measuredFragments.fragment_formula,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_average,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_cv,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_stdev,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_units,
                    data_stage02_isotopomer_measuredFragments.scan_type,
                    data_stage02_isotopomer_measuredFragments.met_elements,
                    data_stage02_isotopomer_measuredFragments.met_atompositions).order_by(
                    data_stage02_isotopomer_measuredFragments.experiment_id.asc(),
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation.asc(),
                    data_stage02_isotopomer_measuredFragments.met_id.asc(),
                    data_stage02_isotopomer_measuredFragments.fragment_formula.desc(),
                    data_stage02_isotopomer_measuredFragments.time_point.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                            'sample_name_abbreviation':d.sample_name_abbreviation,
                            'time_point':d.time_point,
                            'met_id':d.met_id,
                            'fragment_id':d.fragment_id,
                            'fragment_formula':d.fragment_formula,
                            'intensity_normalized_average':d.intensity_normalized_average,
                            'intensity_normalized_cv':d.intensity_normalized_cv,
                            'intensity_normalized_stdev':d.intensity_normalized_stdev,
                            'intensity_normalized_units':d.intensity_normalized_units,
                            'scan_type':d.scan_type,
                            'met_elements':d.met_elements,
                            'met_atompositions':d.met_atompositions};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_row_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFragments(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry rows for the sample_name_abbreviation that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_measuredFragments.experiment_id,
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation,
                    data_stage02_isotopomer_measuredFragments.time_point,
                    data_stage02_isotopomer_measuredFragments.met_id,
                    data_stage02_isotopomer_measuredFragments.fragment_id,
                    data_stage02_isotopomer_measuredFragments.fragment_formula,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_average,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_cv,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_stdev,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_units,
                    data_stage02_isotopomer_measuredFragments.scan_type,
                    data_stage02_isotopomer_measuredFragments.met_elements,
                    data_stage02_isotopomer_measuredFragments.met_atompositions).filter(
                    data_stage02_isotopomer_measuredFragments.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage02_isotopomer_measuredFragments.used_.is_(True)).group_by(
                    data_stage02_isotopomer_measuredFragments.experiment_id,
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation,
                    data_stage02_isotopomer_measuredFragments.time_point,
                    data_stage02_isotopomer_measuredFragments.met_id,
                    data_stage02_isotopomer_measuredFragments.fragment_id,
                    data_stage02_isotopomer_measuredFragments.fragment_formula,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_average,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_cv,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_stdev,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_units,
                    data_stage02_isotopomer_measuredFragments.scan_type,
                    data_stage02_isotopomer_measuredFragments.met_elements,
                    data_stage02_isotopomer_measuredFragments.met_atompositions).order_by(
                    data_stage02_isotopomer_measuredFragments.experiment_id.asc(),
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation.asc(),
                    data_stage02_isotopomer_measuredFragments.met_id.asc(),
                    data_stage02_isotopomer_measuredFragments.fragment_formula.desc(),
                    data_stage02_isotopomer_measuredFragments.time_point.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                            'sample_name_abbreviation':d.sample_name_abbreviation,
                            'time_point':d.time_point,
                            'met_id':d.met_id,
                            'fragment_id':d.fragment_id,
                            'fragment_formula':d.fragment_formula,
                            'intensity_normalized_average':d.intensity_normalized_average,
                            'intensity_normalized_cv':d.intensity_normalized_cv,
                            'intensity_normalized_stdev':d.intensity_normalized_stdev,
                            'intensity_normalized_units':d.intensity_normalized_units,
                            'scan_type':d.scan_type,
                            'met_elements':d.met_elements,
                            'met_atompositions':d.met_atompositions};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    # query row from data_stage02_isotopomer_measuredFragments
    def get_row_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage02IsotopomerMeasuredFragments(self,experiment_id_I,sample_name_abbreviation_I,time_point_I):
        '''Querry rows for the sample_name_abbreviation that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_measuredFragments.experiment_id,
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation,
                    data_stage02_isotopomer_measuredFragments.time_point,
                    data_stage02_isotopomer_measuredFragments.met_id,
                    data_stage02_isotopomer_measuredFragments.fragment_id,
                    data_stage02_isotopomer_measuredFragments.fragment_formula,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_average,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_cv,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_stdev,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_units,
                    data_stage02_isotopomer_measuredFragments.scan_type,
                    data_stage02_isotopomer_measuredFragments.met_elements,
                    data_stage02_isotopomer_measuredFragments.met_atompositions).filter(
                    data_stage02_isotopomer_measuredFragments.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_measuredFragments.time_point.like(time_point_I),
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage02_isotopomer_measuredFragments.used_.is_(True)).group_by(
                    data_stage02_isotopomer_measuredFragments.experiment_id,
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation,
                    data_stage02_isotopomer_measuredFragments.time_point,
                    data_stage02_isotopomer_measuredFragments.met_id,
                    data_stage02_isotopomer_measuredFragments.fragment_id,
                    data_stage02_isotopomer_measuredFragments.fragment_formula,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_average,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_cv,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_stdev,
                    data_stage02_isotopomer_measuredFragments.intensity_normalized_units,
                    data_stage02_isotopomer_measuredFragments.scan_type,
                    data_stage02_isotopomer_measuredFragments.met_elements,
                    data_stage02_isotopomer_measuredFragments.met_atompositions).order_by(
                    data_stage02_isotopomer_measuredFragments.experiment_id.asc(),
                    data_stage02_isotopomer_measuredFragments.sample_name_abbreviation.asc(),
                    data_stage02_isotopomer_measuredFragments.met_id.asc(),
                    data_stage02_isotopomer_measuredFragments.fragment_formula.desc(),
                    data_stage02_isotopomer_measuredFragments.time_point.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                            'sample_name_abbreviation':d.sample_name_abbreviation,
                            'time_point':d.time_point,
                            'met_id':d.met_id,
                            'fragment_id':d.fragment_id,
                            'fragment_formula':d.fragment_formula,
                            'intensity_normalized_average':d.intensity_normalized_average,
                            'intensity_normalized_cv':d.intensity_normalized_cv,
                            'intensity_normalized_stdev':d.intensity_normalized_stdev,
                            'intensity_normalized_units':d.intensity_normalized_units,
                            'scan_type':d.scan_type,
                            'met_elements':d.met_elements,
                            'met_atompositions':d.met_atompositions};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    ## Query from data_stage02_isotopomer_measuredFluxes
    # query rows from data_stage02_isotopomer_measuredFluxes
    def get_rows_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFluxes(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_measuredFluxes).filter(
                    data_stage02_isotopomer_measuredFluxes.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage02_isotopomer_measuredFluxes.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_measuredFluxes.used_.is_(True)).order_by(
                    data_stage02_isotopomer_measuredFluxes.model_id.asc(),
                    data_stage02_isotopomer_measuredFluxes.rxn_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                    'model_id':d.model_id,
                    'sample_name_abbreviation':d.sample_name_abbreviation,
                    #'time_point':d.time_point,
                    'rxn_id':d.rxn_id,
                    'flux_average':d.flux_average,
                    'flux_stdev':d.flux_stdev,
                    'flux_lb':d.flux_lb,
                    'flux_ub':d.flux_ub,
                    'flux_units':d.flux_units,
                    'used_':d.used_,
                    'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFluxes(self,experiment_id_I,model_id_I,sample_name_abbreviation_I):
        '''Querry rows by model_id that are used'''
        try:
            data = self.session.query(data_stage02_isotopomer_measuredFluxes).filter(
                    data_stage02_isotopomer_measuredFluxes.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage02_isotopomer_measuredFluxes.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_measuredFluxes.model_id.like(model_id_I),
                    data_stage02_isotopomer_measuredFluxes.used_.is_(True)).order_by(
                    data_stage02_isotopomer_measuredFluxes.model_id.asc(),
                    data_stage02_isotopomer_measuredFluxes.rxn_id.asc()).all();
            rows_O = [];
            if data: 
                for d in data:
                    row_tmp = {'experiment_id':d.experiment_id,
                    'model_id':d.model_id,
                    'sample_name_abbreviation':d.sample_name_abbreviation,
                    #'time_point':d.time_point,
                    'rxn_id':d.rxn_id,
                    'flux_average':d.flux_average,
                    'flux_stdev':d.flux_stdev,
                    'flux_lb':d.flux_lb,
                    'flux_ub':d.flux_ub,
                    'flux_units':d.flux_units,
                    'used_':d.used_,
                    'comment_':d.comment_};
                    rows_O.append(row_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def add_data_stage02_isotopomer_measuredFragments(self, data_I):
        '''add rows of data_stage02_isotopomer_measuredFragments'''
        if data_I:
            for d in data_I:
                intensity_normalized_average = None;
                if d['intensity_normalized_average']:
                    intensity_normalized_average = d['intensity_normalized_average']
                    intensity_normalized_average = intensity_normalized_average.replace('{','')
                    intensity_normalized_average = intensity_normalized_average.replace('}','')
                    intensity_normalized_average = intensity_normalized_average.split(',')
                intensity_normalized_cv = None;
                if d['intensity_normalized_cv']:
                    intensity_normalized_cv = d['intensity_normalized_cv']
                    intensity_normalized_cv = intensity_normalized_cv.replace('{','')
                    intensity_normalized_cv = intensity_normalized_cv.replace('}','')
                    intensity_normalized_cv = intensity_normalized_cv.split(',')
                intensity_normalized_stdev = None;
                if d['intensity_normalized_stdev']:
                    intensity_normalized_stdev = d['intensity_normalized_stdev']
                    intensity_normalized_stdev = intensity_normalized_stdev.replace('{','')
                    intensity_normalized_stdev = intensity_normalized_stdev.replace('}','')
                    intensity_normalized_stdev = intensity_normalized_stdev.split(',')
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
                try:
                    data_add = data_stage02_isotopomer_measuredFragments(d['experiment_id'],
                                d['sample_name_abbreviation'],
                                d['time_point'],
                                d['met_id'],
                                d['fragment_id'],
                                d['fragment_formula'],
                                intensity_normalized_average,
                                intensity_normalized_cv,
                                intensity_normalized_stdev,
                                d['intensity_normalized_units'],
                                d['scan_type'],
                                met_elements,
                                met_atompositions,
                                d['used_'],
                                d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_measuredFluxes(self, data_I):
        '''add rows of data_stage02_isotopomer_measuredFluxes'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_measuredFluxes(d['experiment_id'],
                            d['model_id'],
                            d['sample_name_abbreviation'],
                            #d['time_point'],
                            d['rxn_id'],
                            d['flux_average'],
                            d['flux_stdev'],
                            d['flux_lb'],
                            d['flux_ub'],
                            d['flux_units'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_measuredPools(self, data_I):
        '''add rows of data_stage02_isotopomer_measuredPools'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_measuredPools(d['experiment_id'],
                            d['model_id'],
                            d['sample_name_abbreviation'],
                            d['time_point'],
                            d['met_id'],
                            d['pool_size'],
                            d['concentration_average'],
                            d['concentration_var'],
                            d['concentration_lb'],
                            d['concentration_ub'],
                            d['concentration_units'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_measuredFluxes(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_measuredFluxes'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_measuredFluxes).filter(
                            #sample.sample_name.like(d['sample_name'])
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            #'time_point':d['time_point'],
                            'rxn_id':d['rxn_id'],
                            'flux_average':d['flux_average'],
                            'flux_stdev':d['flux_stdev'],
                            'flux_lb':d['flux_lb'],
                            'flux_ub':d['flux_ub'],
                            'flux_units':d['flux_units'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_measuredPools(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_measuredPools'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_measuredPools).filter(
                            #sample.sample_name.like(d['sample_name'])
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'met_id':d['met_id'],
                            'pool_size':d['pool_size'],
                            'concentration_average':d['concentration_average'],
                            'concentration_var':d['concentration_var'],
                            'concentration_lb':d['concentration_lb'],
                            'concentration_ub':d['concentration_ub'],
                            'concentration_units':d['concentration_units'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_measuredFragments(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_measuredFragments'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_measuredFragments).filter(
                            #sample.sample_name.like(d['sample_name'])
                            ).update(
                            {'experiment_id':d['experiment_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'met_id':d['met_id'],
                            'fragment_id':d['fragment_id'],
                            'fragment_formula':d['fragment_formula'],
                            'intensity_normalized_average':d['intensity_normalized_average'],
                            'intensity_normalized_cv':d['intensity_normalized_cv'],
                            'intensity_normalized_stdev':d['intensity_normalized_stdev'],
                            'intensity_normalized_units':d['intensity_normalized_units'],
                            'scan_type':d['scan_type'],
                            'met_elements':d['met_elements'],
                            'met_atompositions':d['met_atompositions'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def initialize_dataStage02_isotopomer_measuredData(self):
        try: 
            data_stage02_isotopomer_measuredFluxes.__table__.create(self.engine,True);
            data_stage02_isotopomer_measuredPools.__table__.create(self.engine,True);
            data_stage02_isotopomer_measuredFragments.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage02_isotopomer_measuredData(self):
        try:
            data_stage02_isotopomer_measuredFluxes.__table__.drop(self.engine,True);
            data_stage02_isotopomer_measuredPools.__table__.drop(self.engine,True);
            data_stage02_isotopomer_measuredFragments.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_isotopomer_measuredPools(self,experiment_id_I = None):
        try:
            reset = self.session.query(data_stage02_isotopomer_measuredPools).filter(data_stage02_isotopomer_measuredPools.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_isotopomer_measuredFluxes(self,experiment_id_I,sample_name_abbreviations_I=[]):
        try:
            if sample_name_abbreviations_I:
                for sna in sample_name_abbreviations_I:
                    reset = self.session.query(data_stage02_isotopomer_measuredFluxes).filter(
                        data_stage02_isotopomer_measuredFluxes.experiment_id.like(experiment_id_I),
                        data_stage02_isotopomer_measuredFluxes.sample_name_abbreviation.like(sna)).delete(
                        synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_measuredFluxes).filter(
                    data_stage02_isotopomer_measuredFluxes.experiment_id.like(experiment_id_I)).delete(
                    synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_isotopomer_measuredFragments(self,experiment_id_I,sample_name_abbreviations_I=[]):
        try:
            if sample_name_abbreviations_I:
                for sna in sample_name_abbreviations_I:
                    reset = self.session.query(data_stage02_isotopomer_measuredFragments).filter(
                        data_stage02_isotopomer_measuredFragments.experiment_id.like(experiment_id_I),
                        data_stage02_isotopomer_measuredFragments.sample_name_abbreviation.like(sna)).delete(
                        synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_measuredFragments).filter(
                    data_stage02_isotopomer_measuredFragments.experiment_id.like(experiment_id_I)).delete(
                    synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);

