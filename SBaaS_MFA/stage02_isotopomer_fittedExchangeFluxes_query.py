#LIMS
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *
#SBaaS
from .stage02_isotopomer_fittedExchangeFluxes_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base

class stage02_isotopomer_fittedExchangeFluxes_query(sbaas_base):
    ## Query from data_stage02_isotopomer_fittedExchangeFluxes
    # query simulation_dateAndTimes from data_stage02_isotopomer_fittedExchangeFluxes   
    def get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I):
        '''Query reaction ids that are used from the fitted fluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).group_by(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime).order_by(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime.asc()).all();
            simulation_dateAndTimes_O = [];
            if data: 
                for d in data:
                    simulation_dateAndTimes_O.append(d.simulation_dateAndTime);
            return simulation_dateAndTimes_O;
        except SQLAlchemyError as e:
            print(e); 
    # query rxn_ids from data_stage02_isotopomer_fittedExchangeFluxes   
    def get_rxnIDs_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I,simulation_dateAndTime_I):
        '''Query reaction ids that are used from the fitted fluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes.rxn_id).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).group_by(
                    data_stage02_isotopomer_fittedExchangeFluxes.rxn_id).order_by(
                    data_stage02_isotopomer_fittedExchangeFluxes.rxn_id.asc()).all();
            rxn_ids_O = [];
            if data: 
                for d in data:
                    rxn_ids_O.append(d.rxn_id);
            return rxn_ids_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_rxnIDs_simulationIDAndSimulationDateAndTimeAndFluxUnits_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I,simulation_dateAndTime_I,flux_units_I):
        '''Query reaction ids that are used from the fitted fluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes.rxn_id).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.flux_exchange_units.like(flux_units_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).group_by(
                    data_stage02_isotopomer_fittedExchangeFluxes.rxn_id).order_by(
                    data_stage02_isotopomer_fittedExchangeFluxes.rxn_id.asc()).all();
            rxn_ids_O = [];
            if data: 
                for d in data:
                    rxn_ids_O.append(d.rxn_id);
            return rxn_ids_O;
        except SQLAlchemyError as e:
            print(e);   
    # query flux_units from data_stage02_isotopomer_fittedExchangeFluxes  
    def get_fluxUnits_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I,simulation_dateAndTime_I):
        '''Query flux_units that are used from data_stage02_isotopomer_fittedExchangeFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes.flux_exchange_units).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).group_by(
                    data_stage02_isotopomer_fittedExchangeFluxes.flux_exchange_units).order_by(
                    data_stage02_isotopomer_fittedExchangeFluxes.flux_exchange_units.asc()).all();
            flux_units_O = [];
            if data: 
                for d in data:
                    flux_units_O.append(d.flux_exchange_units);
            return flux_units_O;
        except SQLAlchemyError as e:
            print(e);  
    # query flux_average, flux_stdev, flux_lb, and flux_ub from data_stage02_isotopomer_fittedExchangeFluxes  
    def get_fluxMinAndMax_simulationID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I):
        '''query the minimum and maximum flux from data_stage02_isotopomer_fittedExchangeFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            fluxList_O=[];
            min_flux_O=None;
            max_flux_O=None;
            if data: 
                for d in data:
                    fluxList_O.append(d.flux_exchange);
                    fluxList_O.append(d.flux_exchange_lb);
                    fluxList_O.append(d.flux_exchange_ub);
                fluxList_O.sort();
                min_flux_O = min(fluxList_O);
                max_flux_O = max(fluxList_O)
            return min_flux_O,max_flux_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_fluxMinAndMax_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I,simulation_dateAndTime_I):
        '''query the minimum and maximum flux from data_stage02_isotopomer_fittedExchangeFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            fluxList_O=[];
            min_flux_O=None;
            max_flux_O=None;
            if data: 
                for d in data:
                    fluxList_O.append(d.flux_exchange);
                    fluxList_O.append(d.flux_exchange_lb);
                    fluxList_O.append(d.flux_exchange_ub);
                fluxList_O.sort();
                min_flux_O = min(fluxList_O);
                max_flux_O = max(fluxList_O)
            return min_flux_O,max_flux_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_flux_simulationIDAndRxnID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I,rxn_id_I):
        '''query flux_average, flux_stdev, flux_lb, and flux_ub from data_stage02_isotopomer_fittedExchangeFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.rxn_id.like(rxn_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=0.0,0.0,0.0,0.0,'';
            if len(data)>1:
                print('more than 1 row found')
                return;
            if data: 
                for d in data:
                    flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O = d.flux_exchange,d.flux_exchange_stdev,d.flux_exchange_lb,d.flux_exchange_ub,d.flux_exchange_units;
            return flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O;
        except SQLAlchemyError as e:
            print(e);    
    def get_flux_simulationIDAndSimulationDateAndTimeAndRxnID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I,simulation_dateAndTime_I,rxn_id_I):
        '''query flux_average, flux_stdev, flux_lb, and flux_ub from data_stage02_isotopomer_fittedExchangeFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedExchangeFluxes.rxn_id.like(rxn_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=0.0,0.0,0.0,0.0,'';
            if len(data)>1:
                print('more than 1 row found')
                return;
            if data: 
                for d in data:
                    flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O = d.flux_exchange,d.flux_exchange_stdev,d.flux_exchange_lb,d.flux_exchange_ub,d.flux_exchange_units;
            return flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_flux_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I,simulation_dateAndTime_I,flux_units_I,rxn_id_I):
        '''query flux_average, flux_stdev, flux_lb, and flux_ub from data_stage02_isotopomer_fittedExchangeFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.flux_exchange_units.like(flux_units_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedExchangeFluxes.rxn_id.like(rxn_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=0.0,0.0,0.0,0.0,'';
            if len(data)>1:
                print('more than 1 row found')
                return;
            if data: 
                for d in data:
                    flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O = d.flux_exchange,d.flux_exchange_stdev,d.flux_exchange_lb,d.flux_exchange_ub,d.flux_exchange_units;
            return flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_fluxes_simulationIDAndSimulationDateAndTimeAndFluxUnits_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I,simulation_dateAndTime_I,flux_units_I):
        '''query flux_average, flux_stdev, flux_lb, and flux_ub from data_stage02_isotopomer_fittedExchangeFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.flux_exchange_units.like(flux_units_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=[],[],[],[],[];
            if data: 
                for d in data:
                    flux_O.append(d.flux_exchange)
                    flux_stdev_O.append(d.flux_exchange_stdev)
                    flux_lb_O.append(d.flux_exchange_lb)
                    flux_ub_O.append(d.flux_exchange_ub)
                    flux_units_O.append(d.flux_exchange_units);
            return flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O;
        except SQLAlchemyError as e:
            print(e);   
    # query rows from data_stage02_isotopomer_fittedExchangeFluxes   
    def get_rows_simulationID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I):
        '''Query rows that are used from the flux_average'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = d.__repr__dict__();
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_rowsDict_simulationID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I):
        '''Query rows that are used from the flux_average'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.rxn_id in rows_O:
                        print('duplicate rxn_id found!');
                    else:
                        rows_O[d.rxn_id]={
                        'flux':d.flux_exchange,
                        'flux_stdev':d.flux_exchange_stdev,
                        'flux_units':d.flux_exchange_units,
                        'flux_lb':d.flux_exchange_lb,
                        'flux_ub':d.flux_exchange_ub};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherFluxLbUb_simulationID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I):
        '''Query rows that are used from the flux_average'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            rows_O = [None,None];
            rows_O[0] = {};
            rows_O[1] = {}
            if data: 
                for d in data:
                    rows_O[0][d.rxn_id]=d.flux_exchange_lb;
                    rows_O[1][d.rxn_id]=d.flux_exchange_ub;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherFlux_simulationID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I):
        '''Query rows that are used from the flux_average
        output: dict, rxn_id:flux'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            rows_O = {}
            if data: 
                for d in data:
                    rows_O[d.rxn_id]=d.flux_exchange;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherFluxList_simulationID_dataStage02IsotopomerfittedExchangeFluxes(self,simulation_id_I):
        '''Query rows that are used from the flux_average
        output: list, [analysis_id,values:{rxn_id:flux}]'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.used_.is_(True)).all();
            rows_O = []
            if data: 
                for d in data:
                    rows_O.append({'simulation_id':d.simulation_id,
                                   'values': {d.rxn_id:d.flux_exchange}
                                   });
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage02_isotopomer_fittedExchangeFluxes(self):
        try:
            data_stage02_isotopomer_fittedExchangeFluxes.__table__.create(self.engine,True);
            data_stage02_isotopomer_fittedExchangeFluxStatistics.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage02_isotopomer_fittedExchangeFluxes(self):
        try:
            data_stage02_isotopomer_fittedExchangeFluxes.__table__.drop(self.engine,True);
            data_stage02_isotopomer_fittedExchangeFluxStatistics.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_isotopomer_fittedExchangeFluxes(self,simulation_id_I = None,simulation_dateAndTime_I=None):
        try:
            if simulation_id_I and simulation_dateAndTime_I:
                reset = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_dateAndTime==self.convert_string2datetime(simulation_dateAndTime_I)).delete(synchronize_session=False);
            elif simulation_id_I:
                reset = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                    data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(data_stage02_isotopomer_fittedExchangeFluxes.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_isotopomer_fittedExchangeFluxStatistics(self,simulation_id_I = None,simulation_dateAndTime_I=None):
        try:
            if simulation_id_I and simulation_dateAndTime_I:
                reset = self.session.query(data_stage02_isotopomer_fittedExchangeFluxStatistics).filter(
                    data_stage02_isotopomer_fittedExchangeFluxStatistics.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxStatistics.simulation_dateAndTime==self.convert_string2datetime(simulation_dateAndTime_I)).delete(synchronize_session=False);
            elif simulation_id_I:
                reset = self.session.query(data_stage02_isotopomer_fittedExchangeFluxStatistics).filter(
                    data_stage02_isotopomer_fittedExchangeFluxStatistics.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_fittedExchangeFluxStatistics).filter(data_stage02_isotopomer_fittedExchangeFluxStatistics.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
            
    #Query data_stage02_isotopomer_fittedExchangeFluxStatistics
    def get_rows_simulationID_dataStage02IsotopomerFittedExchangeFluxStatistics(self,simulation_id_I):
        '''Query rows by simulation_id that are used from the fittedExchangeFluxStatistics'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxStatistics).filter(
                    data_stage02_isotopomer_fittedExchangeFluxStatistics.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxStatistics.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = d.__repr__dict__();
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rows_simulationIDAndFluxUnits_dataStage02IsotopomerFittedExchangeFluxStatistics(self,simulation_id_I,flux_units_I):
        '''Query rows by simulation_id and flux units that are used from the fittedExchangeFluxStatistics'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedExchangeFluxStatistics).filter(
                    data_stage02_isotopomer_fittedExchangeFluxStatistics.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedExchangeFluxStatistics.flux_exchange_units.like(flux_units_I),
                    data_stage02_isotopomer_fittedExchangeFluxStatistics.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = d.__repr__dict__();
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def add_data_stage02_isotopomer_fittedExchangeFluxes(self, data_I):
        '''add rows of data_stage02_isotopomer_fittedExchangeFluxes'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_fittedExchangeFluxes(d['simulation_id'],
                        d['simulation_dateAndTime'],
                        d['rxn_id'],
                        d['flux_exchange'],
                        d['flux_exchange_stdev'],
                        d['flux_exchange_lb'],
                        d['flux_exchange_ub'],
                        d['flux_exchange_units'],
                        d['flux_exchange_normalized'],
                        d['flux_exchange_normalized_stdev'],
                        d['flux_exchange_normalized_lb'],
                        d['flux_exchange_normalized_ub'],
                        d['flux_exchange_normalized_units'],
                        d['used_'],
                        d['comment_'],);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_fittedExchangeFluxes(self,data_I):
        '''update rows of data_stage02_isotopomer_fittedExchangeFluxes'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_fittedExchangeFluxes).filter(
                            data_stage02_isotopomer_fittedExchangeFluxes.id==d['id']
                            ).update(
                            {'simulation_id':d['simulation_id'],
                            'simulation_dateAndTime':d['simulation_dateAndTime'],
                            'rxn_id':d['rxn_id'],
                            'flux_exchange':d['flux_exchange'],
                            'flux_exchange_stdev':d['flux_exchange_stdev'],
                            'flux_exchange_lb':d['flux_exchange_lb'],
                            'flux_exchange_ub':d['flux_exchange_ub'],
                            'flux_exchange_units':d['flux_exchange_units'],
                            'flux_exchange_normalized':d['flux_exchange_normalized'],
                            'flux_exchange_normalized_stdev':d['flux_exchange_normalized_stdev'],
                            'flux_exchange_normalized_lb':d['flux_exchange_normalized_lb'],
                            'flux_exchange_normalized_ub':d['flux_exchange_normalized_ub'],
                            'flux_exchange_normalized_units':d['flux_exchange_normalized_units'],
                            'used_':d['used_'],
                            'comment_':d['comment_'],},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

