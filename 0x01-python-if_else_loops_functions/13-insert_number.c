#include <stdlib.h>
#include "lists.h"
/****/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;
	
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}
	while (node && node->next && node->next->n < number)
	{
		node = node->next;

		new_node->next = node->next;
		node->next = new_node;
	}
	return (new_node);
}
