// Write a Program To Insert Item In Middle Of The Linked List.

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

void insertMiddle(struct Node *head, int value) 
{
    struct Node *slow = head;
    struct Node *fast = head;

    while (fast != NULL && fast->next != NULL) 
    { 
        slow = slow->next;
        fast = fast->next->next;
    }
    
    struct Node *newNode = createNode(value);
    newNode->next = slow->next;
    slow->next = newNode;
}

int main() 
{
    struct Node *head = NULL;

    head = createNode(10);
    head->next = createNode(20);
    head->next->next = createNode(30);
    
    printf("The Linked List Is : ");
    printList(head);

    insertMiddle(head, 25);
    
    printf("After Inserting 25 In The Middle : ");
    printList(head);

    return 0;
}