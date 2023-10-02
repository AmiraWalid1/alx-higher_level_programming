#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t *curr, *test;
	int idx = 0, i;

	curr = list;
	while (curr)
	{
		idx++;
		curr = curr->next;
		test = list;
		for (i = 0 ; i < idx ; i++)
		{
			if (curr == test)
			{
				return (1);
			}
			test = test->next;
		}
	}
	return (0);
}
