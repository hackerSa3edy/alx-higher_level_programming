#include "lists.h"

listint_t *reverse_listint(listint_t **head);

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: head node.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int palindrome, head_data, tail_data, list_len, tempCounter;
	listint_t *head_node, *tail_node, *temp_node;

	head_node = tail_node = temp_node = NULL;
	list_len = 0;
	palindrome = 1;

	if (head == NULL)
		return (palindrome = 0);

	if (*head == NULL || (*head)->next == NULL)
		return (palindrome);

	temp_node = *head;
	for (; temp_node; temp_node = temp_node->next)
		list_len++;

	head_node = tail_node = *head;
	for (tempCounter = 1; tempCounter < (int)(list_len / 2); tempCounter++)
		tail_node = tail_node->next;
	if (list_len % 2 != 0)
		tail_node = tail_node->next;

	reverse_listint(&tail_node);

	for (tempCounter = 0; tempCounter < (int)(list_len / 2); tempCounter++)
	{
		head_data = head_node->n;
		tail_data = tail_node->n;
		if (head_data != tail_data)
		{
			palindrome = 0;
			break;
		}
		head_node = head_node->next;
		tail_node = tail_node->next;
	}

	if (list_len % 2 != 0)
		head_node = head_node->next;

	reverse_listint(&head_node);

	return (palindrome);
}


/**
 * reverse_listint - reverse a linked list.
 *
 * @head: head node.
 *
 * Return: pointer to the first node.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *temp = NULL, *ptr = NULL;

	if (head == NULL || *head == NULL)
		return (NULL);

	temp = *head;
	while (temp->next != NULL)
	{
		ptr = temp->next;
		temp->next = (temp->next)->next;
		ptr->next = *head;
		*head = ptr;
	}

	return (*head);
}
