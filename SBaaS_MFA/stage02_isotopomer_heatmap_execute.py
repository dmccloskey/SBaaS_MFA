# SBaaS
from .stage02_isotopomer_heatmap_io import stage02_isotopomer_heatmap_io
from .stage02_isotopomer_fittedNetFluxes_query import stage02_isotopomer_fittedNetFluxes_query
from .stage02_isotopomer_analysis_query import stage02_isotopomer_analysis_query
# Resources
from python_statistics.calculate_heatmap import calculate_heatmap
import numpy
# TODO: remove after making add methods
from .stage02_isotopomer_heatmap_postgresql_models import *

class stage02_isotopomer_heatmap_execute(stage02_isotopomer_heatmap_io,
                                         stage02_isotopomer_fittedNetFluxes_query,
                                         stage02_isotopomer_analysis_query):
    def execute_heatmap(self,
                analysis_id_I,simulation_ids_I=[],simulation_dateAndTimes_I=[],
                flux_units_I=[],rxn_ids_I=[],
                row_pdist_metric_I='euclidean',row_linkage_method_I='complete',
                col_pdist_metric_I='euclidean',col_linkage_method_I='complete',
                observable_only_I = False,
                order_rxnBySim_I = True,
                order_simulation_ids_I=False,
                order_rxn_ids_I=False,
                rxn_id_reverse_I=[]):
        '''Execute hierarchical cluster on row and column data
        INPUT:
        analysis_id_I = string, analysis id
        simulation_ids_I = list of simulation_ids
        simulation_dataAndTimes_I = list of simulation_dateAndTimes_I
        flux_units = list of flux units
        rxn_ids_I = list of rxn_ids
        observable_only_I = include only observable reactions
        order_rxnBySim_I = if True, rows will represent the fluxes and columns will represent the simulations
                           if False, rows will represent the simulations and columns will represent the fluxes
        order_simulation_ids_I = if True, order of the simulation_ids will be kept
        order_rxn_ids_I = if True, order of the rxn_ids will be kept
        rxn_id_reverse_I = list of rxn_ids to reverse the flux direction
        Assumptions:
        all simulation_ids must be unique (i.e., 1 simulation but 2 simulation_dateAndTimes will break the algorithm)
        all simulation_ids must have the same flux units (i.e., 
        '''

        #print('executing heatmap...');
        calculateheatmap = calculate_heatmap();
        ## Pass 1: get all the data
        data_O = {};
        rxn_ids_all = [];
        unobservable_fu_rxn_ids = {};
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
        for simulation_cnt_1, simulation_id_1 in enumerate(simulation_ids):
            #print('generating a heatmap for simulation_id ' + simulation_id_1);
            # get the units
            if flux_units_I:
                flux_units = flux_units_I;
            else:
                flux_units = [];
                flux_units = self.get_fluxUnits_simulationIDAndSimulationDateAndTime_dataStage02IsotopomerfittedNetFluxes(simulation_id_1,simulation_dateAndTimes[simulation_cnt_1])
            for fu_cnt,fu in enumerate(flux_units):
                # initialize only on first iteration
                if simulation_cnt_1==0:
                    data_O[fu] = {};
                    unobservable_fu_rxn_ids[fu] = set();
                #print('generating a heatmap for flux_units ' + fu);
                # get the rxn_ids
                if rxn_ids_I:
                    rxn_ids = rxn_ids_I;
                else:
                    rxn_ids = [];
                    rxn_ids = self.get_rxnIDs_simulationIDAndSimulationDateAndTimeAndFluxUnits_dataStage02IsotopomerfittedNetFluxes(simulation_id_1,simulation_dateAndTimes[simulation_cnt_1],fu);
                for rxn_id in rxn_ids:
                    if simulation_cnt_1==0:
                        data_O[fu][rxn_id] = [];
                    if simulation_cnt_1!=0 and not rxn_id in data_O[fu].keys():
                        continue;
                    rxn_ids_all.append(rxn_id);
                    #print('generating a heatmap for rxn_id ' + rxn_id);
                    # get the fluxes
                    row = {};
                    row = self.get_row_simulationIDAndSimulationDateAndTimeAndFluxUnitsAndRxnID_dataStage02IsotopomerfittedNetFluxes(simulation_id_1,simulation_dateAndTimes[simulation_cnt_1],fu,rxn_id);
                    if row:    
                        # change the direction of specified fluxes
                        if row['rxn_id'] in rxn_id_reverse_I:
                            row['flux']=-row['flux'];
                            row['flux_lb']=-row['flux_lb'];
                            row['flux_ub']=-row['flux_ub'];
                        if observable_only_I:
                            observable_1 = mfamethods.check_observableNetFlux(row['flux'],row['flux_lb'],row['flux_ub'])
                            if observable_1: 
                                data_O[fu][rxn_id].append(dendrogram_row_1row);
                                unobservable_fu_rxn_ids[fu].add(rxn_id);
                        else:
                            data_O[fu][rxn_id].append(row);
        ## Pass 2: data integrity check
        rxn_ids_unique = list(set(rxn_ids_all));
        rxn_ids_unique.sort();
        data_heatmap = {};
        rxn_ids_dict = {};
        for fu_cnt,fu in enumerate(list(data_O.keys())):
            data_heatmap[fu] = {};
            rxn_ids_dict[fu] = set();
            for rxn_id in rxn_ids_unique:
                if rxn_id in unobservable_fu_rxn_ids[fu]:
                    continue;
                data_tmp = [];
                for simulation_cnt_1, simulation_id_1 in enumerate(simulation_ids):
                    for d in data_O[fu][rxn_id]:
                        if d['simulation_id'] == simulation_id_1 and d['simulation_dateAndTime'] == simulation_dateAndTimes[simulation_cnt_1]:
                            data_tmp.append(d);
                            break;
                # check that the length matches
                if len(data_tmp) == len(simulation_ids):
                    data_heatmap[fu][rxn_id]= data_tmp;
                    rxn_ids_dict[fu].add(rxn_id);
        ## Pass 3: generate the heatmap for each flux_unit
        heatmap_O = [];
        dendrogram_col_O = [];
        dendrogram_row_O = [];
        for fu_cnt,fu in enumerate(list(data_heatmap.keys())):
            # generate the clustering for the heatmap
            heatmap_1 = [];
            dendrogram_col_1 = {};
            dendrogram_row_1 = {};
            # extract out the data {rxn_id:[{},...],...} -> [[{},...],...] -> [{},...]
            data1 = [v for v in data_heatmap[fu].values()];
            data2=[];
            for d in data1:
                data2.extend(d);
            if order_rxnBySim_I:
                heatmap_1,dendrogram_col_1,dendrogram_row_1 = calculateheatmap.make_heatmap(data2,
                    'rxn_id','simulation_id','flux',
                    row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                    col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I,
                    filter_rows_I=rxn_ids_I,
                    filter_columns_I=simulation_ids_I,
                    order_rowsFromTemplate_I=rxn_ids_I,
                    order_columnsFromTemplate_I=simulation_ids_I,);
            else:
                heatmap_1,dendrogram_col_1,dendrogram_row_1 = calculateheatmap.make_heatmap(data2,
                    'simulation_id','rxn_id','flux',
                    row_pdist_metric_I=row_pdist_metric_I,row_linkage_method_I=row_linkage_method_I,
                    col_pdist_metric_I=col_pdist_metric_I,col_linkage_method_I=col_linkage_method_I,
                    filter_rows_I=simulation_ids_I,
                    filter_columns_I=rxn_ids_I,
                    order_rowsFromTemplate_I=simulation_ids_I,
                    order_columnsFromTemplate_I=rxn_ids_I,);
            # add data to to the database for the heatmap
            for d in heatmap_1:
                d['analysis_id']=analysis_id_I;
                d['value_units']=fu;
                d['used_']=True;
                d['comment_']=None;
                heatmap_O.append(d);
            # add data to the database for the dendrograms
            dendrogram_col_1['analysis_id']=analysis_id_I;
            dendrogram_col_1['value_units']=fu;
            dendrogram_col_1['used_']=True;
            dendrogram_col_1['comment_']=None;
            dendrogram_col_O.append(dendrogram_col_1);
            dendrogram_row_1['analysis_id']=analysis_id_I;
            dendrogram_row_1['value_units']=fu;
            dendrogram_row_1['used_']=True;
            dendrogram_row_1['comment_']=None;
            dendrogram_row_O.append(dendrogram_row_1);
        self.add_rows_table('data_stage02_isotopomer_heatmap',heatmap_O);
        self.add_rows_table('data_stage02_isotopomer_dendrogram',dendrogram_col_O);
        self.add_rows_table('data_stage02_isotopomer_dendrogram',dendrogram_row_O);