#System
import re
#SBaaS
from .stage02_isotopomer_simulation_io import stage02_isotopomer_simulation_io
from .stage02_isotopomer_tracers_query import stage02_isotopomer_tracers_query
from .stage02_isotopomer_measuredData_query import stage02_isotopomer_measuredData_query
from SBaaS_models.models_MFA_execute import models_MFA_execute
#Dependencies
from genomeScale_MFA_INCA.INCA_api import inca_api

class stage02_isotopomer_simulation_execute(stage02_isotopomer_simulation_io,
                                            stage02_isotopomer_tracers_query,
                                            stage02_isotopomer_measuredData_query,
                                            models_MFA_execute):
    def execute_makeIsotopomerSimulation_INCA(self,simulation_id_I, stationary_I = True, parallel_I = False, ko_list_I=[],flux_dict_I={},description_I=None):
        '''export a fluxomics experimental data for simulation using INCA'''
        #Input:
        #   stationary_I = boolean
        #                  indicates whether each time-point is written to a separate file, or part of a time-course
        #   parallel_I = boolean
        #                  indicates whether multiple tracers were used


        # get simulation information
        simulation_info = {};
        simulation_info = self.get_simulation_simulationID_dataStage02IsotopomerSimulation(simulation_id_I);

        # extract model/mapping info
        if len(simulation_info['model_id'])>1 or len(simulation_info['mapping_id'])>1:
            print('multiple model and mapping ids found for the simulation!');
            print('only the first model/mapping id will be used');
        # determine if the simulation is a parallel labeling experiment, non-stationary, or both
        multiple_experiment_ids = False;
        multiple_snas = False;
        multiple_time_points = False;
        if len(simulation_info['experiment_id'])>1 and len(simulation_info['sample_name_abbreviation'])>1:
            print('multiple experiment_ids and sample_name_abbreviations found for the simulation!')
            print('only 1 experiment_ids and with multiple sample_name_abbreviations or 1 sample_name_abbreviation with multiple experiments can be specified')
        elif len(simulation_info['experiment_id'])>1:
            multiple_experiment_ids = True;
        elif len(simulation_info['sample_name_abbreviation'])>1:
            multiple_snas = True;
        if len(simulation_info['time_point'])>1:
            multiple_time_points = True;

        if parallel_I and multiple_experiment_ids:
            self.make_isotopomerSimulation_parallel_experimentID_INCA(simulation_info,stationary_I,ko_list_I,flux_dict_I,description_I)
        elif parallel_I and multiple_snas:
            self.make_isotopomerSimulation_parallel_sna_INCA(simulation_info,stationary_I,ko_list_I,flux_dict_I,description_I)
        else:
            self.make_isotopomerSimulation_individual_INCA(simulation_info,stationary_I,ko_list_I,flux_dict_I,description_I)
    def make_isotopomerSimulation_parallel_experimentID_INCA(self,simulation_info, stationary_I = True, ko_list_I=[],flux_dict_I={},description_I=None):
        '''Make parallel labeling simulation by experiment_id for INCA'''
        
        inca = inca_api();
        model_id = simulation_info['model_id'][0]
        mapping_id = simulation_info['mapping_id'][0]
        time_points = simulation_info['time_point'][0]
        experiment_ids = simulation_info['experiment_id']
        sna = simulation_info['sample_name_abbreviation'][0]
        # collect the simulation data
        modelReaction_data,modelMetabolite_data,measuredFluxes_data,experimentalMS_data,tracers = [],[],[],[],[];
        for experiment_cnt,experiment_id in enumerate(experiment_ids):
            # get the tracers
            tracers_tmp = [];
            tracers_tmp = self.get_rows_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerTracers(experiment_id,sna);  
            tracers.extend(tracers_tmp); 
            # get flux measurements
            measuredFluxes_data_tmp = [];
            measuredFluxes_data_tmp = self.get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFluxes(experiment_id,model_id,sna);
            measuredFluxes_data.extend(measuredFluxes_data_tmp)
            # get the ms_data
            if stationary_I:
                experimentalMS_data_tmp = [];
                experimentalMS_data_tmp = self.get_row_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage02IsotopomerMeasuredFragments(experiment_id,sna,time_points[0]);
                experimentalMS_data.extend(experimentalMS_data_tmp);
            else:
                experimentalMS_data_tmp = [];
                experimentalMS_data = self.get_row_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFragments(experiment_id,sna);
                experimentalMS_data.extend(experimentalMS_data_tmp);
            #get model reactions
            if not modelReaction_data: #only once
                modelReaction_data = [];
                modelReaction_data = self.get_rows_modelID_dataStage02IsotopomerModelReactions(model_id);
                #simulate the model
                cobra_model = self.simulate_model(model_id,ko_list_I,flux_dict_I,measuredFluxes_data,description_I);
                for i,row in enumerate(modelReaction_data):
                    #get atom mapping data
                    atomMapping = {};
                    atomMapping = self.get_row_mappingIDAndRxnID_dataStage02IsotopomerAtomMappingReactions(mapping_id,row['rxn_id']);
                    #generate reaction equations
                    rxn_equation = '';
                    print(row['rxn_id'])
                    #if row['rxn_id'] == 'EX_glc_LPAREN_e_RPAREN_':
                    #    print 'check'
                    if atomMapping:
                        rxn_equation = inca.make_isotopomerRxnEquations_INCA(
                                    row['reactants_ids'],
                                    row['products_ids'],
                                    row['reactants_stoichiometry'],
                                    row['products_stoichiometry'],
                                    row['reversibility'],
                                    atomMapping['reactants_stoichiometry_tracked'],
                                    atomMapping['products_stoichiometry_tracked'],
                                    atomMapping['reactants_ids_tracked'],
                                    atomMapping['products_ids_tracked'],
                                    atomMapping['reactants_elements_tracked'],
                                    atomMapping['products_elements_tracked'],
                                    atomMapping['reactants_positions_tracked'],
                                    atomMapping['products_positions_tracked'],
                                    atomMapping['reactants_mapping'],
								    atomMapping['products_mapping']);
                    else:
                        rxn_equation = inca.make_isotopomerRxnEquations_INCA(
                                    row['reactants_ids'],
                                    row['products_ids'],
                                    row['reactants_stoichiometry'],
                                    row['products_stoichiometry'],
                                    row['reversibility'],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
								    []);
                    atomMapping['rxn_equation']=rxn_equation;
                    modelReaction_data[i].update(atomMapping);
                    # update the lower bounds and upper bounds of the model to represent the experimental data
                    if measuredFluxes_data:
                        for flux in measuredFluxes_data:
                            if row['rxn_id'] == flux['rxn_id']:
                                modelReaction_data[i]['lower_bound'] = flux['flux_lb']
                                modelReaction_data[i]['upper_bound'] = flux['flux_ub']
                    # update the lower bounds and upper bounds of the model to represent the input data (if the model has not already been updated)
                    for ko in ko_list_I: # implement optimal KOs
                        if row['rxn_id'] == ko:
                            modelReaction_data[i]['lower_bound'] = 0.0;
                            modelReaction_data[i]['upper_bound'] = 0.0;
                    for rxn,flux in flux_dict_I.items():  # implement flux constraints:
                        if row['rxn_id'] == rxn:
                            modelReaction_data[i]['lower_bound'] = flux['lb'];
                            modelReaction_data[i]['upper_bound'] = flux['ub'];
                    # add in a flux_val field to supply an initial starting guess for the MFA solver
                    if cobra_model.solution.f:
                        modelReaction_data[i]['flux_val'] = cobra_model.solution.x_dict[row['rxn_id']];
                    else:
                        modelReaction_data[i]['flux_val'] = 0;
            # get model metabolites
            if not modelMetabolite_data: #only once
                modelMetabolite_data = [];
                modelMetabolite_data = self.get_rows_modelID_dataStage02IsotopomerModelMetabolites(model_id);
                for i,row in enumerate(modelMetabolite_data):
                    #get atom mapping data
                    atomMapping = {};
                    atomMapping = self.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(mapping_id,row['met_id']);
                    #update
                    if atomMapping:
                        modelMetabolite_data[i].update(atomMapping);
                    else:
                        modelMetabolite_data[i].update({
                            'met_elements':None,
                            'met_atompositions':None,
                            'met_symmetry_elements':None,
                            'met_symmetry_atompositions':None});
        # Write out to matlab script
        filename_mat = settings.workspace_data + '/_output/' + re.sub('[.\/]','',simulation_info['simulation_id'][0]);
        filename_mat_model = filename_mat + "_model" + '.m';
        mat_script = '';
        mat_script += inca.writeScript_model_INCA(modelReaction_data,modelMetabolite_data,
                                        measuredFluxes_data,experimentalMS_data,tracers)
        mat_script += inca.writeScript_simulationOptions_Inca(stationary_I)
        mat_script += inca.writeScript_experiment_INCA(modelReaction_data,modelMetabolite_data,
                                                measuredFluxes_data,experimentalMS_data,tracers,
                                                'sample_name_abbreviation')
        with open(filename_mat_model,'w') as f:
            f.write(mat_script);
    def make_isotopomerSimulation_parallel_sna_INCA(self,simulation_info, stationary_I = True, ko_list_I=[],flux_dict_I={},description_I=None):
        '''Make parallel labeling simulation by sample name abbreviation for INCA'''
        
        inca = inca_api();
        model_id = simulation_info['model_id'][0]
        mapping_id = simulation_info['mapping_id'][0]
        time_points = simulation_info['time_point']
        experiment_id = simulation_info['experiment_id'][0]
        sample_name_abbreviations = simulation_info['sample_name_abbreviation']
        # collect the simulation data
        modelReaction_data,modelMetabolite_data,measuredFluxes_data,experimentalMS_data,tracers = [],[],[],[],[];
        for sna_cnt,sna in enumerate(sample_name_abbreviations):
            # get the tracers
            tracers_tmp = [];
            tracers_tmp = self.get_rows_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerTracers(experiment_id,sna);  
            tracers.extend(tracers_tmp); 
            # get flux measurements
            measuredFluxes_data_tmp = [];
            measuredFluxes_data_tmp = self.get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFluxes(experiment_id,model_id,sna);
            measuredFluxes_data.extend(measuredFluxes_data_tmp)
            # get the ms_data
            if stationary_I:
                experimentalMS_data_tmp = [];
                experimentalMS_data_tmp = self.get_row_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage02IsotopomerMeasuredFragments(experiment_id,sna,time_points[0]);
                experimentalMS_data.extend(experimentalMS_data_tmp);
            else:
                experimentalMS_data_tmp = [];
                experimentalMS_data = self.get_row_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFragments(experiment_id,sna);
                experimentalMS_data.extend(experimentalMS_data_tmp);
            #get model reactions
            if not modelReaction_data: #only once
                modelReaction_data = [];
                modelReaction_data = self.get_rows_modelID_dataStage02IsotopomerModelReactions(model_id);
                #simulate the model
                cobra_model = self.simulate_model(model_id,ko_list_I,flux_dict_I,measuredFluxes_data,description_I);
                for i,row in enumerate(modelReaction_data):
                    #get atom mapping data
                    atomMapping = {};
                    atomMapping = self.get_row_mappingIDAndRxnID_dataStage02IsotopomerAtomMappingReactions(mapping_id,row['rxn_id']);
                    #generate reaction equations
                    rxn_equation = '';
                    print(row['rxn_id'])
                    #if row['rxn_id'] == 'EX_glc_LPAREN_e_RPAREN_':
                    #    print 'check'
                    if atomMapping:
                        rxn_equation = inca.make_isotopomerRxnEquations_INCA(
                                    row['reactants_ids'],
                                    row['products_ids'],
                                    row['reactants_stoichiometry'],
                                    row['products_stoichiometry'],
                                    row['reversibility'],
                                    atomMapping['reactants_stoichiometry_tracked'],
                                    atomMapping['products_stoichiometry_tracked'],
                                    atomMapping['reactants_ids_tracked'],
                                    atomMapping['products_ids_tracked'],
                                    atomMapping['reactants_elements_tracked'],
                                    atomMapping['products_elements_tracked'],
                                    atomMapping['reactants_positions_tracked'],
                                    atomMapping['products_positions_tracked'],
                                    atomMapping['reactants_mapping'],
								    atomMapping['products_mapping']);
                    else:
                        rxn_equation = inca.make_isotopomerRxnEquations_INCA(
                                    row['reactants_ids'],
                                    row['products_ids'],
                                    row['reactants_stoichiometry'],
                                    row['products_stoichiometry'],
                                    row['reversibility'],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
								    []);
                    atomMapping['rxn_equation']=rxn_equation;
                    modelReaction_data[i].update(atomMapping);
                    # update the lower bounds and upper bounds of the model to represent the experimental data
                    if measuredFluxes_data:
                        for flux in measuredFluxes_data:
                            if row['rxn_id'] == flux['rxn_id']:
                                modelReaction_data[i]['lower_bound'] = flux['flux_lb']
                                modelReaction_data[i]['upper_bound'] = flux['flux_ub']
                    # update the lower bounds and upper bounds of the model to represent the input data (if the model has not already been updated)
                    for ko in ko_list_I: # implement optimal KOs
                        if row['rxn_id'] == ko:
                            modelReaction_data[i]['lower_bound'] = 0.0;
                            modelReaction_data[i]['upper_bound'] = 0.0;
                    for rxn,flux in flux_dict_I.items():  # implement flux constraints:
                        if row['rxn_id'] == rxn:
                            modelReaction_data[i]['lower_bound'] = flux['lb'];
                            modelReaction_data[i]['upper_bound'] = flux['ub'];
                    # add in a flux_val field to supply an initial starting guess for the MFA solver
                    if cobra_model.solution.f:
                        modelReaction_data[i]['flux_val'] = cobra_model.solution.x_dict[row['rxn_id']];
                    else:
                        modelReaction_data[i]['flux_val'] = 0;
            # get model metabolites
            if not modelMetabolite_data: #only once
                modelMetabolite_data = [];
                modelMetabolite_data = self.get_rows_modelID_dataStage02IsotopomerModelMetabolites(model_id);
                for i,row in enumerate(modelMetabolite_data):
                    #get atom mapping data
                    atomMapping = {};
                    atomMapping = self.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(mapping_id,row['met_id']);
                    #update
                    if atomMapping:
                        modelMetabolite_data[i].update(atomMapping);
                    else:
                        modelMetabolite_data[i].update({
                            'met_elements':None,
                            'met_atompositions':None,
                            'met_symmetry_elements':None,
                            'met_symmetry_atompositions':None});
        # Write out to matlab script
        filename_mat = settings.workspace_data + '/_output/' + re.sub('[.\/]','',simulation_info['simulation_id'][0]);
        filename_mat_model = filename_mat + "_model" + '.m';
        mat_script = '';
        mat_script += inca.writeScript_model_INCA(modelReaction_data,modelMetabolite_data,
                                        measuredFluxes_data,experimentalMS_data,tracers)
        mat_script += inca.writeScript_simulationOptions_Inca(stationary_I)
        mat_script += inca.writeScript_experiment_INCA(modelReaction_data,modelMetabolite_data,
                                                measuredFluxes_data,experimentalMS_data,tracers,
                                                'sample_name_abbreviation')
        with open(filename_mat_model,'w') as f:
            f.write(mat_script);
    def make_isotopomerSimulation_individual_INCA(self,simulation_info, stationary_I = True, ko_list_I=[],flux_dict_I={},description_I=None):
        '''Make individual labeling simulations for INCA'''
        
        inca = inca_api();
        model_id = simulation_info['model_id'][0]
        mapping_id = simulation_info['mapping_id'][0]
        time_points = simulation_info['time_point']
        experiment_ids = simulation_info['experiment_id']
        sample_name_abbreviations = simulation_info['sample_name_abbreviation']
        for experiment_id in experiment_ids:
            for sna_cnt,sna in enumerate(sample_name_abbreviations):
                print('Collecting and writing experimental and model data for sample name abbreviation ' + sna);
                # get the tracers
                tracers = [];
                tracers = self.get_rows_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerTracers(experiment_id,sna);

                # data containers
                modelReaction_data,modelMetabolite_data,measuredFluxes_data,experimentalMS_data = [],[],[],[];  
                # get flux measurements
                measuredFluxes_data = [];
                measuredFluxes_data = self.get_rows_experimentIDAndModelIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFluxes(experiment_id,model_id,sna);
                # get the ms_data
                if stationary_I:
                    experimentalMS_data = [];
                    experimentalMS_data = self.get_row_experimentIDAndSampleNameAbbreviationAndTimePoint_dataStage02IsotopomerMeasuredFragments(experiment_id,sna,time_points[0]);
                else:
                    experimentalMS_data = [];
                    experimentalMS_data = self.get_row_experimentIDAndSampleNameAbbreviation_dataStage02IsotopomerMeasuredFragments(experiment_id,sna);
                #get model reactions
                modelReaction_data = [];
                modelReaction_data = self.get_rows_modelID_dataStage02IsotopomerModelReactions(model_id);
                #simulate the model
                cobra_model = None;
                #cobra_model = self.simulate_model(model_id,ko_list_I,flux_dict_I,measuredFluxes_data,description_I);
                for i,row in enumerate(modelReaction_data):
                    #get atom mapping data
                    atomMapping = {};
                    atomMapping = self.get_row_mappingIDAndRxnID_dataStage02IsotopomerAtomMappingReactions(mapping_id,row['rxn_id']);
                    #generate reaction equations
                    rxn_equation = '';
                    print(row['rxn_id'])
                    #if row['rxn_id'] == 'EX_glc_LPAREN_e_RPAREN_':
                    #    print 'check'
                    if atomMapping:
                        rxn_equation = inca.make_isotopomerRxnEquations_INCA(
                                    row['reactants_ids'],
                                    row['products_ids'],
                                    row['reactants_stoichiometry'],
                                    row['products_stoichiometry'],
                                    row['reversibility'],
                                    atomMapping['reactants_stoichiometry_tracked'],
                                    atomMapping['products_stoichiometry_tracked'],
                                    atomMapping['reactants_ids_tracked'],
                                    atomMapping['products_ids_tracked'],
                                    atomMapping['reactants_elements_tracked'],
                                    atomMapping['products_elements_tracked'],
                                    atomMapping['reactants_positions_tracked'],
                                    atomMapping['products_positions_tracked'],
                                    atomMapping['reactants_mapping'],
								    atomMapping['products_mapping']);
                    else:
                        rxn_equation = inca.make_isotopomerRxnEquations_INCA(
                                    row['reactants_ids'],
                                    row['products_ids'],
                                    row['reactants_stoichiometry'],
                                    row['products_stoichiometry'],
                                    row['reversibility'],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
                                    [],
								    []);
                    atomMapping['rxn_equation']=rxn_equation;
                    modelReaction_data[i].update(atomMapping);
                    # update the lower bounds and upper bounds of the model to represent the experimental data
                    if measuredFluxes_data:
                        for flux in measuredFluxes_data:
                            if row['rxn_id'] == flux['rxn_id']:
                                modelReaction_data[i]['lower_bound'] = flux['flux_lb']
                                modelReaction_data[i]['upper_bound'] = flux['flux_ub']
                    # update the lower bounds and upper bounds of the model to represent the input data (if the model has not already been updated)
                    for ko in ko_list_I: # implement optimal KOs
                        if row['rxn_id'] == ko:
                            modelReaction_data[i]['lower_bound'] = 0.0;
                            modelReaction_data[i]['upper_bound'] = 0.0;
                    for rxn,flux in flux_dict_I.items():  # implement flux constraints:
                        if row['rxn_id'] == rxn:
                            modelReaction_data[i]['lower_bound'] = flux['lb'];
                            modelReaction_data[i]['upper_bound'] = flux['ub'];
                    # add in a flux_val field to supply an initial starting guess for the MFA solver
                    if cobra_model and cobra_model.solution.f and row['rxn_id'] in cobra_model.solution.x_dict:
                        modelReaction_data[i]['flux_val'] = cobra_model.solution.x_dict[row['rxn_id']];
                    else:
                        modelReaction_data[i]['flux_val'] = 0;
                # get model metabolites
                modelMetabolite_data = [];
                modelMetabolite_data = self.get_rows_modelID_dataStage02IsotopomerModelMetabolites(model_id);
                for i,row in enumerate(modelMetabolite_data):
                    #get atom mapping data
                    atomMapping = {};
                    atomMapping = self.get_rows_mappingIDAndMetID_dataStage02IsotopomerAtomMappingMetabolites(mapping_id,row['met_id']);
                    #update
                    if atomMapping:
                        modelMetabolite_data[i].update(atomMapping);
                    else:
                        modelMetabolite_data[i].update({
                            'met_elements':None,
                            'met_atompositions':None,
                            'met_symmetry_elements':None,
                            'met_symmetry_atompositions':None});

                ## dump the experiment to a matlab script to generate the matlab files in matlab
                # Matlab script file to make the structures
                filename_mat = self.settings['workspace_data'] + '/_output/' + re.sub('[.\/]','',simulation_info['simulation_id'][0]);
                filename_mat_model = filename_mat + '.m';
                mat_script = '';
                mat_script += inca.writeScript_model_INCA(modelReaction_data,modelMetabolite_data,
                                                measuredFluxes_data,experimentalMS_data,tracers)
                mat_script += inca.writeScript_simulationOptions_Inca(stationary_I)
                mat_script += inca.writeScript_experiment_INCA(modelReaction_data,modelMetabolite_data,
                                                        measuredFluxes_data,experimentalMS_data,tracers,
                                                        'sample_name_abbreviation')
        with open(filename_mat_model,'w') as f:
            f.write(mat_script); 