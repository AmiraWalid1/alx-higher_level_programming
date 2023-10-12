#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer to head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *curr;
	int *arr, len = 0, i = 0;

	if (!head)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	curr = *head;
	while (curr)
	{
		len++;
		curr = curr->next;
	}
	arr = malloc(sizeof(int) * len);
	if (!arr)
		return (0);
	curr = *head;
	while (curr)
	{
		arr[i] = curr->n;
		curr = curr->next;
		i++;
	}
	for (i = 0 ; i < len / 2 ; i++)
	{
		if (arr[i] != arr[len - i - 1])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
