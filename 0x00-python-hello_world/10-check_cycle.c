#include "lists.h"

/**
 * check_cycle - Check if a linked list have a cycle.
 *
 * @list: Pointer to a linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast_node = NULL, *slow_node = NULL;
	int flag = 1;

	if (!list)
		return (0);

	fast_node = list, slow_node = list;

	while (!(fast_node == slow_node) || flag)
	{
		flag = 0;

		if (fast_node->next != NULL)
			fast_node = fast_node->next;
		else
			return (0);

		if (fast_node->next != NULL)
			fast_node = fast_node->next;
		else
			return (0);

		slow_node = slow_node->next;
	}

	return (1);
}
