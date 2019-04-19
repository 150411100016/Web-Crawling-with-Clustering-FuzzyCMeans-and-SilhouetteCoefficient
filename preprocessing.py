import my_function as func

if __name__== "__main__":
    #Uni Gram
    print("Load data......")
    data = func.load_list("data")
    woorkbook = func.create_excel()
    
    print("Lowercase......")
    lowercase = func.lowercase(data)
    func.add_sheet('lowercase', lowercase,woorkbook)
    func.save_list("lowercase",lowercase)
    
    print("Remove symbol......")
    symbol_remover = func.symbol_remover(lowercase)
    func.add_sheet('remove symbol', symbol_remover,woorkbook)
    func.save_list("symbol",symbol_remover)
    
    print("Tokenisasi......")
    tokenisasi = func.tokenisasi(symbol_remover)
    for i in range(len(tokenisasi)):
        tokenisasi[i] = [x for x in tokenisasi[i] if x != "b"]
        tokenisasi[i] = [x for x in tokenisasi[i] if x != "suara"]
        tokenisasi[i] = [x for x in tokenisasi[i] if x != "com"]
    func.add_sheet_list('tokenisasi', tokenisasi,woorkbook)
    func.save_list("token",tokenisasi)
    
    print("Stopword......")
    stopword_s = func.stopword_s(tokenisasi)
    func.add_sheet_list('stopwords', stopword_s,woorkbook)
    func.save_list("stopword",stopword_s)
    
    print("Stemming......")
    stemming = func.stemming(stopword_s)
    func.add_sheet_list('stemming', stemming,woorkbook)
    func.save_list("stemming",stemming)
    
    print("VSM......")
    collecting_fiture = func.collecting_fiture(stemming)
    vsm = func.vsm(stemming,collecting_fiture,woorkbook)
    func.save_list("collecting_fiture",collecting_fiture)
    func.save_list("vsm",vsm)
    
    func.save_excel("Preprocessing",woorkbook)
    
    #Bi Gram
    n = 2
    
    woorkbook = func.create_excel()
    n_gram = func.generate_ngrams(stemming, n)
    func.add_sheet_list('tokenisasi', n_gram,woorkbook)
    func.save_list("token_2",n_gram)
    
    print("Load collecting_fiture....")
    collecting_fiture = func.collecting_fiture(n_gram)
    func.save_list("collecting_fiture_2",collecting_fiture)
    
    print("Load vsm....")
    vsm = func.vsm(n_gram,collecting_fiture,woorkbook)
    func.save_list("vsm_2",vsm)
    
    func.save_excel('Preprocessing_2',woorkbook)