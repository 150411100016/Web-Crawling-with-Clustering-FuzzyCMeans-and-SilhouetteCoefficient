import my_function as func

if __name__== "__main__":
    crawl  = func.crawl_web('https://www.suara.com/indeks/terkini/all/2019')
    func.save_content(crawl)
    func.save_list("crawl",crawl)