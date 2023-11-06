#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: head node.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int palindrome, counter, head_data, tail_data, list_len, tempCounter;
	listint_t *head_node, *tail_node, *temp_node;

	head_node = tail_node = temp_node = NULL;
	palindrome = counter = list_len = 0;

	if (head == NULL)
		return (palindrome);

	if (*head == NULL || (*head)->next == NULL)
		return (palindrome = 1);

	temp_node = *head;
	for (; temp_node; temp_node = temp_node->next)
		list_len++;

	head_node = tail_node = *head;
	while (counter <= (int)(list_len / 2))
	{
		head_data = head_node->n;

		for (tempCounter = 1; tempCounter < list_len - counter; tempCounter++)
			tail_node = tail_node->next;

		tail_data = tail_node->n;

		if (tail_data != head_data)
		{
			palindrome = 0;
			break;
		}
		head_node = head_node->next;
		tail_node = *head;
		counter++;
		palindrome = 1;
	}
	return (palindrome);
}
