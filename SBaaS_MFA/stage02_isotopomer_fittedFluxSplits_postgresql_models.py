from SBaaS_base.postgresql_orm_base import *
class data_stage02_isotopomer_fittedFluxSplits(Base):
    __tablename__ = 'data_stage02_isotopomer_fittedFluxSplits'
    id = Column(Integer, Sequence('data_stage02_isotopomer_fittedFluxSplits_id_seq'), primary_key=True)
    simulation_id = Column(String(500))
    simulation_dateAndTime = Column(DateTime);
    #experiment_id = Column(String(50))
    #model_id = Column(String(50))
    #mapping_id = Column(String(100))
    #sample_name_abbreviation = Column(String(100))
    #time_point = Column(String(10))
    split_id = Column(String(100))
    split_rxn_id = Column(String(100))
    split = Column(Float);
    split_stdev = Column(Float);
    split_lb = Column(Float); # based on 95% CI
    split_ub = Column(Float);
    split_units = Column(String(50));
    used_ = Column(Boolean);
    comment_ = Column(Text);

    __table_args__ = (
            #ForeignKeyConstraint(['simulation_id'], ['data_stage02_isotopomer_simulation.simulation_id']),
            UniqueConstraint('simulation_id','split_id','split_rxn_id','simulation_dateAndTime','split_units'),
            )
    
    def __init__(self, 
                row_dict_I,
                ):
        self.split_id=data_dict_I['split_id'];
        self.simulation_dateAndTime=data_dict_I['simulation_dateAndTime'];
        self.simulation_id=data_dict_I['simulation_id'];
        self.comment_=data_dict_I['comment_'];
        self.used_=data_dict_I['used_'];
        self.split_units=data_dict_I['split_units'];
        self.split_ub=data_dict_I['split_ub'];
        self.split_lb=data_dict_I['split_lb'];
        self.split_stdev=data_dict_I['split_stdev'];
        self.split=data_dict_I['split'];
        self.split_rxn_id=data_dict_I['split_rxn_id'];

    def __set__row__(self,simulation_id_I,
        simulation_dateAndTime_I,
        #experiment_id_I,
        #model_id_I,
        #mapping_id_I,
        #sample_name_abbreviation_I,
        #time_point_I,
        split_id_I,
        split_rxn_id_I,
        split_I,
        split_stdev_I,
        split_lb_I,
        split_ub_I,
        split_units_I,
        used__I,
        comment__I):
        self.simulation_id=simulation_id_I
        self.simulation_dateAndTime=simulation_dateAndTime_I
        #self.experiment_id=experiment_id_I
        #self.model_id=model_id_I
        #self.mapping_id=mapping_id_I
        #self.sample_name_abbreviation=sample_name_abbreviation_I
        #self.time_point=time_point_I
        self.split_id=split_id_I
        self.split_rxn_id=split_rxn_id_I
        self.split=split_I
        self.split_stdev=split_stdev_I
        self.split_lb=split_lb_I
        self.split_ub=split_ub_I
        self.split_units=split_units_I
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
        'split_id':self.split_id,
        'split_rxn_id':self.split_rxn_id,
        'split':self.split,
        'split_stdev':self.split_stdev,
        'split_lb':self.split_lb,
        'split_ub':self.split_ub,
        'split_units':self.split_units,
        'used_':self.used_,
        'comment_':self.comment_}
    
    def __repr__json__(self):
        return json.dumps(self.__repr__dict__())