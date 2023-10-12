#include "lists.h"

/**
 * addNodeToBegin - add Node To Begin of list
 * @head: pointer to pointer to head
 * @n: n of new node
 *
 * Return: pointer to node of (NULL) if failed
*/
listint_t *addNodeToBegin(listint_t **head, int n)
{
	listint_t *new_node;

	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = n;
	new_node->next = *head;
	*head = new_node;
	return (new_node);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *h_temp = NULL, *curr, *curr_temp;

	if (!head)
		return (0);
	curr = *head;
	while (curr)
	{
		addNodeToBegin(&h_temp, curr->n);
		curr = curr->next;
	}
	curr_temp = h_temp;
	while (curr && curr_temp)
	{
		if (curr->n != curr_temp->n)
		{
			free_listint(h_temp);
			return (0);
		}
		curr = curr->next;
		curr_temp = curr_temp->next;
	}
	free_listint(h_temp);
	return (1);
}
