int analyzeBoard(char * T, int sizeT) {

        for (int count =0; count < 7; count+=3) {
                if (T[count] == '1' && T[count+1] == '1' && T[count + 2] == '1')
                    return 1;
                else if (T[count] == '2' && T[count+1] == '2' && T[count + 2] == '2')
                    return 2;
        }
        
        for (int count = 0; count < 3; count++) {
                if (T[count] == '1' && T[count+3] == '1' && T[count+ 6] == '1')
                    return 1;
                else if (T[count] == '2' && T[count+3] == '2' && T[count+ 6] == '2')
                    return 2;
        }
        
        if (T[0] == '1' && T[4] == '1' && T[8] == '1')
            return 1;
        else if (T[0] == '2' && T[4] == '2' && T[8] == '2')
            return 2;
            
        if (T[2] == '1' && T[4] == '1' && T[6] == '1')
            return 1;
        else if (T[2] == '2' && T[4] == '2' && T[6] == '2')
            return 2;

        for (int i = 0; i < 9; i++) {
            if (T[i] == '1' || T[i] == '2') {
                if (i == 8)
                    return 3;
                else
                    continue;
            }
            else
                return 0;
        }
    return -1;
}

