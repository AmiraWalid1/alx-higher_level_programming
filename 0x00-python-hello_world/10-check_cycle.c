#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *curr;

	curr = list;
	while (curr)
	{
		curr = curr->next;
		if (curr == list)
		{
			return (1);
		}
	}
	return (0);
}
