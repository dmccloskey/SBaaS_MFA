from SBaaS_base.postgresql_orm_base import *
class data_stage02_isotopomer_fittedFluxes(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedFluxes'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedFluxes_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    #experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #mapping_id = Column(String(100))
    #sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    rxn_id = Column(String(100))
    flux = Column(Float);
    flux_stdev = Column(Float);
    flux_lb = Column(Float); # based on 95% CI
    flux_ub = Column(Float);
    flux_units = Column(String(50));
    fit_alf = Column(Float);
    fit_chi2s = Column(postgresql.ARRAY(Float));
    fit_cor = Column(postgresql.ARRAY(Float));
    fit_cov = Column(postgresql.ARRAY(Float));
    free = Column(Boolean);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','rxn_id','simulation_dateAndTime'),
            )

    def __init__(self, 
                row_dict_I,
                ):
        self.fit_cov=row_dict_I['fit_cov'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.free=row_dict_I['free'];
        self.simulation_id=row_dict_I['simulation_id'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.rxn_id=row_dict_I['rxn_id'];
        self.flux=row_dict_I['flux'];
        self.flux_stdev=row_dict_I['flux_stdev'];
        self.flux_lb=row_dict_I['flux_lb'];
        self.flux_ub=row_dict_I['flux_ub'];
        self.flux_units=row_dict_I['flux_units'];
        self.fit_alf=row_dict_I['fit_alf'];
        self.fit_chi2s=row_dict_I['fit_chi2s'];
        self.fit_cor=row_dict_I['fit_cor'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        #experiment_id_I,
        #model_id_I,
        #mapping_id_I,
        #sample_name_abbreviation_I,
        #time_point_I,
        rxn_id_I,
        flux_I,
        flux_stdev_I,
        flux_lb_I,
        flux_ub_I,
        flux_units_I,
        fit_alf_I,
        fit_chi2s_I,
        fit_cor_I,
        fit_cov_I,
        free_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        #self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.mapping_id=mapping_id_I
        #self.sample_name_abbreviation=sample_name_abbreviation_I
        #self.time_point=time_point_I
        self.rxn_id=rxn_id_I
        self.flux=flux_I
        self.flux_stdev=flux_stdev_I
        self.flux_lb=flux_lb_I
        self.flux_ub=flux_ub_I
        self.flux_units=flux_units_I
        self.fit_alf=fit_alf_I
        self.fit_chi2s=fit_chi2s_I
        self.fit_cor=fit_cor_I
        self.fit_cov=fit_cov_I
        self.free=free_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        #'experiment_id':self.experiment_id,
        #'model_id':self.model_id,
        #'mapping_id':self.mapping_id,
        #'sample_name_abbreviation':self.sample_name_abbreviation,
        #'time_point':self.time_point,
        'rxn_id':self.rxn_id,
        'flux':self.flux,
        'flux_stdev':self.flux_stdev,
        'flux_lb':self.flux_lb,
        'flux_ub':self.flux_ub,
        'flux_units':self.flux_units,
        'fit_alf':self.fit_alf,
        'fit_chi2s':self.fit_chi2s,
        'fit_cor':self.fit_cor,
        'fit_cov':self.fit_cov,
        'free':self.free,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_fittedFragments(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedFragments'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedFragments_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    experiment_id = Column(String(50));
    #model_id = Column(String(50));
    #mapping_id = Column(String(100));
    sample_name_abbreviation = Column(String(100));
    time_point = Column(String(10));
    fragment_id = Column(String(100));
    #fragment_formula = Column(String(500));
    fragment_mass = Column(Integer);
    fit_val = Column(Float);
    fit_stdev = Column(Float);
    fit_units = Column(String(50));
    fit_alf = Column(Float);
    fit_cor = Column(postgresql.ARRAY(Float));
    fit_cov = Column(postgresql.ARRAY(Float));
    free = Column(Boolean);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','time_point','fragment_id','fragment_mass','simulation_dateAndTime'),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.simulation_id=row_dict_I['simulation_id'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.free=row_dict_I['free'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.fit_cov=row_dict_I['fit_cov'];
        self.fit_cor=row_dict_I['fit_cor'];
        self.fit_alf=row_dict_I['fit_alf'];
        self.fit_units=row_dict_I['fit_units'];
        self.fit_stdev=row_dict_I['fit_stdev'];
        self.fit_val=row_dict_I['fit_val'];
        self.fragment_mass=row_dict_I['fragment_mass'];
        self.fragment_id=row_dict_I['fragment_id'];
        self.time_point=row_dict_I['time_point'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.experiment_id=row_dict_I['experiment_id'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        experiment_id_I,
        #model_id_I,
        #mapping_id_I,
        sample_name_abbreviation_I,
        time_point_I,
        fragment_id_I,
        #fragment_formula_I,
        fragment_mass_I,
        fit_val_I,
        fit_stdev_I,
        fit_units_I,
        fit_alf_I,
        fit_cor_I,
        fit_cov_I,
        free_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.mapping_id=mapping_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.fragment_id=fragment_id_I
        #self.fragment_formula=fragment_formula_I
        self.fragment_mass=fragment_mass_I
        self.fit_val=fit_val_I
        self.fit_stdev=fit_stdev_I
        self.fit_units=fit_units_I
        self.fit_alf=fit_alf_I
        self.fit_cor=fit_cor_I
        self.fit_cov=fit_cov_I
        self.free=free_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        'experiment_id':self.experiment_id,
        #'model_id':self.model_id,
        #'mapping_id':self.mapping_id,
        'sample_name_abbreviation':self.sample_name_abbreviation,
        'time_point':self.time_point,
        'fragment_id':self.fragment_id,
        #'fragment_formula':self.fragment_formula,
        'fragment_mass':self.fragment_mass,
        'fit_val':self.fit_val,
        'fit_stdev':self.fit_stdev,
        'fit_units':self.fit_units,
        'fit_alf':self.fit_alf,
        'fit_chi2s':self.fit_chi2s,
        'fit_cor':self.fit_cor,
        'fit_cov':self.fit_cov,
        'free':self.free,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_fittedData(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedData'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedData_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    #experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #mapping_id = Column(String(100))
    #sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    fitted_echi2 = Column(postgresql.ARRAY(Float));
    fitted_alf = Column(Float);
    fitted_chi2 = Column(Float);
    fitted_dof = Column(Integer);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','simulation_dateAndTime'),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.fitted_alf=row_dict_I['fitted_alf'];
        self.fitted_chi2=row_dict_I['fitted_chi2'];
        self.fitted_dof=row_dict_I['fitted_dof'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.simulation_id=row_dict_I['simulation_id'];
        self.fitted_echi2=row_dict_I['fitted_echi2'];

    def __set__row__(self,
        simulation_id_I,
        simulation_dateAndTime_I,
        #experiment_id_I,
        #model_id_I,
        #mapping_id_I,
        #sample_name_abbreviation_I,
        #time_point_I,
        fitted_echi2_I,
        fitted_alf_I,
        fitted_chi2_I,
        fitted_dof_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        #self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.mapping_id=mapping_id_I
        #self.sample_name_abbreviation=sample_name_abbreviation_I
        #self.time_point=time_point_I
        self.fitted_echi2=fitted_echi2_I
        self.fitted_alf=fitted_alf_I
        self.fitted_chi2=fitted_chi2_I
        self.fitted_dof=fitted_dof_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        #'experiment_id':self.experiment_id,
        #'model_id':self.model_id,
        #'mapping_id':self.mapping_id,
        #'sample_name_abbreviation':self.sample_name_abbreviation,
        #'time_point':self.time_point,
        'fitted_echi2':self.fitted_echi2,
        'fitted_alf':self.fitted_alf,
        'fitted_chi2':self.fitted_chi2,
        'fitted_dof':self.fitted_dof,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_fittedMeasuredFluxes(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedMeasuredFluxes'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedMeasuredFluxes_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #mapping_id = Column(String(100))
    sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    rxn_id = Column(String(100))
    fitted_sres = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','rxn_id','simulation_dateAndTime'),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.experiment_id=row_dict_I['experiment_id'];
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.fitted_sres=row_dict_I['fitted_sres'];
        self.rxn_id=row_dict_I['rxn_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.simulation_id=row_dict_I['simulation_id'];

    def __set__row__(self,
        simulation_id_I,
        simulation_dateAndTime_I,
        experiment_id_I,
        #model_id_I,
        #mapping_id_I,
        sample_name_abbreviation_I,
        #time_point_I,
        rxn_id_I,
        fitted_sres_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.mapping_id=mapping_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        #self.time_point=time_point_I
        self.rxn_id=rxn_id_I
        self.fitted_sres=fitted_sres_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        'experiment_id':self.experiment_id,
        #'model_id':self.model_id,
        #'mapping_id':self.mapping_id,
        'sample_name_abbreviation':self.sample_name_abbreviation,
        #'time_point':self.time_point,
        'rxn_id':self.rxn_id,
        'fitted_sres':self.fitted_sres,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_fittedMeasuredFragments(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedMeasuredFragments'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedMeasuredFragments_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #mapping_id = Column(String(100))
    sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    #met_id = Column(String(100))
    fragment_id = Column(String(100))
    #fragment_formula = Column(String(500))
    fitted_sres = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','fragment_id','simulation_dateAndTime'),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.comment_=row_dict_I['comment_'];
        self.used_=row_dict_I['used_'];
        self.fitted_sres=row_dict_I['fitted_sres'];
        self.fragment_id=row_dict_I['fragment_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.simulation_id=row_dict_I['simulation_id'];

    def __set__row__(self,simulation_id_I,
    simulation_dateAndTime_I,
    experiment_id_I,
    #model_id_I,
    #mapping_id_I,
    sample_name_abbreviation_I,
    #time_point_I,
    #met_id_I,
    fragment_id_I,
    #fragment_formula_I,
    fitted_sres_I,
    used__I,
    comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.mapping_id=mapping_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        #self.time_point=time_point_I
        #self.met_id=met_id_I
        self.fragment_id=fragment_id_I
        #self.fragment_formula=fragment_formula_I
        self.fitted_sres=fitted_sres_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        'experiment_id':self.experiment_id,
        #'model_id':self.model_id,
        #'mapping_id':self.mapping_id,
        'sample_name_abbreviation':self.sample_name_abbreviation,
        #'time_point':self.time_point,
        #'met_id':self.met_id,
        'fragment_id':self.fragment_id,
        #'fragment_formula':self.fragment_formula,
        'fitted_sres':self.fitted_sres,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_fittedMeasuredFluxResiduals(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedMeasuredFluxResiduals'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedMeasuredFluxResiduals_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #mapping_id = Column(String(100))
    sample_name_abbreviation = Column(String(100))
    time_point = Column(String(10))
    rxn_id = Column(String(100))
    res_data = Column(Float);
    res_esens = Column(Float);
    res_fit = Column(Float);
    res_msens = Column(Float);
    res_peak = Column(String(100));
    res_stdev = Column(Float);
    res_val = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','rxn_id','time_point','simulation_dateAndTime'),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.res_stdev=row_dict_I['res_stdev'];
        self.res_peak=row_dict_I['res_peak'];
        self.res_msens=row_dict_I['res_msens'];
        self.res_fit=row_dict_I['res_fit'];
        self.res_esens=row_dict_I['res_esens'];
        self.used_=row_dict_I['used_'];
        self.simulation_id=row_dict_I['simulation_id'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.time_point=row_dict_I['time_point'];
        self.rxn_id=row_dict_I['rxn_id'];
        self.res_data=row_dict_I['res_data'];
        self.res_val=row_dict_I['res_val'];
        self.comment_=row_dict_I['comment_'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        experiment_id_I,
        #model_id_I,
        #mapping_id_I,
        sample_name_abbreviation_I,
        time_point_I,
        rxn_id_I,
        res_data_I,
        res_esens_I,
        res_fit_I,
        res_msens_I,
        res_peak_I,
        res_stdev_I,
        res_val_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.mapping_id=mapping_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.rxn_id=rxn_id_I
        self.res_data=res_data_I
        self.res_esens=res_esens_I
        self.res_fit=res_fit_I
        self.res_msens=res_msens_I
        self.res_peak=res_peak_I
        self.res_stdev=res_stdev_I
        self.res_val=res_val_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        'experiment_id':self.experiment_id,
        #'model_id':self.model_id,
        #'mapping_id':self.mapping_id,
        'sample_name_abbreviation':self.sample_name_abbreviation,
        'time_point':self.time_point,
        'rxn_id':self.rxn_id,
        'res_data':self.res_data,
        'res_esens':self.res_esens,
        'res_fit':self.res_fit,
        'res_msens':self.res_msens,
        'res_peak':self.res_peak,
        'res_stdev':self.res_stdev,
        'res_val':self.res_val,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_fittedMeasuredFragmentResiduals(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedMeasuredFragmentResiduals'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedMeasuredFragmentResiduals_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    experiment_id = Column(String(50));
    #model_id = Column(String(50));
    #mapping_id = Column(String(100));
    sample_name_abbreviation = Column(String(100));
    time_point = Column(String(10));
    fragment_id = Column(String(100));
    #fragment_formula = Column(String(500));
    fragment_mass = Column(Integer);
    res_data = Column(Float);
    res_esens = Column(Float);
    res_fit = Column(Float);
    res_msens = Column(Float);
    res_peak = Column(String(100));
    res_stdev = Column(Float);
    res_val = Column(Float);
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','time_point','fragment_id','fragment_mass','simulation_dateAndTime'),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.res_val=row_dict_I['res_val'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];
        self.simulation_id=row_dict_I['simulation_id'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.experiment_id=row_dict_I['experiment_id'];
        self.sample_name_abbreviation=row_dict_I['sample_name_abbreviation'];
        self.time_point=row_dict_I['time_point'];
        self.fragment_id=row_dict_I['fragment_id'];
        self.fragment_mass=row_dict_I['fragment_mass'];
        self.res_data=row_dict_I['res_data'];
        self.res_esens=row_dict_I['res_esens'];
        self.res_fit=row_dict_I['res_fit'];
        self.res_msens=row_dict_I['res_msens'];
        self.res_peak=row_dict_I['res_peak'];
        self.res_stdev=row_dict_I['res_stdev'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        experiment_id_I,
        #model_id_I,
        #mapping_id_I,
        sample_name_abbreviation_I,
        time_point_I,
        fragment_id_I,
        #fragment_formula_I,
        fragment_mass_I,
        res_data_I,
        res_esens_I,
        res_fit_I,
        res_msens_I,
        res_peak_I,
        res_stdev_I,
        res_val_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.mapping_id=mapping_id_I
        self.sample_name_abbreviation=sample_name_abbreviation_I
        self.time_point=time_point_I
        self.fragment_id=fragment_id_I
        #self.fragment_formula=fragment_formula_I
        self.fragment_mass=fragment_mass_I
        self.res_data=res_data_I
        self.res_esens=res_esens_I
        self.res_fit=res_fit_I
        self.res_msens=res_msens_I
        self.res_peak=res_peak_I
        self.res_stdev=res_stdev_I
        self.res_val=res_val_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        'experiment_id':self.experiment_id,
        #'model_id':self.model_id,
        #'mapping_id':self.mapping_id,
        'sample_name_abbreviation':self.sample_name_abbreviation,
        'time_point':self.time_point,
        'fragment_id':self.fragment_id,
        #'fragment_formula':self.fragment_formula,
        'fragment_mass':self.fragment_mass,
        'res_data':self.res_data,
        'res_esens':self.res_esens,
        'res_fit':self.res_fit,
        'res_msens':self.res_msens,
        'res_peak':self.res_peak,
        'res_stdev':self.res_stdev,
        'res_val':self.res_val,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_fittedFluxStatistics(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedFluxStatistics'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedFluxStatistics_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    n_fluxes = Column(Integer)
    n_observableFluxes = Column(Integer)
    total_precision = Column(Float)
    total_observablePrecision = Column(Float)
    relative_nObservableFluxes = Column(Float)
    average_observableFluxPrecision = Column(Float);
    average_fluxPrecision = Column(Float); 
    flux_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','simulation_dateAndTime','flux_units'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.total_precision=row_dict_I['total_precision'];
        self.relative_nObservableFluxes=row_dict_I['relative_nObservableFluxes'];
        self.average_observableFluxPrecision=row_dict_I['average_observableFluxPrecision'];
        self.average_fluxPrecision=row_dict_I['average_fluxPrecision'];
        self.flux_units=row_dict_I['flux_units'];
        self.used_=row_dict_I['used_'];
        self.comment_=row_dict_I['comment_'];
        self.simulation_id=row_dict_I['simulation_id'];
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.n_fluxes=row_dict_I['n_fluxes'];
        self.n_observableFluxes=row_dict_I['n_observableFluxes'];
        self.total_observablePrecision=row_dict_I['total_observablePrecision'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        n_fluxes_I,
        n_observableFluxes_I,
        total_precision_I,
        total_observablePrecision_I,
        relative_nObservableFluxes_I,
        average_observableFluxPrecision_I,
        average_fluxPrecision_I,
        flux_units_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        self.n_fluxes=n_fluxes_I
        self.n_observableFluxes=n_observableFluxes_I
        self.total_precision=total_precision_I
        self.total_observablePrecision=total_observablePrecision_I
        self.relative_nObservableFluxes=relative_nObservableFluxes_I
        self.average_observableFluxPrecision=average_observableFluxPrecision_I
        self.average_fluxPrecision=average_fluxPrecision_I
        self.flux_units=flux_units_I
        self.used_=used__I
        self.comment_=comment__I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
        'simulation_dateAndTime':self.simulation_dateAndTime,
        'n_fluxes':self.n_fluxes,
        'n_observableFluxes':self.n_observableFluxes,
        'total_precision':self.total_precision,
        'total_observablePrecision':self.total_observablePrecision,
        'relative_nObservableFluxes':self.relative_nObservableFluxes,
        'average_observableFluxPrecision':self.average_observableFluxPrecision,
        'average_fluxPrecision':self.average_fluxPrecision,
        'flux_units':self.flux_units,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_simulationParameters(Base):
    __tablename__ = 'data_stage02_isotopomer_simulationParameters'
    id = Column(Integer, Sequence('data_stage02_isotopomer_simulationParameters_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    original_filename=Column(Text); #TODO add in new column
    cont_alpha = Column(Float);
    cont_reltol = Column(Float);
    cont_steps = Column(Float);
    fit_nudge = Column(Float);
    fit_reinit = Column(Boolean);
    fit_reltol = Column(Float);
    fit_starts = Column(Float);
    fit_tau = Column(Float);
    hpc_mcr = Column(String(50));
    hpc_on = Column(Boolean);
    hpc_serve = Column(String(50));
    int_maxstep = Column(Float);
    int_reltol = Column(Float);
    int_senstol = Column(Float);
    int_timeout = Column(Float);
    int_tspan = Column(Float);
    ms_correct = Column(Boolean);
    oed_crit = Column(String(50))
    oed_reinit = Column(Boolean);
    oed_tolf = Column(Float);
    oed_tolx = Column(Float);
    sim_more = Column(Boolean);
    sim_na = Column(Boolean);
    sim_sens = Column(Boolean);
    sim_ss = Column(Boolean);
    sim_tunit = Column(String(50));

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','simulation_dateAndTime'),
            )
    def __init__(self, 
                row_dict_I,
                ):
        self.simulation_dateAndTime=row_dict_I['simulation_dateAndTime'];
        self.sim_tunit=row_dict_I['sim_tunit'];
        self.original_filename=row_dict_I['original_filename']
        self.sim_ss=row_dict_I['sim_ss'];
        self.sim_sens=row_dict_I['sim_sens'];
        self.sim_na=row_dict_I['sim_na'];
        self.sim_more=row_dict_I['sim_more'];
        self.oed_tolx=row_dict_I['oed_tolx'];
        self.oed_tolf=row_dict_I['oed_tolf'];
        self.oed_reinit=row_dict_I['oed_reinit'];
        self.oed_crit=row_dict_I['oed_crit'];
        self.ms_correct=row_dict_I['ms_correct'];
        self.int_tspan=row_dict_I['int_tspan'];
        self.int_timeout=row_dict_I['int_timeout'];
        self.int_senstol=row_dict_I['int_senstol'];
        self.int_reltol=row_dict_I['int_reltol'];
        self.int_maxstep=row_dict_I['int_maxstep'];
        self.hpc_serve=row_dict_I['hpc_serve'];
        self.hpc_on=row_dict_I['hpc_on'];
        self.hpc_mcr=row_dict_I['hpc_mcr'];
        self.fit_tau=row_dict_I['fit_tau'];
        self.fit_starts=row_dict_I['fit_starts'];
        self.fit_reltol=row_dict_I['fit_reltol'];
        self.fit_reinit=row_dict_I['fit_reinit'];
        self.fit_nudge=row_dict_I['fit_nudge'];
        self.cont_steps=row_dict_I['cont_steps'];
        self.cont_reltol=row_dict_I['cont_reltol'];
        self.cont_alpha=row_dict_I['cont_alpha'];
        self.simulation_id=row_dict_I['simulation_id'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        original_filename_I,
        cont_alpha_I,
        cont_reltol_I,
        cont_steps_I,
        fit_nudge_I,
        fit_reinit_I,
        fit_reltol_I,
        fit_starts_I,
        fit_tau_I,
        hpc_mcr_I,
        hpc_on_I,
        hpc_serve_I,
        int_maxstep_I,
        int_reltol_I,
        int_senstol_I,
        int_timeout_I,
        int_tspan_I,
        ms_correct_I,
        oed_crit_I,
        oed_reinit_I,
        oed_tolf_I,
        oed_tolx_I,
        sim_more_I,
        sim_na_I,
        sim_sens_I,
        sim_ss_I,
        sim_tunit_I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        self.original_filename=original_filename_I;
        self.cont_alpha=cont_alpha_I
        self.cont_reltol=cont_reltol_I
        self.cont_steps=cont_steps_I
        self.fit_nudge=fit_nudge_I
        self.fit_reinit=fit_reinit_I
        self.fit_reltol=fit_reltol_I
        self.fit_starts=fit_starts_I
        self.fit_tau=fit_tau_I
        self.hpc_mcr=hpc_mcr_I
        self.hpc_on=hpc_on_I
        self.hpc_serve=hpc_serve_I
        self.int_maxstep=int_maxstep_I
        self.int_reltol=int_reltol_I
        self.int_senstol=int_senstol_I
        self.int_timeout=int_timeout_I
        self.int_tspan=int_tspan_I
        self.ms_correct=ms_correct_I
        self.oed_crit=oed_crit_I
        self.oed_reinit=oed_reinit_I
        self.oed_tolf=oed_tolf_I
        self.oed_tolx=oed_tolx_I
        self.sim_more=sim_more_I
        self.sim_na=sim_na_I
        self.sim_sens=sim_sens_I
        self.sim_ss=sim_ss_I
        self.sim_tunit=sim_tunit_I

    def __repr__dict__(self):
        return {'id':self.id,
                'simulation_id':self.simulation_id,
            'simulation_dateAndTime':self.simulation_dateAndTime,
            'original_filename':self.original_filename,
            'cont_alpha':self.cont_alpha,
            'cont_reltol':self.cont_reltol,
            'cont_steps':self.cont_steps,
            'fit_nudge':self.fit_nudge,
            'fit_reinit':self.fit_reinit,
            'fit_reltol':self.fit_reltol,
            'fit_starts':self.fit_starts,
            'fit_tau':self.fit_tau,
            'hpc_mcr':self.hpc_mcr,
            'hpc_on':self.hpc_on,
            'hpc_serve':self.hpc_serve,
            'int_maxstep':self.int_maxstep,
            'int_reltol':self.int_reltol,
            'int_senstol':self.int_senstol,
            'int_timeout':self.int_timeout,
            'int_tspan':self.int_tspan,
            'ms_correct':self.ms_correct,
            'oed_crit':self.oed_crit,
            'oed_reinit':self.oed_reinit,
            'oed_tolf':self.oed_tolf,
            'oed_tolx':self.oed_tolx,
            'sim_more':self.sim_more,
            'sim_na':self.sim_na,
            'sim_sens':self.sim_sens,
            'sim_ss':self.sim_ss,
            'sim_tunit':self.sim_tunit}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())