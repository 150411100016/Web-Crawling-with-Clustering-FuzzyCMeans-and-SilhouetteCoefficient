import my_function as func

if __name__== "__main__":
    
    #Uni Gram
    
    stemming = func.load_list("stemming")
    collecting_fiture = func.load_list("new_collecting_fiture")
    
    woorkbook = func.create_excel()
    print("Load Tf....")
    tf_a = func.tf(stemming,collecting_fiture,woorkbook,'tf')
    func.save_list("tf",tf_a)
    func.save_excel('tf',woorkbook)
    
    woorkbook = func.create_excel()
    print("Load idf...")
    idf_a = func.idf(tf_a)
    func.add_sheet('idf', idf_a,woorkbook)
    func.save_list("idf",idf_a)
    func.save_excel('idf',woorkbook)
    
    woorkbook = func.create_excel()
    print("Load tf_idf...")
    tf_idf_a = func.tf_idf(tf_a,idf_a,collecting_fiture,woorkbook)
    func.save_list("tf_idf",tf_idf_a)
    func.save_excel('tf_idf',woorkbook)
    
    #Bi Gram
    
    n_gram = func.load_list("token_2")
    collecting_fiture_n_gram = func.load_list("new_collecting_fiture_2")
    
    woorkbook = func.create_excel()
    print("Load Tf_n_gram....")
    tf_n_gram = func.tf(n_gram,collecting_fiture_n_gram,woorkbook,'tf_2')
    func.save_list("tf_2",tf_n_gram)
    func.save_excel('tf_2',woorkbook)
    
    woorkbook = func.create_excel()
    print("Load idf_n_gram...")
    idf_n_gram = func.idf(tf_n_gram)
    func.add_sheet('idf_2', idf_n_gram,woorkbook)
    func.save_list("idf_2",idf_n_gram)
    func.save_excel('idf_2',woorkbook)
    
    woorkbook = func.create_excel()
    print("Load tf_idf_n_gram...")
    tf_idf_n_gram = func.tf_idf(tf_n_gram,idf_n_gram,collecting_fiture_n_gram,woorkbook)
    func.save_list("tf_idf_2",tf_idf_n_gram)
    func.save_excel('tf_idf_2',woorkbook)