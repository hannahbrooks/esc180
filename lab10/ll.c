#include <stdio.h>
#include <stdlib.h>
#include "ll.h"

int ll_del_from_tail(llnode **ppList) {
    
    llnode *temp;
    temp = (llnode*)malloc(sizeof(llnode));
    temp = *ppList;
    *ppList = temp->next;
    free(temp);
    
    return 0;
}


int ll_del_from_head(llnode **ppList) {
    int myval = 0;
    
    if ((*ppList)->next == NULL) {
        myval = (*ppList)->val;
        free(*ppList);
        return myval;
    }
    
    llnode *current = *ppList;
    
    while (current->next->next != NULL) {
        current = current->next;
    }
    
    myval = current->next->val;
    
    free(current->next);
    current->next = NULL;
    return myval;
}


int ll_sort(llnode **ppList) {
    int swapped = 1, myval = 0;
    struct llnode *head;
    struct llnode *lptr = NULL;
    
    if (*ppList == NULL)
        return 0;
    
    while (swapped) {
        swapped = 0;
        head = *ppList;
        
        while (head->next != lptr) {
            if (head->val > head->next->val)
            {
                myval = (head)->val;
                head->val = head->next->val;
                head->next->val = myval;
                swapped = 1;
            }
            head = head->next;
        }
        lptr = head;
    }
    return 0;
}


int ll_find_by_value(llnode *pList,int val) {
    llnode *current = pList;
    while (current != NULL) {
        if (current->val == val)
            return 1;
        
        current = current->next;
    }
    return 0;
}
int ll_del_by_value(llnode **ppList,int val) {
    llnode* temp = *ppList, *prev;
    
    if (temp != NULL && temp->val == val)
    {
        *ppList = temp->next;
        free(temp);
        return 0;
    }
    
    while (temp != NULL && temp->val != val)
    {
        prev = temp;
        temp = temp->next;
    }
    
    if (temp == NULL) return 0;
    
    prev->next = temp->next;
    
    free(temp);
    
    return 0;
}


int ll_insert_in_order(llnode **ppList,int val) {
    llnode **current = ppList;
    
    llnode *new;
    new = (llnode*) malloc(sizeof( llnode));
    new->val = val;
    
    if ((*ppList)->val > new->val) {
        int myval = (*ppList)->val;
        new->next = (*ppList)->next;
        (*ppList)->val = new->val;
        new->val = myval;
        (*ppList)->next = new;
        return 0;
    }
    
    while((*current)->next != NULL)
        *current = (*current)->next;
    
    if ((*current)->val < val) {
        (*current)->next = new;
        new->next = NULL;
        return 0;
    }
    
    current = ppList;
    
    while ((*current)->next != NULL) {
        if ((*current)->next->val > val)
            break;
        *current = (*current)->next;
    }
    new->next = (*current)->next;
    
    return 0;
}

int ll_concat(llnode **pSrcA,llnode **pSrcB){
    llnode *next = NULL;
    
    if(pSrcA == NULL)
        return -1;
    if(*pSrcA == NULL)
        return -1;
    if(pSrcB == NULL)
        return -1;
    
    next = next -> next;
    while (next != NULL){
        int i;
        i = ll_add_to_tail(pSrcA, next -> val);
        next = next -> next;}
    return 0;
}

int ll_add_to_head( llnode **head, int val) {
    llnode *old_head;
    if (head == NULL) {
        return -1;
    }
    old_head = *head;
    
    *head = ( llnode *) malloc(sizeof( llnode));
    (*head) -> val = val;
    (*head) -> next = old_head;
    return 0;
}

int ll_add_to_tail( llnode **head, int val) {
    if (head == NULL) {
        return -1;
    }
    if (*head == NULL) {
        *head = ( llnode *) malloc(sizeof( llnode));
        (*head) -> val = val;
        (*head) -> next = NULL;
        return 0;
    } else {
        return ll_add_to_tail(&((*head)->next), val);
    }
}

int ll_print( llnode *p) {
    if (p==NULL)
        return 0;
    else {
        printf("val = %d\n",p->val);
        return ll_print(p->next);
    }
}

int ll_free( llnode *p) {
    if (p==NULL) {
        return -1;
    } else {
        llnode *f=p->next;
        free(p);
        return ll_free(f);
    }
}

