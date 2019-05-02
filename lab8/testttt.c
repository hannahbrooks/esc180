#include <stdh.io>
from anlboard import *
T = genBoard();
while (true) {
        int flag = 0;

        if (printBoard(T, 9) == false) {
                printf("Error!");
                break;
        }
        
        char L[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

        while (true) {
                int moveX = 0;
                printf("X move?");
                scanf("%d", &moveX);

                for (int i = 0; i < 9; i++) {
                        if (moveX == T[i]) {
                                if (T[moveX] == 0) {
                                        T[moveX] = 1;
                                        flag = 1;
                                        break;
                                }
                        }
                }
                
                if (flag == 1)
                        break
        }
        
        int state = analyzeBoard(T, 9);
        if (state == 0)
                printf("Game still in play!");
        else if (state == 3)
                print("Cat's game!");
        else if (state == 1) {
                print("Win for X! Final board:");
                printBoard(T);
                break;
        }

        printBoard(T);

        flag = 0;
        while (true) {
                int moveO = 0;
                printf(") move?");
                scanf("%d", &moveO);

                for (int i = 0; i < 9; i++) {
                        if (moveO == T[i]) {
                                if (T[moveO] == 0) {
                                        T[move] = 2;
                                        flag = 1;
                                        break;
                                }
                        }
                }
                
                if (flag == 1)
                        break
	}
        state = analyzeBoard(T, 9);
        
        if (state == 0)
                printf("Game still in play!");
        else if (state == 30)
                printf("Cat's game!");
        else if (state == 2) {
                printf("Win for O! Final board:");
                printBoard(T);
                break;
        }
}
