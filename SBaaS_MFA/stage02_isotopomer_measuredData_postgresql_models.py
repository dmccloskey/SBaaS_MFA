from SBaaS_base.postgresql_orm_base import *
class data_stage02_isotopomer_measuredFluxes(Base):
    __tablename__ = 'data_stage02_isotopomer_measuredFluxes'
    id = Column(Integer, Sequence('data_stage02_isotopomer_measuredFluxes_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    rxn_id = Column(String(100))
    flux_average = Column(Float);
    flux_stdev = Column(Float);
    flux_lb = Column(Float); # based on 95% CI
    flux_ub = Column(Float);
    flux_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            UniqueConstraint('experiment_id','model_id','sample_name_abbreviation','rxn_id','flux_units'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.experiment_id=data_dict_I['experiment_id'];
        self.comment_=data_dict_I['comment_'];
        self.flux_average=data_dict_I['flux_average'];
        self.flux_units=data_dict_I['flux_units'];
        self.used_=data_dict_I['used_'];
        self.flux_stdev=data_dict_I['flux_stdev'];
        self.flux_lb=data_dict_I['flux_lb'];
        self.flux_ub=data_dict_I['flux_ub'];
        self.rxn_id=data_dict_I['rxn_id'];
        self.sample_name_abbreviation=data_dict_I['sample_name_abbreviation'];
        self.model_id=data_dict_I['model_id'];

    def __set__row__(self,experiment_id_I,
            model_id_I,
            sample_name_abbreviation_I,
            #time_point_I,
            rxn_id_I,
            flux_average_I,
            flux_stdev_I,
            flux_lb_I,
            flux_ub_I,
            flux_units_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        #self.time_point=time_point_I
        self.rxn_id=rxn_id_I
        self.flux_average=flux_average_I
        self.flux_stdev=flux_stdev_I
        self.flux_lb=flux_lb_I
        self.flux_ub=flux_ub_I
        self.flux_units=flux_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                    'model_id':self.model_id,
                    'sample_name_abbreviation':self.sample_name_abbreviation,
                    #'time_point':self.time_point,
                    'rxn_id':self.rxn_id,
                    'flux_average':self.flux_average,
                    'flux_stdev':self.flux_stdev,
                    'flux_lb':self.flux_lb,
                    'flux_ub':self.flux_ub,
                    'flux_units':self.flux_units,
                    'used_':self.used_,
                    'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
    
class data_stage02_isotopomer_measuredPools(Base):
    __tablename__ = 'data_stage02_isotopomer_measuredPools'
    id = Column(Integer, Sequence('data_stage02_isotopomer_measuredPools_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    model_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    met_id = Column(String(50))
    # Time-course simulations only:
    pool_size = Column(Float) # 0 if steady-state
    concentration_average = Column(Float) #derived from experimentally measured values or estimations from simulations
    concentration_var = Column(Float) #derived from experimentally measured values or estimations from simulations
    concentration_lb = Column(Float) #derived from experimentally measured values or estimations from simulations
    concentration_ub = Column(Float) #derived from experimentally measured values or estimations from simulations
    concentration_units = Column(String(50))
    used_ = Column(Boolean)
    comment_ = Column(Text);
    __table_args__ = (
            UniqueConstraint('experiment_id','model_id','time_point','sample_name_abbreviation','met_id','concentration_units'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.concentration_var=data_dict_I['concentration_var'];
        self.concentration_units=data_dict_I['concentration_units'];
        self.used_=data_dict_I['used_'];
        self.comment_=data_dict_I['comment_'];
        self.concentration_ub=data_dict_I['concentration_ub'];
        self.concentration_lb=data_dict_I['concentration_lb'];
        self.concentration_average=data_dict_I['concentration_average'];
        self.pool_size=data_dict_I['pool_size'];
        self.met_id=data_dict_I['met_id'];
        self.time_point=data_dict_I['time_point'];
        self.sample_name_abbreviation=data_dict_I['sample_name_abbreviation'];
        self.model_id=data_dict_I['model_id'];
        self.experiment_id=data_dict_I['experiment_id'];

    def __set__row__(self,experiment_id_I,
            model_id_I,
            sample_name_abbreviation_I,
            time_point_I,
            met_id_I,
            pool_size_I,
            concentration_average_I,
            concentration_var_I,
            concentration_lb_I,
            concentration_ub_I,
            concentration_units_I,
            used__I,
            comment__I):
        self.experiment_id=experiment_id_I
        self.model_id=model_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.met_id=met_id_I
        self.pool_size=pool_size_I
        self.concentration_average=concentration_average_I
        self.concentration_var=concentration_var_I
        self.concentration_lb=concentration_lb_I
        self.concentration_ub=concentration_ub_I
        self.concentration_units=concentration_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                    'model_id':self.model_id,
                    'sample_name_abbreviation':self.sample_name_abbreviation,
                    #'time_point':self.time_point,
                    'met_id':self.met_id,
                    'pool_size':self.pool_size,
                    'concentration_average':self.concentration_average,
                    'concentration_var':self.concentration_var,
                    'concentration_lb':self.concentration_lb,
                    'concentration_ub':self.concentration_ub,
                    'concentration_units':self.concentration_units,
                    'used_':self.used_,
                    'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())

class data_stage02_isotopomer_measuredFragments(Base):
    __tablename__ = 'data_stage02_isotopomer_measuredFragments'
    id = Column(Integer, Sequence('data_stage02_isotopomer_measuredFragments_id_seq'), primary_key=True)
    experiment_id = Column(String(50))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    met_id = Column(String(100))
    fragment_id = Column(String(100))
    fragment_formula = Column(String(500))
    #fragment_mass = Column(Integer)
    #n_replicates = Column(Integer)
    intensity_normalized_average = Column(postgresql.ARRAY(Float))
    intensity_normalized_cv = Column(postgresql.ARRAY(Float))
    intensity_normalized_stdev = Column(postgresql.ARRAY(Float))
    intensity_normalized_units = Column(String(20))
    scan_type = Column(String(50));
    met_elements = Column(postgresql.ARRAY(String(3))) # the elements that are tracked (e.g. C,C,C)
    met_atompositions = Column(postgresql.ARRAY(Integer)) #the atoms positions that are tracked (e.g. 1,2,3) 
    used_ = Column(Boolean);
    comment_ = Column(Text);
    __table_args__ = (
            UniqueConstraint('experiment_id','sample_name_abbreviation','time_point','fragment_id','intensity_normalized_units','scan_type'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.intensity_normalized_stdev=data_dict_I['intensity_normalized_stdev'];
        self.intensity_normalized_units=data_dict_I['intensity_normalized_units'];
        self.scan_type=data_dict_I['scan_type'];
        self.met_atompositions=data_dict_I['met_atompositions'];
        self.met_elements=data_dict_I['met_elements'];
        self.used_=data_dict_I['used_'];
        self.comment_=data_dict_I['comment_'];
        self.experiment_id=data_dict_I['experiment_id'];
        self.sample_name_abbreviation=data_dict_I['sample_name_abbreviation'];
        self.time_point=data_dict_I['time_point'];
        self.met_id=data_dict_I['met_id'];
        self.fragment_id=data_dict_I['fragment_id'];
        self.fragment_formula=data_dict_I['fragment_formula'];
        self.intensity_normalized_average=data_dict_I['intensity_normalized_average'];
        self.intensity_normalized_cv=data_dict_I['intensity_normalized_cv'];

    def __set__row__(self, experiment_id_I, sample_name_abbreviation_I, 
                 time_point_I, met_id_I,fragment_id_I,
                    fragment_formula_I,
                    #fragment_mass_I,
                    #n_replicates_I,
                    intensity_normalized_average_I, intensity_normalized_cv_I,
                    intensity_normalized_stdev_I,
                    intensity_normalized_units_I, scan_type_I,
                    met_elements_I,
                    met_atompositions_I,used__I,comment__I):
        self.experiment_id = experiment_id_I;
        self.sample_name_abbreviation = sample_name_abbreviation_I;
        self.time_point = time_point_I;
        self.met_id = met_id_I;
        self.fragment_id = fragment_id_I;
        self.fragment_formula = fragment_formula_I;
        #self.fragment_mass = fragment_mass_I;
        #self.n_replicates = n_replicates_I;
        self.intensity_normalized_average = intensity_normalized_average_I;
        self.intensity_normalized_cv = intensity_normalized_cv_I;
        self.intensity_normalized_stdev = intensity_normalized_stdev_I;
        self.intensity_normalized_units = intensity_normalized_units_I;
        self.scan_type = scan_type_I;
        self.met_elements=met_elements_I;
        self.met_atompositions=met_atompositions_I;
        self.used_=used__I;
        self.comment_=comment__I;

    def __repr__dict__(self):
        return {'id':self.id,
                'experiment_id':self.experiment_id,
                'sample_name_abbreviation':self.sample_name_abbreviation,
                'time_point':self.time_point,
                'met_id':self.met_id,
                'fragment_id':self.fragment_id,
                'fragment_formula':self.fragment_formula,
                'intensity_normalized_average':self.intensity_normalized_average,
                'intensity_normalized_cv':self.intensity_normalized_cv,
                'intensity_normalized_stdev':self.intensity_normalized_stdev,
                'intensity_normalized_units':self.intensity_normalized_units,
                'scan_type':self.scan_type,
                'met_elements':self.met_elements,
                'met_atompositions':self.met_atompositions,
                'used_':self.used_,
                'comment_':self.comment_};
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())