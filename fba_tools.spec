/*
A KBase module: fba_tools
This module contains the implementation for the primary methods in KBase for metabolic model reconstruction, gapfilling, and analysis
*/

module fba_tools {
    /*
        A binary boolean
    */
    typedef int bool;
    /*
        A string representing a Genome id.
    */
    typedef string genome_id;
    /*
        A string representing a Media id.
    */
    typedef string media_id;
    /*
        A string representing a NewModelTemplate id.
    */
    typedef string template_id;
    /*
        A string representing a FBAModel id.
    */
    typedef string fbamodel_id;
    /*
        A string representing a protein comparison id.
    */
    typedef string proteincomparison_id;
    /*
        A string representing a FBA id.
    */
    typedef string fba_id;
    /*
        A string representing a FBAPathwayAnalysis id.
    */
    typedef string fbapathwayanalysis_id;
    /*
        A string representing a FBA comparison id.
    */
    typedef string fbacomparison_id;
    /*
        A string representing a phenotype set id.
    */
    typedef string phenotypeset_id;
    /*
        A string representing a phenotype simulation id.
    */
    typedef string phenotypesim_id;
	 /*
        A string representing an expression matrix id.
    */
    typedef string expseries_id;
    /*
        A string representing a reaction id.
    */
    typedef string reaction_id;
    /*
        A string representing a feature id.
    */
    typedef string feature_id;
    /*
        A string representing a compound id.
    */
    typedef string compound_id;
    /*
        A string representing a workspace name.
    */
    typedef string workspace_name;
	/* 
        The workspace ID for a FBAModel data object.
        @id ws KBaseFBA.FBAModel
    */
    typedef string ws_fbamodel_id;
    /* 
        The workspace ID for a FBA data object.
        @id ws KBaseFBA.FBA
    */
    typedef string ws_fba_id;
    /* 
        The workspace ID for a FBA data object.
        @id ws KBaseFBA.FBA
    */
    typedef string ws_fbacomparison_id;
	/* 
        The workspace ID for a phenotype set simulation object.
        @id ws KBasePhenotypes.PhenotypeSimulationSet
    */
	typedef string ws_phenotypesim_id;
	/* 
        The workspace ID for a FBA pathway analysis object
        @id ws KBaseFBA.FBAPathwayAnalysis
    */
	typedef string ws_fbapathwayanalysis_id;
	/* 
        The workspace ID for a Report object
        @id ws KBaseReport.Report
    */
	typedef string ws_report_id;


    typedef structure {
		genome_id genome_id;
		workspace_name genome_workspace;
		media_id media_id;
		workspace_name media_workspace;
		fbamodel_id fbamodel_output_id;
		workspace_name workspace;
		template_id template_id;
		workspace_name template_workspace;
		bool coremodel;
		bool gapfill_model;
		bool thermodynamic_constraints;
		bool comprehensive_gapfill;
		
		list<string> custom_bound_list;
		list<compound_id> media_supplement_list;
		
		expseries_id expseries_id;
		workspace_name expseries_workspace;
		string expression_condition;
		float exp_threshold_percentile;
		float exp_threshold_margin;
		float activation_coefficient;
		float omega;
		float objective_fraction;
		float minimum_target_flux;
		int number_of_solutions;
    } BuildMetabolicModelParams;
    
    typedef structure {
        ws_fbamodel_id new_fbamodel_ref;
        ws_fba_id new_fba_ref;
        int number_gapfilled_reactions;
        int number_removed_biomass_compounds;
    } BuildMetabolicModelResults;
    /*
        Build a genome-scale metabolic model based on annotations in an input genome typed object
    */
    funcdef build_metabolic_model(BuildMetabolicModelParams params) returns (BuildMetabolicModelResults) authentication required;
    
    typedef structure {
		fbamodel_id fbamodel_id;
		workspace_name fbamodel_workspace;
		media_id media_id;
		workspace_name media_workspace;
		reaction_id target_reaction;
		fbamodel_id fbamodel_output_id;
		workspace_name workspace;
		bool thermodynamic_constraints;
		bool comprehensive_gapfill;
		fbamodel_id source_fbamodel_id;
		workspace_name source_fbamodel_workspace;
		
		list<feature_id> feature_ko_list;
		list<reaction_id> reaction_ko_list;
		list<string> custom_bound_list;
		list<compound_id> media_supplement_list;
		
		expseries_id expseries_id;
		workspace_name expseries_workspace;
		string expression_condition;
		float exp_threshold_percentile;
		float exp_threshold_margin;
		float activation_coefficient;
		float omega;
		float objective_fraction;
		float minimum_target_flux;
		int number_of_solutions;
    } GapfillMetabolicModelParams;
    
    typedef structure {
        ws_fbamodel_id new_fbamodel_ref;
        ws_fba_id new_fba_ref;
        int number_gapfilled_reactions;
        int number_removed_biomass_compounds;
    } GapfillMetabolicModelResults;
    /*
        Gapfills a metabolic model to induce flux in a specified reaction
    */
    funcdef gapfill_metabolic_model(GapfillMetabolicModelParams params) returns (GapfillMetabolicModelResults results) authentication required;
    
    typedef structure {
		fbamodel_id fbamodel_id;
		workspace_name fbamodel_workspace;
		media_id media_id;
		workspace_name media_workspace;
		reaction_id target_reaction;
		fba_id fba_output_id;
		workspace_name workspace;
		
		bool thermodynamic_constraints;
		bool fva;
		bool minimize_flux;
		bool simulate_ko;
		bool find_min_media;
		bool all_reversible;
		
		list<feature_id> feature_ko_list;
		list<reaction_id> reaction_ko_list;
		list<string> custom_bound_list;
		list<compound_id> media_supplement_list;
		
		expseries_id expseries_id;
		workspace_name expseries_workspace;
		string expression_condition;
		float exp_threshold_percentile;
		float exp_threshold_margin;
		float activation_coefficient;
		float omega;
		float objective_fraction;
		
		float max_c_uptake;
		float max_n_uptake;
		float max_p_uptake;
		float max_s_uptake;
		float max_o_uptake;
		float default_max_uptake;
		
		string notes;
		string massbalance;
    } RunFluxBalanceAnalysisParams;
    
