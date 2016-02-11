from SBaaS_base.postgresql_orm_base import *
class data_stage02_isotopomer_fittedNetFluxes(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedNetFluxes'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedNetFluxes_id_seq'), primary_key=True)
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
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','rxn_id','simulation_dateAndTime','flux_units'),
            )

    def __init__(self,simulation_id_I,
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
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())
class data_stage02_isotopomer_fittedNetFluxStatistics(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedNetFluxStatistics'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedNetFluxStatistics_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    n_fluxes = Column(Integer)
    n_observableFluxes = Column(Integer)
    total_precision = Column(Float)
    total_observablePrecision = Column(Float)
    relative_nObservableFluxes = Column(Float);
    average_observableFluxPrecision = Column(Float);
    average_fluxPrecision = Column(Float); 
    flux_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','simulation_dateAndTime','flux_units'),
            )

    def __init__(self,simulation_id_I,
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