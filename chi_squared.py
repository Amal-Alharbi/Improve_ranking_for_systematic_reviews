def find_chi_squared(topics,frq_word_rel_doc,frq_word_non_rel_doc,threshold): 
     
     """
     This method finds the chi squared (chi) for terms in the training dataset
     For each topic in the training dataset, it uses the text of relevant and non-relevant documents.
     then calculate the average ll for each term by divide the value by the total number of topics in the training dataset
     
     topics --> list of the training dataset topics
     frq_word_rel_doc --> frequency of the term in the relevant documents
     frq_word_non_rel_doc --> frequency of the term in the non-relevant documents
     threshold --> to exclude terms appears less than the threshold
     
     """
    chi_squared = list()
  
    for topic in topics:                  
      for i, word in enumerate(frq_word_rel_doc):
        #calculate the expected values: E1 and E2
        a = frq_word_rel_doc[i][1] 
        b = frq_word_non_rel_doc[i][1]
        c = frq_word_rel_doc[i][2] # c = C-a
        d = frq_word_non_rel_doc[i][2] # d = D-b
        C = total_rel  
        D = total_non_rel  

        #E1, E2
        E1 = C * (a + b)/(C + D)
        E2 = D * (a + b)/(C + D)

        chi = ((a - E1)**2 / E1) + ((b - E2)**2 / E2)

        chi_squared.append((frq_word_rel_doc[i][0],chi))

    chi_sorted = sorted(chi_squared,key=lambda l:l[1], reverse=True)
    chi_all.append((topic[1],chi_sorted))
    combained_list = list()
    
    for i,record in enumerate(chi_all): 
        for j,t in enumerate(chi_all[i][1]): 
            combained_list.append((t[0],t[1])) 
            
    # for ecah term find all the chi values, example (blood,[20,11,17])
    term_chis = {}
    for tuple in combained_list:
        key,val = tuple
        term_chis.setdefault(key, []).append(val)
     
   
    temp = list()
    terms_chi = []
    
    #calculate the average chi (divide the chi by total number of topics)
    for term , value in term_chis.items():
        temp.append((term, (sum(value)/len(topics))))
     
    #sort the list of chi   
    temp = sorted(temp,key=lambda l:l[1], reverse=True)
       
    for term, value in temp:
        terms_chi.append((term,str(value)))
 
    return terms_chi