    typedef structure {
        ws_fba_id new_fba_ref;
        int objective;
    } RunFluxBalanceAnalysisResults;
    /*
        Run flux balance analysis and return ID of FBA object with results 
    */
    funcdef run_flux_balance_analysis(RunFluxBalanceAnalysisParams params) returns (RunFluxBalanceAnalysisResults results) authentication required;
 
    typedef structure {
		list<fba_id> fba_id_list;
		workspace_name fba_workspace;
		fbacomparison_id fbacomparison_output_id;
		workspace_name workspace;
    } CompareFBASolutionsParams;
    
    typedef structure {
        ws_fbacomparison_id new_fbacomparison_ref;
    } CompareFBASolutionsResults;
    /*
        Compares multiple FBA solutions and saves comparison as a new object in the workspace
    */
    funcdef compare_fba_solutions(CompareFBASolutionsParams params) returns (CompareFBASolutionsResults results) authentication required;
	
	typedef structure {
		fbamodel_id fbamodel_id;
		workspace_name fbamodel_workspace;
		proteincomparison_id proteincomparison_id;
		workspace_name proteincomparison_workspace;
		fbamodel_id fbamodel_output_id;
		workspace_name workspace;
		bool keep_nogene_rxn;
		bool gapfill_model;
		media_id media_id;
		workspace_name media_workspace;
		
		bool thermodynamic_constraints;
		bool comprehensive_gapfill;
		
		list<string> custom_bound_list;
		list<compound_id> media_supplement_list;
		
		expseries_id expseries_id;
		workspace_name expseries_workspace;
		string expression_condition;
		float exp_threshold_percentile;
		float exp_threshold_margin;
		float activation_coefficient;
		float omega;
		float objective_fraction;
		float minimum_target_flux;
		int number_of_solutions;
    } PropagateModelToNewGenomeParams;
    
    typedef structure {
        ws_fbamodel_id new_fbamodel_ref;
        ws_fba_id new_fba_ref;
        int number_gapfilled_reactions;
        int number_removed_biomass_compounds;
    } PropagateModelToNewGenomeResults;
	/*
        Translate the metabolic model of one organism to another, using a mapping of similar proteins between their genomes
    */
	funcdef propagate_model_to_new_genome(PropagateModelToNewGenomeParams params) returns (PropagateModelToNewGenomeResults results) authentication required;
	
	typedef structure {
		fbamodel_id fbamodel_id;
		workspace_name fbamodel_workspace;
		phenotypeset_id phenotypeset_id;
		workspace_name phenotypeset_workspace;
		phenotypesim_id phenotypesim_output_id;
		workspace_name workspace;
		bool all_reversible;
		list<feature_id> feature_ko_list;
		list<reaction_id> reaction_ko_list;
		list<string> custom_bound_list;
		list<compound_id> media_supplement_list;
    } SimulateGrowthOnPhenotypeDataParams;
    
    typedef structure {
        ws_phenotypesim_id new_phenotypesim_ref;
    } SimulateGrowthOnPhenotypeDataResults;	
	/*
         Use Flux Balance Analysis (FBA) to simulate multiple growth phenotypes.
    */
	funcdef simulate_growth_on_phenotype_data(SimulateGrowthOnPhenotypeDataParams params) returns (SimulateGrowthOnPhenotypeDataResults results) authentication required;
	
	typedef structure {
		list<fbamodel_id> fbamodel_id_list;
		workspace_name fbamodel_workspace;
		fbamodel_id fbamodel_output_id;
		workspace_name workspace;
		bool mixed_bag_model;
    } MergeMetabolicModelsIntoCommunityModelParams;
    
    typedef structure {
        ws_fbamodel_id new_fbamodel_ref;
    } MergeMetabolicModelsIntoCommunityModelResults;
    /*
         Merge two or more metabolic models into a compartmentalized community model
    */
	funcdef merge_metabolic_models_into_community_model(MergeMetabolicModelsIntoCommunityModelParams params) returns (MergeMetabolicModelsIntoCommunityModelResults results) authentication required;
	
	typedef structure {
		fba_id fba_id;
		workspace_name fba_workspace;
		expseries_id expseries_id;
		workspace_name expseries_workspace;
		string expression_condition;
		float exp_threshold_percentile;
		bool estimate_threshold;
		bool maximize_agreement;
		fbapathwayanalysis_id fbapathwayanalysis_output_id;
		workspace_name workspace;
    } CompareFluxWithExpressionParams;
    
    typedef structure {
        ws_fbapathwayanalysis_id new_fbapathwayanalysis_ref;
    } CompareFluxWithExpressionResults;
    /*
         Merge two or more metabolic models into a compartmentalized community model
    */
	funcdef compare_flux_with_expression(CompareFluxWithExpressionParams params) returns (CompareFluxWithExpressionResults results) authentication required;

	typedef structure {
		fbamodel_id fbamodel_id;
		workspace_name fbamodel_workspace;
		workspace_name workspace;
    } CheckModelMassBalanceParams;
    
    typedef structure {
        ws_report_id new_report_ref;
    } CheckModelMassBalanceResults;
    /*
         Identifies reactions in the model that are not mass balanced
    */
	funcdef check_model_mass_balance(CheckModelMassBalanceParams params) returns (CheckModelMassBalanceResults results) authentication required;
};