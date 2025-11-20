// Write a C Program To Create a Simple Linked List In C Using Pointer And Structure.

#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int data;           
    struct Node *next;  
};

struct Node* createNode(int value) 
{
    struct Node *newNode = (struct Node*) malloc(sizeof(struct Node));
    
    if (newNode == NULL) 
    {
        printf("Memory Allocation Failed\n");
        return NULL;
    }

    newNode->data = value;  
    newNode->next = NULL;   

    return newNode;        
}

void printList(struct Node *head) 
{
    struct Node *temp = head; 

    while (temp != NULL) 
    {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }

    printf("NULL\n");
}

int main() 
{
    struct Node *head = NULL;  
    
    head = createNode(10);    
    head->next = createNode(20); 
    head->next->next = createNode(30);
    
    printf("The Linked List Is : ");
    printList(head);

    return 0;
}