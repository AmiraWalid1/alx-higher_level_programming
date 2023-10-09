#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer to head
 * @number: n of new node
 *
 * Return: the address of the new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev = NULL, *new_node = malloc(sizeof(listint_t));

	new_node->n = number;
	if (!head)
	{
		free(new_node);
		return (NULL);
	}
	curr = *head;
	if (curr == NULL || curr->n >= number)
	{
		new_node->next = curr;
		*head = new_node;
		return (new_node);
	}
	while (curr)
	{
		if (curr->n >= number)
		{
			break;
		}
		prev = curr;
		curr = curr->next;
	}
	new_node->next = curr;
	prev->next = new_node;
	return (new_node);
}
