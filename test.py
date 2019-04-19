import my_function as func

if __name__== "__main__":
    
    s_avg =  func.load_list("s_avg")
    print(s_avg.index(max(s_avg))+2)
        
    s_avg =  func.load_list("s_avg_2")
    print(s_avg.index(max(s_avg))+2)
    