import math

# np.import_array()

cpdef list possible_words(str word, list pattern, list guesses):

    cdef str guess
    cdef int j
    cdef int color
    cdef str wj
    cdef str gj
    cdef list possible_solutions = []

    for guess in guesses:

        for j, color in enumerate(pattern):

            wj = word[j]
            gj = guess[j]

            if wj in guess and color == 0:
                break

            elif (wj not in guess or wj == gj) and color == 1:
                break

            elif wj != gj and color == 2:
                break

        else:
            possible_solutions.append(guess)

    return possible_solutions


cpdef float exp_inf(str word, list patterns, list allowed_guesses):

    cdef int i
    cdef int N = len(patterns)
    cdef list pat
    cdef list poss_words
    cdef float p
    cdef int omega = len(allowed_guesses)
    cdef float var = 0.0

    for i in range(N):
        
        pat = list(patterns[i])
        poss_words = possible_words(word, pat, allowed_guesses)
        p = len(poss_words) / omega
        
        if p == 0.0:
            continue
        
        else:
            var += p * math.log2(p)
    
    return - var


cpdef list generate_exp_inf(list words, list patterns, list allowed_guesses):
    
    cdef int i
    cdef int N = len(words)
    cdef str word
    cdef float val
    cdef list results = []
    
    for i in range(N):
        
        word = words[i]
        val = exp_inf(word, patterns, allowed_guesses)
        results.append(val)
    
    return results