#SBaaS
from .stage02_isotopomer_fittedFluxSplits_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage02_isotopomer_fittedFluxSplits_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for ...
        '''
        tables_supported = {'data_stage02_isotopomer_fittedFluxSplits':data_stage02_isotopomer_fittedFluxSplits,
                        };
        self.set_supportedTables(tables_supported); 
    ## Query from data_stage02_isotopomer_fittedFluxSplits
    # query simulation_dateAndTimes from data_stage02_isotopomer_fittedFluxSplits   
    def get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I):
        '''Query split ids that are used from the fitted splites'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits.simulation_dateAndTime).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).group_by(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_dateAndTime).order_by(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_dateAndTime.asc()).all();
            simulation_dateAndTimes_O = [];
            if data: 
                for d in data:
                    simulation_dateAndTimes_O.append(d.simulation_dateAndTime);
            return simulation_dateAndTimes_O;
        except SQLAlchemyError as e:
            print(e); 
    # query split_ids from data_stage02_isotopomer_fittedFluxSplits   
    def get_splitIDs_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I,simulation_dateAndTime_I):
        '''Query split ids that are used from the fitted splites'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits.split_id).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).group_by(
                    data_stage02_isotopomer_fittedFluxSplits.split_id).order_by(
                    data_stage02_isotopomer_fittedFluxSplits.split_id.asc()).all();
            split_ids_O = [];
            if data: 
                for d in data:
                    split_ids_O.append(d.split_id);
            return split_ids_O;
        except SQLAlchemyError as e:
            print(e);   
    # query split_units from data_stage02_isotopomer_fittedFluxSplits  
    def get_splitUnits_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I,simulation_dateAndTime_I):
        '''Query split_units that are used from data_stage02_isotopomer_fittedFluxSplits'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits.split_units).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).group_by(
                    data_stage02_isotopomer_fittedFluxSplits.split_units).order_by(
                    data_stage02_isotopomer_fittedFluxSplits.split_units.asc()).all();
            split_units_O = [];
            if data: 
                for d in data:
                    split_units_O.append(d.split_units);
            return split_units_O;
        except SQLAlchemyError as e:
            print(e);  
    # query split_average, split_stdev, split_lb, and split_ub from data_stage02_isotopomer_fittedFluxSplits   
    def get_split_simulationIDAndSplitID_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I,split_id_I):
        '''query split_average, split_stdev, split_lb, and split_ub from data_stage02_isotopomer_fittedFluxSplits'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.split_id.like(split_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).order_by(
                    data_stage02_isotopomer_fittedFluxSplits.split_rxn_id.asc()).all();
            split_rxn_id_O,split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O=[],[],[],[],[],[];
            if data: 
                for d in data:
                    split_rxn_id_O.append(d.split_rxn_id);
                    split_O.append(d.split);
                    split_stdev_O.append(d.split_stdev);
                    split_lb_O.append(d.split_lb);
                    split_ub_O.append(d.split_ub);
                    split_units_O.append(d.split_units);
            return split_rxn_id_O,split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O;
        except SQLAlchemyError as e:
            print(e);    
    def get_split_simulationIDAndSimulationDateAndTimeAndSplitID_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I,simulation_dateAndTime_I,split_id_I):
        '''query split_average, split_stdev, split_lb, and split_ub from data_stage02_isotopomer_fittedFluxSplits'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedFluxSplits.split_id.like(split_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).order_by(
                    data_stage02_isotopomer_fittedFluxSplits.split_rxn_id.asc()).all();
            split_rxn_id_O,split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O=[],[],[],[],[],[];
            if data: 
                for d in data:
                    split_rxn_id_O.append(d.split_rxn_id);
                    split_O.append(d.split);
                    split_stdev_O.append(d.split_stdev);
                    split_lb_O.append(d.split_lb);
                    split_ub_O.append(d.split_ub);
                    split_units_O.append(d.split_units);
            return split_rxn_id_O,split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_split_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndSplitID_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I,simulation_dateAndTime_I,split_units_I,split_id_I):
        '''query split_average, split_stdev, split_lb, and split_ub from data_stage02_isotopomer_fittedFluxSplits'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.split_units.like(split_units_I),
                    data_stage02_isotopomer_fittedFluxSplits.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedFluxSplits.split_id.like(split_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).order_by(
                    data_stage02_isotopomer_fittedFluxSplits.split_rxn_id.asc()).all();
            split_rxn_id_O,split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O=[],[],[],[],[],[];
            if data: 
                for d in data:
                    split_rxn_id_O.append(d.split_rxn_id);
                    split_O.append(d.split);
                    split_stdev_O.append(d.split_stdev);
                    split_lb_O.append(d.split_lb);
                    split_ub_O.append(d.split_ub);
                    split_units_O.append(d.split_units);
            return split_rxn_id_O,split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O;
        except SQLAlchemyError as e:
            print(e);     
    def get_split_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndSplitIDAndSplitRxnId_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I,simulation_dateAndTime_I,split_units_I,split_id_I,split_rxn_id_I):
        '''query split_average, split_stdev, split_lb, and split_ub from data_stage02_isotopomer_fittedFluxSplits'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.split_units.like(split_units_I),
                    data_stage02_isotopomer_fittedFluxSplits.split_rxn_id.like(split_rxn_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedFluxSplits.split_id.like(split_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).all();
            split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O=0.0,0.0,0.0,0.0,'';
            if len(data)>1:
                print('more than 1 row found')
                return;
            if data: 
                for d in data:
                    split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O = d.split,d.split_stdev,d.split_lb,d.split_ub,d.split_units;
            return split_O,split_stdev_O,split_lb_O,split_ub_O,split_units_O;
        except SQLAlchemyError as e:
            print(e);   
    # query rows from data_stage02_isotopomer_fittedFluxSplits   
    def get_rows_simulationID_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I):
        '''Query rows that are used from the split_average'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = {'id':d.id,
                        'simulation_id':d.simulation_id,
                        'simulation_dateAndTime':d.simulation_dateAndTime,
                        'split_id':d.split_id,
                        'split_rxn_id':d.split_rxn_id,
                        'split':d.split,
                        'split_stdev':d.split_stdev,
                        'split_units':d.split_units,
                        'split_lb':d.split_lb,
                        'split_ub':d.split_ub,
                        'used_':d.used_,
                        'comment_':d.comment_};
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_rowsDict_simulationID_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I):
        '''Query rows that are used from the split_average'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.split_id in rows_O:
                        print('duplicate split_id found!');
                    else:
                        rows_O[d.split_id]={
                        'split':d.split,
                        'split_stdev':d.split_stdev,
                        'split_units':d.split_units,
                        'split_lb':d.split_lb,
                        'split_ub':d.split_ub};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherFluxLbUb_simulationID_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I):
        '''Query rows that are used from the split_average'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).all();
            rows_O = [None,None];
            rows_O[0] = {};
            rows_O[1] = {}
            if data: 
                for d in data:
                    rows_O[0][d.split_id]=d.split_lb;
                    rows_O[1][d.split_id]=d.split_ub;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherFlux_simulationID_dataStage02IsotopomerfittedFluxSplits(self,simulation_id_I):
        '''Query rows that are used from the split_average
        output: dict, split_id:split'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.used_.is_(True)).all();
            rows_O = {}
            if data: 
                for d in data:
                    rows_O[d.split_id]=d.split;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage02_isotopomer_fittedFluxSplits(self):
        try:
            data_stage02_isotopomer_fittedFluxSplits.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage02_isotopomer_fittedFluxSplits(self):
        try:
            data_stage02_isotopomer_fittedFluxSplits.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_isotopomer_fittedFluxSplits(self,simulation_id_I = None,simulation_dateAndTime_I=None):
        try:
            if simulation_id_I and simulation_dateAndTime_I:
                reset = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(
                    data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxSplits.simulation_dateAndTime==self.convert_string2datetime(simulation_dateAndTime_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_fittedFluxSplits).filter(data_stage02_isotopomer_fittedFluxSplits.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);

