from SBaaS_base.postgresql_orm_base import *
class data_stage02_isotopomer_fittedFluxRatios(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedFluxRatios'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedFluxRatios_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    #experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #mapping_id = Column(String(100))
    #sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    ratio_id = Column(String(100))
    ratio_rxn_ids = Column(postgresql.ARRAY(String(100)))
    ratio = Column(Float);
    ratio_stdev = Column(Float);
    ratio_lb = Column(Float); # based on 95% CI
    ratio_ub = Column(Float);
    ratio_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','ratio_id','simulation_dateAndTime','ratio_units'),
            )

    def __init__(self,simulation_id_I,
        simulation_dateAndTime_I,
        #experiment_id_I,
        #model_id_I,
        #mapping_id_I,
        #sample_name_abbreviation_I,
        #time_point_I,
        ratio_id_I,
        ratio_rxn_ids_I,
        ratio_I,
        ratio_stdev_I,
        ratio_lb_I,
        ratio_ub_I,
        ratio_units_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        #self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.mapping_id=mapping_id_I
        #self.sample_name_abbreviation=sample_name_abbreviation_I
        #self.time_point=time_point_I
        self.ratio_id=ratio_id_I
        self.ratio_rxn_ids=ratio_rxn_ids_I
        self.ratio=ratio_I
        self.ratio_stdev=ratio_stdev_I
        self.ratio_lb=ratio_lb_I
        self.ratio_ub=ratio_ub_I
        self.ratio_units=ratio_units_I
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
        'ratio_id':self.ratio_id,
        'ratio_rxn_ids':self.ratio_rxn_ids,
        'ratio':self.ratio,
        'ratio_stdev':self.ratio_stdev,
        'ratio_lb':self.ratio_lb,
        'ratio_ub':self.ratio_ub,
        'ratio_units':self.ratio_units,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())