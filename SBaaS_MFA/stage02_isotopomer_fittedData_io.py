# System
import json
# SBaaS
from .stage02_isotopomer_fittedData_query import stage02_isotopomer_fittedData_query
from .stage02_isotopomer_simulation_query import stage02_isotopomer_simulation_query
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from genomeScale_MFA_INCA.INCA_i import inca_i

class stage02_isotopomer_fittedData_io(stage02_isotopomer_fittedData_query,
                                       stage02_isotopomer_simulation_query):
    def import_isotopomerSimulationResults_INCA(self, simulation_id, filename, model_rxn_conversion_I=None):
        '''import results from a fluxomics simulation using INCA1.3
        INPUT:
        simulation_id = string, simulation_id
        filename = string, name of the matlab file
        model_rxn_conversion_I = optional {}, of INCA rxn_ids to model_rxn_ids (deprecated)
        Note: Please reference the model, fitdata, and simdata class structures in the INCA documentation
        for further information on the .mat file structure'''
        
        # lookup information about the simulation:
        simulation_info = {};
        simulation_info = self.get_simulation_simulationID_dataStage02IsotopomerSimulation(simulation_id);

        # import the data using inca_i
        incai = inca_i();
        incai.import_isotopomerSimulationResults_INCA(simulation_id=simulation_id,
                                                       filename=filename,
                                                       simulation_info=simulation_info,
                                                       model_rxn_conversion_I=model_rxn_conversion_I)

        # add data to the database
        self.add_data_stage02_isotopomer_fittedData(incai.fittedData);
        self.add_data_stage02_isotopomer_fittedFluxes(incai.fittedFluxes);
        self.add_data_stage02_isotopomer_fittedFragments(incai.fittedFragments);
        self.add_data_stage02_isotopomer_fittedMeasuredFluxes(incai.fittedMeasuredFluxes);
        self.add_data_stage02_isotopomer_fittedMeasuredFragments(incai.fittedMeasuredFragments);
        self.add_data_stage02_isotopomer_fittedMeasuredFluxResiduals(incai.fittedMeasuredFluxResiduals);
        self.add_data_stage02_isotopomer_fittedMeasuredFragmentResiduals(incai.fittedMeasuredFragmentResiduals);
        self.add_data_stage02_isotopomer_simulationParameters(incai.simulationParameters);
    def export_data_stage02_isotopomer_fittedFluxStatistics_csv(self,simulation_ids_I,filename_O,flux_units_I=[]):
        """export data_stage02_isotopomer_fittedFluxStatistics
        INPUT:
        simulation_id_I = [] of string, simulation_id
        filename_O = string, filename for export"""
        data_O = [];
        for simulation_id in simulation_ids_I:
            if flux_units_I:
                for flux_units in flux_units_I:
                    data_tmp =[];
                    data_tmp = self.get_rows_simulationIDAndFluxUnits_dataStage02IsotopomerFittedFluxStatistics(simulation_id,flux_units);
                    data_O.extend(data_tmp);
            else:
                data_tmp =[];
                data_tmp = self.get_rows_simulationID_dataStage02IsotopomerFittedFluxStatistics(simulation_id);
                data_O.extend(data_tmp);
        if data_O:
            io = base_exportData(data_O);
            io.write_dict2csv(filename_O);
    def export_data_stage02_isotopomer_fittedMeasuredFragments_csv(self,simulation_ids_I,filename_O):
        """export data_stage02_isotopomer_fittedMeasuredFragments
        INPUT:
        simulation_id_I = [] of string, simulation_id
        filename_O = string, filename for export"""
        data_O = [];
        for simulation_id in simulation_ids_I:
            data_tmp =[];
            data_tmp = self.get_rows_simulationID_dataStage02IsotopomerFittedMeasuredFragments(simulation_id);
            data_O.extend(data_tmp);
        if data_O:
            io = base_exportData(data_O);
            io.write_dict2csv(filename_O)
    def export_data_stage02_isotopomer_fittedData_csv(self,simulation_ids_I,filename_O):
        """export data_stage02_isotopomer_fittedData
        INPUT:
        simulation_id_I = [] of string, simulation_id
        filename_O = string, filename for export"""
        data_O = [];
        for simulation_id in simulation_ids_I:
            data_tmp =[];
            data_tmp = self.get_rows_simulationID_dataStage02IsotopomerFittedData(simulation_id);
            data_O.extend(data_tmp);
        if data_O:
            io = base_exportData(data_O);
            io.write_dict2csv(filename_O);
    def export_data_stage02_isotopomer_fittedFluxes_csv(self,simulation_ids_I,filename_O,flux_units_I=[]):
        """export data_stage02_isotopomer_fittedFluxes
        INPUT:
        simulation_id_I = [] of string, simulation_id
        filename_O = string, filename for export"""
        data_O = [];
        for simulation_id in simulation_ids_I:
            if flux_units_I:
                for flux_units in flux_units_I:
                    data_tmp =[];
                    data_tmp = self.get_rows_simulationIDAndFluxUnits_dataStage02IsotopomerfittedFluxes(simulation_id,flux_units);
                    data_O.extend(data_tmp);
            else:
                data_tmp =[];
                data_tmp = self.get_rows_simulationID_dataStage02IsotopomerFittedFluxes(simulation_id);
                data_O.extend(data_tmp);
        if data_O:
            io = base_exportData(data_O);
            io.write_dict2csv(filename_O);
   