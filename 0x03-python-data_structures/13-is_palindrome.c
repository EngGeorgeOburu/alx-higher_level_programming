include "lists.h"
/**
* reverse_listint - function reverses a linked list
* @head: A ponter to the first node in the list
* Return: Pointer 
*/
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;
	
	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
}
/**
* is_palindrome - Checks if there a singly linkedlist is apalondrome
* @head: pointer to a pointer to the linked lsit
* Return: Alway 1
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow_node, *fast_node, *previous_slow;
	listint_t *second_node, *mid_node;
	
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	
	slow_node = fast_node = *head;
	previous_slow = NULL;
	
	while (fast_node != NULL && fast_node->next !=NULL)
	{
		fast_node = fast_node->next->next;
		previous_slow = slow_node;
		slow_node =slow_node->next;
	}
	if (fast != NULL)
	{
	mid_node = slow_node;
	slow_node = slow-node->next;
	}
	second_node = slow_node;
	previous_slow->next = NULL;
	reverse_list(&second_half);
	is_palindrome = compare_lists(*head, second_node)
	
	reverse_list(&second_node);

	if (mid_node != NULL)
	{
		previous_slow->next = mid_node;
		mid_node->next = second_node;
	}
	else
	{
		previous_slow->next = second_node;
	}
	return is_palindrome;
}
