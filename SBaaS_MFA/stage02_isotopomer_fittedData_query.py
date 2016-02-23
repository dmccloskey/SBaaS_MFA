#SBaaS
from .stage02_isotopomer_fittedData_postgresql_models import *

from SBaaS_base.sbaas_base import sbaas_base
from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage02_isotopomer_fittedData_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for ...
        '''
        tables_supported = {'data_stage02_isotopomer_fittedFluxes':data_stage02_isotopomer_fittedFluxes,
            'data_stage02_isotopomer_fittedFragments':data_stage02_isotopomer_fittedFragments,
            'data_stage02_isotopomer_fittedData':data_stage02_isotopomer_fittedData,
            'data_stage02_isotopomer_fittedMeasuredFluxes':data_stage02_isotopomer_fittedMeasuredFluxes,
            'data_stage02_isotopomer_fittedMeasuredFragments':data_stage02_isotopomer_fittedMeasuredFragments,
            'data_stage02_isotopomer_fittedMeasuredFluxResiduals':data_stage02_isotopomer_fittedMeasuredFluxResiduals,
            'data_stage02_isotopomer_fittedMeasuredFragmentResiduals':data_stage02_isotopomer_fittedMeasuredFragmentResiduals,
            'data_stage02_isotopomer_fittedFluxStatistics':data_stage02_isotopomer_fittedFluxStatistics,
            'data_stage02_isotopomer_simulationParameters':data_stage02_isotopomer_simulationParameters,
                        };
        self.set_supportedTables(tables_supported);
    ## Query from data_stage02_isotopomer_fittedFluxes
    # query simulation_dateAndTimes from data_stage02_isotopomer_fittedFluxes   
    def get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedFluxes(self,simulation_id_I):
        '''Query reaction ids that are used from the fitted fluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes.simulation_dateAndTime).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).group_by(
                    data_stage02_isotopomer_fittedFluxes.simulation_dateAndTime).order_by(
                    data_stage02_isotopomer_fittedFluxes.simulation_dateAndTime.asc()).all();
            simulation_dateAndTimes_O = [];
            if data: 
                for d in data:
                    simulation_dateAndTimes_O.append(d.simulation_dateAndTime);
            return simulation_dateAndTimes_O;
        except SQLAlchemyError as e:
            print(e); 
    # query rxn_ids from data_stage02_isotopomer_fittedFluxes   
    def get_rxnIDs_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedFluxes(self,simulation_id_I,simulation_dateAndTime_I):
        '''Query reaction ids that are used from the fitted fluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes.rxn_id).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).group_by(
                    data_stage02_isotopomer_fittedFluxes.rxn_id).order_by(
                    data_stage02_isotopomer_fittedFluxes.rxn_id.asc()).all();
            rxn_ids_O = [];
            if data: 
                for d in data:
                    rxn_ids_O.append(d.rxn_id);
            return rxn_ids_O;
        except SQLAlchemyError as e:
            print(e);   
    # query flux_average, flux_stdev, flux_lb, and flux_ub from data_stage02_isotopomer_fittedFluxes   
    def get_flux_simulationIDAndRxnID_dataStage02IsotopomerfittedFluxes(self,simulation_id_I,rxn_id_I):
        '''query flux_average, flux_stdev, flux_lb, and flux_ub from data_stage02_isotopomer_fittedFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.rxn_id.like(rxn_id_I),
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).all();
            flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=0.0,0.0,0.0,0.0,'';
            if len(data)>1:
                print('more than 1 row found')
                return;
            if data: 
                for d in data:
                    flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O = d.flux,d.flux_stdev,d.flux_lb,d.flux_ub,d.flux_units;
            return flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O;
        except SQLAlchemyError as e:
            print(e);    
    def get_flux_simulationIDAndSimulationDateAndTimeAndRxnID_dataStage02IsotopomerfittedFluxes(self,simulation_id_I,simulation_dateAndTime_I,rxn_id_I):
        '''query flux_average, flux_stdev, flux_lb, and flux_ub from data_stage02_isotopomer_fittedFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedFluxes.rxn_id.like(rxn_id_I),
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).all();
            flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=0.0,0.0,0.0,0.0,'';
            if len(data)>1:
                print('more than 1 row found')
                return;
            if data: 
                for d in data:
                    flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O = d.flux,d.flux_stdev,d.flux_lb,d.flux_ub,d.flux_units;
            return flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_fluxes_simulationIDAndSimulationDateAndTimeAndFluxUnits_dataStage02IsotopomerfittedFluxes(self,simulation_id_I,simulation_dateAndTime_I,flux_units_I):
        '''query flux_average, flux_stdev, flux_lb, and flux_ub from data_stage02_isotopomer_fittedNetFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.flux_units.like(flux_units_I),
                    data_stage02_isotopomer_fittedFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).all();
            flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=[],[],[],[],[];
            if data: 
                for d in data:
                    flux_O.append(d.flux)
                    flux_stdev_O.append(d.flux_stdev)
                    flux_lb_O.append(d.flux_lb)
                    flux_ub_O.append(d.flux_ub)
                    flux_units_O.append(d.flux_units);
            return flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O;
        except SQLAlchemyError as e:
            print(e);   
    # query fluxes from data_stage02_isotopomer_fittedFluxes
    def get_fluxMinAndMax_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedFluxes(self,simulation_id_I,simulation_dateAndTime_I):
        '''query the minimum and maximum flux from data_stage02_isotopomer_fittedFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.simulation_dateAndTime==simulation_dateAndTime_I,
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).all();
            fluxList_O=[];
            min_flux_O=None;
            max_flux_O=None;
            if data: 
                for d in data:
                    fluxList_O.append(d.flux);
                    fluxList_O.append(d.flux_lb);
                    fluxList_O.append(d.flux_ub);
                fluxList_O.sort();
                min_flux_O = min(fluxList_O);
                max_flux_O = max(fluxList_O)
            return min_flux_O,max_flux_O;
        except SQLAlchemyError as e:
            print(e);   
    # query rows from data_stage02_isotopomer_fittedFluxes   
    def get_rows_simulationID_dataStage02IsotopomerfittedFluxes(self,simulation_id_I):
        '''Query rows by simulation id and flux units that are used from data_stage02_isotopomer_fittedFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = d.__repr__dict__();
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);   
    def get_rows_simulationIDAndFluxUnits_dataStage02IsotopomerfittedFluxes(self,simulation_id_I,flux_units_I):
        '''Query rows by simulation id and flux units that are used from data_stage02_isotopomer_fittedFluxes'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.flux_units.like(flux_units_I),
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = d.__repr__dict__();
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);     
    def get_rowsDict_simulationID_dataStage02IsotopomerfittedFluxes(self,simulation_id_I):
        '''Query rows that are used from the flux_average'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).all();
            rows_O = {};
            if data: 
                for d in data:
                    if d.rxn_id in rows_O:
                        print('duplicate rxn_id found!');
                    else:
                        rows_O[d.rxn_id]={
                        'flux':d.flux,
                        'flux_stdev':d.flux_stdev,
                        'flux_units':d.flux_units,
                        'flux_lb':d.flux_lb,
                        'flux_ub':d.flux_ub};
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherFluxLbUb_simulationID_dataStage02IsotopomerfittedFluxes(self,simulation_id_I):
        '''Query rows that are used from the flux_average'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).all();
            rows_O = [None,None];
            rows_O[0] = {};
            rows_O[1] = {}
            if data: 
                for d in data:
                    rows_O[0][d.rxn_id]=d.flux_lb;
                    rows_O[1][d.rxn_id]=d.flux_ub;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def get_rowsEscherFlux_simulationID_dataStage02IsotopomerfittedFluxes(self,simulation_id_I):
        '''Query rows that are used from the flux_average'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                    data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxes.used_.is_(True)).all();
            rows_O = {}
            if data: 
                for d in data:
                    rows_O[d.rxn_id]=d.flux;
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
    def add_data_stage02_isotopomer_fittedFluxes(self, data_I):
        '''add rows of data_stage02_isotopomer_fittedFluxes'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_fittedFluxes(d['simulation_id'],
                    d['simulation_dateAndTime'],
                    #d['experiment_id'],
                    #d['model_id'],
                    #d['mapping_id'],
                    #d['sample_name_abbreviation'],
                    #d['time_point'],
                    d['rxn_id'],
                    d['flux'],
                    d['flux_stdev'],
                    d['flux_lb'],
                    d['flux_ub'],
                    d['flux_units'],
                    d['fit_alf'],
                    d['fit_chi2s'],
                    d['fit_cor'],
                    d['fit_cov'],
                    d['free'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_fittedFragments(self, data_I):
        '''add rows of data_stage02_isotopomer_fittedFragments'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_fittedFragments(d['simulation_id'],
                            d['simulation_dateAndTime'],
                            d['experiment_id'],
                            #d['model_id'],
                            #d['mapping_id'],
                            d['sample_name_abbreviation'],
                            d['time_point'],
                            d['fragment_id'],
                            #d['fragment_formula'],
                            d['fragment_mass'],
                            d['fit_val'],
                            d['fit_stdev'],
                            d['fit_units'],
                            d['fit_alf'],
                            d['fit_cor'],
                            d['fit_cov'],
                            d['free'],
                            d['used_'],
                            d['comment_']
                            );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_fittedData(self, data_I):
        '''add rows of data_stage02_isotopomer_fittedData'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_fittedData(d['simulation_id'],
                    d['simulation_dateAndTime'], 
                    d['Original Filename'],
                    #d['experiment_id'], 
                    #d['model_id'],
                    #d['mapping_id'],
                    #d['sample_name_abbreviation'],
                    #d['time_point'],
                    d['fitted_echi2'],
                    d['fitted_alf'],
                    d['fitted_chi2'],
                    d['fitted_dof'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_fittedMeasuredFluxes(self, data_I):
        '''add rows of data_stage02_isotopomer_fittedMeasuredFluxes'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_fittedMeasuredFluxes(d['simulation_id'],
                    d['simulation_dateAndTime'],
                    d['experiment_id'],
                    #d['model_id'],
                    #d['mapping_id'],
                    d['sample_name_abbreviation'],
                    #d['time_point'],
                    d['rxn_id'],
                    d['fitted_sres'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_fittedMeasuredFragments(self, data_I):
        '''add rows of data_stage02_isotopomer_fittedMeasuredFragments'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_fittedMeasuredFragments(d['simulation_id'],
                    d['simulation_dateAndTime'],
                    d['experiment_id'],
                    #d['model_id'],
                    #d['mapping_id'],
                    d['sample_name_abbreviation'],
                    #d['time_point'],
                    #d['met_id'],
                    d['fragment_id'],
                    #d['fragment_formula'],
                    d['fitted_sres'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_fittedMeasuredFluxResiduals(self, data_I):
        '''add rows of data_stage02_isotopomer_fittedMeasuredFluxResiduals'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_fittedMeasuredFluxResiduals(d['simulation_id'],
                    d['simulation_dateAndTime'],
                    d['experiment_id'],
                    #d['model_id'],
                    #d['mapping_id'],
                    d['sample_name_abbreviation'],
                    d['time_point'],
                    d['rxn_id'],
                    d['res_data'],
                    d['res_esens'],
                    d['res_fit'],
                    d['res_msens'],
                    d['res_peak'],
                    d['res_stdev'],
                    d['res_val'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_data_stage02_isotopomer_fittedMeasuredFragmentResiduals(self, data_I):
        '''add rows of data_stage02_isotopomer_fittedMeasuredFragmentResiduals'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_fittedMeasuredFragmentResiduals(d['simulation_id'],
                    d['simulation_dateAndTime'],
                    d['experiment_id'],
                    #d['model_id'],
                    #d['mapping_id'],
                    d['sample_name_abbreviation'],
                    d['time_point'],
                    d['fragment_id'],
                    #d['fragment_formula'],
                    d['fragment_mass'],
                    d['res_data'],
                    d['res_esens'],
                    d['res_fit'],
                    d['res_msens'],
                    d['res_peak'],
                    d['res_stdev'],
                    d['res_val'],
                    d['used_'],
                    d['comment_']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_fittedFluxes(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_fittedFluxes'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(
                            #data_stage02_isotopomer_fittedFluxes.sample_name.like(d['sample_name'])
                            ).update(
                            {'simulation_id':d['simulation_id'],
                            'simulation_dateAndTime':d['simulation_dateAndTime'],
                            #'experiment_id':d['experiment_id'],
                            #'model_id':d['model_id'],
                            #'mapping_id':d['mapping_id'],
                            #'sample_name_abbreviation':d['sample_name_abbreviation'],
                            #'time_point':d['time_point'],
                            'rxn_id':d['rxn_id'],
                            'flux':d['flux'],
                            'flux_stdev':d['flux_stdev'],
                            'flux_lb':d['flux_lb'],
                            'flux_ub':d['flux_ub'],
                            'flux_units':d['flux_units'],
                            'fit_alf':d['fit_alf'],
                            'fit_chi2s':d['fit_chi2s'],
                            'fit_cor':d['fit_cor'],
                            'fit_cov':d['fit_cov'],
                            'free':d['free'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_fittedFragments(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_fittedFragments'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_fittedFragments).filter(
                            #data_stage02_isotopomer_fittedFragments.sample_name.like(d['sample_name'])
                            ).update(
                            {'simulation_id':d['simulation_id'],
                            'simulation_dateAndTime':d['simulation_dateAndTime'],
                            'experiment_id':d['experiment_id'],
                            #'model_id':d['model_id'],
                            #'mapping_id':d['mapping_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'fragment_id':d['fragment_id'],
                            #'fragment_formula':d['fragment_formula'],
                            'fragment_mass':d['fragment_mass'],
                            'fit_val':d['fit_val'],
                            'fit_stdev':d['fit_stdev'],
                            'fit_units':d['fit_units'],
                            'fit_alf':d['fit_alf'],
                            'fit_chi2s':d['fit_chi2s'],
                            'fit_cor':d['fit_cor'],
                            'fit_cov':d['fit_cov'],
                            'free':d['free'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_fittedData(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_fittedData'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_fittedData).filter(
                            #data_stage02_isotopomer_fittedData.sample_name.like(d['sample_name'])
                            ).update(
                            {'simulation_id':d['simulation_id'],
                            'simulation_dateAndTime':d['simulation_dateAndTime'],
                            'original_filename':d['Original Filename'],
                            #'experiment_id':d['experiment_id'],
                            #'model_id':d['model_id'],
                            #'mapping_id':d['mapping_id'],
                            #'sample_name_abbreviation':d['sample_name_abbreviation'],
                            #'time_point':d['time_point'],
                            'fitted_echi2':d['fitted_echi2'],
                            'fitted_alf':d['fitted_alf'],
                            'fitted_chi2':d['fitted_chi2'],
                            'fitted_dof':d['fitted_dof'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_fittedMeasuredFluxes(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_fittedMeasuredFluxes'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_fittedMeasuredFluxes).filter(
                            #data_stage02_isotopomer_fittedMeasuredFluxes.sample_name.like(d['sample_name'])
                            ).update(
                            {'simulation_id':d['simulation_id'],
                            'simulation_dateAndTime':d['simulation_dateAndTime'],
                            'experiment_id':d['experiment_id'],
                            #'model_id':d['model_id'],
                            #'mapping_id':d['mapping_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            #'time_point':d['time_point'],
                            'rxn_id':d['rxn_id'],
                            'fitted_sres':d['fitted_sres'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_fittedMeasuredFragments(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_fittedMeasuredFragments'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_fittedMeasuredFragments).filter(
                            #data_stage02_isotopomer_fittedMeasuredFragments.sample_name.like(d['sample_name'])
                            ).update(
                            {'simulation_id':d['simulation_id'],
                            'simulation_dateAndTime':d['simulation_dateAndTime'],
                            'experiment_id':d['experiment_id'],
                            #'model_id':d['model_id'],
                            #'mapping_id':d['mapping_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            #'time_point':d['time_point'],
                            #'met_id':d['met_id'],
                            'fragment_id':d['fragment_id'],
                            #'fragment_formula':d['fragment_formula'],
                            'fitted_sres':d['fitted_sres'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_fittedMeasuredFluxResiduals(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_fittedMeasuredFluxResiduals'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_fittedMeasuredFluxResiduals).filter(
                            #data_stage02_isotopomer_fittedMeasuredFluxResiduals.sample_name.like(d['sample_name'])
                            ).update(
                            {'simulation_id':d['simulation_id'],
                            'simulation_dateAndTime':d['simulation_dateAndTime'],
                            'experiment_id':d['experiment_id'],
                            #'model_id':d['model_id'],
                            #'mapping_id':d['mapping_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'rxn_id':d['rxn_id'],
                            'res_data':d['res_data'],
                            'res_esens':d['res_esens'],
                            'res_fit':d['res_fit'],
                            'res_msens':d['res_msens'],
                            'res_peak':d['res_peak'],
                            'res_stdev':d['res_stdev'],
                            'res_val':d['res_val'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_fittedMeasuredFragmentResiduals(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_fittedMeasuredFragmentResiduals'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_fittedMeasuredFragmentResiduals).filter(
                            #data_stage02_isotopomer_fittedMeasuredFragmentResiduals.sample_name.like(d['sample_name'])
                            ).update(
                            {'simulation_id':d['simulation_id'],
                            'simulation_dateAndTime':d['simulation_dateAndTime'],
                            'experiment_id':d['experiment_id'],
                            #'model_id':d['model_id'],
                            #'mapping_id':d['mapping_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'fragment_id':d['fragment_id'],
                            #'fragment_formula':d['fragment_formula'],
                            'fragment_mass':d['fragment_mass'],
                            'res_data':d['res_data'],
                            'res_esens':d['res_esens'],
                            'res_fit':d['res_fit'],
                            'res_msens':d['res_msens'],
                            'res_peak':d['res_peak'],
                            'res_stdev':d['res_stdev'],
                            'res_val':d['res_val'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def initialize_dataStage02_isotopomer_fittedData(self):
        try:
            data_stage02_isotopomer_fittedFluxes.__table__.create(self.engine,True);
            data_stage02_isotopomer_fittedFragments.__table__.create(self.engine,True);
            data_stage02_isotopomer_fittedData.__table__.create(self.engine,True);
            data_stage02_isotopomer_fittedMeasuredFluxes.__table__.create(self.engine,True);
            data_stage02_isotopomer_fittedMeasuredFragments.__table__.create(self.engine,True);
            data_stage02_isotopomer_fittedMeasuredFluxResiduals.__table__.create(self.engine,True);
            data_stage02_isotopomer_fittedMeasuredFragmentResiduals.__table__.create(self.engine,True);
            data_stage02_isotopomer_fittedFluxStatistics.__table__.create(self.engine,True);
            data_stage02_isotopomer_simulationParameters.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage02_isotopomer_fittedData(self):
        try:
            data_stage02_isotopomer_fittedFluxes.__table__.drop(self.engine,True);
            data_stage02_isotopomer_fittedFragments.__table__.drop(self.engine,True);
            data_stage02_isotopomer_fittedData.__table__.drop(self.engine,True);
            data_stage02_isotopomer_fittedMeasuredFluxes.__table__.drop(self.engine,True);
            data_stage02_isotopomer_fittedMeasuredFragments.__table__.drop(self.engine,True);
            data_stage02_isotopomer_fittedMeasuredFluxResiduals.__table__.drop(self.engine,True);
            data_stage02_isotopomer_fittedMeasuredFragmentResiduals.__table__.drop(self.engine,True);
            data_stage02_isotopomer_fittedFluxStatistics.__table__.drop(self.engine,True);
            data_stage02_isotopomer_simulationParameters.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage02_isotopomer_fittedData(self,simulation_id_I = None):
        try:
            if simulation_id_I:
                reset = self.session.query(data_stage02_isotopomer_fittedFluxes).filter(data_stage02_isotopomer_fittedFluxes.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedFragments).filter(data_stage02_isotopomer_fittedFragments.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedData).filter(data_stage02_isotopomer_fittedData.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedMeasuredFluxes).filter(data_stage02_isotopomer_fittedMeasuredFluxes.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedMeasuredFragments).filter(data_stage02_isotopomer_fittedMeasuredFragments.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedMeasuredFluxResiduals).filter(data_stage02_isotopomer_fittedMeasuredFluxResiduals.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedMeasuredFragmentResiduals).filter(data_stage02_isotopomer_fittedMeasuredFragmentResiduals.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_simulationParameters).filter(data_stage02_isotopomer_simulationParameters.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedFluxStatistics).filter(data_stage02_isotopomer_fittedFluxStatistics.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_fittedFluxes).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedFragments).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedData).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedMeasuredFluxes).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedMeasuredFragments).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedMeasuredFluxResiduals).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedMeasuredFragmentResiduals).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_simulationParameters).delete(synchronize_session=False);
                reset = self.session.query(data_stage02_isotopomer_fittedFluxStatistics).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def add_data_stage02_isotopomer_simulationParameters(self, data_I):
        '''add rows of data_stage02_isotopomer_simulationParameters'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage02_isotopomer_simulationParameters(d['simulation_id'],
                    d['simulation_dateAndTime'],
                    d['cont_alpha'],
                    d['cont_reltol'],
                    d['cont_steps'],
                    d['fit_nudge'],
                    d['fit_reinit'],
                    d['fit_reltol'],
                    d['fit_starts'],
                    d['fit_tau'],
                    d['hpc_mcr'],
                    d['hpc_on'],
                    d['hpc_serve'],
                    d['int_maxstep'],
                    d['int_reltol'],
                    d['int_senstol'],
                    d['int_timeout'],
                    d['int_tspan'],
                    d['ms_correct'],
                    d['oed_crit'],
                    d['oed_reinit'],
                    d['oed_tolf'],
                    d['oed_tolx'],
                    d['sim_more'],
                    d['sim_na'],
                    d['sim_sens'],
                    d['sim_ss'],
                    d['sim_tunit']);
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_data_stage02_isotopomer_simulationParameters(self,data_I):
        #TODO:
        '''update rows of data_stage02_isotopomer_simulationParameters'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage02_isotopomer_simulationParameters).filter(
                            #data_stage02_isotopomer_simulationParameters.sample_name.like(d['sample_name'])
                            ).update(
                            {'simulation_id':d['simulation_id'],
                            'simulation_dateAndTime':d['simulation_dateAndTime'],
                            'cont_alpha':d['cont_alpha'],
                            'cont_reltol':d['cont_reltol'],
                            'cont_steps':d['cont_steps'],
                            'fit_nudge':d['fit_nudge'],
                            'fit_reinit':d['fit_reinit'],
                            'fit_reltol':d['fit_reltol'],
                            'fit_starts':d['fit_starts'],
                            'fit_tau':d['fit_tau'],
                            'hpc_mcr':d['hpc_mcr'],
                            'hpc_on':d['hpc_on'],
                            'hpc_serve':d['hpc_serve'],
                            'int_maxstep':d['int_maxstep'],
                            'int_reltol':d['int_reltol'],
                            'int_senstol':d['int_senstol'],
                            'int_timeout':d['int_timeout'],
                            'int_tspan':d['int_tspan'],
                            'ms_correct':d['ms_correct'],
                            'oed_crit':d['oed_crit'],
                            'oed_reinit':d['oed_reinit'],
                            'oed_tolf':d['oed_tolf'],
                            'oed_tolx':d['oed_tolx'],
                            'sim_more':d['sim_more'],
                            'sim_na':d['sim_na'],
                            'sim_sens':d['sim_sens'],
                            'sim_ss':d['sim_ss'],
                            'sim_tunit':d['sim_tunit']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def reset_datastage02_isotopomer_fittedFluxStatistics(self,simulation_id_I = None,simulation_dateAndTime_I=None):
        try:
            if simulation_id_I and simulation_dateAndTime_I:
                reset = self.session.query(data_stage02_isotopomer_fittedFluxStatistics).filter(
                    data_stage02_isotopomer_fittedFluxStatistics.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxStatistics.simulation_dateAndTime==self.convert_string2datetime(simulation_dateAndTime_I)).delete(synchronize_session=False);
            elif simulation_id_I:
                reset = self.session.query(data_stage02_isotopomer_fittedFluxStatistics).filter(
                    data_stage02_isotopomer_fittedFluxStatistics.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage02_isotopomer_fittedFluxStatistics).filter(data_stage02_isotopomer_fittedFluxStatistics.simulation_id.like(simulation_id_I)).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);

    #Query data_stage02_isotopomer_fittedFluxStatistics
    def get_rows_simulationID_dataStage02IsotopomerFittedFluxStatistics(self,simulation_id_I):
        '''Query rows by simulation_id that are used from the fittedFluxStatistics'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxStatistics).filter(
                    data_stage02_isotopomer_fittedFluxStatistics.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxStatistics.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = d.__repr__dict__();
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e); 
    def get_rows_simulationIDAndFluxUnits_dataStage02IsotopomerFittedFluxStatistics(self,simulation_id_I,flux_units_I):
        '''Query rows by simulation_id and flux units that are used from the fittedFluxStatistics'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedFluxStatistics).filter(
                    data_stage02_isotopomer_fittedFluxStatistics.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedFluxStatistics.flux_units.like(flux_units_I),
                    data_stage02_isotopomer_fittedFluxStatistics.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = d.__repr__dict__();
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    #Query data_stage02_isotopomer_fittedMeasuredFragments
    def get_rows_simulationID_dataStage02IsotopomerFittedMeasuredFragments(self,simulation_id_I):
        '''Query rows by simulation_id that are used from the fittedMeasuredFragments'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedMeasuredFragments).filter(
                    data_stage02_isotopomer_fittedMeasuredFragments.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedMeasuredFragments.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = d.__repr__dict__();
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);

    #Query data_stage02_isotopomer_fittedData
    def get_rows_simulationID_dataStage02IsotopomerFittedData(self,simulation_id_I):
        '''Query rows by simulation_id that are used from the fittedData'''
        try:
            data = self.session.query(data_stage02_isotopomer_fittedData).filter(
                    data_stage02_isotopomer_fittedData.simulation_id.like(simulation_id_I),
                    data_stage02_isotopomer_fittedData.used_.is_(True)).all();
            rows_O = [];
            if data: 
                for d in data:
                    data_tmp = d.__repr__dict__();
                    rows_O.append(data_tmp);
            return rows_O;
        except SQLAlchemyError as e:
            print(e);
