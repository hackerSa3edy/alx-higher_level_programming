#include "lists.h"

/**
 * check_cycle - finds the loop in a linked list.
 *
 * @head: head node.
 *
 * Return: (1) there is a cycle, (0) otherwise.
 */
int check_cycle(listint_t *head)
{
	listint_t *temp1, *temp2;

	if (head == NULL)
		return (0);

	temp1 = head;
	temp2 = head;
	while (temp2 && temp2->next)
	{
		temp1 = temp1->next;
		temp2 = (temp2->next)->next;
		if ((void *)temp1 == (void *)temp2)
		{
			temp1 = head;
			while ((void *)temp1 != (void *)temp2)
			{
				temp1 = temp1->next;
				temp2 = temp2->next;
			}
			return (1);
		}
	}
	return (0);
}
