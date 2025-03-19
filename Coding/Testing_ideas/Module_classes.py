class sequence:
    def __init__(self, study_name, random_seed, date_created, fraction_time, assay_list=None, plates_per_assay, samples_per_plate, assay_sweep_mode, final_well_position, created_by):
        self.study=study_name
        self.seed=random_seed
        self.date=date_created
        self.ft=fraction_time
        self.assay_list=assay_list
        self.ppa=plates_per_assay
        self.spp=samples_per_plate
        self.snake=assay_sweep_mode
        self.terminus=final_well_position
        self.creator=created_by
