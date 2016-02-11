#SBaaS
from .stage02_isotopomer_fittedFluxSplits_io import stage02_isotopomer_fittedFluxSplits_io
from .stage02_isotopomer_fittedNetFluxes_query import stage02_isotopomer_fittedNetFluxes_query
#SBaaS
from .stage02_isotopomer_fittedFluxSplits_postgresql_models import *
#Resources
from genomeScale_MFA.MFA_fluxSplits import isotopomer_fluxSplits
from genomeScale_MFA.MFA_methods import MFA_methods

class stage02_isotopomer_fittedFluxSplits_execute(stage02_isotopomer_fittedFluxSplits_io,
                                                  stage02_isotopomer_fittedNetFluxes_query):
    def execute_calculateFluxSplits(self,simulation_id_I,simulation_dateAndTimes_I=[],flux_splits_I=None,
                                    calculate_fluxStdevFromLBAndUB_I=True,
                                    calculate_fluxAverageFromLBAndUB_I=False,
                                    criteria_I = 'flux_lb/flux_ub'):
        '''calculate the flux splits
        INPUT:
        calculate_fluxStdevFromLBAndUB_I = substitute the calculated standard deviation with the lb/ub as follows:
                            (flux_ub_I - flux_lb_I)/4
        calculate_fluxAverageFromLBAndUB_I = calculate the flux average from the mean of the lb/ub
        criteria_I = string, flux_lb/flux_ub: use flux_lb and flux_ub to determine the confidence intervals (default)
                             flux_mean/flux_stdev: use the flux_mean and flux_stdev to determine the confidence intervals '''
        #Input:
        #   simulation_id_I = string, simulation id
        #   flux_splits_I = dict, {split_id:[rxn_id_1,rxn_id_2]}
        
        mfamethods = MFA_methods();
        if not flux_splits_I:
            flux_splits = isotopomer_fluxSplits();
            flux_splits_I=flux_splits.isotopomer_splits;

        data_O = [];
        print('calculating flux splits...')
        # simulation_dateAndTime
        if simulation_dateAndTimes_I:
            simulation_dateAndTimes = [self.convert_string2datetime(x) for x in simulation_dateAndTimes_I];
        else:
            simulation_dateAndTimes = [];
            simulation_dateAndTimes = self.get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedNetFluxes(simulation_id_I);
        for simulation_dateAndTime in simulation_dateAndTimes:
            print('calculating flux splits for simulation_dateAndTime ' + str(simulation_dateAndTime))
            # get all flux_units
            flux_units = [];
            flux_units = self.get_fluxUnits_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedNetFluxes(simulation_id_I,simulation_dateAndTime)
            for flux_unit_cnt,flux_unit in enumerate(flux_units):
                # check for more than 1 flux_unit
                if flux_unit_cnt>0:
                    break; #splits do not depend on the flux_unit
                print('calculating flux splits for flux_unit ' + str(flux_unit))
                for k,v in flux_splits_I.items():
                    print('flux_split ' + str(k))
                    # get the fluxes
                    flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1=[],[],[],[],[]
                    for rxn_id in v:
                        flux_average_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2 = self.get_flux_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedNetFluxes(simulation_id_I,simulation_dateAndTime,flux_unit,rxn_id);
                        flux_average_1.append(flux_average_2);
                        flux_stdev_1.append(flux_stdev_2);
                        flux_lb_1.append(flux_lb_2);
                        flux_ub_1.append(flux_ub_2);
                        flux_units_1.append(flux_units_2);
                    # calculate the split
                    split,split_stdev,split_lb,split_ub,split_units=mfamethods.calculate_fluxSplit(flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,criteria_I)
                    # correct the flux stdev
                    if calculate_fluxStdevFromLBAndUB_I: split_stdev = mfamethods.calculate_fluxStdevFromLBAndUB(split_lb,split_ub);
                    if calculate_fluxAverageFromLBAndUB_I: split = mfamethods.calculate_fluxAverageFromLBAndUB(split,split_lb,split_ub);
                    # record the data
                    for rxn_id_cnt,rxn_id in enumerate(v):
                        data_O.append({'simulation_id':simulation_id_I,
                            'simulation_dateAndTime':simulation_dateAndTime,
                            'split_id':k,
                            'split_rxn_ids':rxn_id,
                            'split':split[rxn_id_cnt],
                            'split_stdev':split_stdev[rxn_id_cnt],
                            'split_lb':split_lb[rxn_id_cnt],
                            'split_ub':split_ub[rxn_id_cnt],
                            'split_units':split_units[rxn_id_cnt],
                            'used_':True,
                            'comment_':None})
        # add the data to the database:
        for d in data_O:
            row=None;
            row=data_stage02_isotopomer_fittedFluxSplits(d['simulation_id'],
                                d['simulation_dateAndTime'],
                                d['split_id'],
                                d['split_rxn_ids'],
                                d['split'],
                                d['split_stdev'],
                                d['split_lb'],
                                d['split_ub'],
                                d['split_units'],
                                d['used_'],
                                d['comment_']);
            self.session.add(row);
        self.session.commit();