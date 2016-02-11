#SBaaS
from .stage02_isotopomer_fittedNetFluxDifferences_io import stage02_isotopomer_fittedNetFluxDifferences_io
from .stage02_isotopomer_fittedNetFluxes_query import stage02_isotopomer_fittedNetFluxes_query
#Resources
from genomeScale_MFA.MFA_methods import MFA_methods

class stage02_isotopomer_fittedNetFluxDifferences_execute(stage02_isotopomer_fittedNetFluxDifferences_io,
                                                          stage02_isotopomer_fittedNetFluxes_query):
    def execute_findNetFluxSignificantDifferences(self,analysis_id_I, criteria_I = 'flux_lb/flux_ub',
                                               simulation_ids_I=[],simulation_dateAndTimes_I = [],
                                               rxn_ids_I = [],flux_units_I = [],
                                               control_simulation_id_I=None, 
                                               control_simulation_dateAndTime_I=None,
                                               redundancy_I=False,
                                               observable_only_I=False):
        """Find fluxes that are significantly different
        Input:
        analysis_id_I = string,
        criteria_I = string, flux_lb/flux_ub: use flux_lb and flux_ub to determine significance (default)
                             flux_mean/flux_stdev: use the flux_mean and flux_stdev to determine significance
        control_simulation_id_I = string, simulation_id to compare all other simulation_ids to
        simulation_dateAndTime_I =  string, simulation_dateAndTime to compare all other simulation_ids to
        redundancy_I =  boolean, if true, all values with be compared, if false (default), only unique comparisons will be made
        observable_only_I =  boolean, if true, only observable fluxes will be compared, if false (default), observable and unobservable fluxes will be compared
        """
        mfamethods = MFA_methods();
        data_O = [];
        print('executing findNetFluxSignificantDifferences...')
        # get the simulation_id and simulation_id dateAndTimes
        if simulation_ids_I and simulation_dateAndTimes_I:
            simulation_ids = simulation_ids_I;
            simulation_dateAndTimes = simulation_dateAndTimes_I;
        else:
            simulation_ids = [];
            simulation_ids_unique = [];
            simulation_dateAndTimes = [];
            # get the simulation unique ids
            simulation_ids_unique = self.get_simulationID_analysisID_dataStage02IsotopomerAnalysis(analysis_id_I);
            for simulation_id in simulation_ids_unique:
                # get the simulation dateAndTimes
                simulation_dateAndTimes_tmp = []
                simulation_dateAndTimes_tmp = self.get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedNetFluxes(simulation_id);
                simulation_ids_tmp = [simulation_id for x in simulation_dateAndTimes_tmp];
                simulation_dateAndTimes.extend(simulation_dateAndTimes_tmp)
                simulation_ids.extend(simulation_ids_tmp)
            if control_simulation_id_I and control_simulation_dateAndTime_I:
                index = simulation_ids.index(control_simulation_id_I);
                value = simulation_ids.pop(index);
                simulation_ids.insert(0, value);
                control_simulation_dateAndTime_I = self.convert_string2datetime(control_simulation_dateAndTime_I);
                index = simulation_dateAndTimes.index(control_simulation_dateAndTime_I);
                value = simulation_dateAndTimes.pop(index)
                simulation_dateAndTimes.insert(0, value);
        for simulation_cnt_1, simulation_id_1 in enumerate(simulation_ids):
            print("calculating netFluxDifferences for simulation_id " + simulation_id_1);
            # check for control
            if control_simulation_id_I and control_simulation_dateAndTime_I and simulation_cnt_1>0:
                break;
            #prevents redundancy and 
            if simulation_cnt_1+1 >= len(simulation_ids):
                break;
            # get the units
            if flux_units_I:
                flux_units = flux_units_I;
            else:
                flux_units = self.get_fluxUnits_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedNetFluxes(simulation_id_1,simulation_dateAndTimes[simulation_cnt_1])
            for flux_unit in flux_units:    
                print("calculating netFluxDifferences for flux_units " + flux_unit);
                # get the rxn_ids
                if rxn_ids_I:
                    rxn_ids = rxn_ids_I;
                else:
                    rxn_ids = [];
                    rxn_ids = self.get_rxnIDs_simulationIDAndSimulationDateAndTimeAndFluxUnits_dataStage02IsotopomerfittedNetFluxes(simulation_id_1,simulation_dateAndTimes[simulation_cnt_1],flux_unit);
                for rxn_id in rxn_ids:
                    print("calculating netFluxDifferes for rxn_id " + rxn_id);
                    # get simulation_id_1 flux data
                    flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1=None,None,None,None,None;
                    flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1=self.get_flux_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedNetFluxes(simulation_id_1,simulation_dateAndTimes[simulation_cnt_1],flux_unit,rxn_id);
                    if not mfamethods.check_criteria(flux_1,flux_stdev_1,flux_lb_1,flux_ub_1, criteria_I):
                        continue;
                    if redundancy_I: list_2 = simulation_ids;
                    else: list_2 = simulation_ids[simulation_cnt_1+1:];
                    if observable_only_I:
                        observable_1 = mfamethods.check_observableNetFlux(flux_1,flux_lb_1,flux_ub_1)
                        if not observable_1: continue;
                    for cnt,simulation_id_2 in enumerate(list_2): #prevents redundancy
                        if redundancy_I: simulation_cnt_2 = cnt;
                        else: simulation_cnt_2 = simulation_cnt_1+cnt+1;
                        if simulation_cnt_2 == simulation_cnt_1:
                            continue;
                        # simulation_id_2 flux_data
                        flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2=None,None,None,None,None;
                        flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2=self.get_flux_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedNetFluxes(simulation_id_2,simulation_dateAndTimes[simulation_cnt_2],flux_unit,rxn_id);
                        if not mfamethods.check_criteria(flux_2,flux_stdev_2,flux_lb_2,flux_ub_2, criteria_I):
                            continue;
                        if observable_only_I:
                            observable_2 = mfamethods.check_observableNetFlux(flux_2,flux_lb_2,flux_ub_2);
                            if not observable_2: continue;
                        flux_diff,flux_distance,fold_change,significant = None,None,None,False;
                        flux_diff,flux_distance,fold_change,significant = mfamethods.calculate_fluxDifference(flux_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                                                                            flux_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2,
                                                                            criteria_I = criteria_I);
                        # record the data
                        data_O.append({
                            'analysis_id':analysis_id_I,
                            'simulation_id_1':simulation_id_1,
                            'simulation_dateAndTime_1':simulation_dateAndTimes[simulation_cnt_1],
                            'simulation_id_2':simulation_id_2,
                            'simulation_dateAndTime_2':simulation_dateAndTimes[simulation_cnt_2],
                            'rxn_id':rxn_id,
                            'flux_difference':flux_diff,
                            'significant':significant,
                            'significant_criteria':criteria_I,
                            'flux_units':flux_unit,
                            'fold_change_geo':fold_change,
                            'flux_distance':flux_distance,
                            'used_':True,
                            'comment_':None});
        # add data to the database
        self.add_data_stage02_isotopomer_fittedNetFluxDifferences(data_O);