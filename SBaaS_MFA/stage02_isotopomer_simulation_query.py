#SBaaS
from .stage02_isotopomer_simulation_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage02_isotopomer_simulation_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for ...
        '''
        tables_supported = {'data_stage02_isotopomer_simulation':data_stage02_isotopomer_simulation,
                        };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage02_isotopomer_simulation
    # query simulation_id
    def get_simulationID_experimentIDAndSampleNameAbbreviationsAndModelIDAndMappingID_dataStage02IsotopomerSimulation(self,experiment_id_I,sample_name_abbreviation_I,model_id_I,mapping_id_I):
        '''Querry model_ids for the sample_name_abbreviation that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation.simulation_id).filter(
                    data_stage02_isotopomer_simulation.model_id.like(model_id_I),
                    data_stage02_isotopomer_simulation.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage02_isotopomer_simulation.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_simulation.mapping_id.like(mapping_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).group_by(
                    data_stage02_isotopomer_simulation.simulation_id).order_by(
                    data_stage02_isotopomer_simulation.simulation_id.asc()).all();
            simulation_ids_O = [];
            if data: 
                for d in data:
                    simulation_ids_O.append(d.simulation_id);
            return simulation_ids_O;
        except SQLAlchemyError as e:
            print(e);
    # query sample_name_abbreviations from data_stage02_isotopomer_simulation
    def get_sampleNameAbbreviations_experimentID_dataStage02IsotopomerSimulation(self,experiment_id_I):
        '''Querry sample_name_abbreviations that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation.sample_name_abbreviation).filter(
                    data_stage02_isotopomer_simulation.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).group_by(
                    data_stage02_isotopomer_simulation.sample_name_abbreviation).order_by(
                    data_stage02_isotopomer_simulation.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            if data: 
                for d in data:
                    sample_name_abbreviations_O.append(d.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndModelIDAndMappingID_dataStage02IsotopomerSimulation(self,experiment_id_I,model_id_I,mapping_id_I):
        '''Querry sample_name_abbreviations for the model_id and mapping that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation.sample_name_abbreviation).filter(
                    data_stage02_isotopomer_simulation.model_id.like(model_id_I),
                    data_stage02_isotopomer_simulation.mapping_id.like(mapping_id_I),
                    data_stage02_isotopomer_simulation.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).group_by(
                    data_stage02_isotopomer_simulation.sample_name_abbreviation).order_by(
                    data_stage02_isotopomer_simulation.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            if data: 
                for d in data:
                    sample_name_abbreviations_O.append(d.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    def get_sampleNameAbbreviations_experimentIDAndModelID_dataStage02IsotopomerSimulation(self,experiment_id_I,model_id_I):
        '''Querry sample_name_abbreviations for the model_id  that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation.sample_name_abbreviation).filter(
                    data_stage02_isotopomer_simulation.model_id.like(model_id_I),
                    data_stage02_isotopomer_simulation.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).group_by(
                    data_stage02_isotopomer_simulation.sample_name_abbreviation).order_by(
                    data_stage02_isotopomer_simulation.sample_name_abbreviation.asc()).all();
            sample_name_abbreviations_O = [];
            if data: 
                for d in data:
                    sample_name_abbreviations_O.append(d.sample_name_abbreviation);
            return sample_name_abbreviations_O;
        except SQLAlchemyError as e:
            print(e);
    # query model_ids from data_stage02_isotopomer_simulation
    def get_modelID_experimentIDAndSampleNameAbbreviations_dataStage02IsotopomerSimulation(self,experiment_id_I,sample_name_abbreviation_I):
        '''Querry model_ids for the sample_name_abbreviation that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation.model_id).filter(
                    data_stage02_isotopomer_simulation.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage02_isotopomer_simulation.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).group_by(
                    data_stage02_isotopomer_simulation.model_id).order_by(
                    data_stage02_isotopomer_simulation.model_id.asc()).all();
            model_ids_O = [];
            if data: 
                for d in data:
                    model_ids_O.append(d.model_id);
            return model_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_modelID_experimentID_dataStage02IsotopomerSimulation(self,experiment_id_I):
        '''Querry model_ids that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation.model_id).filter(
                    data_stage02_isotopomer_simulation.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).group_by(
                    data_stage02_isotopomer_simulation.model_id).order_by(
                    data_stage02_isotopomer_simulation.model_id.asc()).all();
            model_ids_O = [];
            if data: 
                for d in data:
                    model_ids_O.append(d.model_id);
            return model_ids_O;
        except SQLAlchemyError as e:
            print(e);
    # query mapping_ids from data_stage02_isotopomer_simulation
    def get_mappingID_experimentIDAndSampleNameAbbreviationsAndModelID_dataStage02IsotopomerSimulation(self,experiment_id_I,sample_name_abbreviation_I,model_id_I):
        '''Querry model_ids for the sample_name_abbreviation that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation.mapping_id).filter(
                    data_stage02_isotopomer_simulation.model_id.like(model_id_I),
                    data_stage02_isotopomer_simulation.sample_name_abbreviation.like(sample_name_abbreviation_I),
                    data_stage02_isotopomer_simulation.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).group_by(
                    data_stage02_isotopomer_simulation.mapping_id).order_by(
                    data_stage02_isotopomer_simulation.mapping_id.asc()).all();
            mapping_ids_O = [];
            if data: 
                for d in data:
                    mapping_ids_O.append(d.mapping_id);
            return mapping_ids_O;
        except SQLAlchemyError as e:
            print(e);
    def get_mappingID_experimentIDAndModelID_dataStage02IsotopomerSimulation(self,experiment_id_I,model_id_I):
        '''Querry mapping_ids for the model_id that are used from the experiment'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation.mapping_id).filter(
                    data_stage02_isotopomer_simulation.model_id.like(model_id_I),
                    data_stage02_isotopomer_simulation.experiment_id.like(experiment_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).group_by(
                    data_stage02_isotopomer_simulation.mapping_id).order_by(
                    data_stage02_isotopomer_simulation.mapping_id.asc()).all();
            mapping_ids_O = [];
            if data: 
                for d in data:
                    mapping_ids_O.append(d.mapping_id);
            return mapping_ids_O;
        except SQLAlchemyError as e:
            print(e);
    # query rows from data_stage02_isotopomer_simulation
    def get_rows_simulationID_dataStage02IsotopomerSimulation(self,simulation_id_I):
        '''Querry rows that are used from the simulation'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation).filter(
                    data_stage02_isotopomer_simulation.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    rows_O.append({
                            'simulation_id':d.simulation_id,
                            'experiment_id':d.experiment_id,
                            'model_id':d.model_id,
                            'mapping_id':d.mapping_id,
                            'sample_name_abbreviation':d.sample_name_abbreviation,
                            'time_point':d.time_point,
                            'used_':d.used_,
                            'comment_':d.comment_});
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_simulation_simulationID_dataStage02IsotopomerSimulation(self,simulation_id_I):
        '''Querry rows that are used from the simulation'''
        try:
            data = self.session.query(data_stage02_isotopomer_simulation).filter(
                    data_stage02_isotopomer_simulation.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_simulation.used_.is_(True)).all();
            simulation_id_O = []
            experiment_id_O = []
            model_id_O = []
            mapping_id_O = []
            sample_name_abbreviation_O = []
            time_point_O = []
            simulation_O = {};
            if data: 
                for d in data:
                    simulation_id_O.append(d.simulation_id);
                    experiment_id_O.append(d.experiment_id);
                    model_id_O.append(d.model_id);
                    mapping_id_O.append(d.mapping_id);
                    sample_name_abbreviation_O.append(d.sample_name_abbreviation);
                    time_point_O.append(d.time_point);
                simulation_id_O = list(set(simulation_id_O))
                experiment_id_O = list(set(experiment_id_O))
                model_id_O = list(set(model_id_O))
                mapping_id_O = list(set(mapping_id_O))
                sample_name_abbreviation_O = list(set(sample_name_abbreviation_O))
                time_point_O = list(set(time_point_O))
                simulation_O={
                        'simulation_id':simulation_id_O,
                        'experiment_id':experiment_id_O,
                        'model_id':model_id_O,
                        'mapping_id':mapping_id_O,
                        'sample_name_abbreviation':sample_name_abbreviation_O,
                        'time_point':time_point_O};
                
            return simulation_O;
        except SQLAlchemyError as e:
            print(e);
    def add_data_stage02_isotopomer_simulation(self, data_I):
        '''add rows of data_stage02_isotopomer_simulation'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_simulation(d['simulation_id'],
                            d['experiment_id'],
                            d['model_id'],
                            d['mapping_id'],
                            d['sample_name_abbreviation'],
                            d['time_point'],
                            d['used_'],
                            d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit()
    def update_data_stage02_isotopomer_simulation(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_simulation'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_simulation).filter(
                            data_stage02_isotopomer_simulation.id.like(d['id'])
                            ).update(
                            {
                            'simulation_id':d['simulation_id'],
                            'experiment_id':d['experiment_id'],
                            'model_id':d['model_id'],
                            'mapping_id':d['mapping_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def initialize_datastage02_simulation(self):
        try:
            data_stage02_isotopomer_simulation.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_datastage02_simulation(self):
        try:
            data_stage02_isotopomer_simulation.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_datastage02_isotopomer_simulation(self,simulation_id_I):
        """Remove fitted flux information by simulation_id"""
        query_cmd = ('''DELETE FROM "data_stage02_isotopomer_simulationParameters"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedData"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedFluxes"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedFragments"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedMeasuredFluxResiduals"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedMeasuredFluxes"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedMeasuredFragmentResiduals"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedMeasuredFragments"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedNetFluxes"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedNetFluxStatistics"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedFluxStatistics"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fittedNetFluxDifferences"
                WHERE simulation_id LIKE '%s';
                DELETE FROM "data_stage02_isotopomer_fluxSplits"
                WHERE simulation_id LIKE '%s';
        ''' %(simulation_id_I,simulation_id_I,simulation_id_I,simulation_id_I,simulation_id_I,simulation_id_I,simulation_id_I,simulation_id_I,simulation_id_I,
              simulation_id_I,simulation_id_I,simulation_id_I,simulation_id_I))

        data = self.session.execute(query_cmd);
        self.session.commit();
    def update_datastage02_isotopomer_simulationID(self,simulation_id_new,simulation_id_old):
        '''Update the simulation ID'''
        try:
            query_cmd = ('''UPDATE "data_stage02_isotopomer_simulationParameters"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedData"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedFluxes"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedFragments"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedMeasuredFluxResiduals"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedMeasuredFluxes"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedMeasuredFragmentResiduals"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedMeasuredFragments"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedNetFluxStatistics"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedFluxStatistics"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedNetFluxes"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_simulation"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_analysis"
                        SET simulation_id='%s'
                        WHERE simulation_id LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedNetFluxDifferences"
                        SET simulation_id_1='%s'
                        WHERE simulation_id_1 LIKE '%s';
                        UPDATE "data_stage02_isotopomer_fittedNetFluxDifferences"
                        SET simulation_id_2='%s'
                        WHERE simulation_id_2 LIKE '%s';''' 
                          %(simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                            simulation_id_new,simulation_id_old,
                              ))

            data = self.session.execute(query_cmd);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def update_datastage02_isotopomer_analysisID(self,analysis_id_new,analysis_id_old):
        '''Update the analysis ID'''
        try:
            query_cmd = ('''UPDATE "data_stage02_isotopomer_analysis"
                    SET analysis_id='%s'
                    WHERE analysis_id LIKE '%s';
                    UPDATE "data_stage02_isotopomer_fittedNetFluxDifferences"
                    SET analysis_id='%s'
                    WHERE analysis_id LIKE '%s';''' 
                      %(analysis_id_new,analysis_id_old,
                      analysis_id_new,analysis_id_old
                          ))

            data = self.session.execute(query_cmd);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
