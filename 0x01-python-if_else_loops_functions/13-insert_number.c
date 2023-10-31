#include "lists.h"

/**
 * insert_node - insert new node at sorted listint_t list.
 *
 * @head: head node.
 * @number: data for the new node.
 *
 * Return: the new node address.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode;
	listint_t *tempNode;

	if (head == NULL)
		return (NULL);

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);

	newNode->n = number;
	if (*head == NULL || (*head)->n >= number)
	{
		newNode->next = *head;
		*head = newNode;
		return (newNode);
	}

	tempNode = *head;
	while (tempNode->next != NULL && (tempNode->next)->n < number)
		tempNode = tempNode->next;

	if (tempNode != NULL)
	{
		newNode->next = tempNode->next;
		tempNode->next = newNode;
	}
	return (newNode);
}
