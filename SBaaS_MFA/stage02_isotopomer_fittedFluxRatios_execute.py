#SBaaS
from .stage02_isotopomer_fittedFluxRatios_io import stage02_isotopomer_fittedFluxRatios_io
from .stage02_isotopomer_fittedFluxRatios_postgresql_models import *
#Resources
from genomeScale_MFA.MFA_methods import MFA_methods

class stage02_isotopomer_fittedFluxRatios_execute(stage02_isotopomer_fittedFluxRatios_io):
    def execute_calculateFluxRatios(self,simulation_id_I,simulation_dateAndTimes_I=[],flux_ratios_I={}):
        '''calculate the flux ratios'''
        #Input:
        #   simulation_id_I = string, simulation id
        #   flux_ratios_I = dict, {ratio_id:[rxn_id_1,rxn_id_2]}

        data_O = [];
        print('calculating flux ratios...')
        # simulation_dateAndTime
        if simulation_dateAndTimes_I:
            simulation_dateAndTimes = [self.convert_string2datetime(x) for x in simulation_dateAndTimes_I];
        else:
            simulation_dateAndTimes = [];
            simulation_dateAndTimes = self.get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedFluxes(simulation_id_I);
        for simulation_dateAndTime in simulation_dateAndTimes:
            print('calculating flux ratios for simulation_dataAndTime ' + str(simulation_dateAndTime))
            # get all flux_units
            flux_units = [];
            flux_units = self.get_fluxUnits_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedNetFluxes(simulation_id_I,simulation_dateAndTime)
            for flux_unit_cnt,flux_unit in enumerate(flux_units):
                print('calculating flux ratios for flux_units ' + str(flux_unit))
                # check for more than 1 flux_unit
                if flux_unit_cnt>0:
                    break; #ratios do not depend on the flux_unit
                for k,v in flux_ratios_I.items():
                    print('calculating flux ratios for flux_ratio ' + str(k))
                    # get the fluxes
                    flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1 = self.get_flux_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedNetFluxes(simulation_id_I,simulation_dateAndTime,flux_unit,v[0]);
                    flux_average_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2 = self.get_flux_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedNetFluxes(simulation_id_I,simulation_dateAndTime,flux_unit,v[1]);
                    # calculate the ratio
                    ratio,ratio_stdev,ratio_lb,ratio_ub,ratio_units=self.calculate_fluxRatio(flux_average_1,flux_stdev_1,flux_lb_1,flux_ub_1,flux_units_1,
                                                                                             flux_average_2,flux_stdev_2,flux_lb_2,flux_ub_2,flux_units_2)
                    # record the data
                    data_O.append({'simulation_id':simulation_id_I,
                        'simulation_dateAndTime':simulation_dateAndTime,
                        'ratio_id':k,
                        'ratio_rxn_ids':v,
                        'ratio':ratio,
                        'ratio_stdev':ratio_stdev,
                        'ratio_lb':ratio_lb,
                        'ratio_ub':ratio_ub,
                        'ratio_units':ratio_units,
                        'used_':True,
                        'comment_':None})
        # add the data to the database:
        for d in data_O:
            row=None;
            row=data_stage02_isotopomer_fittedFluxRatios(d['simulation_id'],
                                d['simulation_dateAndTime'],
                                d['ratio_id'],
                                d['ratio_rxn_ids'],
                                d['ratio'],
                                d['ratio_stdev'],
                                d['ratio_lb'],
                                d['ratio_ub'],
                                d['ratio_units'],
                                d['used_'],
                                d['comment_']);
            self.session.add(row);
        self.session.commit();