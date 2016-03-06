#SBaaS
from .stage02_isotopomer_fittedData_io import stage02_isotopomer_fittedData_io
#SBaaS
from .stage02_isotopomer_fittedData_postgresql_models import *
#Resources
from genomeScale_MFA.MFA_methods import MFA_methods

class stage02_isotopomer_fittedData_execute(stage02_isotopomer_fittedData_io):
    def execute_calculateFluxStatistics(self,simulation_id_I,simulation_dateAndTimes_I=[],flux_units_I=[]):
        '''Calculate:
        1. # of unresolved fluxes per total # of reactions
        2. average flux precision per resolved flux'''
        mfamethods = MFA_methods();

        data_O = [];
        print('calculating fit statistics...')
        # simulation_dateAndTime
        if simulation_dateAndTimes_I:
            simulation_dateAndTimes = [self.convert_string2datetime(x) for x in simulation_dateAndTimes_I];
        else:
            simulation_dateAndTimes = [];
            simulation_dateAndTimes = self.get_simulationDateAndTimes_simulationID_dataStage02IsotopomerfittedFluxes(simulation_id_I);
        for simulation_dateAndTime in simulation_dateAndTimes:
            print('calculating flux ratios for simulation_dataAndTime ' + str(simulation_dateAndTime))
            # get all flux_units
            if flux_units_I:
                flux_units = flux_units_I;
            else:
                flux_units = [];
                flux_units = self.get_fluxUnits_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedNetFluxes(simulation_id_I,simulation_dateAndTime)
            for flux_unit_cnt,flux_unit in enumerate(flux_units):
                print('calculating fit statistics for flux_units ' + str(flux_unit))
                # get the net fluxes
                flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=[],[],[],[],[];
                flux_O,flux_stdev_O,flux_lb_O,flux_ub_O,flux_units_O=self.get_fluxes_simulationIDAndSimulationDateAndTimeAndFluxUnits_dataStage02IsotopomerfittedFluxes(simulation_id_I,simulation_dateAndTime,flux_unit);
                total_fluxes,observable_fluxes,relative_nObservableFluxes = mfamethods.calculate_relativeNObservableFluxes(flux_O,flux_lb_O,flux_ub_O);
                average_fluxPrecision,average_observable_fluxPrecision = mfamethods.calculate_averageFluxPrecision(flux_O,flux_stdev_O,flux_lb_O,flux_ub_O);
                total_fluxPrecision,total_observable_fluxPrecision = mfamethods.calculate_totalFluxPrecision(flux_O,flux_stdev_O,flux_lb_O,flux_ub_O);
                tmp = {};
                tmp['simulation_id'] = simulation_id_I;
                tmp['simulation_dateAndTime'] = simulation_dateAndTime;
                tmp['n_fluxes'] = total_fluxes
                tmp['n_observableFluxes'] = observable_fluxes
                tmp['total_precision'] = total_fluxPrecision
                tmp['total_observablePrecision'] = total_observable_fluxPrecision
                tmp['relative_nObservableFluxes']= relative_nObservableFluxes;
                tmp['average_observableFluxPrecision'] = average_observable_fluxPrecision;
                tmp['average_fluxPrecision'] = average_fluxPrecision
                tmp['flux_units'] = flux_unit;
                tmp['used_'] = True;
                tmp['comment_'] = None;
                data_O.append(tmp);
        self.add_data_stage02_isotopomer_fittedFluxStatistics(data_O);