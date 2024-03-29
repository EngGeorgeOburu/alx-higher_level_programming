#include<stdlib.h>
#include"lists.h"
/**
 * check_cycle - checks if a singly linked list has a circle.
 * @list: Singly linked list
 * Return: Always 0 if successful, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return(0);
	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return(1);
		turtle = turtle->next;
		hare = hare->next->next;
	}
	return (0);
}



