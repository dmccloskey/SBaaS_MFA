#SBaaS
from .stage02_isotopomer_measuredData_io import stage02_isotopomer_measuredData_io
from SBaaS_isotopomer.stage01_isotopomer_averages_query import stage01_isotopomer_averages_query
from SBaaS_physiology.stage01_physiology_rates_query import stage01_physiology_rates_query
from SBaaS_LIMS.lims_msMethod_query import lims_msMethod_query
#SBaaS
from .stage02_isotopomer_measuredData_postgresql_models import *
from genomeScale_MFA.MFA_utilities import MFA_utilities
#resources
import re
from math import sqrt

class stage02_isotopomer_measuredData_execute(stage02_isotopomer_measuredData_io,
                                              stage01_isotopomer_averages_query,
                                              lims_msMethod_query,
                                              stage01_physiology_rates_query):
    def execute_makeMeasuredFragments(self,experiment_id_I, sample_name_abbreviations_I = [], time_points_I = [], scan_types_I = [], met_ids_I = []):
        '''Collect and format MS data from data_stage01_isotopomer_averagesNormSum for fluxomics simulation'''
        mfautilities = MFA_utilities();

        # get experiment information:
        met_id_conv_dict = {'Hexose_Pool_fru_glc-D':'glc-D',
                            'Pool_2pg_3pg':'3pg',
                            '23dpg':'13dpg'};
        data_O = [];
        experiment_stdev = [];
        # get sample names and sample name abbreviations
        if sample_name_abbreviations_I:
            sample_abbreviations = sample_name_abbreviations_I;
            st = 'Unknown';
            sample_types_lst = [];
            sample_types_lst.extend([st for i in range(len(sample_abbreviations))]);
        else:
            sample_abbreviations = [];
            sample_types = ['Unknown'];
            sample_types_lst = [];
            for st in sample_types:
                sample_abbreviations_tmp = [];
                sample_abbreviations_tmp = self.get_sampleNameAbbreviations_experimentIDAndSampleType_dataStage01AveragesNormSum(experiment_id_I,st);
                sample_abbreviations.extend(sample_abbreviations_tmp);
                sample_types_lst.extend([st for i in range(len(sample_abbreviations_tmp))]);
        for sna_cnt,sna in enumerate(sample_abbreviations):
            print('Collecting experimental MS data for sample name abbreviation ' + sna);
            # get time points
            if time_points_I:
                time_points = time_points_I;
            else:
                time_points = [];
                time_points = self.get_timePoint_experimentIDAndSampleNameAbbreviation_dataStage01AveragesNormSum(experiment_id_I,sna);
            for tp in time_points:
                print('Collecting experimental MS data for time-point ' + str(tp));
                # get the scan_types
                if scan_types_I:
                    scan_types = [];
                    scan_types_tmp = [];
                    scan_types_tmp = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01AveragesNormSum(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                    scan_types = [st for st in scan_types_tmp if st in scan_types_I];
                else:
                    scan_types = [];
                    scan_types = self.get_scanTypes_experimentIDAndTimePointAndSampleAbbreviationsAndSampleType_dataStage01AveragesNormSum(experiment_id_I,tp,sna,sample_types_lst[sna_cnt]);
                for scan_type in scan_types:
                    print('Collecting experimental MS data for scan type ' + scan_type)
                    # met_ids
                    if not met_ids_I:
                        met_ids = [];
                        met_ids = self.get_metIDs_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanType_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type);
                    else:
                        met_ids = met_ids_I;
                    if not(met_ids): continue #no component information was found
                    for met in met_ids:
                        print('Collecting experimental MS data for metabolite ' + met);
                        # format the metabolite
                        if met in list(met_id_conv_dict.keys()):
                            met_formatted = met_id_conv_dict[met];
                        else: met_formatted = met;
                        met_formatted = re.sub('-','_DASH_',met_formatted)
                        met_formatted = re.sub('[(]','_LPARANTHES_',met_formatted)
                        met_formatted = re.sub('[)]','_RPARANTHES_',met_formatted)
                        # fragments
                        fragment_formulas = [];
                        fragment_formulas = self.get_fragmentFormula_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetID_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met);
                        # frag c map
                        frag_cmap = {};
                        frag_cmap = self.get_precursorFormulaAndProductFormulaAndCMapsAndPositions_metID(met,'-','tuning');
                        for frag in fragment_formulas:
                            # data
                            data_mat = [];
                            data_mat_cv = [];
                            data_mat_n = [];
                            data_mat, data_mat_cv, data_mat_n = self.get_spectrum_experimentIDAndSampleAbbreviationAndTimePointAndSampleTypeAndScanTypeAndMetIDAndFragmentFormula_dataStage01AveragesNormSum( \
                                experiment_id_I,sna,tp,sample_types_lst[sna_cnt],scan_type,met,frag);
                            # combine into a structure
                            positions,elements = [],[];
                            positions,elements = mfautilities.convert_fragmentAndElements2PositionAndElements(frag_cmap[frag]['fragment'],frag_cmap[frag]['fragment_elements']);
                            #fragname = met_formatted+'_c'+'_'+ re.sub('[-+]','',frag);
                            fragname = met_formatted+'_c'+'_'+ re.sub('[-+]','',frag)+'_'+scan_type;
                            data_names = [];
                            data_stdev = [];
                            data_stderr = [];
                            for i,d in enumerate(data_mat):
                                stdev = 0.0;
                                stderr = 0.0;
                                if data_mat_cv[i]: 
                                    if data_mat_n[i]==1:
                                        stdev = 0.05;
                                    else:
                                        stdev = data_mat[i]*data_mat_cv[i]/100;
                                    stderr = stdev/sqrt(data_mat_n[i]);
                                data_names.append(fragname+str(i));
                                data_stdev.append(stdev);
                                data_stderr.append(stderr);
                                experiment_stdev.append(stdev);
                            data_tmp = {'experiment_id':experiment_id_I,
                                           'sample_name_abbreviation':sna,
                                           'sample_type':sample_types_lst[sna_cnt],
                                           'time_point':tp,
                                            'met_id':met_formatted+'_c',
                                            'fragment_id':fragname,
                                            'fragment_formula':frag,
                                            'intensity_normalized_average':data_mat,
                                            'intensity_normalized_cv':data_mat_cv,
                                            'intensity_normalized_stdev':data_stdev,
                                            'intensity_normalized_n':data_mat_n,
                                            'intensity_normalized_units':'normSum',
                                            'met_elements':elements,
                                            'met_atompositions':positions};
                            data_O.append(data_tmp);
                            #add data to the database
                            row = [];
                            row = data_stage02_isotopomer_measuredFragments(
                                    experiment_id_I,
                                    sna,
                                    tp,
                                    met_formatted+'_c',
                                    fragname,
                                    frag,
                                    data_mat,
                                    data_mat_cv,
                                    data_stdev,
                                    'normSum',
                                    scan_type,
                                    elements,
                                    positions,
                                    True,
                                    None);
                            self.session.add(row);
        self.session.commit();
    def execute_addMeasuredFluxes(self,experiment_id_I, ko_list={}, flux_dict={}, model_ids_I=[], sample_name_abbreviations_I=[]):
        '''Add flux data for physiological simulation'''
        #Input:
            #flux_dict = {};
            #flux_dict['iJO1366'] = {};
            #flux_dict['iJO1366'] = {};
            #flux_dict['iJO1366']['sna'] = {};
            #flux_dict['iJO1366']['sna']['Ec_biomass_iJO1366_WT_53p95M'] = {'ave':None,'stdev':None,'units':'mmol*gDCW-1*hr-1','lb':0.704*0.9,'ub':0.704*1.1};
            #flux_dict['iJO1366']['sna']['EX_ac_LPAREN_e_RPAREN_'] = {'ave':None,'stdev':None,'units':'mmol*gDCW-1*hr-1','lb':2.13*0.9,'ub':2.13*1.1};
            #flux_dict['iJO1366']['sna']['EX_o2_LPAREN_e_RPAREN__reverse'] = {'ave':None,'units':'mmol*gDCW-1*hr-1','stdev':None,'lb':0,'ub':16};
            #flux_dict['iJO1366']['sna']['EX_glc_LPAREN_e_RPAREN_'] = {'ave':None,'stdev':None,'units':'mmol*gDCW-1*hr-1','lb':-7.4*1.1,'ub':-7.4*0.9};

        data_O = [];
        # get the model ids:
        if model_ids_I:
            model_ids = model_ids_I;
        else:
            model_ids = [];
            model_ids = self.get_modelID_experimentID_dataStage02IsotopomerSimulation(experiment_id_I);
        for model_id in model_ids:
            # get sample names and sample name abbreviations
            if sample_name_abbreviations_I:
                sample_name_abbreviations = sample_name_abbreviations_I;
            else:
                sample_name_abbreviations = [];
                sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentIDAndModelID_dataStage02IsotopomerSimulation(experiment_id_I,model_id);
            for sna_cnt,sna in enumerate(sample_name_abbreviations):
                print('Adding experimental fluxes for sample name abbreviation ' + sna);
                if flux_dict:
                    for k,v in flux_dict[model_id][sna].items():
                        # record the data
                        data_tmp = {'experiment_id':experiment_id_I,
                                'model_id':model_id,
                                'sample_name_abbreviation':sna,
                                'rxn_id':k,
                                'flux_average':v['ave'],
                                'flux_stdev':v['stdev'],
                                'flux_lb':v['lb'], 
                                'flux_ub':v['ub'],
                                'flux_units':v['units'],
                                'used_':True,
                                'comment_':None}
                        data_O.append(data_tmp);
                        ##add data to the database
                        #row = [];
                        #row = data_stage02_isotopomer_measuredFluxes(
                        #    experiment_id_I,
                        #    model_id,
                        #    sna,
                        #    k,
                        #    v['ave'],
                        #    v['stdev'],
                        #    v['lb'], 
                        #    v['ub'],
                        #    v['units'],
                        #    True,
                        #    None);
                        #self.session.add(row);
                if ko_list:
                    for k in ko_list[model_id][sna]:
                        # record the data
                        data_tmp = {'experiment_id':experiment_id_I,
                                'model_id':model_id,
                                'sample_name_abbreviation':sna,
                                'rxn_id':k,
                                'flux_average':0.0,
                                'flux_stdev':0.0,
                                'flux_lb':0.0, 
                                'flux_ub':0.0,
                                'flux_units':'mmol*gDCW-1*hr-1',
                                'used_':True,
                                'comment_':None}
                        data_O.append(data_tmp);
                        ##add data to the database
                        #row = [];
                        #row = data_stage02_isotopomer_measuredFluxes(
                        #    experiment_id_I,
                        #    model_id,
                        #    sna,
                        #    k,
                        #    0.0,
                        #    0.0,
                        #    0.0, 
                        #    0.0,
                        #    'mmol*gDCW-1*hr-1',
                        #    True,
                        #    None);
                        #self.session.add(row);
        # add data to the DB
        self.add_data_stage02_isotopomer_measuredFluxes(data_O);
        #self.session.commit();
    def execute_makeMeasuredFluxes(self,experiment_id_I, metID2RxnID_I = {}, sample_name_abbreviations_I = [], met_ids_I = [],snaIsotopomer2snaPhysiology_I={},
                                   correct_EX_glc_LPAREN_e_RPAREN_I = True):
        '''Collect and flux data from data_stage01_physiology_ratesAverages for fluxomics simulation
        Input:
           metID2RxnID_I = e.g. {'glc-D':{'model_id':'140407_iDM2014','rxn_id':'EX_glc_LPAREN_e_RPAREN_'},
                                'ac':{'model_id':'140407_iDM2014','rxn_id':'EX_ac_LPAREN_e_RPAREN_'},
                                'succ':{'model_id':'140407_iDM2014','rxn_id':'EX_succ_LPAREN_e_RPAREN_'},
                                'lac-L':{'model_id':'140407_iDM2014','rxn_id':'EX_lac_DASH_L_LPAREN_e_RPAREN_'},
                                'biomass':{'model_id':'140407_iDM2014','rxn_id':'Ec_biomass_iJO1366_WT_53p95M'}};
           snaIsotopomer2snaPhysiology_I = {'OxicEvo04Ecoli13CGlc':'OxicEvo04EcoliGlc',
                                'OxicEvo04gndEcoli13CGlc':'OxicEvo04gndEcoliGlc',
                                'OxicEvo04pgiEcoli13CGlc':'OxicEvo04pgiEcoliGlc',
                                'OxicEvo04sdhCBEcoli13CGlc':'OxicEvo04sdhCBEcoliGlc',
                                'OxicEvo04tpiAEcoli13CGlc':'OxicEvo04tpiAEcoliGlc'}
        '''
        '''TODO:'''
        #   Need to implement a way to detect the direction of the reaction,
        #   and change direction of the rate accordingly

        data_O = [];
        # get sample names and sample name abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I;
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage02IosotopomerSimulation(experiment_id_I);
        for sna in sample_name_abbreviations:
            print('Collecting experimental fluxes for sample name abbreviation ' + sna);
            query_sna = sna;
            if snaIsotopomer2snaPhysiology_I: query_sna = snaIsotopomer2snaPhysiology_I[sna];
            # get met_ids
            if not met_ids_I:
                met_ids = [];
                met_ids = self.get_metID_experimentIDAndSampleNameAbbreviation_dataStage01PhysiologyRatesAverages(experiment_id_I,query_sna);
            else:
                met_ids = met_ids_I;
            if not(met_ids): continue #no component information was found
            for met in met_ids:
                print('Collecting experimental fluxes for metabolite ' + met);
                # get rateData
                slope_average, intercept_average, rate_average, rate_lb, rate_ub, rate_units, rate_var = None,None,None,None,None,None,None;
                slope_average, intercept_average, rate_average, rate_lb, rate_ub, rate_units, rate_var = self.get_rateData_experimentIDAndSampleNameAbbreviationAndMetID_dataStage01PhysiologyRatesAverages(experiment_id_I,query_sna,met);
                rate_stdev = sqrt(rate_var);
                model_id = metID2RxnID_I[met]['model_id'];
                rxn_id = metID2RxnID_I[met]['rxn_id'];
                # correct for glucose uptake
                if rxn_id == 'EX_glc_LPAREN_e_RPAREN_' and correct_EX_glc_LPAREN_e_RPAREN_I:
                    rate_lb_tmp,rate_ub_tmp = rate_lb,rate_ub;
                    rate_lb = min([abs(x) for x in [rate_lb_tmp,rate_ub_tmp]]);
                    rate_ub = max([abs(x) for x in [rate_lb_tmp,rate_ub_tmp]]);
                    rate_average = abs(rate_average);
                # record the data
                data_tmp = {'experiment_id':experiment_id_I,
                        'model_id':model_id,
                        'sample_name_abbreviation':sna,
                        'rxn_id':rxn_id,
                        'flux_average':rate_average,
                        'flux_stdev':rate_stdev,
                        'flux_lb':rate_lb, 
                        'flux_ub':rate_ub,
                        'flux_units':rate_units,
                        'used_':True,
                        'comment_':None}
                data_O.append(data_tmp);
                ##add data to the database
                #row = [];
                #row = data_stage02_isotopomer_measuredFluxes(
                #    experiment_id_I,
                #    model_id,
                #    sna,
                #    rxn_id,
                #    rate_average,
                #    rate_stdev,
                #    rate_lb, 
                #    rate_ub,
                #    rate_units,
                #    True,
                #    None);
                #self.session.add(row);
        #add data to the DB
        self.add_data_stage02_isotopomer_measuredFluxes(data_O);
        #self.session.commit();