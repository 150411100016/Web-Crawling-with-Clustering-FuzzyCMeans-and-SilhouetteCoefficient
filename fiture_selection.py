import my_function as func
    
if __name__== "__main__":
    vsm =  func.load_list("vsm")
    collecting_fiture =  func.load_list("collecting_fiture")
    new_vsm,new_collecting_fiture = func.drop_highly_correlation(vsm,collecting_fiture)
    func.save_list("new_vsm",new_vsm)
    func.save_list("new_collecting_fiture",new_collecting_fiture)
    
    vsm_n_gram =  func.load_list("vsm_2")
    collecting_fiture_n_gram =  func.load_list("collecting_fiture_2")
    new_vsm_n_gram,new_collecting_fiture_n_gram = func.drop_highly_correlation(vsm_n_gram,collecting_fiture_n_gram)
    func.save_list("new_vsm_2",new_vsm_n_gram)
    func.save_list("new_collecting_fiture_2",new_collecting_fiture_n_gram)